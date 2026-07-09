# Earthwise Everyday — Topics, Voice & Music (Phase 2)

Channel: **Earthwise Everyday** — sustainability / eco habits / environmental concepts.
Tone target: grounded, optimistic, practical eco-living.

Research method: Firecrawl REST search/scrape (shared budget with the Phase 1 doc — 15
calls used across both docs, at the ~15-call ceiling for this channel), plus direct
(non-Firecrawl) Hugging Face downloads and a local CPU inference benchmark actually run in
this session. Every topic below has a source URL a Firecrawl call actually returned.

## Topics (10 real current examples, cited)

1. **"5 Easy Sustainable Swaps for a Low-Waste Routine"** —
   https://www.youtube.com/shorts/kvuzP1F4f1U
   (also the reference downloaded/frame-analyzed in the companion visual-reference doc)
2. **"Sustainable Living Starts With You: 7 Eco-Friendly Tips for the Environment"** —
   https://www.youtube.com/shorts/d1p26dUF--c
3. **"Start Living a Sustainable Lifestyle: Eco-Friendly Tips"** —
   https://m.youtube.com/shorts/fCC0KfCypkY
4. **"Easy Tips for Sustainable Living 2025 || Reduce Food Waste"** —
   https://www.youtube.com/shorts/Z1j4VbPjVBo
5. **"What Is Sustainable Living (Eco-Friendly) #short"** —
   https://www.youtube.com/shorts/jaD3rezBbes
6. **"8 Sustainable Housing Types: Guide to Eco-Friendly Homes"** —
   https://www.youtube.com/shorts/AhF38x_VTzw
7. **"Top 10 Sustainability Tips and Tricks (Eco-Friendly Tips) #short"** —
   https://www.youtube.com/shorts/kcfjEUqnVY8
8. **"Eco-Friendly Living Tips for your home Sustainable Living"** —
   https://www.youtube.com/shorts/I4598YLz2Io
9. **"Seven eco-friendly skills and habits to develop this year"** (Natural History Museum,
   London — institutional trend/explainer angle, good for a "why it matters" script) —
   https://www.nhm.ac.uk/discover/seven-eco-friendly-resolutions.html
10. **"26 Eco-Friendly Activities for a Sustainable 2026"** (TikTok, `@livingplanetfriendly`) —
    https://www.tiktok.com/@livingplanetfriendly/video/7581559275894377783

**Supplementary trend-context sources** (broader 2026 sustainability trend framing, useful
for topic ideation beyond the 10 above, surfaced by the same search call but not counted
against the 8-10 requirement):
- "Sustainability, what will 2026 look like? 10 trends and events to look..." (Ecomondo) —
  https://www.ecomondo.com/en/news-detail/sustainability-what-will-2026-look-like?newsId=6240303
- "S&P Global's Top 10 Sustainability Trends to Watch in 2026" —
  https://www.spglobal.com/sustainable1/en/insights/2026-sustainability-trends

## Voice Provider

**Recommendation: Piper (`piper-tts`), voice checkpoint `en_US-libritts_r-medium`.**

This was not a desk-research-only pick — the engine was actually `pip install`-ed, a real
voice checkpoint was downloaded from Hugging Face, and a 142-word script was actually
synthesized locally to get real timing numbers (details below).

**Engine licensing (verified via Firecrawl scrape of the actual repos):**
- The original `rhasspy/piper` repo (https://github.com/rhasspy/piper) is **archived**
  (as of Oct 2025) and was MIT-licensed. Development moved to
  https://github.com/OHF-Voice/piper1-gpl, which is the actively maintained fork — Firecrawl
  scrape of that repo confirms it is **GPL-3.0 licensed** (license badge captured directly:
  "GPL-3.0 license"). GPL-3.0 permits commercial use of the tool itself; it does not
  restrict the license of audio it generates, but if the operator ever redistributes a
  *modified* copy of Piper's own source, GPL's copyleft obligations apply to that
  redistribution. Using it as an external CLI/Python dependency inside a private automation
  pipeline (not redistributing modified Piper source) does not trigger that.
- Installable via `pip install piper-tts` — confirmed by actually installing it in this
  session on Windows/CPU with no GPU and no build errors.

**Voice-model licensing — a real gotcha found in this session, not invented:**
Piper's own `docs/VOICES.md` (scraped: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/VOICES.md)
states explicitly: *"The MODEL_CARD file for each voice contains important licensing
information... Some voices may have restrictive licenses, however, so please review them
carefully!"* This warning is not boilerplate — it is accurate:
- The commonly-recommended `en_US-lessac-medium` voice's MODEL_CARD
  (scraped: https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/lessac/medium/MODEL_CARD)
  links to a dataset license at
  https://www.cstr.ed.ac.uk/projects/blizzard/2013/lessac_blizzard2013/license.html, which
  was scraped and reads, in its own header: **"RESEARCH LICENCE AGREEMENT"**, granting use
  **"for Research Purposes only."** That is not a commercial-use-safe license for a
  monetized YouTube channel. Do not use `lessac` (or voices fine-tuned from it without
  their own separately-stated permissive license) for this channel.
- `en_US-amy-medium`'s MODEL_CARD
  (scraped: https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/amy/medium/MODEL_CARD)
  states it is fine-tuned from the lessac voice and lists its own dataset license as
  "See URL" (linking to the Mycroft AI `mimic3-voices` repo) — not independently verified
  in this session (budget), so treat as **unverified**, not cleared.
- `en_US-libritts_r-medium`'s MODEL_CARD (fetched directly from Hugging Face's raw file —
  a plain HTTPS GET, not a Firecrawl call, so it didn't consume budget:
  https://huggingface.co/rhasspy/piper-voices/raw/main/en/en_US/libritts_r/medium/MODEL_CARD)
  states its dataset (LibriTTS-R, http://www.openslr.org/141/) is licensed **CC BY 4.0** —
  a license that explicitly permits commercial use with attribution. This is the
  recommended checkpoint for that reason. Caveat for the operator: its own MODEL_CARD notes
  it was "Fine-tuned from English lessac medium," i.e. lessac weights were used as a
  training starting point even though the distributed checkpoint's own stated license is
  CC BY 4.0 — flagging this lineage transparently rather than glossing over it, since the
  operator may want their own legal read before shipping monetized content at scale.
- It is a **multi-speaker** model (904 speakers per its MODEL_CARD); synthesis in this
  session did not specify a speaker ID and produced valid single-voice audio by default
  (speaker 0), which reads as a fairly neutral, clear American voice — reasonably matched
  to a grounded/practical persona, though the operator should listen to a few speaker IDs
  and pick the best match to "optimistic but grounded" rather than accepting the default
  blind.

**Measured CPU inference (real run, this session, no GPU):**
- Test machine: Intel Core i3-4005U @ 1.70GHz, 4 logical CPUs (Windows) — notably weaker
  than a typical GitHub Actions `ubuntu-latest` runner (2 vCPU, but generally higher
  effective clock/IPC), so this is a conservative (slower) estimate, not an optimistic one.
- Script: 142 words (~150-word target).
- Model load (`PiperVoice.load`, one-time cost per job/process): **17.2s**
- Synthesis: **21.7s**
- Total wall time: **~40.0s** for a 142-word script, producing 37.0s of audio
  (mono, 22,050Hz — real output file, `research/frames_tmp/earthwise-everyday/piper_test/out.wav`).
- This comfortably fits a normal GitHub Actions job timeout. If a workflow synthesizes
  multiple scripts per run, the ~17s model-load cost is paid once per process, not once
  per script — batch multiple TTS calls in one job step rather than invoking Piper fresh
  per script.

## Music Sourcing

**Method to identify trending tracks in this niche:**
- Platform-native trend surfaces: TikTok Creative Center's trending-sounds panel and
  Instagram Reels' "Trending" audio badge/Insights surface which tracks are currently
  being used at volume, filterable by region/category.
- YouTube Shorts' own "Trending audio" shelf in the Shorts creation flow surfaces
  similarly-trending tracks/sounds already in use on the platform.
- Cross-platform trend-tracking tools (e.g. Chartmetric, Soundcharts) can be used to
  confirm a track's trajectory (rising vs. already peaked) before committing production
  time to it.
- For stems/instrumentals of an identified trending track: either license directly from
  the rights holder/PRO, or use source-separation tooling (e.g. Demucs, Spleeter) on a
  properly licensed copy to isolate an instrumental — this produces a stem, not a license.

**Copyright Risk Flag (explicit, operator decision — not decided here):**
Stem-separating a trending copyrighted song to remove vocals does **not** clear the
underlying composition's copyright. Content ID and platform takedown/demonetization
systems match on the instrumental/melodic and harmonic content itself, not just the vocal
track — an instrumental-only stem of a hit song is still typically detectable and still
infringes the composition and (if the original master was used as the separation source)
the sound recording, regardless of vocal removal. For a monetized, automated,
multi-upload-per-day channel, this risk compounds: repeated strikes can affect the whole
channel, not just one video.

This leaves two real paths, with a genuine tradeoff the operator must weigh, not one this
research doc will pick for them:
- **Trending-but-risky:** using stems of an actually-trending copyrighted track for
  maximum algorithmic alignment with what's currently being pushed, accepting real
  Content ID / demonetization / takedown exposure that scales with upload volume and
  channel monetization status.
- **Royalty-free-but-safer:** sourcing music from a properly licensed royalty-free/synced
  library (e.g. YouTube's own Audio Library, Epidemic Sound, Artlist, Soundstripe, Pixabay
  Music) intended for commercial/monetized use, at the cost of not riding a specific viral
  trend's exact audio.

The operator should make this call explicitly per-channel (and can mix strategies —
e.g. royalty-free as the default with occasional deliberate, individually-cleared
trending-audio use) rather than defaulting to trending-stems for every upload.

## Open Gaps

- `en_US-amy-medium`'s actual license (linked as "See URL" to the Mycroft AI
  `mimic3-voices` repo) was **not verified** in this session — budget was spent instead on
  confirming the `lessac` research-only restriction and the `libritts_r` CC BY 4.0
  alternative, which was judged more decision-relevant. If the operator specifically wants
  `amy`'s voice character, verify its license before commercial use.
- No other open-source TTS engines (e.g. Coqui TTS, and its variants) were comparatively
  evaluated against Piper within this channel's budget — Piper was chosen directly based on
  it being the engine explicitly known to run CPU-only on constrained runners, and that
  was confirmed by actually running it, not just asserted.
- Music-sourcing platform names (TikTok Creative Center, Chartmetric, Epidemic Sound, etc.)
  reflect established, real, named products but were not individually re-verified via
  Firecrawl in this session (budget was allocated to the topics/design/voice-license
  investigations, which surfaced a concrete legal caveat worth the trade-off) — if the
  operator needs a specific current URL/pricing for one of these, verify directly.
