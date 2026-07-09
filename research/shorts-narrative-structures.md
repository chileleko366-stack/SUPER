# Frame Pacing, Cut Frequency & Narrative Structure — Shared Across Channels

Sourced via Firecrawl search + scrape (2026-07-09). Channel-specific application
notes are in each channel's `research/channels/<slug>-topics-voice-music.md`.

## Sources
- https://virvid.ai/blog/first-3-seconds-hook-faceless-shorts-2026 (hook structures for faceless Shorts, 2026)
- https://www.shortimize.com/blog/youtube-shorts-retention-rate (YouTube Shorts retention metric definitions post March 2025 view-counting change, Jan 2026)
- https://www.opus.pro/blog/ideal-youtube-shorts-length-format-retention
- https://www.insidetheedit.com/blog/pacing-in-video-editing (pacing variation theory)
- https://www.visla.us/blog/guides/video-editing-pacing-what-it-is-and-how-to-control-it/
- https://www.youtube.com/watch?v=V-LSb15ZhtY ("The 70% Retention Rule That Makes Shorts Go Viral")

## The hook window (0-3s) — the single hardest constraint

Per virvid.ai (citing Paddy Galloway's analysis of 3.3B Shorts, and 2025
Zebracat data):
- YouTube's Shorts distribution is decided almost immediately by an
  "explore-and-exploit" test against a seed audience, gated on **swipe-away
  behavior in the first ~3 seconds**.
- Videos with 70-90% "Viewed vs. Swiped Away" (VVSA) get pushed; under 60%
  VVSA collapses distribution. This is a **gate metric**, separate from the
  retention curve — you can have great retention and still die at the gate.
- An immediate hook within the first 2 seconds retains ~19% more viewers
  than a slow start (Zebracat 2025 data via virvid.ai).
- Per Shortimize (Jan 2026): as of March 31 2025 YouTube changed "views" to
  count on any play/replay with no minimum watch time, but **monetization
  (YPP, ad revenue share) is keyed to "Engaged views,"** not raw views — so
  optimizing only for the swipe-away gate isn't sufficient; the full
  retention curve still matters for revenue, not just distribution.

**Five hook structures** (virvid.ai): bold claim, curiosity gap, micro-story
opening, visual shock, direct question. Faceless channels lean harder on
audio-visual hooks (no face/personal-brand recognition to fall back on) —
first line of VO + first visual beat both need to land inside frame 1-2 of
the composition (well under the 3s/180-frame mark at 60fps).

**Hook killers** (virvid.ai): slow builds, generic greetings, buried lead —
if the strongest point lands at 15s, ~70% of the audience is already gone.

## Cut frequency & pacing variation

Per Inside The Edit: pacing should not be uniform-fast or uniform-slow —
audiences are wired for **variation** (dopamine response to novel stimuli).
Design a "pacing rollercoaster": vary cut rate, not just hold it fast
throughout. Applied to our hard-cuts-only spec (Phase 3: no crossfades):
- Hook window (0-3s / frames 0-180 @ 60fps): fastest cut rate of the video —
  establish energy immediately, cuts roughly every 0.5-1s (30-60 frames).
- Body: cut rate should breathe with the VO's cadence and information
  density, not run at a single fixed interval — a dense data-driven beat
  (Market Lens, Penny Blueprint) can sustain faster cuts than a
  contemplative beat (Thought Tides) without feeling frantic, and vice
  versa a slow-cut Thought Tides segment shouldn't just be "the fast rate
  but slower" — it should be a deliberately different rhythm.
- Payoff/CTA: often a beat of relative stillness (held frame, single card)
  right before the loop/end-card — a deliberate pacing dip after the "roller
  coaster," per the variation principle, so the ending doesn't blur past.

This is a directional framework, not a fixed cuts-per-second number — actual
target cut frequency per channel is set from that channel's Phase 1 contact-
sheet analysis of real high-performing references in its niche, not
invented generically here.

## Proven Shorts narrative structures (map to niches)

| Structure | Shape | Best-suited niches (this build) |
|---|---|---|
| Bold claim → proof → payoff | Assert a surprising claim in the hook, spend the body substantiating it, close on the implication | Penny Blueprint, Market Lens, Venture Forge — claim-driven, data-backed niches |
| Curiosity gap → reveal | Pose an unanswered question/mystery in the hook, withhold the answer until late body/payoff | Cosmic Window, Echoes of Ages, Silver Screen Insight — discovery/mystery-driven niches |
| Micro-story opening | Cold-open into a specific scene/moment (a founder's decision, a historical turning point, a psychological anecdote) before zooming out to the general lesson | Echoes of Ages, Venture Forge, Mind Mosaic — narrative-anecdote-friendly niches |
| Direct question → framework answer | Address viewer directly with a question they likely have, answer with a structured framework/list | Mind Mosaic, Thought Tides, Earthwise Everyday — advice/framework-driven niches |
| Visual shock / juxtaposition | Open on a visually striking or counter-intuitive image/data point that doesn't need explanation to land | Code Trail (surprising code/algorithm behavior), Market Lens (dramatic chart), Cosmic Window (scale/size shock) |

Each channel config should pick a **primary** structure matched to its niche
per this table, with a secondary structure as fallback for topics that don't
fit the primary — this is a starting hypothesis to validate against each
channel's own Phase 1 reference set, not a rigid rule.

## Open gap
No first-party A/B data exists yet from these 10 channels — all figures
above are third-party industry data as of early 2026. Once channels are
live, actual VVSA/retention/engaged-view data should supersede these
external benchmarks for pacing decisions.
