> **Update 2026-07-11 (later same day):** the structural fix this summary recommends
> (full-article sourcing + an automated grounding gate) has been built and validated
> against all 8 channels. See [GATE_VALIDATION_2026-07-11.md](GATE_VALIDATION_2026-07-11.md)
> for full results — short version: venture-forge's LendingClub fabrication and 3 other
> HIGH-risk findings below are now either fixed at the source or caught and blocked before
> render; 4 of 8 channels currently render clean, 4 are correctly blocked pending richer
> sourcing for those specific topics. venture-forge's original bad render was never public
> and has been quarantined (`out/_quarantined/venture-forge-20260710-112941/`).

# Fabrication Audit — Cross-Channel Summary

**Audited:** 2026-07-11
**Scope:** the 8 production channels with rendered runs (`code-trail`, `cosmic-window`, `earthwise-everyday`, `echoes-of-ages`, `market-lens`, `silver-screen-insight`, `thought-tides`, `venture-forge`). Each channel's full claim-by-claim breakdown is in its own file in this directory.

## Method

For each channel, the audit read the actual `out/<slug>/<run_id>/topic.json` (exactly what Firecrawl returned that run: one query, one title, one URL, one short meta-description) and the corresponding `script.json` (everything NIM generated from it), and checked every specific factual claim in the script against that snippet. Nothing else was treated as "ground truth" — not general web search, not re-fetching the source URL today — because the goal is to see what the pipeline actually had to work with at generation time, the same gap that let the Charlie Kirk date through.

The core structural finding, true across all 8 channels: **Firecrawl only ever returns a title + a one-sentence meta-description, never full article text.** Every script beat beyond a bare restatement of that title/description is necessarily NIM filling in from its own training knowledge, not the sourced material. Whether that's a problem depends entirely on whether NIM's fill-in happens to be true.

## Risk ranking

| Channel | Risk | Headline finding |
|---|---|---|
| **venture-forge** | HIGH | Hook falsely names a real company ("LendingClub Bankruptcies Skyrocketing") with zero source support — closest analogue to the Charlie Kirk incident, and it's in the rendered hook. |
| **market-lens** | HIGH | Opens with one real, correctly-cited statistic (0.6pp / year 3), which lends unearned authority to an invented causal mechanism ("global supply chains") and two fabricated interim chart values spliced next to the real one. |
| **silver-screen-insight** | HIGH | Firecrawl's own snippet was truncated mid-sentence twice; NIM filled in a specific director attribution, a specific theme, an invented scene, and an invented narrative technique for a real, named film. |
| **cosmic-window** | HIGH | Invents the wrong physical mechanism for a real reported phenomenon (attributes the "jellyfish" launch effect to satellites burning up on reentry, which is a different, unrelated phenomenon). |
| **echoes-of-ages** | MODERATE (process risk) | All 5 on-screen `TimelineReveal` dates were supplied by NIM with no dates anywhere in the source — this run's dates all independently check out as correct, but that's luck, not a verification step. This is the exact beat type that produced the Charlie Kirk date; the pipeline still has no fact-check gate here. |
| **code-trail** | MODERATE | Invents a specific "GitHub trending algorithm" explanation the source (a bare repo-name list) never described. |
| **thought-tides** | LOW-MODERATE | Borrows two real video titles verbatim (looks well-sourced) but never retrieves either video's actual content, then fills the gap with generic invented category labels. |
| **earthwise-everyday** | LOW | Stays within one topic explicitly named in the source (composting); all claims beyond the snippet are uncontroversial, verifiably-true general knowledge, no invented specifics/names/dates. |

## What to do with this

Per your instruction, nothing has been auto-fixed. Ranked by what most needs attention before anything else goes out:

1. **venture-forge** — the LendingClub claim is a false statement about a real, named company. Highest priority to pull/re-render regardless of anything else.
2. **market-lens, silver-screen-insight, cosmic-window** — each mixes a thin grain of real sourcing with confidently-asserted invented specifics (causal mechanisms, a director/scene attribution, a wrong physical explanation). Same fix shape: either re-prompt to hedge unsupported claims, or source a fuller article body (not just title+description) before scripting.
3. **echoes-of-ages** — not wrong this run, but structurally the highest-exposure beat type (`TimelineReveal` renders NIM dates as literal badges from a source that never has dates). Worth a standing fact-check step even though nothing's broken today.
4. **code-trail, thought-tides** — lower stakes (no named-entity or date claims at risk), but same root cause.
5. **earthwise-everyday** — no action needed.
