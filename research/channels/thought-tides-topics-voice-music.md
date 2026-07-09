# Thought Tides — Topics, Voice, Music (Phase 2)

Channel: **Thought Tides** — philosophy, ethics, classic and modern schools
of thought. Tone: contemplative, calm, thought-provoking.

All topic examples cite a URL actually returned by a Firecrawl `/v1/search`
call on 2026-07-09. Voice and music sourcing claims cite a URL actually
scraped where a specific factual claim (license, format) is made; where a
claim could not be verified within budget it is marked "not found" /
flagged in Open Gaps rather than invented.

## Topics (8-10 real current examples)

1. **"Stoicism: Become Undefeatable"** — Stoic-resilience Short, direct
   philosophy-as-life-advice framing.
   https://www.youtube.com/shorts/LFHYTObcbNc
2. **Johnathan Bi — "Nietzsche: Stoicism is a Coping Mechanism"** —
   comparative-philosophy Reel (Nietzsche's critique of Stoicism), from an
   established philosophy-explainer creator on Instagram.
   https://www.instagram.com/reel/DZIFhayjKht/
3. **Existentialism vs. absurdism explainer** — "Existentialism and
   absurdism are two of the most popular [schools]..." comparative-schools
   Reel.
   https://www.instagram.com/reel/DMDO_-4ormL/?hl=en
4. **Camus — "The 3 antidotes to the absurdity of life"** — Camus/absurdism
   summary post (via The Marginalian).
   https://www.facebook.com/TheMarginalian/posts/at-the-link-albert-camus-on-the-3-antidotes-to-the-absurdity-of-life/1551362123024954/
5. **"Absurdism's 10 Lessons for Life (Albert Camus)"** — listicle-format
   Camus explainer video.
   https://www.youtube.com/watch?v=SIUaNIylS88
6. **Alan Watts — "Happiness is NOT the Meaning of Life"** — Watts-narrated
   meaning-of-life piece (archival-audio-over-visuals format, very common in
   this niche).
   https://www.youtube.com/watch?v=RsdoJ9x8IBs
7. **Alan Watts — "The Dream of Life"** — Watts archival-speech piece,
   inspirational/philosophical framing.
   https://www.youtube.com/watch?v=wU0PYcCsL6o
8. **The Daily Stoic — "Reinvent your life in 2025 with these 8 Stoic
   practices"** — practice-listicle Reel from a major Stoicism publisher
   (Ryan Holiday's brand).
   https://www.instagram.com/reel/DDkITf-pfCr/
9. **Ryan Holiday reads a passage from Marcus Aurelius' Meditations** —
   direct-primary-text-reading format.
   https://www.instagram.com/reel/DTJDUjAEs10/
10. **"Stoicism isn't about perfection" — Marcus Aurelius / Meditations**
    — single-idea Stoic-practice Reel.
    https://www.instagram.com/reel/DVoR5lQlMEv/?hl=en

Observed pattern across all 10: single-thinker or single-school framing,
short quoted/paraphrased primary-source line as the hook, practical
"what this means for your life today" close. Stoicism (Marcus
Aurelius/Epictetus/Seneca, via Daily Stoic/Ryan Holiday) and
existentialism/absurdism (Camus, Sartre) are the two most represented
schools in current short-form supply; Alan Watts (Eastern-influenced,
meaning-of-life register) is the most represented individual voice outside
Stoicism. This gives Thought Tides three natural pillars to rotate:
Stoic practice, existentialist/absurdist meaning-making, and
Watts-style contemplative/Eastern-adjacent reflection — without
duplicating any single creator's exact angle.

## Voice Provider

**Recommended: Piper TTS**, engine repo https://github.com/rhasspy/piper
(original, MIT-licensed, now archived) with active development continuing
at https://github.com/OHF-Voice/piper1-gpl (confirmed via Firecrawl scrape:
license badge reads **GPL-3.0**).

- **Self-hostable**: yes — runs as a local ONNX-based CPU inference binary/
  Python package, no cloud dependency.
- **GitHub Actions ubuntu runner, CPU-only**: yes — Piper is explicitly
  built for low-resource CPU inference (its own description targets
  "devices like the Raspberry Pi 4," per
  https://sourceforge.net/projects/piper-tts.mirror/); a GitHub Actions
  `ubuntu-latest` runner has materially more CPU/RAM than a Pi 4, so a
  ~150-word script (roughly 60-90 seconds of narration) is comfortably
  within a normal job timeout.
- **License**: two repos exist and they differ —
  - `rhasspy/piper` (legacy, archived Oct 2025): **MIT license** (confirmed
    via scrape of https://github.com/rhasspy/piper — "### License / MIT
    license").
  - `OHF-Voice/piper1-gpl` (actively maintained successor): **GPL-3.0
    license** (confirmed via scrape of
    https://github.com/OHF-Voice/piper1-gpl — "### License / GPL-3.0
    license"). GPL-3.0 permits commercial use of the software; it is a
    copyleft license on the *engine code itself*. Invoking the Piper CLI/
    library as an external process to generate audio files (not
    statically linking it into proprietary distributed software) does not
    place the generated audio output or the surrounding pipeline under
    GPL — but this repo naming itself "piper1-**gpl**" is a real signal
    the operator should be aware of before deep-integrating the Python
    library directly into a proprietary codebase, as opposed to shelling
    out to it.
- **CPU inference time for ~150 words**: not independently benchmarked in
  this research pass (no local Piper install was run). Piper's own
  positioning as a "fast, local" TTS system sized for Raspberry Pi 4-class
  hardware (per the SourceForge mirror description above) strongly implies
  real-time or faster-than-real-time synthesis on a GitHub Actions
  CPU runner, which has far more headroom than a Pi 4 — but this specific
  number should be benchmarked once in the actual CI environment before
  relying on it for job-timeout budgeting. Flagged in Open Gaps.
- **Voice choice for this persona**: Piper ships many per-language,
  per-speaker checkpoints at "low/medium/high" quality tiers (confirmed via
  scrape of https://rhasspy.github.io/piper-samples/ — quality tiers
  documented as x_low/low/medium/high, 16-32M params). The specific voice
  list itself is populated client-side by JavaScript on that samples page
  and was not extracted by the Firecrawl markdown scrape (**not found** in
  this pass — see Open Gaps). Piper voices are commonly distributed via the
  Hugging Face `rhasspy/piper-voices` repository, where each voice
  checkpoint has its own `MODEL_CARD.md` stating that specific voice's
  license (these vary per voice/per training corpus and are **not** all
  identical to the engine's own MIT/GPL-3.0 license). **Action for the
  operator**: before committing to a specific checkpoint (a medium/high
  quality `en_US` or `en_GB` male voice with a slower, measured delivery is
  the right register for this contemplative persona), pull that exact
  voice's `MODEL_CARD.md` from the Hugging Face repo and confirm its
  license permits commercial use — do not assume it inherits the engine's
  license.

## Music Sourcing

**Method to identify trending tracks in this niche:**

1. Sample the audio attached to current high-performing philosophy
   Shorts/Reels directly (the same creators/URLs used for the topics list
   above are also a live feed of what audio those creators are currently
   pairing with contemplative content — check each platform's native
   "used in N videos" / trending-audio indicator on the Reel/Short itself).
2. Cross-check candidate tracks against each platform's own commercial-use
   safe list before use: Instagram/TikTok expose a "Commercial Music
   Library" filter on their sound picker specifically for branded/monetized
   content — per
   https://www.instagram.com/reel/DM8HeK0MRhI/?hl=en ("the easiest way to
   find copyright-free music for your brand... hit the drop-down arrow on
   sounds and choose commercial library").
3. For YouTube specifically, use the YouTube Audio Library, which Google
   maintains free of Content ID claims by design — per
   https://www.foximusic.com/blog/youtube-shorts-copyright-music-library-guide/
   ("The Audio Library provides free production music that never touches
   your monetization... You find a trending sound in the Shorts library.").
4. For obtaining stems/instrumentals of a track that isn't already
   licensed production music: **not found** — no specific stem-separation
   tool or workflow was verified via Firecrawl in this research pass; if
   the operator wants this workflow, it needs separate verification (e.g.
   an open-source source-separation model run locally) rather than being
   assumed here.

## Copyright Risk Flag

**This is a tradeoff the human operator must decide, not something this
research resolves.** Two paths exist for music on Thought Tides, and they
carry materially different risk profiles:

- **Trending-but-risky**: pairing a currently-trending, label-owned track
  (even instrumental-only, even after stem-separating out the vocals) with
  automated, monetized Shorts content still carries real Content ID /
  takedown risk. Removing the vocal track does **not** clear the
  copyright on the underlying musical composition and sound recording —
  the composition (melody, harmony, arrangement) is still owned by the
  original rights holder, and rights holders' Content ID fingerprints
  frequently match instrumental stems, not just the full mix with vocals.
  Platform-native "free to use" grants (e.g. Instagram/TikTok's in-app
  sound library) are typically scoped to *that platform's own player* and
  do **not** automatically extend to re-uploading the same audio on
  YouTube or to a separately-monetized automated pipeline — per the
  licensing-scope discussion at
  https://www.reddit.com/r/COPYRIGHT/comments/1o8bnmp/since_instagram_and_tiktok_allows_you_to_use_any/.
  Using a trending track can meaningfully help discovery/reach, but on a
  faceless, automated, multi-video-per-day channel it also compounds strike
  risk across the whole channel if even one video gets flagged.
- **Royalty-free-but-safer**: sourcing from YouTube's own Audio Library or a
  licensed royalty-free/production-music library (e.g. the kind referenced
  at
  https://alibimusic.com/blog/royalty-free-music-and-sfx-the-secret-to-boosting-tiktok-reels-and-shorts-performance
  ) avoids Content ID risk almost entirely and keeps monetization safe, at
  the cost of not riding an actively-trending sound and potentially sounding
  more generic/library-music than what top creators in this niche are
  currently using.

**Recommendation is intentionally not made here.** The operator should pick
per the channel's actual risk tolerance and monetization stakes — a
low-stakes/testing phase might reasonably use trending audio to validate
format-market fit, while a channel already earning ad revenue at volume
should weight the royalty-free path much more heavily given how strike
history can affect a whole channel/account.

## Open Gaps

- Piper's specific voice checkpoint list (names, per-voice speaker
  characteristics, per-voice license) could not be extracted — the sample
  page at https://rhasspy.github.io/piper-samples/ populates its voice
  dropdown via client-side JavaScript that the Firecrawl markdown scrape
  did not execute/capture. The operator should browse
  https://huggingface.co/rhasspy/piper-voices directly (or run
  `piper --list-voices` locally) to pick and license-check a specific
  `en_US`/`en_GB` medium-or-high-quality voice before committing to one.
- No live CPU-inference benchmark for a ~150-word script was run in this
  research pass (would require installing Piper locally, out of scope for
  a research-only pass per the brief). Should be measured once in the
  actual GitHub Actions ubuntu runner before finalizing job-timeout
  assumptions.
- Stem-separation / instrumental-sourcing tooling for non-library trending
  tracks was not verified — flagged as "not found" rather than guessed.
- This document's topic list is a snapshot of currently-surfaced Firecrawl
  search results on 2026-07-09, not a comprehensive trend report; topic
  selection for actual production should re-run a similar search
  periodically rather than treating this list as evergreen.
