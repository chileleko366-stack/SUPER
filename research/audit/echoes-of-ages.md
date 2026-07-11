# Fabrication Audit — Echoes of Ages (`echoes-of-ages`)

**Run audited:** `out/echoes-of-ages/20260711-123714/`
**Audited:** 2026-07-11

## What Firecrawl actually returned

- **Query:** `on this day in history ancient world event`
- **Title:** Today in History - On This Day
- **URL:** https://www.onthisday.com/today/events.php
- **Description (verbatim, as captured in `topic.json`):**
  > Today in History · Emperor Antoninus Pius · Battle of the Golden Spurs · Henry VIII Excommunicated · Return of Samuel de Champlain · Euclid's Parallel Postulate.

The source is a bare list of event *names* with **no dates attached at all** — every date in this script's `timelineEvents` was supplied by NIM from its own training knowledge, not from the Firecrawl result.

## Claim-by-claim findings

### hook — "A day that shaped empires, shook thrones, and forged destinies."
- **Status:** N/A — atmospheric framing, no specific claim.

### context_card — "Emperor Antoninus Pius, Battle of the Golden Spurs, and more."
- **Traits:** AncientRome, MedievalBattle, HistoricalTensions
- **Status:** SOURCE-GROUNDED — names lifted directly from the source list.

### timeline_map — 5 `timelineEvents` (this is the highest-stakes beat: dates render as literal on-screen badges)
| Label | Date shown | Status | Note |
|---|---|---|---|
| Roman Empire at its peak | 138-161 | GENERAL-KNOWLEDGE, verified accurate | Matches Antoninus Pius's real reign (138–161 CE). Not in the source snippet (which has no dates), but independently correct. |
| Battle of the Golden Spurs | 1302 | GENERAL-KNOWLEDGE, verified accurate | Real date (11 July 1302), matches today's date in-context. Not in the source snippet. |
| Henry VIII Excommunicated | 1533 | GENERAL-KNOWLEDGE, verified accurate | Real date (excommunication bull, 1533). Not in the source snippet. |
| Euclid's Parallel Postulate published | c. 300 BCE | GENERAL-KNOWLEDGE, verified accurate | Correct general dating for Euclid's *Elements*. "published" is a slight overclaim (there's no publication event / exact date for ancient texts), but the hedge "c." matches the system prompt's instruction to avoid false precision. Not in the source snippet. |
| Samuel de Champlain returns to Quebec | 1608 | GENERAL-KNOWLEDGE, verified accurate | Consistent with Champlain's founding of Quebec in 1608. Not in the source snippet. |

**None of these five dates came from Firecrawl.** They all happen to check out against real history, but this is exactly the mechanism by which the Charlie Kirk date was fabricated — NIM supplying a specific date from general knowledge with nothing in the sourced material to catch it if it's wrong. This run got lucky (or NIM's general knowledge of these particular events is solid); the pipeline has no verification step that would have caught it if one of these five had been wrong.

### turning_point — "A pivotal day in the annals of history, where empires clashed."
- **Status:** N/A — generic framing.

### rise — "As empires rise and fall, the consequences of their actions unfold."
- **Status:** N/A — generic framing.

### legacy — "A lasting impact on the course of human civilization."
- **Traits:** EmpireBuilding, ConflictResolution, LegacyOfPower
- **Status:** N/A — generic framing, no specific claim.

### conclusion — "Remember the turning points that shaped the world we live in today."
- **Status:** N/A — generic CTA.

## Summary

| Status | Count |
|---|---|
| Source-grounded | 1 |
| General-knowledge, verified accurate | 5 |
| N/A (no claim) | 5 |

**Overall risk: MODERATE (process risk, not this-run risk).** Every specific date in this run happens to be independently verifiable and correct — I checked all five by hand. But structurally this channel is the highest-exposure one in the entire slate: `TimelineReveal` renders NIM-supplied dates as literal on-screen badges, and the source only ever supplies bare event *names*, never dates. There is currently no per-run fact-check step between NIM's output and the render — this run's accuracy is NIM getting lucky on well-known dates, not the pipeline verifying anything. Recommend adding a lightweight date cross-check (or at minimum, a manual spot-check pass) for every `TimelineReveal` beat going forward, since this is precisely the beat type that produced the Charlie Kirk incident.
