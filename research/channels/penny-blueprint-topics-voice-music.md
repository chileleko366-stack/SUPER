# Penny Blueprint — Topics, Voice, Music (Phase 2)

Channel: **Penny Blueprint** — budgeting, investing, taxes, debt reduction,
practical wealth-building. Tone target: practical, trustworthy, no-hype
personal finance.

Firecrawl usage for this channel (shared with Phase 1, same session): 12
calls total (5 `/v1/search`, 7 `/v1/scrape`), within the ~15-call budget.
Voice-provider and music-sourcing research below used WebSearch/WebFetch
(not counted against the Firecrawl budget, per the brief's allowance to use
non-Firecrawl tools for anything other than current design-trend/topic
facts) — every claim below still traces to a URL actually fetched.

## Topics — 8-10 real current examples

Each entry is a real, currently-live topic sourced via Firecrawl search
(not invented), with the URL actually fetched and a one-line note on the
Shorts-worthy angle.

1. **"Loud budgeting"** — the TikTok-originated trend of being vocal about
   spending limits/financial goals rather than quietly declining. Strong,
   already-proven Shorts hook format ("say no out loud").
   https://www.bankrate.com/banking/loud-budgeting/
2. **Cash stuffing / doom spending / "social-media money habits"** — Gen Z
   money-management trends being actively covered by a bank's own content
   team, i.e. proven mainstream-finance-brand-relevant angle.
   https://www.bokfinancial.com/insights/articles/is-social-media-shaping-your-money-habits
3. **"Cash condensing"** — visual short-form format of converting small
   bills into a large round savings total (July 2026 example, i.e. live
   right now).
   https://www.youtube.com/watch?v=lM3Kxl1-OzE
4. **"Innovative Budgeting Techniques for 2026"** — Rachel Cruze (Ramsey
   Solutions personality) posting budgeting-method content on TikTok;
   useful as a direct in-niche creator/format benchmark.
   https://www.tiktok.com/@rachelcruze/video/7590044811357343007
5. **"2026 All-In-One Budget Planner"** — creator content built around a
   budget-planner tool/template, tagged `#debtfreejourney` — evergreen
   "tool tour" Shorts format.
   https://www.tiktok.com/@plan.it.easy/video/7594481243589283084
6. **6-Step Financial Plan for 2026** (California DFPI, government/consumer-
   protection source) — covers the 50/30/20 budgeting rule framing directly.
   https://dfpi.ca.gov/news/insights/6-step-financial-plan-for-2026/
7. **Money resolutions: paying down debt, saving for retirement, student
   loans, starting to invest** (PBS NewsHour, expert-sourced) — a
   multi-topic explainer piece that maps to several standalone Shorts.
   https://www.pbs.org/newshour/economy/expert-tips-for-paying-down-debt-saving-for-retirement-and-other-financial-goals
8. **Building an emergency fund, paying off debt, and making a 2026 money
   plan** (Orlando Sentinel).
   https://www.orlandosentinel.com/2026/01/10/how-to-build-an-emergency-fund-pay-off-debt-and-make-a-plan-for-your-money-in-2026/
9. **"6 Financial Changes To Make in 2026"** — paying off high-interest
   debt, consolidating forgotten retirement accounts (Money Guy).
   https://moneyguy.com/article/6-financial-changes-to-make-in-2026/
10. **"5 Simple Budgeting Tips for Beginners"** — a real, currently-live
    sub-60s Short (49s) already performing this exact format; also the
    video downloaded and frame-analyzed in the companion Phase 1 doc, so
    its structure (5 numbered tips, title card + b-roll + caption bar,
    CTA outro) is directly evidenced, not just described secondhand.
    https://www.youtube.com/watch?v=YtCRwOQZ3xg

## Voice Provider

**Kokoro-82M**, checkpoint `hexgrad/Kokoro-82M` (v1.0), run via the
`kokoro-onnx` ONNX Runtime inference path for CPU use.

- Model card: https://huggingface.co/hexgrad/Kokoro-82M — confirmed
  **Apache-2.0 license** on the weights. The card states the model "can be
  deployed anywhere from production environments to personal projects" and
  "has been deployed in numerous projects and commercial APIs" —
  commercial use is explicitly permitted, with no separate non-commercial
  clause (unlike, e.g., Coqui XTTS v2's CPML license, which this research
  pass therefore ruled out for this channel).
- Repo: https://github.com/hexgrad/kokoro — Apache-2.0 confirmed in the
  repo footer/license file.
- Size: 82M parameters, described as a "lightweight architecture" —
  substantially smaller than diffusion/flow-based TTS stacks, which is why
  it's a realistic candidate for a shared/no-GPU CI runner.
- CPU inference path: the community `Kokoro-FastAPI` wrapper
  (https://github.com/remsky/Kokoro-FastAPI, Apache-2.0 for the wrapper and
  the underlying weights, MIT for the StyleTTS2-derived inference code)
  ships a documented **CPU-only Docker path** (`docker/cpu`,
  `kokoro-fastapi-cpu` image), confirming CPU-only operation is a
  first-class, supported use case, not a hack.
- CPU speed benchmark actually found: a public benchmark
  (https://gist.github.com/efemaer/23d9a3b949b751dde315192b4dcf0653) shows
  Kokoro-82M running at **RTF ≈ 5x realtime on both PyTorch and ONNX CPU
  backends**, tested on a 32-vCPU AWS `c6a.8xlarge` instance.
- **Rough CPU inference time for a ~150-word script on a GitHub Actions
  runner:** GitHub's own docs
  (https://docs.github.com/en/actions/reference/runners/github-hosted-runners)
  confirm the standard `ubuntu-latest` runner has **2 vCPUs / 7GB RAM** —
  1/16th the cores of the 32-vCPU box the 5x figure was measured on. A
  ~150-word script is roughly 60–70 seconds of natural-pace spoken audio.
  This research pass did **not** directly benchmark Kokoro on an actual GH
  Actions runner, so treat the following as a reasoned extrapolation, not a
  measured number: even in a pessimistic scenario where the 2-vCPU runner
  gets none of the multi-core speedup and only achieves roughly real-time
  (RTF ≈ 1x) throughput, synthesizing ~60–70s of audio would still take
  only **roughly 60–70 seconds of CPU time** — comfortably inside a normal
  CI job timeout. **Recommend a timed smoke-test run in the actual GitHub
  Actions environment before relying on this for pipeline scheduling.**
- Why Kokoro over the alternatives checked: Piper TTS
  (https://github.com/rhasspy/piper) was also considered — it's fast and
  historically MIT-licensed, but active development has moved to
  https://github.com/OHF-Voice/piper1-gpl, which is **GPL-3.0**, a
  meaningfully murkier commercial-licensing story for an automated,
  monetized pipeline than Kokoro's clean Apache-2.0. Coqui XTTS v2 was
  ruled out without a fresh fetch this pass because it is widely documented
  as shipping under Coqui's non-commercial CPML license, which would fail
  the brief's "license permitting commercial use" requirement outright —
  flagged here as based on prior knowledge, not re-verified via a fresh
  citation this session (see Open Gaps).
- Persona fit: Kokoro's American-English voice packs include calm, clear,
  neutral-register options well suited to a "practical, trustworthy,
  no-hype" explainer read (as opposed to a hyped/energetic delivery). This
  research pass did not run an independent listening test to pick a single
  named voice ID from Kokoro's voice pack — that's a fast, low-risk task
  for the production pipeline itself (generate 2–3 sample lines with the
  candidate voice IDs and pick by ear), flagged in Open Gaps rather than
  guessed here.

## Music Sourcing

**Method to identify trending tracks in this niche:** use TikTok Creative
Center's Trends → Songs tool
(https://ads.tiktok.com/business/creativecenter/inspiration/popular/music/pc/en,
confirmed via search to be TikTok's own free, no-login-required trending-
sounds dashboard, filterable by region and time period, with per-track
interest-over-time and related-video analytics) as the primary discovery
surface, cross-referenced against what comparable finance/budgeting
creators are actually using in their current posts (e.g. the TikTok
examples cited in Topics above). For platform-specific safety, note that
most tracks surfaced in the general Trends tool are cleared for organic
posts only — TikTok's separate Commercial Music Library is the
ads-cleared subset, relevant if any paid-promotion is layered on top of
organic uploads later. YouTube Shorts' own in-app "trending audio"
indicator on the Shorts creation screen is the equivalent first-party
signal for that platform and should be checked directly at production
time (not independently fetched this pass — see Open Gaps).

**Method to obtain stems/instrumentals:**
1. **Royalty-free route (safer):** licensed/free libraries — YouTube Audio
   Library (most tracks free for commercial use, no attribution required
   for the majority of the catalog), Uppbeat (real free tier plus a paid
   Pro plan whose license extends to client work/advertising, and which
   offers "channel safelisting" specifically to help prevent automated
   copyright claims), and subscription libraries like Epidemic Sound or
   Artlist (flat monthly fee, full composition + master rights bundled,
   cleared across platforms, no per-track credit required). These were
   confirmed via a July 2026 comparison search rather than assumed from
   prior knowledge.
2. **Stem-separation route (for working with a trending track):** run the
   trending track through an open-source source-separation model —
   **Demucs** (https://github.com/facebookresearch/demucs, Meta AI
   Research, **MIT license**, "free for personal and commercial use") is
   the standard open tool for splitting a mixed track into vocal,
   drum, bass, and "other" stems, letting a creator isolate the
   instrumental bed of a trending song. Community CLI wrappers such as
   `python-audio-separator` build directly on Demucs/UVR models for this
   exact vocals-vs-instrumental use case.

### Copyright Risk Flag

Stem-separating the vocals out of a trending, currently-copyrighted song
and using only the resulting instrumental does **not** clear the
underlying composition's copyright — the melody, chord progression, and
arrangement are still owned by the songwriter/publisher regardless of
whether a vocal stem is present. On a monetized, automated channel this
still carries real Content ID and takedown/demonetization risk: match
systems are not purely vocal-fingerprint based, and even where an
automated match is avoided, a manual claim or takedown from the rights
holder remains possible at any time after upload — including well after
the video has already accumulated views and been scheduled/forgotten by an
automated pipeline. Removing vocals reduces detection risk; it does not
eliminate legal risk. Against that, royalty-free/licensed-library tracks
carry essentially none of that risk but also carry none of the
"riding a trending sound" discovery/algorithmic boost that a currently-
viral track can provide — and for a **practical, trustworthy** personal-
finance brand specifically, an unexpected copyright strike or
demonetization event is also a credibility/trust cost, not just a
takedown-logistics cost. This is a real trending-but-risky vs.
royalty-free-but-safer tradeoff, and it is **not being decided here** — it
is the operator's call to make per video, weighing appetite for
takedown/claim risk and brand-trust exposure against the discovery upside
of a trending sound, especially given this channel's likely automated/
scheduled upload cadence where nobody may be watching in real time to
react to a claim.

## Open Gaps

- Coqui XTTS v2's license (referenced above as a reason to prefer Kokoro)
  was **not** re-fetched from a live source this session — it's stated
  based on prior knowledge that Coqui ships XTTS v2 under a non-commercial
  Coqui Public Model License (CPML). Verify the current license on
  https://huggingface.co/coqui/XTTS-v2 or https://github.com/coqui-ai/TTS
  directly before treating this as final, since license terms can change.
- No specific Kokoro voice-pack ID was selected for the persona — a fast
  listening test (2–3 sample lines per candidate American-English voice
  ID) is recommended in the production pipeline itself rather than picked
  blind here.
- Kokoro's ~5x-realtime CPU figure was measured on a 32-vCPU cloud
  instance, not on an actual 2-vCPU GitHub Actions `ubuntu-latest` runner —
  the ~60–70s inference estimate above is a reasoned extrapolation, not a
  direct benchmark. Run an actual timed smoke test in CI before finalizing
  pipeline timeout budgets.
- YouTube Shorts' own in-app "trending audio" panel was not independently
  fetched this pass (TikTok Creative Center was the one trending-sounds
  surface actually verified via search) — check it directly at production
  time as a second trending-audio signal alongside TikTok's.
- No live "here is today's specific trending track in the personal-finance
  niche" example was pulled — the sourcing *method* above is real and
  verified, but a dated snapshot of an actual current trending track was
  not captured, to conserve research time for the higher-priority topic/
  voice/visual research. The operator should run the TikTok Creative Center
  lookup live at production time rather than rely on a snapshot from this
  research date (2026-07-09).
