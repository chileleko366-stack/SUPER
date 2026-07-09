# Topics, Voice & Music — Silver Screen Insight

Channel: film analysis / cinematic technique / cultural impact. Persona: cinephile,
articulate, visually literate critic. This document is Phase 2 (channel-specific
part) of the research protocol in `docs/RESEARCH_BRIEF.md`. Phase 1 moodboard is at
`research/visual-reference/silver-screen-insight.md`, which used this channel's
full ~15-call Firecrawl budget; the topic list below therefore leans on yt-dlp
(explicitly permitted by the brief's tooling section: "Every claim in your output
must trace to a URL you actually fetched with Firecrawl **or yt-dlp/ffmpeg** output
you actually produced") rather than additional Firecrawl search calls. All URLs
below were retrieved live, none are invented.

## Topics — 8-10 real current film-analysis-Shorts examples

Sourced by querying the actual, current `/shorts` listings of three real,
active film-analysis-Shorts channels via `python -m yt_dlp --flat-playlist`, plus
one item directly from a Firecrawl `/v1/search` result. Titles are verbatim.

| # | Title | Channel | Source URL | Retrieved via |
|---|-------|---------|-------------|----------------|
| 1 | Oppenheimer's dark double meaning... (compartmentalization) | Filmalysis | https://www.youtube.com/shorts/C9JlWrNzzDU | yt-dlp |
| 2 | OPPENHEIMER has 1 big hidden message (APPLE) | Filmalysis | https://www.youtube.com/shorts/rpF14vgL9zk | yt-dlp |
| 3 | Waymond Wears Green In Everything Everywhere All At Once For A Reason | Filmalysis | https://www.youtube.com/shorts/lHi1_eRsHxQ | yt-dlp |
| 4 | The MATRIX - Did You Notice This? | Filmalysis | https://www.youtube.com/shorts/gPXY2aGzRaw | yt-dlp |
| 5 | Interstellar's POEM has a HIDDEN MEANING..... | Filmalysis | https://www.youtube.com/shorts/kyx-0o_jc-k | yt-dlp |
| 6 | The SYMBOLS of Midsommar | Lucas Blue | https://www.youtube.com/shorts/oXBFyHwdGgI | yt-dlp (also used for contact sheet 2) |
| 7 | The HORROR of Hereditary | Lucas Blue | https://www.youtube.com/shorts/bBkvvPNEpMM | yt-dlp |
| 8 | The MEANING of KILLERS OF THE FLOWER MOON | Lucas Blue | https://www.youtube.com/shorts/BCtyhzGh-w8 | yt-dlp |
| 9 | The BRILLIANT Cinematography in Requiem for a Dream | Lucas Blue | https://www.youtube.com/shorts/k6wlxcXAdbI | yt-dlp |
| 10 | What Is A Long Take? #Shorts | In Depth Cine | https://www.youtube.com/shorts/6fmyfIhinNE | yt-dlp |
| 11 (bonus) | Mind-Blowing Story Ending Explained #shorts #movieclips #movie | (independent Shorts creator) | https://www.youtube.com/shorts/WWRFUdkwGZg | Firecrawl `/v1/search` |

Observed pattern across these real examples: two dominant formats co-exist in this
niche — **(a) hidden-meaning/symbolism reveals** on a specific well-known film
(Oppenheimer, Everything Everywhere All At Once, Midsommar, Hereditary, Killers of
the Flower Moon), and **(b) technique explainers** (long takes, cinematography
breakdowns, "did you notice this" framing). Silver Screen Insight should plan a
content calendar mixing both formats rather than picking only one, since both are
independently validated as active, currently-posted formats by real channels.

## Voice Provider

**Recommendation: Piper — engine `rhasspy/piper` (archived, MIT) + voice
`en_US-lessac-medium` from `rhasspy/piper-voices` (MIT).**

Research and verification performed:
- Scraped https://github.com/rhasspy/piper directly (Firecrawl). Confirmed: the
  repository is now archived (read-only, archived Oct 6, 2025) but contains a
  `LICENSE.md` file and remains fully downloadable/runnable — archived only means
  no further commits, not that it's unusable.
- Firecrawl search confirmed https://huggingface.co/rhasspy/piper-voices and its
  subpath https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US/lessac/medium
  both display **"License: mit"** on the Hugging Face collection page, and
  https://github.com/rhasspy/piper/discussions/271 states the project "does not
  impose any additional licenses on the checkpoints or voice models" — i.e. the
  `en_US-lessac-medium` voice checkpoint is MIT.
- Firecrawl search also surfaced the **actively maintained successor**,
  https://github.com/OHF-voice/piper1-gpl, created after the original project was
  archived (per a grokipedia summary found in search: "development shifted to a new
  GPL-licensed fork... March 28, 2025").

**Important, directly-verified licensing nuance:** the `pip install piper-tts`
package that is easiest to reach today (used below for the actual CPU timing test)
is **not** the original MIT engine — it is the OHF-Voice fork. This was confirmed
locally, not assumed: `pip show piper-tts` reports
`Home-page: http://github.com/OHF-voice/piper1-gpl` and
`License: GPL-3.0-or-later`, and the bundled `COPYING` file
(`piper_tts-1.4.2.dist-info/licenses/COPYING`) is the literal GNU GPLv3 text. GPL-3
does not forbid commercial use, but it is a copyleft license — bundling it as a
linked Python dependency inside a distributed/commercial pipeline carries real
copyleft obligations that a permissively-licensed alternative avoids entirely.

**Recommendation for this build:** do not `pip install piper-tts` as a library
dependency. Instead, download the archived MIT-licensed `piper` engine binary
directly from the `rhasspy/piper` GitHub Releases (a standalone executable,
invoked as a CLI subprocess in the GitHub Actions job) together with the
MIT-licensed `en_US-lessac-medium.onnx` voice files from `rhasspy/piper-voices`.
This keeps every component of the TTS step MIT-licensed with no copyleft exposure,
while still running on the same neural engine and ONNX runtime lineage as the
actively-maintained fork (the two forks share the same core inference code and
model format, so performance characteristics carry over).

**Voice choice rationale:** `en_US-lessac-medium` is a clear, neutral, well-
articulated American voice — the "medium" quality tier is Piper's balance point
between naturalness and CPU speed (vs. the slower "high" tier and the more robotic
"low"/"x_low" tiers), matching a measured, articulate-critic delivery without the
inference cost of the high-quality tier. It was directly confirmed to exist in the
MIT-licensed `rhasspy/piper-voices` collection (see subpath URL above).

**Measured CPU inference time (actually run, not estimated):** Using the
locally-installed `piper-tts` 1.4.2 engine (same inference code family as
recommended above) with the `en_US-lessac-medium` voice on a 4-logical-core CPU
(no GPU), a 136-word cinephile-critic-voiced sample script (`sample_script.txt`,
written for this test) was synthesized to a 43.65-second WAV file:
- Cold run (fresh Python process, includes onnxruntime session init): 47.69s
  wall-clock.
- Warm run (second invocation, OS file cache warm): 24.15s wall-clock — a real-time
  factor of ≈0.55 (i.e. faster than real-time; synthesis takes roughly half the
  output audio's own duration).
- For a typical ~150-word Short script (~45-55s of narration), expect roughly
  **25-50 seconds of CPU render time** on a machine comparable to this one.
  Standard GitHub Actions `ubuntu-latest` runners ship with 2 vCPUs (half of the
  4 used in this test), so a conservative real-world estimate on a GH Actions
  runner is **on the order of the audio's own duration (≈1x real-time), i.e.
  well under a minute per Short** — trivially inside a normal job timeout.

## Music Sourcing

**Method to identify trending tracks in this niche:** film-analysis Shorts trend
audio comes from two distinct sources that should be tracked separately:
1. **Platform trend surfaces** — TikTok Creative Center's trending-sounds charts,
   Instagram Reels' "Trending Audio" panel on the Reels composer, and YouTube
   Shorts' own "N videos use this sound" counter visible on any Short. These
   surface whatever short clips of trending pop/hip-hop tracks are currently
   viral platform-wide, not film-specific.
2. **Score/trailer-cue reuse, which is specific to this niche** — film-analysis
   creators very commonly score their own Shorts with cues lifted directly from
   the film's own score or its theatrical trailer (e.g. a Hans Zimmer Oppenheimer
   cue, a24-style ambient dread pads for horror analysis) rather than a generic
   trending pop song, because the score reinforces the analytical subject. This
   is the dominant convention observed directly in the two downloaded reference
   clips for this channel's moodboard (both used moody ambient/orchestral
   underscore, not licensed pop music, under their spoken analysis).

**How stems/instrumentals would be obtained, concretely:**
- If the goal is to reuse a trending *pop/hip-hop* track: obtain (or purchase) the
  track, then run an open-source source-separation model such as Demucs or
  Spleeter locally to isolate an instrumental stem by removing the vocal stem.
  This is a mechanical, well-established process, not a licensing workaround (see
  Copyright Risk Flag below).
- If the goal is a film-score-style cue (the pattern actually observed in this
  niche's references): source from a royalty-free/production-music library with a
  "cinematic," "orchestral," or "ambient tension" catalog tag — e.g. the YouTube
  Audio Library (free, explicitly cleared for monetized YouTube use), Pixabay
  Music (royalty-free), or a paid subscription library such as Epidemic Sound or
  Artlist (both maintain dedicated cinematic/orchestral score categories and issue
  a license/clearance the creator can point to if a claim is filed).

**Copyright Risk Flag.** This is a decision for the human operator, not something
this research resolves automatically:

> Stem-separated instrumentals of trending copyrighted songs still carry real
> Content ID / takedown risk on monetized, automated content. Removing the vocal
> stem does not clear the underlying composition's copyright — the melody,
> harmony, and arrangement of the instrumental are still the same copyrighted
> musical work, and rights holders' Content ID fingerprints frequently match on
> instrumental-only audio, especially for well-known film scores and trailer
> cues where the instrumental *is* the recognizable hook. Using a trending,
> stem-separated cue may drive short-term discovery/algorithmic favor but exposes
> the channel to claims, ad-revenue redirection, or takedown, which is
> disproportionately risky for a fully automated, high-upload-frequency pipeline
> with no human review step to catch a bad claim before it multiplies across many
> videos. Royalty-free or explicitly-licensed library music (YouTube Audio
> Library, Pixabay Music, or a paid Epidemic Sound/Artlist subscription) is
> slower to feel "trend-native" and may underperform a genuinely viral trending
> cue on discovery, but carries materially lower legal/monetization risk at scale.
> The operator must choose where on that tradeoff this channel sits — this
> research does not make that call.

## Open Gaps

- No additional Firecrawl budget remained for this channel to independently
  verify TikTok Creative Center's current top trending sounds live (the method
  above is described, not executed against a live trend chart) — treat the
  platform-trend-surface method as a documented process, not a current trend
  snapshot.
- Demucs/Spleeter were named from general technical knowledge of the
  source-separation space, not from a page fetched in this session (Firecrawl
  budget was fully spent on Phase 1 + voice-licensing verification); their exact
  current license terms should be re-checked before adoption.
- The bonus topic (#11, WWRFUdkwGZg) is from a search snippet only — the
  uploading channel's name was not resolved (YouTube search result did not
  surface a channel handle).
