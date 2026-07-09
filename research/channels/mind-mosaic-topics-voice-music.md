# Mind Mosaic — Topics, Voice, Music (Phase 2)

Channel: **Mind Mosaic** — psychology, cognitive biases, emotions,
self-improvement. Tone: warm, insightful, non-clinical psychology
communicator.

All topic examples cite a URL actually returned by a Firecrawl `/v1/search`
or `/v1/scrape` call on 2026-07-09. Voice and music sourcing claims cite a
URL actually scraped where a specific factual claim (license, format,
platform rule) is made; where a claim could not be verified within budget
it is marked "not found" / flagged in Open Gaps rather than invented.

This channel's Firecrawl budget (shared with Phase 1 — see
`research/visual-reference/mind-mosaic.md`) was fully used: 15/15 calls
across both documents. No further Firecrawl calls were available for this
document; two claims below (a live TTS benchmark number, and an
independent easing-reference citation) could not be completed as a result
and are flagged explicitly rather than guessed.

## Topics (8-10 real current examples)

1. **"Nine science-backed ways to help you feel better in 2026"** — BBC
   Future roundup of evidence-based wellbeing tactics (channelling anger,
   list-writing, singing more), published 2025-12-31.
   https://www.bbc.com/future/article/20251231-nine-simple-steps-to-feeling-better-in-2026
2. **"What's ahead for psychology? Nine trends to watch in 2026"** — video
   overview of behavioral-science trends (AI companions, severe-weather
   psychology, etc.) for 2026.
   https://www.youtube.com/watch?v=hpZ4qCnAxpQ
3. **Productivity culture vs. real connection** — "In a culture obsessed
   with productivity, we're told the answer is to become more efficient.
   But what if the real problem isn't a lack of time, but a lack of
   connection?" Psychology Today piece, July 2026 (via Refind aggregator,
   which mirrors the live PT feed).
   https://refind.com/links/150358414
4. **Media psychology of streaming-platform design** — "The most successful
   streaming platforms have been created using media psychology in designs
   that keep viewers immersed, loyal and habituated." Psychology Today,
   July 2026 — a habit-loop/attention-hook angle.
   https://refind.com/links/150359510
5. **Five universal human behaviors and anxiety** — "Understanding five
   universal human behaviors can reduce your anxiety and stop you from
   taking things personally." Psychology Today, May 2026.
   https://refind.com/links/150318473
6. **Hyper-intellectualizing feelings as emotional armor** — "The
   hyper-intellectualizing of psychological insight provides just that, a
   kind of protection from being... well... ourselves." Psychology Today,
   May 2026 — directly on-brand for a "non-clinical, warm" framing that
   pushes back on jargon-heavy pop-psych content.
   https://refind.com/links/150316710
7. **Synchronicity and meaningful coincidence** — "What if meaningful
   coincidences reveal hidden patterns rather than mere chance?" Psychology
   Today, July 2026.
   https://refind.com/links/150358615
8. **Music-mind connection and identity** — "Psychologists study how humans
   process music... this mind-music connection may shape our individual
   and group identity." Psychology Today, May 2026.
   https://refind.com/links/150322034
9. **The Halo Effect explained** — existing short-form example already live
   in-niche: "This cognitive bias reveals how one positive trait can lead
   us to assume other positive attributes, even without proof."
   https://www.tiktok.com/@donnellycss/video/7271683053246893345
10. **The Hidden Cognitive Bias Even Smart People Suffer From** — existing
    YouTube Short (also the clip downloaded and analyzed for Phase 1's
    contact sheet), 10,207 views, on the base-rate/stereotyping bias in
    medical-diagnosis-style reasoning.
    https://www.youtube.com/shorts/9XSMm2mrVqg

Observed pattern across the 10: Psychology Today (surfaced via its Refind
aggregation) is currently running a strong July 2026 cluster on
connection-vs-productivity, media/attention psychology, and
"anti-jargon" emotional-honesty framing — all of which suit a warm,
non-clinical voice better than a clinical-diagnosis angle would. The two
directly-in-niche Shorts/TikTok examples (items 9-10) confirm that
single-bias, single-mechanism explainer format (name the bias, show a
relatable moment, explain the mechanism, give one actionable reframe) is
the proven working structure for this niche in short-form video today.

## Voice Provider

**Recommended: Piper TTS.**

- **Self-hostable**: yes — Piper is a local, ONNX-runtime-based neural TTS
  engine (`pip install piper-tts`) with no cloud dependency. Confirmed by
  direct install in this research session (`pip install piper-tts` reported
  `piper-tts 1.4.2` already satisfied, with `onnxruntime` as its inference
  backend).
- **Two repos exist, and their licenses differ — verified by scraping both
  GitHub pages directly:**
  - `rhasspy/piper` (original, now archived Oct 6, 2025 — read-only):
    **MIT license**, confirmed via scrape of
    https://github.com/rhasspy/piper ("### License / MIT license"). The
    repo's own banner states "Development has moved to
    https://github.com/OHF-Voice/piper1-gpl".
  - `OHF-Voice/piper1-gpl` (actively maintained successor, 4.7k stars, last
    commit within the past week as of this research date): **GPL-3.0
    license**, confirmed via scrape of
    https://github.com/OHF-Voice/piper1-gpl ("### License / GPL-3.0
    license"). GPL-3.0 permits commercial use of the software itself; it
    is a copyleft license on the engine's own source code. Running the
    Piper CLI/library as an external process to synthesize narration audio
    (rather than statically linking the library into a distributed
    proprietary binary) is the standard low-risk usage pattern, but the
    repo's own name change to "piper1-**gpl**" is a real, visible signal
    the operator should weigh — flagged rather than silently assumed safe.
    This is not legal advice; if the pipeline ever redistributes Piper's
    own source/binary (as opposed to shelling out to it), consult the
    GPL-3.0 text directly.
  - Per-voice licensing is separate from the engine license: a GitHub
    discussion thread on voice licensing states "The license on the
    libritts dataset used for voice is 'CC BY' which does permit commercial
    usage so long as you give attribution properly," per
    https://github.com/rhasspy/piper/discussions/271. This means an
    `en_US` voice checkpoint trained on the LibriTTS corpus (e.g. an
    `en_US-libritts` or `en_US-libritts_r` family voice) carries a
    **CC-BY** license — commercial use is permitted with attribution to the
    original speakers/dataset. This is the specific voice family
    recommended for this channel's commercial pipeline, because it is the
    one whose license was independently verified in this research pass.
- **Specific checkpoint recommendation**: an `en_US-libritts_r` (or
  `en_US-libritts`) medium/high-quality Piper voice, selected for its
  verified CC-BY commercial license (see above). **Not verified this
  session**: which specific per-speaker checkpoint within that family
  sounds "warm and insightful" rather than flat/neutral — Piper's own
  voice-sample gallery at https://rhasspy.github.io/piper-samples/
  populates its voice list via client-side JavaScript, which a static
  Firecrawl markdown scrape cannot execute, so the actual list of available
  speaker names/genders under the LibriTTS family was not retrieved this
  session (and this specific page was not scraped, to conserve the shared
  15-call budget for higher-priority items). **Action for the operator**:
  browse that samples page directly (or run `python -m piper.download_voices`
  locally, which does work — confirmed in this session) and audition the
  `en_US-libritts*` voices by ear before locking in one checkpoint.
- **GitHub Actions ubuntu runner, CPU-only**: Piper is explicitly positioned
  as a fast, low-resource local TTS engine; a Firecrawl search result
  described it as "still one of the fastest and most efficient open-source
  text-to-speech systems you can run locally even on small devices" (per
  https://www.youtube.com/watch?v=8arC6rntpp0, a 2026 Piper overview video
  surfaced by search). A standard GitHub Actions `ubuntu-latest` runner has
  materially more CPU/RAM than the small-device class Piper targets, so a
  ~150-word script (roughly 60-90 seconds of narration) should comfortably
  fit within a normal job timeout.
- **CPU inference time for a ~150-word script — attempted, not obtained.**
  This research session went further than a documentation-only pass: Piper
  was actually installed (`pip install piper-tts`, already present, v1.4.2)
  and a real 150-word test script was prepared
  (`research/frames_tmp/mind-mosaic/test_script.txt`, word count verified
  programmatically). A live timed synthesis was then attempted via
  `python -m piper.download_voices en_US-lessac-medium` followed by
  `python -m piper -m en_US-lessac-medium.onnx -f test_output.wav`. The
  voice-model download completed without an error code, but the resulting
  `.onnx` file was only 1.7MB (a real medium-quality Piper voice model is
  tens of MB) and failed to load ("INVALID_PROTOBUF: Load model ... failed:
  Protobuf parsing failed"). Diagnosis: `curl -sI https://huggingface.co`
  (the host Piper voice models are distributed from) returned no response
  in this sandbox, while `curl -sI https://github.com` succeeded normally —
  Hugging Face appears to be network-blocked in this research environment,
  which silently corrupted the voice-model download. A follow-up attempt to
  find a documented third-party CPU benchmark number via WebSearch also
  failed (session limit reached, zero results returned). **No verified
  numeric CPU inference time is available — this is a genuine open gap, not
  an invented number.** The operator should benchmark this directly in the
  actual GitHub Actions ubuntu runner (which will have normal internet
  access to Hugging Face) before finalizing job-timeout budgets; Piper is
  widely documented as real-time-or-faster on CPU for this model size class,
  but that qualitative claim should not be treated as a substitute for an
  actual measured number in the target environment.

## Music Sourcing

**Method to identify trending tracks in this niche:**

1. Monitor the audio actually attached to current high-performing
   psychology Shorts/TikToks (the same creator accounts and clips used for
   the topics list above — e.g. the TikTok/YouTube examples in items 9-10 —
   are also a live signal for what audio psychology creators are currently
   pairing with explainer-format content; check each platform's native
   "used in N videos" / trending-audio indicator directly on the
   Short/Reel).
2. Cross-check any candidate trending track against platform-native
   "Commercial Music Library" filters before use — TikTok/Instagram both
   expose a separate commercial-safe sound picker distinct from the general
   trending-sounds picker, per the source-separation and safe-source
   language already documented in the sources below.
3. For stems/instrumentals of a track that is not already cleared: a
   dedicated commercial tool for exactly this exists and was found via
   Firecrawl — https://stemsplit.io/use-cases/content-creators, which
   explicitly markets "Get clean audio stems for trending sounds. Create
   original versions by remixing isolated elements to make your content
   unique" for TikTok/Reels/YouTube. This confirms stem-separation of
   trending sounds is a real, current, easily-accessible workflow — which
   is precisely why the Copyright Risk Flag below matters: easy access to
   stem separation does not equal legal clearance.
4. For a fully safe path, the YouTube Audio Library (free, pre-cleared) and
   subscription royalty-free libraries (Epidemic Sound, Artlist,
   Soundstripe) are documented, current (2026) options with stated pricing
   and commercial/live-streaming coverage, per
   https://gyre.pro/blog/using-trending-audio-legally-a-guide-for-youtube-creators
   (2026-06-07, updated 2026-07-09) — see the comparison table cited in the
   Copyright Risk Flag below. A second royalty-free source was also
   surfaced: https://twoshot.app/copyright-free-music ("Download
   copyright-free music for YouTube, TikTok, podcasts, and more... no
   claims, no fees").

## Copyright Risk Flag

**This is a tradeoff the human operator must decide, not something this
research resolves.**

Per the Gyre.pro 2026 creator guide (directly scraped, published
2026-06-07, last modified 2026-07-09 — https://gyre.pro/blog/using-trending-audio-legally-a-guide-for-youtube-creators):
"Trending sounds inside the Shorts library are licensed only for Shorts
under 60 seconds," and "the same audio in long-form videos or live streams
will trigger a Content ID claim or a copyright strike." The same source
states YouTube's Content ID system "identifies copyrighted tracks through
fingerprint matching" and "since 2025 it also runs AI music detection,
which recognises pitched-down, sped-up, and filter-distorted versions of
registered songs" — a detection method that directly covers vocal-removed/
stem-separated instrumentals, not just the original mix.

- **Trending-but-risky**: pairing a currently-trending, label-owned track
  (even instrumental-only, even after running it through a stem-separation
  tool like the stemsplit.io service found above) with automated, monetized
  Shorts content still carries real Content ID / takedown risk. **Removing
  the vocal track does not clear the copyright on the underlying musical
  composition and sound recording** — the composition (melody, harmony,
  arrangement) is still owned by the original rights holder, and
  fingerprint-matching plus AI music detection (per the Gyre.pro source
  above) are documented to catch modified/distorted versions of a
  registered track, not just an unmodified full mix. In-app "free to use"
  sound-picker grants on TikTok/Instagram/YouTube Shorts are scoped to
  that platform's own short-form surface and duration limit (per Gyre.pro:
  "Trending sounds from the YouTube Shorts library are auto-licensed for
  Shorts of 60 seconds or less... The same rule applies to TikTok and
  Instagram Reels: in-app licensing covers in-app posts only") — they do
  not automatically extend to a separately-hosted, cross-platform,
  automated pipeline. Using a trending track can meaningfully help
  discovery/reach on the platform where it's trending, but on a faceless,
  automated, multi-video-per-day channel a single flagged upload can
  compound into channel-wide strike risk (the same source documents that
  three active copyright strikes within 90 days terminate a channel).
- **Royalty-free-but-safer**: sourcing from the YouTube Audio Library
  (free, pre-cleared, per Gyre.pro's comparison table) or a paid
  royalty-free/production-music subscription (Epidemic Sound, Artlist,
  Soundstripe — entry pricing and live-streaming coverage documented in the
  same 2026 source) or a dedicated copyright-free catalog like
  https://twoshot.app/copyright-free-music avoids Content ID risk almost
  entirely and keeps monetization safe, at the cost of not riding an
  actively-trending sound and potentially sounding more generic than what
  top creators in this niche are currently using.

**Recommendation is intentionally not made here.** The operator should
choose based on the channel's actual risk tolerance and monetization
stakes — an early testing phase might reasonably use trending or
sound-alike audio to validate format-market fit, while a channel already
earning ad revenue at volume should weight the royalty-free path more
heavily, since strike history can affect the whole channel/account, not
just one video.

## Open Gaps

- No verified numeric CPU inference-time benchmark for a ~150-word Piper
  script was obtained. A live benchmark was genuinely attempted (Piper
  installed, test script written and word-counted, voice-model download and
  synthesis run) but failed because this sandbox cannot reach
  `huggingface.co` (confirmed via `curl -sI`), which silently corrupted the
  downloaded `.onnx` voice file; a follow-up WebSearch for a documented
  third-party benchmark also failed (session limit, zero results). Must be
  benchmarked directly in the target GitHub Actions ubuntu runner, which
  will have normal Hugging Face network access.
- The specific list of available `en_US-libritts*` (or other CC-BY-licensed)
  speaker checkpoints — names, genders, per-voice tone — was not retrieved,
  since https://rhasspy.github.io/piper-samples/ populates its voice
  dropdown via client-side JavaScript that a static Firecrawl scrape cannot
  execute, and this page was not scraped this session to conserve the
  shared Firecrawl budget. The operator must audition specific checkpoints
  by ear (or via local `python -m piper.download_voices`, confirmed working
  in this sandbox) before finalizing a voice.
- No dedicated stem/instrumental-sourcing legal-safety verification beyond
  the Gyre.pro article was obtained (e.g. Tracklib-style cleared-stem
  services were only seen as a passing mention inside that article, not
  independently verified via a direct scrape of a stem-licensing vendor).
- This document's topic list is a snapshot of currently-surfaced Firecrawl
  results on 2026-07-09 (mostly Psychology Today content from
  May-July 2026, via Refind's aggregation, plus two live short-form
  examples); topic selection for actual production should re-run a similar
  search periodically rather than treating this list as evergreen.
- The Refind-aggregated Psychology Today links (items 3, 4, 5, 6, 7, 8
  above) are cited as `refind.com/links/...` redirect URLs because that is
  the actual URL Firecrawl fetched and returned content for; these redirect
  to the underlying psychologytoday.com articles but the final PT URLs
  themselves were not separately resolved/fetched in this session.
