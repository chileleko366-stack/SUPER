# Fabrication Audit — Thought Tides (`thought-tides`)

**Run audited:** `out/thought-tides/20260710-112927/`
**Audited:** 2026-07-11

## What Firecrawl actually returned

- **Query:** `stoicism philosophy shorts 2026`
- **Title:** The Stoic Way To Survive 2026
- **URL:** https://www.youtube.com/watch?v=nV9mLzyDrK8&vl=en
- **Description (verbatim, as captured in `topic.json`):**
  > 54 Stoic Truths For Life · 9 Things to CUT From Your Life In 2026 | Stoicism Philosophy Marcus Aurelius · 19 Stoic Stories That Will Improve Your ...

The source is a YouTube search-results listing — a list of *video titles only*. No video was ever transcribed or watched; none of the actual content of any of these videos was retrieved.

## Claim-by-claim findings

### hook — "The impediment to action advances action."
- **Status:** GENERAL-KNOWLEDGE, verified accurate — this is a real, correctly-quoted line from Marcus Aurelius's *Meditations*, Book 5. It does not appear in the Firecrawl snippet at all (which only lists video titles, not quotes), so it's entirely from NIM's training knowledge rather than the sourced material — but it checks out as a real, accurately attributed quote.

### concept_card — "The Stoic Way to Survive 2026"
- **Status:** SOURCE-GROUNDED — exact match to the source video title.

### bridge — "Cutting what holds you back is key to freedom."
- **Status:** N/A — generic framing (echoes the "9 Things to Cut" title without adding a new specific claim).

### example — "Imagine a cluttered desk, a symbol of mental clutter."
- **Status:** ILLUSTRATIVE-BY-DESIGN — explicitly framed with "Imagine," a metaphor rather than a factual claim.

### explanation — "The Stoics teach us to identify and release what's unnecessary."
- **Status:** GENERAL-KNOWLEDGE — a fair, uncontroversial characterization of Stoic philosophy broadly. Not from the source snippet, not attributed to any specific text or person, low risk.

### mechanism — "9 Things to Cut From Your Life In 2026"
- **Traits:** Clutter, Distractions, Unnecessary
- **Status:** SOURCE-GROUNDED (title) / FABRICATED (implied content) — the *title* is lifted directly from the source. But the video's actual 9 items were never fetched — NIM never saw them. The script presents this as if introducing that video's real content, then only offers three generic invented category labels (Clutter, Distractions, Unnecessary) as if they were drawn from the video, when nothing about the video's actual 9 items was ever retrieved.

### conclusion — "Cut the unnecessary to free your mind and find inner strength."
- **Status:** N/A — generic CTA.

## Summary

| Status | Count |
|---|---|
| Source-grounded | 2 |
| General-knowledge, verified accurate | 2 |
| Illustrative-by-design | 1 |
| Fabricated (implied content behind a borrowed title) | 1 |
| N/A (no claim) | 2 |

**Overall risk: LOW-MODERATE.** No invented named entities or dates. The main issue is more subtle than the other channels: this script borrows two real video *titles* verbatim (making it look well-sourced) but never actually retrieves what's inside either video, then fills the gap with generic-sounding invented specifics (the three "traits") presented as if they summarize that real content.
