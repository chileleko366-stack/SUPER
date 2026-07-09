# Echoes of Ages — Topics, Voice, Music (Phase 2)

Channel: **Echoes of Ages** — historical events, civilizations, turning
points, timelines/maps. Tone: epic, documentary-narrator gravitas.

## Topics

Sourced via Firecrawl (`/v1/search` + `/v1/scrape`). Two source types were
used deliberately: (a) "this day in history" style rolling-anniversary
content, which is genuinely *current* every day and is a proven recurring
Shorts format in this niche, and (b) an actively-updated "forgotten
civilizations" listicle (article itself carries a July 2026 publish/update
context on the same site, confirming the source is a live, current
publication, not a stale archive). Every topic below traces to a specific
URL that was actually fetched.

Source articles fetched in full:
- https://www.history.com/this-day-in-history/july-9 (Firecrawl scrape)
- https://www.historysnob.com/places/20-ancient-civilizations-we-never-hear-about (Firecrawl scrape)

1. **Catherine the Great seizes power in a palace coup (July 9, 1762)** —
   Russian army regiments in St. Petersburg turn on Peter III and proclaim
   his wife empress; she rules 34 years, the longest of any female Russian
   ruler. Strong "turning point" narrative with an obvious map/timeline
   angle (Russian Empire's expansion under her reign).
   Source: https://www.history.com/this-day-in-history/july-9
2. **The U.S. takes San Francisco from Mexico (July 9, 1846)** — an American
   naval captain occupies the settlement of Yerba Buena, which becomes San
   Francisco; ties into the wider Mexican-American War and westward
   territorial turnover.
   Source: https://www.history.com/this-day-in-history/july-9
3. **Germany surrenders Southwest Africa to the Union of South Africa (July
   9, 1915)** — a lesser-known WWI theater outside the Western Front, good
   for a "the war you didn't know happened" framing with colonial-map
   visuals.
   Source: https://www.history.com/this-day-in-history/july-9
4. **The Romanov remains are forensically identified via DNA (announced July
   9, 1993)** — closes the loop on the 1918 execution of Russia's last
   imperial family; strong "mystery resolved" hook.
   Source: https://www.history.com/this-day-in-history/july-9
5. **The Sumerians invent writing (cuneiform), ~5,000 years ago** — origin
   point for recorded history itself; the Epic of Gilgamesh as a concrete
   artifact to anchor the story.
   Source: https://www.historysnob.com/places/20-ancient-civilizations-we-never-hear-about
6. **The Hittites built an empire that rivaled Egypt, then vanished
   mysteriously (Anatolia, from ~1600 BCE)** — built-in "unsolved" hook,
   ironworking/chariot-warfare visuals, strong map-of-Anatolia potential.
   Source: https://www.historysnob.com/places/20-ancient-civilizations-we-never-hear-about
7. **The Kingdom of Axum (Ethiopia, 100–940 CE)** — a dominant African
   trading power with colossal obelisks and early Christian adoption,
   linking Africa, Arabia, and Rome — strong trade-route map animation
   candidate.
   Source: https://www.historysnob.com/places/20-ancient-civilizations-we-never-hear-about
8. **The Phoenicians invent the alphabet that became Greek and Latin's
   ancestor** — maritime trade-network story with a clean "why you can read
   this sentence" pay-off line.
   Source: https://www.historysnob.com/places/20-ancient-civilizations-we-never-hear-about
9. **The Sogdians as the uncredited connective tissue of the Silk Road
   (Central Asia, from ~500 BCE)** — trade-route-map friendly, feeds a
   "civilization you've never heard of but that shaped everything" arc.
   Source: https://www.historysnob.com/places/20-ancient-civilizations-we-never-hear-about
10. **The Nabateans carved Petra out of solid sandstone (Jordan)** — highly
    visual single-location story (advanced water engineering) that plays
    well as a "how did they build this" Short.
    Source: https://www.historysnob.com/places/20-ancient-civilizations-we-never-hear-about

Additional candidate topics were visible in the same fetched pages
(Olmecs, Kingdom of Kush, Scythians, Minoans, Teotihuacans, Mycenaeans,
Parthians, Etruscans, Maurya Empire, Berbers, Moche, Epirote Greeks/King
Pyrrhus) — all from the same historysnob.com URL above — giving this single
source alone a runway of 15+ additional topics beyond the 10 selected here.

## Voice Provider

**Recommendation: Kokoro-82M, voice `bm_george` (British English male),
Apache-2.0 license.**

- Model: `hexgrad/Kokoro-82M`, v1.0 (released 2025-01-27). Hugging Face model
  card: https://huggingface.co/hexgrad/Kokoro-82M (fetched via WebFetch).
- License: **Apache-2.0**, weights included — explicitly permits commercial
  use, self-hosting, and redistribution. Confirmed directly from the model
  card.
- Voice: `bm_george` — one of 8 British-English voices documented in
  VOICES.md (https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md,
  confirmed via WebFetch), rated "B" target-quality, the highest overall
  grade ("C") among the British male voices. An authoritative British male
  voice is the closest fit in this voice set to an "epic documentary
  narrator" register (think History-Channel/BBC-documentary cadence) versus
  the flatter American voices in the set. `am_fenrir` (American, "deep,
  authoritative", also B-quality/C+ overall) is a reasonable fallback if
  `bm_george`'s specific timbre doesn't land well on audition — swap by
  changing one voice-id string, no re-architecture needed.
- Self-hostable: yes — the model ships as open weights + an installable
  `kokoro` inference package (https://github.com/hexgrad/kokoro), no API
  dependency.
- **CPU-only on a GitHub Actions ubuntu runner**: Kokoro-82M's published CPU
  real-time factor (RTF) is approximately **0.47–0.51**, i.e. it synthesizes
  audio roughly 2x faster than real-time on CPU (source: web search
  aggregating published Kokoro v1 CPU/GPU benchmarks — see Sources below).
  For a ~150-word narration script (roughly 55–65 seconds of spoken audio at
  a measured documentary-narrator pace), that implies **roughly 25–35
  seconds of CPU inference time**, comfortably inside a normal GitHub
  Actions job timeout (default 6 hours, but this is a trivial fraction of
  even a tight 10-minute budget) on a standard 2-core ubuntu runner with no
  GPU.
- Alternative considered and rejected for this channel: **Piper TTS**
  (MIT-licensed, even faster on CPU — RTF ≈ 0.2, roughly 5x real-time).
  Piper is the safer choice if CPU headroom is the binding constraint across
  all 10 channels, but its available voices read as more flatly
  "assistant/robotic" than Kokoro's, which works against the "epic
  documentary-narrator gravitas" persona specifically. Recommendation: use
  Piper as the cross-channel fallback if Kokoro's runtime becomes a problem
  at scale, but Kokoro/`bm_george` is the better persona fit for this
  channel specifically.

## Music Sourcing

**Method to identify trending tracks in this niche:**
Use TikTok's Creative Center / Commercial Music Library
(https://ads.tiktok.com/business/creativecenter/music/pc/en) to see
currently trending sounds filterable by region/theme/mood — cross-check
against YouTube Shorts' own in-app trending-sounds surface for overlap.
This tells you *what's trending* independent of licensing status; licensing
status must then be checked separately per track (see Risk Flag below).

**Method to obtain safe stems/instrumentals once a direction is chosen:**
- **Pre-cleared route (recommended default)**: pull directly from a
  commercial-music library that is pre-cleared for the target platform —
  TikTok's own Commercial Music Library (tracks pre-cleared for commercial
  use), or a subscription library such as Epidemic Sound (confirmed as a
  certified TikTok Sound Partner, catalog usable across platforms) or the
  free-but-generic YouTube Audio Library. These provide ready-to-use
  instrumentals/stems with a documented commercial license, no separation
  step required.
- **Trending-track route**: if a specific trending copyrighted track is
  wanted for its recognizability, options are (a) use YouTube's own
  "Add Sound" feature only if the track is in YouTube's *licensed* catalog
  (rights holder still gets the revenue via Content ID, but the video stays
  up), or (b) license cleared stems for legal remixing from a stem-licensing
  service such as Tracklib, or (c) commission/record a soundalike cover.
  Do **not** rely on running a generic AI stem-separator (e.g. Demucs/
  Spleeter) on a downloaded trending song to strip vocals and call the
  result "safe" — see the flag below.

### Copyright Risk Flag

**This is a decision for the human operator, not a default this research
makes for you.** There is a real, well-documented tradeoff between using
currently-trending (but copyrighted) music and using royalty-free (but less
recognizable) music, and it does not disappear just because vocals are
removed:

- Stem-separating a trending copyrighted song into an instrumental does
  **not** clear the underlying composition's copyright. YouTube's Content ID
  system has been shown to match tracks from audio segments under three
  seconds long, and duration or vocal-removal is not a legal shield — the
  underlying composition (melody, chord progression, production) is still
  owned by the original rights holder and can still be fingerprint-matched.
  "Royalty-free" is also a distinct concept from "copyright-free": a
  royalty-free license means no *per-use* fee after purchase, not that no
  one owns the copyright — that owner can still have the track registered
  with Content ID.
- On **Shorts specifically**, the downside of guessing wrong is worse than
  on long-form: a 1–3 minute Short that receives a music claim can be
  **blocked entirely**, whereas a standard long-form video with the same
  claim often stays live with ads simply redirected to the rights holder.
  For a monetized, automated, multi-video-per-day pipeline, that means a bad
  music choice risks the video rather than just the revenue.
- **Trending-but-risky**: using an actual currently-viral trending song
  (even instrumental-only, even stem-separated) maximizes discovery/
  algorithmic pickup on Shorts/Reels, but carries real risk of a block or
  claim on a strictly automated channel with no human review per upload,
  especially at volume.
- **Royalty-free-but-safer**: using a pre-cleared library track (TikTok
  Commercial Music Library, Epidemic Sound, YouTube Audio Library) removes
  most takedown/block risk and is far more scalable for unattended
  automation, at the cost of lower "this is the trending sound" discovery
  boost.
- The operator must decide, per channel and per risk tolerance, where on
  that spectrum "Echoes of Ages" sits — this research deliberately does not
  make that call.

### Sources (Music/Voice section, WebSearch — outside Firecrawl budget)
- https://www.foximusic.com/blog/youtube-shorts-copyright-music-library-guide/
- https://gyre.pro/blog/using-trending-audio-legally-a-guide-for-youtube-creators
- https://support.google.com/youtube/answer/13486873?hl=en
- https://help.epidemicsound.com/hc/en-us/articles/26248403674770-Content-ID-Claim-YouTube-Shorts-Policy
- https://ads.tiktok.com/business/en/blog/audio-library-royalty-free-music
- https://ads.tiktok.com/business/creativecenter/music/pc/en
- https://www.epidemicsound.com/tiktok/
- https://huggingface.co/hexgrad/Kokoro-82M
- https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
- https://github.com/hexgrad/kokoro

## Open Gaps

- CPU RTF figures for Kokoro-82M (0.47–0.51) and Piper (~0.2) are drawn from
  third-party benchmark write-ups surfaced via WebSearch, not from a
  benchmark run on an actual GitHub Actions ubuntu runner in this session —
  treat the "~25–35s for 150 words" estimate as a reasoned extrapolation,
  not a measured result. Recommend a real smoke-test job before relying on
  it in production CI.
- No specific *currently-trending* individual song was identified or
  evaluated for this channel (deliberately — that decision/tradeoff is
  flagged to the operator above, not resolved here).
- Topic list draws from two source pages (history.com's July 9 page and
  historysnob.com's forgotten-civilizations listicle); a broader spread
  across more outlets (e.g. dedicated history-news sites, Reddit r/history
  trending threads) was not pulled further to conserve Firecrawl budget —
  both fetched sources are current/live and yielded far more than 10 usable
  topics between them, so this was judged sufficient rather than a gap in
  coverage, but it is a narrower source base than an exhaustive survey would
  use.
