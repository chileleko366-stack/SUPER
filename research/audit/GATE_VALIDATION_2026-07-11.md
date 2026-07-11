# Grounding Gate Validation — 2026-07-11

Confirms whether the new structural fix (full-article Firecrawl sourcing + an automated
NIM-vs-source grounding gate, both added to `pipeline/run_channel.py` /
`pipeline/lib/grounding_gate.py` today) actually catches the fabrications the manual
audit (`research/audit/*.md`, same date) found by hand, before anything is allowed to render.

## What changed

1. **Full-article sourcing** (`source_topic()` in `run_channel.py`): now calls
   `firecrawl_client.scrape(url)` on the chosen search result and stores the full scraped
   markdown as `topic.json`'s new `sourceText` field (capped at 6000 chars), skipping
   results that fail to scrape or scrape too thin. Previously the pipeline only ever kept
   a title + one-sentence search snippet — this is the single biggest change, since most
   of the original fabrication was NIM filling gaps a snippet-only source left wide open.
2. **Script prompt now includes `sourceText`** and explicit instructions not to state
   any name/number/date/cause not in it, and conversely to prefer real specific details
   from it over vague generalities.
3. **Automated grounding gate** (`pipeline/lib/grounding_gate.py`): after script
   generation, every beat's spoken `text` and `timelineEvents` are sent to NIM again (low
   temperature, dedicated fact-check prompt) to verify each against `sourceText`. Any
   ungrounded claim blocks the run (up to 3 script regeneration attempts, then a hard
   `RuntimeError` — no auto-render). A `GROUNDING_REPORT.md` is written to the run's
   `out/` dir either way.
4. Illustrative-by-design content (`chartData`, `codeLines`, `KenBurnsCard`/`CodeBlock`/
   `DataChart` beat text, and the conventionally-rhetorical `bridge`/`conclusion` beats)
   is exempted from the gate — see "Gate limitations found" below for why.

## Per-channel outcome (re-rendered under run-id `20260711-gated`)

| Channel | Result | What happened |
|---|---|---|
| **venture-forge** | ✅ Rendered, 4/4 grounded | The LendingClub fabrication is gone. New script's hook: "Securitas alerts: Small business bankruptcies surging in 2026" and explanation cites the real "67%... 833 filings compared to 499 in Q1 2025" figure straight from the now-fully-scraped source article. No invented company name anywhere. |
| **echoes-of-ages** | ✅ Rendered, 8/8 grounded | The onthisday.com page now scrapes in full (previously only a 5-name snippet). All 3 `timelineEvents` dates in this run (138, 911, 1244) are lifted directly from the scraped page, not NIM's memory. Notably, the *original* run's "Samuel de Champlain returns to Quebec" was dated 1608 by NIM from general knowledge — the real scraped page states 1616 for that specific "returns to Quebec" event. 1608 (Quebec's founding) and 1616 (this return) are different real events NIM's training data conflated; this run didn't reuse that event at all, but it's concrete evidence the original gap was real, not hypothetical. |
| **earthwise-everyday** | ✅ Rendered, 4/4 grounded | Was already LOW risk; still clean. |
| **silver-screen-insight** | ✅ Rendered, 4/4 grounded | Firecrawl's top result changed since the manual audit (now a full, real, non-truncated article on film-psychology from tasteray.com, not the truncated Soderbergh/Disclosure Day snippet). Full-text scraping meant no sentence-completion guessing this time; script's psychology claims ("brains wired to find meaning in chaos," "collaborative hallucination") are lifted near-verbatim from the real article. |
| **code-trail** | 🛑 Blocked by gate (3/3 attempts) | **Reproduces the exact original finding.** Source is `github.com/trending` — a bare repo-name list, still no algorithm explanation after full scraping (the page just doesn't have one). NIM kept trying to write a "mechanism"/"explanation" beat about "how GitHub's trending algorithm works" and the gate correctly rejected it every time as unsupported. This is the gate working as designed, not a bug — the channel's shot grammar needs a beat the sourced page can't honestly fill. |
| **cosmic-window** | 🛑 Blocked by gate (3/3 attempts) | Space.com's homepage scraped too thin (125 chars, likely JS-rendered) and fell through to a real, substantive YouTube video description (Dr. Becky Smethurst's "Night Sky News," citing real papers). But the video's *exoplanet* mention within that description is only one clause ("the new type of exoplanet that's been discovered") — not enough for the channel's `explanation`/`mechanism` beats, so NIM kept writing vague filler ("offers a unique window into the formation of galaxies") the gate correctly flagged as unsupported. |
| **market-lens** | 🛑 Blocked by gate (3/3 attempts) | One attempt is worth flagging specifically: NIM wrote "Tariffs dropped by 16.8% in the US, what's the impact on inflation?" — **the real source says tariffs increased**, and 16.8% appears nowhere in it. The gate caught this immediately (`"US tariff rate increased, not decreased"`). This is precisely the class of error (a specific, checkable, backwards/invented number) the whole audit was worried about, caught before render. |
| **thought-tides** | 🛑 Blocked by gate (3/3 attempts) | NIM repeatedly asserted a specific definition of "moral courage" ("the ability to act with integrity") not present in the source (a Stoicism video-title listing). Gate correctly rejected it each time. |

**4 of 8 channels now render clean through the gate on this pass; 4 are correctly blocked because the source material Firecrawl actually surfaced for them today is too thin for that channel's shot grammar to honestly fill.** That is the gate functioning as specified, not a defect — every one of the 4 blocks traces to a real gap between what the page/video says and what the beat demands, the same failure mode the manual audit found.

## Confirmed: gate catches the manual audit's specific findings

- **venture-forge / LendingClub** (highest-severity manual finding): gone at the source — full-text scraping gave NIM enough real material that it didn't reach for an invented company name. ✅
- **market-lens / inverted-and-invented tariff numbers**: caught live during this exercise (16.8%/"dropped" vs. real source showing tariffs *increased*). ✅
- **code-trail / invented trending-algorithm mechanism**: still generated by NIM (github.com/trending still describes no algorithm), but now blocked before render instead of reaching props.json. ✅
- **cosmic-window / wrong "jellyfish" mechanism**: didn't recur verbatim this run (Firecrawl's top result changed to the Dr. Becky video, different topic entirely), so this specific claim wasn't retested directly — but the same class of ungrounded mechanism claim on a different topic was caught and blocked. Residual risk: if space.com's own page ever scrapes successfully again with the original jellyfish story, this needs a live retest.
- **echoes-of-ages / ungrounded-but-lucky dates**: root cause (snippet-only sourcing) fixed; dates are now lifted from the real page instead of NIM's memory.
- **silver-screen-insight / invented director+scene+technique**: root cause (Firecrawl truncation) addressed by full scraping; not retested on the exact same truncated case since the search result changed, but the mechanism that produced it (guessing past a cut-off sentence) is gone with the truncation itself.
- **thought-tides / invented "moral courage" definition**: this exact class of claim reappeared on a fresh run and was caught and blocked. ✅

## Gate limitations found while building this (documented honestly, not hidden)

- **The verifier is the same small NIM model doing the generating**, just at low temperature with a narrower task. This is real: checking "does source text support claim X" is easier than open-ended writing, but it's not an independent fact-check. Testing surfaced real noise in both directions:
  - **Over-rejection**: initially flagged correctly-hedged illustrative lines ("Imagine a shopkeeper...") as ungrounded for the literal reason "hypothetical example" — contradicting its own instructions not to. Also flagged single-word thematic `traits` (e.g. "financial", "stress") as unsupported claims, and flagged verbatim-or-near-verbatim title restatements as having "no specific claim."
  - **Fixed by scope, not more prompt-tuning**: excluded `traits` from the gate entirely (never the source of a real finding in the manual audit), and exempted `KenBurnsCard`/`CodeBlock`/`DataChart` beat text and the conventional `bridge`/`conclusion` beats (all beats the manual audit itself always treated as non-factual-by-design).
  - Also found and fixed a real robustness bug unrelated to grounding accuracy: the verifier's JSON output occasionally got truncated at the token limit and failed to parse; `nim_client.generate_json` now retries the call itself (not just JSON extraction) and the verifier's `max_tokens` was raised with a "keep reasons under 12 words" instruction to reduce truncation odds.
- **Residual risk this doesn't eliminate**: a sufficiently confident, well-phrased fabrication that happens to *sound* like a paraphrase of the source could still slip past this verifier — this is a real gap, not a solved problem. Treat a pass as "no obvious fabrication caught," not an independent fact-check.

## What's still open (not fixed by this pass)

- **code-trail, cosmic-window, market-lens, thought-tides have no passing re-render right now.** Their currently-configured Firecrawl queries keep surfacing pages/videos too thin (relative to that channel's shot grammar) to honestly fill 2-3 of the required beats. Options, for you to decide, not decided here: (a) adjust `firecrawlQueryPatterns` to target richer long-form sources, (b) simplify those channels' shot grammar to drop the beat(s) that keep failing, or (c) accept these channels render less often (only on days a good source appears) rather than forcing content.
- The music-bed/audio pieces of these 4 blocked runs never got a chance to matter since the gate stopped them before rendering — nothing downstream needs cleanup for them.

Awaiting your call on Track 4 before proceeding.
