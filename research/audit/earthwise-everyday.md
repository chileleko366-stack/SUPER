# Fabrication Audit — Earthwise Everyday (`earthwise-everyday`)

**Run audited:** `out/earthwise-everyday/20260711-124820/`
**Audited:** 2026-07-11

## What Firecrawl actually returned

- **Query:** `sustainable living eco-friendly tips 2026`
- **Title:** 15 Easy Tips For More Sustainable Living in 2026
- **URL:** https://www.extraspace.com/blog/home-organization/tips-for-sustainable-living-in-new-year/
- **Description (verbatim, as captured in `topic.json`):**
  > Grow Your Own Food; Try Your Hand at Composting; Use Less, Save More; Wash with Cold Water; Ditch Single-Use Products; Reduce Your Carbon ...

## Claim-by-claim findings

### hook — "Start your eco-friendly journey with these simple tips!"
- **Status:** N/A — generic framing, no specific claim.

### concept_card — "Sustainable Living for a Greener Tomorrow"
- **Traits:** Eco-Friendly, Green Living, Low-Waste
- **Status:** SOURCE-GROUNDED — restates the source's theme.

### bridge — "Making small changes can add up to make a big difference!"
- **Status:** N/A — generic, no specific claim.

### example — "Compost food scraps to create nutrient-rich soil"
- **Status:** SOURCE-GROUNDED (topic) / GENERAL-KNOWLEDGE (mechanism) — "composting" is explicitly one of the source's bullet points; "creates nutrient-rich soil" is well-established general knowledge about composting, not stated in the snippet itself but not in tension with it either.

### explanation — "Composting helps reduce waste and supports healthy plant growth!"
- **Status:** GENERAL-KNOWLEDGE — accurate, uncontroversial, but not present in the source snippet verbatim.

### mechanism — "How Composting Works: A Simple Guide"
- **Traits:** Composting Basics, Waste Reduction, Soil Enrichment
- **Status:** GENERAL-KNOWLEDGE — heading implies a specific "how it works" explanation is coming, but no actual mechanism/process detail follows in the beat's own text; traits are generic category labels, not specific factual claims.

### conclusion — "Try composting at home to reduce your waste and support local ecosystems!"
- **Status:** N/A — generic CTA.

## Summary

| Status | Count |
|---|---|
| Source-grounded | 2 |
| General-knowledge | 3 |
| N/A (no claim) | 2 |

**Overall risk: LOW.** No specific numbers, dates, names, or named entities were invented. The script stays within one well-established general topic (composting) that is directly named in the sourced list, and every claim made about it is uncontroversial common knowledge rather than a fabricated specific.
