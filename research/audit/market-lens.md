# Fabrication Audit — Market Lens (`market-lens`)

**Run audited:** `out/market-lens/20260711-125230/`
**Audited:** 2026-07-11

## What Firecrawl actually returned

- **Query:** `inflation tariffs economy 2026`
- **Title:** The Effects of Tariffs on the Components of Inflation
- **URL:** https://www.frbsf.org/research-and-insights/publications/economic-letter/2026/03/effects-of-tariffs-on-components-of-inflation/
- **Description (verbatim, as captured in `topic.json`):**
  > Panel B shows that a 10% increase in tariffs generates a peak increase of about 0.6 percentage point for services inflation in year 3 rather than in year 2.

This is a real SF Fed research letter, and the description gives exactly **one** real number: a 0.6-point peak in year 3 (as opposed to year 2).

## Claim-by-claim findings

### hook — "Tariffs hike inflation by 0.6 percentage point in year 3, a surprise finding."
- **Status:** SOURCE-GROUNDED — the 0.6-point / year-3 figure matches the source exactly.

### concept_card — "The Effects of Tariffs on Inflation"
- **Traits:** Tariffs, Inflation, Economic Policy
- **Status:** SOURCE-GROUNDED — restates the source title.

### bridge — "Let's dive into the mechanism behind this surprising result."
- **Status:** N/A — transition.

### data_snapshot — chartData `[Year 1: 0, Year 2: 0.2, Year 3: 0.6]`
- **Status:** MIXED / FABRICATED interim points — Year 3's 0.6 is the one real number from the source. **Year 1 (0) and Year 2 (0.2) do not appear anywhere in the Firecrawl snippet** — NIM invented an interpolated ramp to make a 3-point chart. The chart-generation prompt does instruct NIM to keep DataChart numbers "illustrative," and the spoken line is hedged ("For example... might look like this"), which is the one thing keeping this from being a clean fabrication. But visually, splicing two made-up points onto one real cited statistic in the same chart blurs the "illustrative example" framing — a viewer has no way to tell Year 3's 0.6 is the real finding while Year 1/Year 2 are invented filler.

### explanation — "This difference in timing is due to changes in global supply chains."
- **Status:** FABRICATED — the source snippet states *that* the effect peaks in year 3 rather than year 2, but gives no *reason* for the timing difference. "Changes in global supply chains" is a plausible-sounding but entirely NIM-supplied causal explanation with no support in the sourced text.

### mechanism — "Tariffs cause inflation by disrupting global supply chains."
- **Traits:** Tariffs, Supply Chains, Inflation
- **Status:** FABRICATED — restates and reinforces the same ungrounded causal claim as `explanation`, presented as the on-screen section heading (i.e., presented with more authority, not less).

### conclusion — "Assessing the timing of tariff effects is crucial for informed policy decisions."
- **Status:** N/A — generic, no new claim.

## Summary

| Status | Count |
|---|---|
| Source-grounded | 2 |
| Mixed (real stat + fabricated filler in same chart) | 1 |
| Fabricated | 2 |
| N/A (no claim) | 2 |

**Overall risk: HIGH.** This channel is the most dangerous shape of fabrication in the whole audit: it opens with a real, correctly-cited statistic from a real Fed research letter, which lends the *rest* of the script an air of authority it hasn't earned — the causal explanation for *why* the effect is delayed (global supply chains) is invented outright, and the chart pads two fake numbers around the one real one. A viewer has no way to distinguish the cited finding from the invented mechanism/numbers around it.
