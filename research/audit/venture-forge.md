# Fabrication Audit — Venture Forge (`venture-forge`)

**Run audited:** `out/venture-forge/20260710-112941/`
**Audited:** 2026-07-11

## What Firecrawl actually returned

- **Query:** `startup business model breakdown bankruptcy 2026`
- **Title:** Small Business Bankruptcies Surging in 2026
- **URL:** https://www.securitasglobal.com/risk-perspectives/small-business-bankruptcies-surging-in-2026/
- **Description (verbatim, as captured in `topic.json`):**
  > Small business bankruptcy filings are rising sharply in 2026, and the numbers tell a consistent story across every major data source.

This source describes a general, industry-wide trend. It names **no specific company anywhere.**

## Claim-by-claim findings

### hook — "LendingClub Bankruptcies Skyrocketing"
- **Status:** FABRICATED — **highest-severity finding in this audit.** "LendingClub" is a real, specific, named company. It appears nowhere in the Firecrawl title, URL, or description, which is about small-business bankruptcies as a general economic trend, not any single lender or company going bankrupt. This is structurally identical to the Charlie Kirk date problem: NIM attached a specific, real, checkable proper noun to a claim with zero source support. As written, this beat asserts something false and defamatory-shaped about a real, identifiable company (LendingClub is a real, currently-operating public company; nothing in the source or reality supports "bankruptcies skyrocketing" at LendingClub specifically). This beat renders as the hook's on-screen text and should not go out as-is.

### concept_card — "Small Business Bankruptcy Crisis"
- **Traits:** EconomicDownturn, SmallBusinessStruggles, FinancialStress
- **Status:** SOURCE-GROUNDED — matches the general theme of the source title.

### bridge — "But what's driving this surge in bankruptcies?"
- **Status:** N/A — transition.

### example — "A struggling small business owner facing mounting debt"
- **Status:** ILLUSTRATIVE-BY-DESIGN — generic illustrative scene-setting, not a specific factual claim.

### explanation — "It's a perfect storm of rising interest rates, inflation, and stagnant revenue growth"
- **Status:** FABRICATED (plausible but unsupported) — the source snippet never states a cause; it only asserts that filings are rising. This causal explanation is entirely NIM-supplied. It's a plausible macro narrative (these are real, generically-cited causes of small-business distress in this period) but was not in the source, so presenting it as "the" explanation is unsupported.

### mechanism — "The Debt Burden on Small Businesses"
- **Traits:** DebtToEquityRatio, CashFlowProblems, LiquidityCrisis
- **Status:** N/A / NOT-RENDERED — this beat's primitive is `InfoCard` (per `channels/venture-forge.json`), which only reads `text` and `traits`. The `text` and `traits` here are generic, no specific claim.

  This same `mechanism` object also contains a `timelineEvents` array and a `chartData` object that NIM generated **unprompted** (this channel has no `TimelineReveal` or `DataChart` beat at all):
  - `timelineEvents`: "Interest Rates Rise" → 2022, "Inflation Spikes" → 2023, "Small Businesses Struggle" → 2024 — plausible-sounding but entirely invented specific-year attributions, none traceable to the source.
  - `chartData`: fabricated bankruptcy counts by year (2022: 100, 2023: 200, 2024: 500, 2025: 1000) in a Chart.js-shaped object (`{labels, datasets}`) that doesn't even match the `{label, value}` shape `resolve_chart_data` expects elsewhere in this pipeline.
  - **Status: NOT-RENDERED** — `run_channel.py`'s `InfoCard` handling never reads these fields, so none of this reaches the screen in this run. Still worth flagging: it shows NIM inventing specific years and specific bankruptcy-count numbers with no prompting and no source basis, which is exactly the failure mode this audit is looking for — it just happened to land in a field the pipeline ignores this time.

### conclusion — "Start prioritizing cash flow management and debt reduction to stay afloat in turbulent economic times"
- **Status:** N/A — generic CTA.

## Summary

| Status | Count |
|---|---|
| Source-grounded | 1 |
| Fabricated (rendered) | 2 (hook, explanation) |
| Fabricated (generated but not rendered) | 1 (mechanism's stray timelineEvents/chartData) |
| Illustrative-by-design | 1 |
| N/A (no claim) | 2 |

**Overall risk: HIGH.** The hook's "LendingClub" attribution is the single worst finding across all 8 channels — a real, named, specific company falsely tied to a bankruptcy trend claim with no source support whatsoever, rendered directly as on-screen/spoken text. This channel needs to be pulled and re-rendered, not just flagged.
