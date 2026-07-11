# Fabrication Audit — Cosmic Window (`cosmic-window`)

**Run audited:** `out/cosmic-window/20260711-run2/`
**Audited:** 2026-07-11

## What Firecrawl actually returned

- **Query:** `space astronomy discovery news 2026`
- **Title:** Space.com: NASA, Space Exploration and Astronomy News
- **URL:** https://www.space.com/
- **Description (verbatim, as captured in `topic.json`):**
  > SpaceX launch creates colorful 'jellyfish' in the night sky | Space photo of the day for July 10, 2026 · SpaceX wants to launch 100,000 Starlink satellites to ...

## Claim-by-claim findings

### hook — "A SpaceX launch created a vibrant 'jellyfish' in the night sky"
- **Status:** SOURCE-GROUNDED — directly restates the headline.

### concept_card — "SpaceX's Starlink Satellite Constellation"
- **Traits:** Satellites, SpaceX, Constellation
- **Status:** UNGROUNDED-BUT-PLAUSIBLE — the snippet's second headline fragment ("100,000 Starlink satellites") supports tying this to Starlink, but the description never says the jellyfish photo *is* a Starlink launch specifically (jellyfish plumes are a general upper-atmosphere sunlight-scattering effect seen on many rocket launches, not exclusive to Starlink missions). Reasonable inference, not a confirmed fact from the source.

### bridge — "But what causes this colorful display?"
- **Status:** N/A — rhetorical transition.

### example — "Imagine a thousand twinkling lights scattered across the sky"
- **Status:** ILLUSTRATIVE-BY-DESIGN — explicitly framed with "Imagine," not asserted as fact.

### explanation — "As satellites enter Earth's atmosphere, they burn up, creating bright streaks"
- **Status:** FABRICATED / LIKELY WRONG — this is the highest-severity finding in this channel. The real "jellyfish" phenomenon reported by Space.com is sunlight scattering off an expanding rocket exhaust/fuel-dump plume in the upper atmosphere shortly after launch (a well-documented SpaceX visual effect, distinct from satellite reentry). This script instead describes satellites *burning up on atmospheric reentry* — a real but different phenomenon (space debris/decommissioned-satellite reentry, which produces streaking meteor-like trails, not a jellyfish-shaped plume). NIM appears to have pattern-matched "space + colorful sky effect" to the wrong mechanism. Nothing in the Firecrawl snippet supports either explanation; this one is also physically inconsistent with the described visual (a "jellyfish" shape, not streaks).

### mechanism — "How Satellites Burn Up in the Atmosphere"
- **Traits:** Atmospheric, Entry, Burning
- **Status:** FABRICATED / LIKELY WRONG — same incorrect mechanism as `explanation`, restated as the on-screen section heading. This is the claim most likely to visibly mislead viewers if rendered as-is.

### conclusion — "Next time you see a 'jellyfish' in the night sky, remember the science behind it"
- **Status:** N/A — generic CTA, but implicitly endorses the wrong "science" from `explanation`/`mechanism`.

## Summary

| Status | Count |
|---|---|
| Source-grounded | 1 |
| Ungrounded-but-plausible | 1 |
| Illustrative-by-design | 1 |
| Fabricated / likely wrong | 2 |
| N/A (no claim) | 2 |

**Overall risk: HIGH.** This is the clearest case of NIM inventing an incorrect explanation for a real, named phenomenon rather than just omitting detail — the entire back half of the video (explanation, mechanism, and the conclusion's callback to it) teaches viewers the wrong physical cause for the "jellyfish" effect. Recommend re-sourcing/re-rendering this one specifically.
