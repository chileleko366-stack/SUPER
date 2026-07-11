# Fabrication Audit — Silver Screen Insight (`silver-screen-insight`)

**Run audited:** `out/silver-screen-insight/20260710-113119/`
**Audited:** 2026-07-11

## What Firecrawl actually returned

- **Query:** `film analysis hidden meaning 2026`
- **Title:** Disclosure Day (2026) — Review. It's been called Steven ... - Medium
- **URL:** https://medium.com/b-stories/disclosure-day-2026-review-db5cd812264a
- **Description (verbatim, as captured in `topic.json`):**
  > The 2026 genre film does make use of genre but prioritizes the deepest human themes imaginable. Representing humanity's relationship with ...

Both the title and description are **truncated mid-sentence by Firecrawl itself** ("It's been called Steven ...", "Representing humanity's relationship with ..."). This means even the two claims that look source-grounded are built on guessing how a cut-off sentence ends — the pipeline never fetched the full article.

## Claim-by-claim findings

### hook — "Steven Soderbergh's latest film, Disclosure Day, holds secrets within its genre-bending narrative."
- **Status:** UNVERIFIABLE (plausible completion of a truncated title) — the title fragment ends "It's been called Steven ...", strongly suggesting "Steven Soderbergh" was the intended completion, but this is Firecrawl's truncation plus NIM's guess, not a confirmed fact. Full attribution of a real film to a real, named director based on a cut-off sentence is a specific, checkable claim that was never actually verified.

### concept_card — "Humanity's Relationship with Truth"
- **Traits:** Symbolism, Cinematic Technique, Existentialism
- **Status:** FABRICATED (filled-in-the-blank) — the description literally cuts off at "Representing humanity's relationship with ..." with no word after "with." NIM supplied "Truth" to complete the sentence. This could just as easily have been "technology," "mortality," "each other," etc. — this is NIM inventing the ending of a sentence it was never shown and presenting the invented ending as the film's theme.

### bridge — "But what does it reveal about our connection to reality?"
- **Status:** N/A — transition, though it silently assumes the invented "Truth" theme from `concept_card`.

### example — "A close-up of a character's face, reflecting on their choices."
- **Status:** FABRICATED — describes a specific shot/scene in a specific named film. Nothing in the source snippet describes any scene, shot, or visual moment. This is a concrete visual claim about real film content invented from nothing.

### explanation — "Through non-linear storytelling and subtle visual cues, Soderbergh crafts a thought-provoking exploration of human nature."
- **Status:** FABRICATED — attributes a specific narrative technique ("non-linear storytelling") to a specific named director's specific named film. The source snippet says nothing about the film's structure or technique. Soderbergh has used non-linear structure in some past films, so this is a plausible-sounding guess, but it's asserted as established fact about *this* film with zero support.

### mechanism — "The Power of Misdirection in Film"
- **Traits:** Non-Linear Storytelling, Visual Cues, Audience Manipulation
- **Status:** FABRICATED — restates and hardens the same ungrounded "non-linear storytelling" claim from `explanation` as an on-screen heading.

### conclusion — "Watch Disclosure Day with a critical eye to uncover its hidden meanings and techniques."
- **Status:** N/A — generic CTA, but leans on the invented "hidden meanings/techniques" established above.

## Summary

| Status | Count |
|---|---|
| Unverifiable (plausible but unconfirmed) | 1 |
| Fabricated | 4 |
| N/A (no claim) | 2 |

**Overall risk: HIGH.** This is the second-clearest fabrication case in the slate. Because Firecrawl's own snippet was truncated mid-sentence twice, NIM had almost nothing to work with — and instead of hedging, it filled in a specific director, a specific theme, a specific scene, and a specific narrative technique, all presented as confirmed facts about a real, identifiable film. If the director attribution is wrong, this is a false, specific, checkable claim about a real person's real work — structurally identical to the Charlie Kirk date issue.
