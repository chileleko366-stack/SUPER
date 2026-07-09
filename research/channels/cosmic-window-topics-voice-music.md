# Cosmic Window — Topics, Voice & Music (Phase 2)

Channel: astronomy, space missions, celestial objects, discoveries. Persona:
awe-driven, precise science communicator. This document is Phase 2 of the
per-channel research protocol in `docs/RESEARCH_BRIEF.md`. It shares the
16/~15-call Firecrawl budget spent for this channel — see
`research/visual-reference/cosmic-window.md` for the full call log. Nothing
below is invented; every topic has a URL actually returned/fetched by
Firecrawl in this session, and both TTS licenses were read directly off the
relevant GitHub repo pages.

## Topics — 8-10 real current astronomy/space Shorts-suitable stories

All dated items below come from the two live agency press-release archives
actually scraped this session (ESA/Webb and ESA/Hubble), plus one NASA
skywatching page returned by search. All are current as of the research date
(2026-07-09) and are exactly the kind of single-discovery, visual, ~150-word
narratable story this channel format needs.

1. **"Webb uncovers unusual galaxy shaped by cosmic collision"** (Centaurus A,
   JWST 4th-anniversary imagery) — 6 July 2026.
   https://esawebb.org/news/weic2615/
2. **"Webb studies how a planet survived death of its star"** (exoplanet WD
   1856 b transiting a white dwarf) — 1 July 2026.
   https://esawebb.org/news/weic2614/
3. **"Webb pinpoints millions of stars within Cigar Galaxy"** (M82, edge-on
   starburst spiral) — 23 June 2026.
   https://esawebb.org/news/weic2612/
4. **"Webb finds clues to ancient, distant origin of Comet 3I/ATLAS"**
   (third known interstellar comet, unusual chemistry) — 22 June 2026.
   https://esawebb.org/news/weic2613/
5. **"Webb finds strongest evidence yet for 'black hole stars'"** (little red
   dots / LRD spectrum) — 10 June 2026.
   https://esawebb.org/news/weic2610/
6. **"Webb reveals black hole that formed before its galaxy"** (50-million-
   solar-mass black hole, 13+ billion light-years away) — 27 May 2026.
   https://esawebb.org/news/weic2609/
7. **"Hubble details early galaxy transforming neighbourhood"** (UV light
   from a galaxy 1.4 billion years after the Big Bang) — 23 June 2026.
   https://esahubble.org/news/heic2609/
8. **"Hubble unexpectedly catches comet breaking up"** (Comet C/2025 K1
   ATLAS fragmenting mid-observation) — 18 March 2026.
   https://esahubble.org/news/heic2606/
9. **"Hubble identifies one of darkest known galaxies"** (Candidate Dark
   Galaxy-2, dark-matter-dominated) — 18 February 2026.
   https://esahubble.org/news/heic2605/
10. **"What's Up: July 2026 Skywatching Tips from NASA"** (predawn Moon-and-
    planets meetup, a returning comet, prime Milky Way viewing, Saturn's
    rings at a new angle) — evergreen-style monthly skywatching guide, useful
    as a recurring low-effort Shorts format distinct from the one-off
    discovery stories above.
    https://science.nasa.gov/solar-system/whats-up-july-2026-skywatching-tips-from-nasa/

All ten are single-topic, visually anchored (each has an associated
official image/video asset from the source agency), and short enough in
underlying substance to compress to a ~150-word/45-60s script without losing
precision — matching this channel's "precise" half of its tone requirement.

## Voice Provider

**Recommendation: Piper — self-hosted neural TTS, CPU-only.**

Piper is designed specifically for fast, fully local, CPU-only synthesis —
per its own project listing, it is "optimized for devices like the
Raspberry Pi 4" (SourceForge mirror listing, fetched this session:
https://sourceforge.net/projects/piper-tts.mirror/). A GitHub Actions
`ubuntu-latest` runner's x86 CPU is substantially more powerful than a
Raspberry Pi 4, so Piper synthesis is expected to comfortably finish within
a normal job timeout.

**Licensing — verified directly from the two live GitHub repos this
session, and important to get right, because it has changed:**

- The original repo, `rhasspy/piper` (https://github.com/rhasspy/piper), is
  **archived (read-only since Oct 6, 2025)** and is licensed **MIT**
  (license badge read directly off the repo page: "MIT license").
- Active development has moved to `OHF-Voice/piper1-gpl`
  (https://github.com/OHF-Voice/piper1-gpl), which is licensed
  **GPL-3.0** (license badge read directly off that repo page: "GPL-3.0").

Both MIT and GPL-3.0 permit commercial use of the software itself. GPL-3.0
adds copyleft obligations if you *distribute a modified version* of Piper's
own source, but invoking the Piper CLI/binary as a subprocess in a pipeline
to generate an audio file — without modifying and redistributing Piper's own
source — does not require the calling pipeline's own code to be released
under GPL. This distinction should be confirmed with whoever owns legal
sign-off before shipping, since it is a real license, not a formality, and
the project changed license between the archived and active versions.

**Specific voice checkpoint:** Piper voices are distributed separately from
the engine (`rhasspy/piper-voices` on Hugging Face). This session's attempt
to fetch that model card via Firecrawl returned only boilerplate
(JavaScript-rendered page, no usable per-voice text — see Open Gaps); it
was not possible to verify a specific checkpoint's exact license/dataset
attribution or listen-test its persona fit in this session. Directionally:
pick a **medium-or-higher-quality English voice** (Piper ships quality
tiers x-low/low/medium/high per voice) with a clear, unhurried, documentary-
narrator register — that register is what an "awe-driven, precise" astronomy
narration needs (measured, not hyped; articulate, not casual). Do the actual
voice A/B listening test and per-voice license/attribution check at
implementation time against the live `rhasspy/piper-voices` listing — do not
ship a checkpoint choice made from this document alone.

**CPU inference time for a ~150-word script:** not found as a directly
benchmarked figure in this session's fetches (no real-time-factor number
was present in the README content actually returned). Piper's documented
design target — real-time or faster synthesis on a Raspberry Pi 4 — implies
that on a GitHub Actions x86 runner, a ~150-word script (roughly 60-90
seconds of spoken audio) should synthesize in well under the audio's own
playback length, plausibly single-digit-seconds to a few tens of seconds.
This should be benchmarked directly in a real GitHub Actions job before
being relied on for pipeline timing budgets — treat the estimate above as
directional, not verified.

## Music Sourcing

**Method to identify trending tracks in this niche:** cross-reference (a)
TikTok Creative Center's Trending Sounds tool and (b) YouTube's own Shorts
trending-audio surfacing (audio usage counts shown when browsing Shorts using
a given track) against space/astronomy-content creators specifically, since
general "trending audio" charts are dominated by other niches and won't
reflect what's actually resonating on astronomy content. This is a live,
time-sensitive lookup — it needs to be re-run at production time, not decided
once here, since "trending" by definition changes weekly.

**Method to obtain stems/instrumentals:** for any identified trending track,
an instrumental/stem version is typically obtained either (a) from the
original rights holder's own instrumental release if one exists (some
labels/artists publish official instrumentals), or (b) via AI stem
separation tools (e.g. Spleeter, Demucs — both open-source) run against the
full track to isolate/remove vocals. Separately, a fully royalty-free/
production-music library (YouTube Audio Library, Epidemic Sound, Artlist,
Pixabay Music, or similar) can be used instead of a trending track entirely,
searched for space/ambient/cinematic cues matching this channel's tone.

**Copyright Risk Flag:**

Using a stem-separated instrumental of a *currently trending, commercially
released* song still carries real legal and platform risk on monetized,
automated content. Removing the vocal track does not clear the underlying
musical composition's copyright — the melody, chord progression, and
arrangement are still owned by the original rights holder(s), and YouTube's
Content ID system is generally capable of matching instrumental-only or
re-arranged excerpts of a registered composition, not just exact vocal
audio. This can result in monetization claims, revenue redirection to the
rights holder, or takedowns, and repeated claims can affect a channel's
standing — a materially different risk profile for an automated,
high-volume-upload channel than for a single one-off video. Royalty-free/
licensed production-music libraries carry essentially none of this risk in
exchange for generally lower "trend-surfing" reach/relatability than an
actually-trending track. This is a tradeoff the human operator needs to
decide deliberately per-video (or as a standing channel policy) — this
document is not choosing trending-but-risky vs. royalty-free-but-safer on
the operator's behalf.

## Open Gaps

- Specific Piper voice checkpoint (exact model name, e.g. an `en_US-*` or
  `en_GB-*` identifier) was not selected here — the Hugging Face
  `rhasspy/piper-voices` page returned only JS-shell boilerplate via
  Firecrawl in this session, not the actual per-voice listing/license/
  dataset-attribution text. This must be checked directly (e.g. by browsing
  the live voice-samples site linked from the Piper README,
  `rhasspy.github.io/piper-samples/`, which was not fetched this session) and
  a specific checkpoint chosen by ear before implementation.
- No benchmarked CPU inference time for Piper on a GitHub Actions runner was
  found in this session's fetches — the estimate given above is inferred
  from the project's stated Raspberry-Pi-class design target, not measured.
  Run an actual timed synthesis job before relying on it for pipeline
  scheduling.
- "Trending track" identification is explicitly a live, time-sensitive
  lookup and was not performed against TikTok Creative Center or YouTube's
  trending-audio surfacing in this session — no specific current trending
  astronomy-adjacent track is named here, intentionally, since any such
  claim would be stale by the time of use and unverifiable from this
  session's Firecrawl fetches.
- Only the first page of the ESA/Hubble press-release archive (20 of 492
  total releases) was fetched; this is more than sufficient for the 8-10
  topics required, but is noted so it's clear the archive has far more
  depth available for future topic sourcing than was pulled here.
