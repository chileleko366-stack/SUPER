"""Automated grounding gate: extracts every checkable factual claim from a
NIM-generated script and checks each one against the actually-scraped source
article text, before a channel is allowed to render.

Built in response to the 2026-07-11 fabrication audit (research/audit/), which
found NIM inventing specific names, mechanisms, and dates that weren't in the
Firecrawl result the pipeline had actually retrieved (worst case: venture-forge's
hook attributed a bankruptcy trend to a real, named company -- "LendingClub" --
that appeared nowhere in the source).

Known limitation, stated plainly rather than hidden: this gate asks the same
NIM model that generated the script to also grade it against the source text.
That is a real, meaningfully weaker check than an independent verifier or a
human -- a model that hallucinated a claim in generation may also rate its own
hallucination as grounded on a bad day. It is still worth having, because
verifying "does the source text contain X" is a much narrower, easier task
than open-ended script writing, and it catches the class of claim the audit
actually found (a specific proper noun / date / number / causal mechanism with
literally zero textual support). Treat a pass from this gate as "no obvious
fabrication," not as an independent fact-check.
"""
import json

from . import nim_client

# Fields that carry checkable, on-screen-as-fact content: the spoken/caption
# line, and literal on-screen date badges. chartData and codeLines are
# deliberately excluded -- both are already documented elsewhere
# (run_channel.py's module docstring, resolve_chart_data) as
# illustrative-by-design / example content, not claimed-real data, so
# grounding them against the source text is a category error, not a gap.
# "traits" is also excluded: per the script prompt these are short thematic
# keyword tags (e.g. "financial", "stress"), not factual assertions -- the
# manual fabrication audit (research/audit/) never flagged a trait as the
# source of a real fabrication, only "text" (spoken claims) and
# "timelineEvents" (literal date badges) ever were. Checking single generic
# category words against source text produces noise, not signal (e.g.
# rejecting "financial" because the source doesn't use that exact word),
# so traits are left out of the gate rather than fixed with an ever-growing
# leniency prompt.
CLAIM_FIELDS = ("text", "timelineEvents")

VERIFIER_SYSTEM_PROMPT = """You are a strict fact-checker. You will be given SOURCE TEXT (the only
material actually retrieved for this video) and a list of CLAIMS extracted from a script written about
that source. For each claim, decide whether it is directly supported by the SOURCE TEXT -- stated
outright, or a reasonable close paraphrase of something the source text actually says.

A claim asserting a cause, mechanism, name, date, or number is only "ungrounded" if that
SPECIFIC cause/mechanism/name/date/number is ABSENT from the source text. If the source text
states the same thing (even in different words, or as a list item, or under a heading phrased
as a question), the claim is "grounded" -- read the whole source text before deciding, don't
pattern-match on the claim merely sounding like a causal or specific statement.

Example: if the source text says "Prescott cited the exhaustion of COVID relief funds, rising
labor and material costs, higher borrowing costs, tariffs, and shifting consumer demand", then a
claim like "Rising labor costs and tariffs are driving the surge" is GROUNDED (it restates causes
the source explicitly lists), even though it asserts a specific cause -- asserting a cause is
not itself a problem, asserting an UNSUPPORTED one is.

Mark a claim "ungrounded" only if:
- it names a specific person, company, place, date, or number that does NOT appear anywhere in the source text
- it asserts a specific cause, mechanism, or explanation that the source text does NOT state anywhere, in any form
- it is more specific or more confident than anything the source text supports

Do NOT flag as ungrounded:
- generic rhetorical framing, transitions, or calls to action with no factual content
  (e.g. "But what causes this?", "Try this at home!")
- claims explicitly framed as hypothetical/illustrative ("imagine...", "for example...", "let's say...")
- a claim that is a direct restatement, paraphrase, or summary of something the source text says
- a claim restating a cause/fact/list-item the source text itself provides, even if phrased as a
  question, heading, or in different words

Output ONLY valid JSON, no prose, no markdown fences, shaped exactly like:
{"verdicts": [{"id": "<claim id from input>", "status": "grounded"|"ungrounded", "reason": "under 12 words"}]}
Keep every "reason" under 12 words -- a short pointer, not a quote or explanation.
Every claim id given to you must appear exactly once in "verdicts"."""

# Purely rhetorical/CTA text this common enough not to bother sending to the
# verifier at all -- keeps the claims list focused on the beats actually worth
# an LLM call. Anything not matching is still sent; this is a cheap filter,
# not a substitute for the verifier's own judgment above.
_NO_CLAIM_MARKERS = ("imagine ", "for example", "let's say", "let’s say", "say you")


def extract_claims(script: dict, beat_primitives: dict[str, str] | None = None) -> list[dict]:
    """Flattens every checkable field across all beats into one claim list,
    each tagged with a stable id so verdicts can be matched back up.

    Skips "text" for KenBurnsCard beats entirely: per the script prompt
    (KEN_BURNS_GUIDANCE in run_channel.py) these are mood/b-roll captions --
    unnamed illustrative vignettes or explicit hypotheticals -- the same
    illustrative-by-design category as chartData/codeLines, not a factual
    claim about the sourced topic. In testing, sending these to the verifier
    anyway produced unreliable noise: the small model repeatedly flagged
    correctly-hedged lines like "Imagine a shopkeeper..." as ungrounded for
    the literal reason "hypothetical example", contradicting its own
    instructions not to. Rather than keep patching prompt wording around
    that, the category is exempted the same way chartData/codeLines are.

    Also skips "text" for CodeBlock beats: per CODE_BLOCK_GUIDANCE that text
    is a caption for the demonstrated algorithm itself (e.g. "Here's binary
    search in six lines"), describing generic illustrative codeLines that
    are already exempt -- not a claim about the sourced topic either.

    Also skips "text" for DataChart beats: per the chart_note in
    build_script_prompt, this text is required to be hedged illustrative
    framing ("let's say"/"for example"/"imagine") around the already-exempt
    chartData -- same category, same reasoning. Confirmed in testing: the
    verifier flagged a properly-hedged "Let's say a country imposes a 10%
    tariff..." as ungrounded even though 10% was the exact figure in the
    source, the same instruction-violation pattern as KenBurnsCard.

    Also skips beats conventionally named "bridge" or "conclusion" (used by
    every one of this pipeline's 8 production channels): the manual
    fabrication audit (research/audit/) read every beat of every channel and
    found these two are, without exception, a rhetorical transition question
    or a generic CTA/takeaway -- never a factual claim. Sending them to the
    verifier anyway produced the same unreliable-small-model noise as
    KenBurnsCard: correctly generic filler like "Stay curious, and keep
    looking up" got flagged "no specific connection to exoplanet discovery",
    which is true and irrelevant -- it was never claiming one.
    """
    beat_primitives = beat_primitives or {}
    NON_FACTUAL_BEAT_NAMES = {"bridge", "conclusion"}
    claims = []
    for beat, beat_script in script.items():
        if not isinstance(beat_script, dict):
            continue
        if beat_primitives.get(beat) in ("KenBurnsCard", "CodeBlock", "DataChart"):
            continue
        if beat.lower() in NON_FACTUAL_BEAT_NAMES:
            continue
        for field in CLAIM_FIELDS:
            if field not in beat_script:
                continue
            value = beat_script[field]
            if field == "text":
                text = str(value).strip()
                if text:
                    claims.append({"id": f"{beat}.text", "beat": beat, "field": field, "claim": text})
            elif field == "traits":
                for i, trait in enumerate(value or []):
                    claims.append({"id": f"{beat}.traits[{i}]", "beat": beat, "field": field, "claim": str(trait)})
            elif field == "timelineEvents":
                for i, ev in enumerate(value or []):
                    label = ev.get("label", "")
                    date = ev.get("date", "")
                    claims.append({
                        "id": f"{beat}.timelineEvents[{i}]",
                        "beat": beat,
                        "field": field,
                        "claim": f'"{label}" dated {date}',
                    })
    return claims


def verify_grounding(source_text: str, script: dict, beat_primitives: dict[str, str] | None = None) -> list[dict]:
    """Runs every extracted claim through the verifier prompt and returns the
    claim list annotated with status/reason. Raises if NIM's verdicts don't
    cover every claim id (fail loud rather than silently treat a missing
    verdict as a pass)."""
    claims = extract_claims(script, beat_primitives)
    if not claims:
        return []

    claims_for_prompt = [{"id": c["id"], "claim": c["claim"]} for c in claims]
    user_prompt = (
        f"SOURCE TEXT:\n{source_text}\n\n"
        f"CLAIMS:\n{json.dumps(claims_for_prompt, indent=2)}"
    )
    # Low temperature: fact-checking each claim against source text is a
    # judgment task that should be consistent, not creative -- the default
    # 0.7 (tuned for script writing) made this verifier's own verdicts
    # noticeably noisy from call to call in testing (flip-flopping on claims
    # that clearly were or weren't supported by the source text).
    result = nim_client.generate_json(VERIFIER_SYSTEM_PROMPT, user_prompt, max_tokens=2200, temperature=0.1)
    verdicts = {v["id"]: v for v in result.get("verdicts", [])}

    missing = [c["id"] for c in claims if c["id"] not in verdicts]
    if missing:
        raise RuntimeError(f"Grounding verifier did not return a verdict for claim(s): {missing}")

    for c in claims:
        v = verdicts[c["id"]]
        c["status"] = v.get("status", "ungrounded")
        c["reason"] = v.get("reason", "")
    return claims


def render_report(channel_slug: str, topic: dict, claims: list[dict]) -> str:
    ungrounded = [c for c in claims if c["status"] != "grounded"]
    lines = [
        f"# Grounding Gate Report — {channel_slug}",
        "",
        f"Source: [{topic.get('title', '')}]({topic.get('url', '')})",
        f"Query: `{topic.get('query', '')}`",
        "",
        f"**{len(claims) - len(ungrounded)}/{len(claims)} claims grounded.**",
        "",
        "| Beat | Field | Claim | Status | Reason |",
        "|---|---|---|---|---|",
    ]
    for c in claims:
        claim_text = c["claim"].replace("|", "\\|").replace("\n", " ")
        reason = c.get("reason", "").replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {c['beat']} | {c['field']} | {claim_text} | {c['status']} | {reason} |")
    return "\n".join(lines) + "\n"


def check_gate(channel_slug: str, topic: dict, script: dict, beat_primitives: dict[str, str] | None = None) -> tuple[list[dict], str]:
    """Runs the full gate and returns (claims, report_markdown). Does not
    itself raise on ungrounded claims -- run_channel.py decides what to do
    with the result so the report can be written to disk either way."""
    claims = verify_grounding(topic["sourceText"], script, beat_primitives)
    report = render_report(channel_slug, topic, claims)
    return claims, report
