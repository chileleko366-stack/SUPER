# Gate Validation, Round 2 — 2026-07-12

Follow-up to [GATE_VALIDATION_2026-07-11.md](GATE_VALIDATION_2026-07-11.md), which left 4 channels
blocked. Diagnosed each of the 4 individually before changing anything (see the diagnosis in
conversation, summarized below), then applied two targeted fixes and re-tested all 8 channels.

## Diagnosis (no changes made yet at this point)

| Channel | Diagnosis | Evidence |
|---|---|---|
| code-trail | **(a)** query/selection bug | `github.com/trending` scrapes "successfully" (clears the char floor) but the text is dominated by a language-selector link list, not repo descriptions. The channel's own 3rd query pattern already surfaces a real 1,003-word article profiling 7 specific tools — `source_topic()` just never reached it because it stopped at the first result past the char floor. |
| cosmic-window | **(a)** query/selection bug | Query 1 fell back to a monthly-roundup video that covers 5 topics in one clause each. The channel's own 2nd query pattern surfaces a single-discovery article (Texas A&M/JWST, published in *Nature Astronomy*) with real depth — same root cause as code-trail. |
| market-lens | **Fits none of (a)/(b)/(c)** | Source (an SF Fed economic letter, found on the *first* query) was already dense and specific. The block was verifier noise: it flagged near-verbatim restatements of the source's own title as "no specific claim," while correctly catching one real fabrication (an inverted "tariffs dropped 16.8%" claim, when the source says the rate *increased*). |
| thought-tides | **Fits none of (a)/(b)/(c)** | Source (a Daily Stoic video transcript, found on the *first* query) was rich, with named quotes and anecdotes. NIM's block came from inventing a specific definition-phrasing not in the transcript's own words, not from thin material. |

## Fixes applied

**1. `source_topic()` rewritten (general fix, all channels, not just code-trail/cosmic-window).**
Previously returned the first result that merely cleared `MIN_SOURCE_TEXT_CHARS`. Now scrapes a
bounded set of candidates (`RESULTS_PER_QUERY_TO_SCRAPE = 2` per query pattern, across *all*
configured patterns — previously it stopped at the first pattern that produced any usable result)
and scores each with `_score_source_text()`: a heuristic that penalizes markdown-link-dominated
scrapes (the github.com/trending failure mode) and rewards prose length up to a point. Returns
the max-scoring candidate. Validated the heuristic against 10 real captured texts before wiring it
in — it correctly ranked github.com/trending's link-list scrape lowest (0.35) and the coddykit
listicle article highest (0.95) among code-trail's candidates.

Also added one prompt instruction this surfaced a need for: when the winning source describes
several distinct items (a listicle/roundup), NIM is now told to pick ONE and ground the whole
script in that item's specific details, rather than writing generically about all of them (which
produces exactly the vague, ungrounded filler the gate exists to catch).

**2. Verifier prompt rewritten as an ordered decision procedure** (`pipeline/lib/grounding_gate.py`).
Previously a flat list of rules the model applied inconsistently. Now: STEP 1 explicitly grounds
any restatement/paraphrase of the source's own title or a sentence/heading it contains, even if it
adds no new information. STEP 2 is the highest-priority check for a specific number/date/name/
direction: grounded if it matches the source, **ungrounded if it's absent, different, or inverted**
regardless of how plausible the sentence reads. STEPs 3-5 cover causal claims, rhetorical filler,
and the default case. Validated with a direct unit test against the real FRBSF source text before
touching the pipeline: a claim restating the source's own title now passes, and the known
tariff-inversion fabrication ("Tariffs dropped by 16.8%") is still correctly rejected.

## Re-test results (run-id `20260712-gated`, all 8 channels)

| Channel | Result |
|---|---|
| code-trail | ✅ Now passes. Source-scoring picked the coddykit article (score 0.95 vs. 0.37 for github.com/trending). Needed the listicle-focus prompt addition to stop generating vague cross-tool summaries; passed on the 2nd attempt afterward. |
| cosmic-window | ✅ Now passes. Source-scoring picked a full Webb-telescope video transcript (score 1.00) over the earlier thin roundup. Passed on the 2nd generation attempt; the gate caught and rejected one real error along the way ("Webb's launch marked a major milestone... a decade in the making" — launch was Dec. 2021, not a decade prior). |
| market-lens | ✅ Now passes, first attempt, 4/4 grounded. (Landed on a different, even richer source this run — a J.P. Morgan mid-year outlook PDF, score 1.00 — Firecrawl's top result for this query changes day to day, as expected.) |
| thought-tides | 🛑 **Still blocked** — see below, this is not the restatement/inversion problem the fix targeted. |
| venture-forge, echoes-of-ages, earthwise-everyday, silver-screen-insight | ✅ Regression-checked: all 4 still pass cleanly with both changes in place. silver-screen-insight is worth flagging specifically: this run's source changed to a full YouTube breakdown transcript that explicitly credits "Director: Curry Barker" multiple times (including a quoted Variety interview) — confirmed the gate is grounding a real, textually-supported director attribution now, not repeating the earlier truncated-guess failure mode. |

**Confirms the specific ask**: the restatement-vs-inversion distinction works as intended (unit test
+ market-lens's clean pass on real dense financial text), and it did not weaken the gate's real
catches (cosmic-window's launch-date error and the original tariff-inversion case are both still
caught by design, and code-trail/cosmic-window's genuinely-thin sources are still rejected when
that's actually what's on offer that day).

## thought-tides: still blocked, different reason than what was fixed

Retested twice (fresh source-selection run + a second solo retry). Both times the *source* was rich
(a full Daily Stoic transcript, then a full Alan Watts monologue on meaning/significance) — this
is not a sourcing problem. The block is that the `mechanism` beat (`InfoCard`, wants a crisp
declarative claim) doesn't reduce cleanly out of a discursive, meandering philosophical source
without paraphrase-drift: NIM keeps compressing Watts' rambling argument into modern soundbite
phrasing ("the significance of being," "not in external goals or achievements") that the verifier
correctly can't match back to specific sentences in the source, even though it's a fair thematic
gist.

**Deliberately did not loosen the verifier further to force this through.** The whole value of
STEP 2/3 requiring explicit source support for specific/causal claims is what catches things like
the wrong GitHub-algorithm claim and the tariff inversion — broadening that leniency specifically to
let philosophical paraphrase through risks reopening exactly those holes elsewhere. This is a
different category from the (a)/(b)/(c) framework used on the first 4: not a query problem, not
really day-to-day inconsistency, but a mismatch between this channel's shot grammar (a beat that
wants a crisp mechanism-style claim) and the genre of source it tends to pull (reflective philosophy
that doesn't argue in that shape). Fixing it would mean either accepting looser paraphrase-matching
for this one channel's `mechanism` beat specifically (a real design decision, not a bug fix) or
adjusting that beat's requirement for philosophy-genre channels — left for you to decide, not
decided here.

## Bottom line

7 of 8 channels now render clean through the gate. thought-tides remains blocked, for a structural
reason distinct from anything this round's fixes targeted, and forcing it through would require
weakening a check that's doing real work elsewhere.
