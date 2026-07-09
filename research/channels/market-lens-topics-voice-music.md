# Market Lens — Topics, Voice, Music (Phase 2)

Channel: **Market Lens** — economics, markets, policy, trade, current
trends. Tone target: sharp, analytical, macro-explainer.

Firecrawl usage for this channel (shared with Phase 1, same session): 15
calls total, within the ~15-call budget. Raw responses cached in
`research/frames_tmp/market-lens/s*.json` (gitignored).

## Topics — 8-10 real current examples

Each entry below is a real, currently-live topic sourced via Firecrawl
search (not invented), with the URL actually fetched and a one-line note
on the Shorts-worthy angle.

1. **Fed holds rates, projects only a single 2026 cut** — Fed policy /
   rate-path uncertainty.
   https://www.youtube.com/watch?v=pZTtROnszC8
2. **US inflation picks up, eroding paychecks** (Bloomberg *The Close*,
   6/10/2026) — real-wage erosion framing.
   https://www.youtube.com/watch?v=C3LsP8Vsims
3. **Fed research: tariffs raising core goods PCE prices ~3.1% through
   Feb 2026** — direct tariff-to-inflation transmission, primary-source
   Fed data.
   https://www.federalreserve.gov/econres/notes/feds-notes/detecting-tariff-effects-on-consumer-prices-in-real-time-part-II-20260408.html
4. **"How tariffs will continue to reshape the global economy in 2026"**
   (BBC) — global trade-policy outlook, cites 0.3–0.5pp inflation impact.
   https://www.bbc.com/news/articles/czejp3gep63o
5. **IMF World Economic Outlook** — front-loading ahead of tariffs, fiscal
   expansion in major jurisdictions — macro-outlook angle.
   https://www.imf.org/en/publications/weo
6. **"Scared of an AI stock bubble? Then don't look at this chart"**
   (Yahoo Finance) — AI-trade concentration-risk angle.
   https://finance.yahoo.com/markets/article/scared-of-an-ai-stock-bubble-then-dont-look-at-this-chart-133834616.html
7. **Jobs Surge As AI Stocks Wobble** (Bloomberg *Open Interest*, 5/8/2026)
   — labor-market-vs-AI-selloff divergence.
   https://www.youtube.com/watch?v=xacZIEAMmxQ
8. **San Francisco AI boom pushing home prices up ~15% YoY** (Instagram
   Reel) — AI-boom-hits-real-estate angle, already in native
   vertical-Shorts format.
   https://www.instagram.com/reel/DZycGgQiLiF/
9. **"#Tariffs explained in 60 seconds"** (Instagram Reel) — direct
   short-form competitor example, 60-second explainer format.
   https://www.instagram.com/reel/DMYGKtyR8p9/
10. **"Can Tariffs Actually Work?"** (Economics Explained, 1.4M views) —
    evergreen tariff-mechanics explainer from an established
    econ-explainer channel, useful as a format/pacing benchmark.
    https://www.youtube.com/watch?v=K0V8kZyl1T0

## Voice Provider

**Piper TTS**, voice **`en_US-ryan`** (medium quality checkpoint).

- Project: https://github.com/rhasspy/piper — "A fast, local neural text
  to speech system." Confirmed **MIT license** directly on the repo's
  License panel. Note: the repo is archived (development moved to
  https://github.com/OHF-Voice/piper1-gpl); the MIT-licensed `piper`
  binary/voices are still the current, usable artifact and are what the
  huggingface voice repository serves.
- Voice files: hosted at https://huggingface.co/rhasspy/piper-voices —
  the `en/en_US/` directory (fetched directly) lists real, currently
  published voice folders including `ryan`, `lessac`, `joe`, `norman`,
  `kristin`, `danny`, `bryce`, `john`, `sam`, `kathleen`, `hfc_male`,
  `hfc_female`, among others.
- Licensing detail on the underlying voice training data: per
  https://github.com/rhasspy/piper/discussions/271, at least one commonly
  used voice dataset (LibriTTS) is CC BY, "which does permit commercial
  usage so long as you give attribution properly" — worth re-checking the
  specific `en_US-ryan` voice card on the huggingface page for its own
  dataset attribution before shipping, since different English voices in
  the set are trained on different source datasets.
- CPU-only / GitHub Actions feasibility: not directly benchmarked on a GH
  Actions runner within this research pass (flagged below), but
  https://sourceforge.net/projects/piper-tts.mirror/ describes Piper as
  "optimized for devices like the Raspberry Pi 4" running faster than
  real-time on a single weak ARM core. A GitHub Actions `ubuntu-latest`
  runner (2 vCPU x86_64, ~7GB RAM) is meaningfully more powerful than a
  Pi 4, so synthesis of a ~150-word script (roughly 60–70 seconds of
  spoken audio at a natural pace) should reasonably be expected to
  complete well inside a normal job timeout — **this specific number is
  an inference from the Pi-4 real-time claim, not a directly-sourced GH
  Actions benchmark; treat the "rough CPU inference time" as low
  single-digit-to-tens of seconds, and verify with an actual timed run in
  CI before relying on it for scheduling.**
- Why `ryan` for this persona: it's a standard American male voice in the
  medium-quality tier, which reads as a neutral, authoritative
  "explainer" register appropriate for a sharp/analytical macro channel
  (as opposed to the warmer/younger-skewing voices like `amy` or `kristin`
  in the same set, which are better suited to lifestyle-tone channels).
  This is a judgment call based on the voice's stated persona description
  in the Piper voice set, not a claim backed by an independent listening
  test in this research pass.

## Music Sourcing

**Method to identify trending tracks in this niche:** monitor the
TikTok/Reels/Shorts "trending sounds" surfaces and cross-reference against
what comparable finance/econ/markets creators are actually using in their
recent posts (the Instagram Reel examples cited above are a direct way to
sample current audio choices in-niche). Spotify's Viral 50 and
TikTok's own trending-sounds charts are the standard tools for this;
no independent chart-tracking source was fetched in this pass (see Open
Gaps below).

**Method to obtain stems/instrumentals:**
1. **Royalty-free route:** licensed libraries (YouTube Audio Library,
   Epidemic Sound, Artlist, etc.) — referenced directly in
   https://www.youtube.com/watch?v=ggNt21DC-lc ("FREE Music for YouTube
   Creators — No Copyright Claims") and
   https://www.instagram.com/reel/DXMv5WliALy/ (creator describing use of
   Epidemic Sound "reference tracks" against Content ID/AdSense claims).
   YouTube itself is now testing a first-party tool for this: per
   https://www.tubefilter.com/2026/05/04/youtube-ai-tool-royalty-free-music-resolve-content-id/
   and https://www.instagram.com/p/DX99TRlk4Gl/, YouTube is piloting a
   feature that generates royalty-free instrumental tracks a creator can
   swap in to resolve an existing Content ID claim.
2. **Stem-separation route:** run a trending track through a
   vocal/instrumental separator (e.g., https://stemsplit.io/use-cases/content-creators,
   which explicitly markets itself for this exact use case: "Pick the
   instrumental of a trending song instead of the full mix to dodge
   Content ID matches").

### Copyright Risk Flag

Stem-separating the vocals out of a trending, currently-copyrighted song
and using only the resulting instrumental does **not** clear the
underlying composition's copyright — the melody, chord progression, and
arrangement are still owned by the songwriter/publisher regardless of
whether the vocal stem is present. On a monetized, automated channel this
still carries real Content ID and takedown/demonetization risk: Content ID
match systems are not purely vocal-fingerprint based, and even where an
automated match is avoided, a manual claim or takedown from the rights
holder remains possible at any time after upload. Removing vocals reduces
detection risk; it does not eliminate legal risk. Against that,
royalty-free/licensed-library tracks (or YouTube's own generated
royalty-free instrumentals, once that tool is generally available) carry
essentially none of that risk but also carry none of the "riding a
trending sound" discovery/algorithmic boost that a currently-viral track
can provide. This is a real trending-but-risky vs. royalty-free-but-safer
tradeoff, and it is **not being decided here** — it is the operator's call
to make per video, weighing appetite for takedown/claim risk against the
discovery upside of a trending sound, especially given this channel's
plan to run automated/scheduled uploads where nobody may be watching in
real time to react to a claim.

## Open Gaps

- No independent chart-tracking source (e.g., a live TikTok "trending
  sounds" API/page or a Spotify Viral 50 snapshot) was fetched via
  Firecrawl in this pass — the music-sourcing *method* above is sourced
  and real, but a live example of "here is today's specific trending
  track in the finance niche" was not pulled, to conserve the Firecrawl
  budget for the higher-priority visual/topic/voice research. The
  operator should run that lookup live at production time rather than
  rely on a snapshot from this research date (2026-07-09).
- Piper's CPU inference time for a ~150-word script on an actual GitHub
  Actions `ubuntu-latest` runner is an inference from the Raspberry-Pi-4
  real-time claim, not a directly-measured benchmark — flagged inline
  above. Recommend a timed smoke-test run in the actual CI environment
  before finalizing pipeline timeout budgets.
- The specific training-dataset license for the `en_US-ryan` voice
  checkpoint (as opposed to the LibriTTS-based voices, which are
  confirmed CC BY) was not individually re-verified on its own model card
  within budget — verify the `ryan` voice card on
  https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US/ryan
  before shipping, in addition to the repo-level MIT license already
  confirmed.
