# Venture Forge — Visual Reference Moodboard (Phase 1)

Channel: **Venture Forge** — startups, business models, strategy, founder case studies.
Tone: sharp, energetic, builder-to-builder.

Research method: Firecrawl REST API (search + scrape, 15 calls used against the
~15-call channel budget) for motion-design galleries and real Shorts, plus
`yt-dlp` + `ffmpeg` + `PIL` to download one real reference Short and build a
contact sheet with measured pixel data. No fabricated sources — every claim
below traces to a fetched URL or a locally-produced frame/contact-sheet
measurement.

## Source References

Motion-design gallery references (Firecrawl `search` + `scrape`):

1. https://dribbble.com/search/dashboard-for-fintech (search index)
2. https://dribbble.com/shots/26931900-Fintech-Dashboard-Motion-Design-Animation-for-Finance-App (scraped — dark-UI fintech dashboard motion piece with a published designer color palette)
3. https://dribbble.com/search/dashboard-2025 (search index)
4. https://dribbble.com/shots/24459570-FinTech-UI-Motion-Design-Product-Video (scraped — fintech product/explainer motion video shot)
5. https://dribbble.com/search/finance-motion (search index)
6. https://www.awwwards.com/websites/sites_of_the_day/ (search result only, not deep-scraped — see Open Gaps)
7. https://www.awwwards.com/websites/business-corporate/ (search result only, not deep-scraped — see Open Gaps)

Choreography/timing best-practice references (per brief instruction, cited directly, not deep-scraped):

8. https://motion.dev/docs/easing-functions
9. https://motion.dev/docs/spring

Real high-performing/relevant Shorts references (Firecrawl `search`, real current YouTube Shorts URLs):

10. https://www.youtube.com/shorts/eBZyBNVP6YQ — "Del Monte Bankruptcy Explained | Business Model Breakdown" — channel **Agribusiness Academy**, uploaded 2025-07-05, 93s, ~2,984 views at time of research (confirmed via `yt-dlp --dump-json`). **This is the video downloaded and analyzed below.**
11. https://www.youtube.com/shorts/hLg86-Ju9oM — "How Much Should A Small Business Spend on Payroll?"
12. https://www.youtube.com/shorts/p1ZVXvTQp3w — "E-2 Visa: Franchise vs. Startup vs. Existing Business"
13. https://www.youtube.com/shorts/k79AvuTOVW0 — "Most founders don't realize this until it's too late #startup #mistake"
14. https://www.youtube.com/shorts/wrffahYeZjc — "Initial Startup Costs of a Cloud Kitchen | Mesa Dissects Rotiwala.com"
15. https://www.youtube.com/shorts/FxA5MJVhN-U — "Why Most Founders Chase the Wrong Thing" (Beyond Titles, Tamseel Hussain)

Video reference obtained and analyzed via yt-dlp + ffmpeg + PIL:

- Downloaded: `https://www.youtube.com/shorts/eBZyBNVP6YQ` → saved to
  `research/frames_tmp/venture-forge/ref1_eBZyBNVP6YQ.mp4` (360x640, 30fps,
  92.83s, h264/aac).
- Frames extracted at 1 frame/3s (31 frames) → contact sheet built with PIL,
  committed (small, compressed) at:
  `research/visual-reference/venture-forge/contact_sheet_1.jpg`
  (full-resolution working copy retained, gitignored, at
  `research/frames_tmp/venture-forge/contact_sheet_1.png`)
- A second, finer-grained pass at 4fps for the first 20s (80 frames) was
  extracted specifically to measure cut frequency (gitignored working file,
  not committed): `research/frames_tmp/venture-forge/cutcheck_sheet.png`
- Only **one** video reference was downloaded and analyzed in depth (the
  brief allows "1-2"). A second full contact sheet was not produced within
  the Firecrawl/time budget — see Open Gaps.

## Extracted Color Tokens

Two distinct, separately-grounded palettes — an **aspirational UI/motion-design
palette** (from the Dribbble fintech dashboard shot, which publishes its own
exact hex palette) and an **observed on-screen Shorts palette** (measured
directly from downloaded video frame pixels with PIL).

**A. Aspirational dashboard/motion-design palette** (published by the
designer on dribbble.com/shots/26931900, downloaded via the shot's own
"Download color palette" link data returned by Firecrawl scrape):

| Hex | Role (as used in the shot) |
|---|---|
| `#070403` | near-black dark-UI background |
| `#E82B08` | primary accent red |
| `#FA9F1A` | accent orange |
| `#F25D0D` | accent orange-red (mid-ramp) |
| `#59372D` | dark warm brown (secondary surface) |
| `#FBC65B` | accent amber/gold |
| `#E8D6B4` | light warm neutral (text-safe surface) |
| `#AA3F21` | deep burnt-orange (shadow/accent) |

This is a dark-mode fintech dashboard built on a near-black base with a
single warm red→orange→amber accent ramp — described in the shot's own
project text as "a dark UI that keeps the focus where it matters."

**B. Observed on-screen Shorts palette** (sampled with PIL directly from
pixels of `ref1_eBZyBNVP6YQ.mp4` frames — coordinates and method: PIL
`Image.getpixel` / masked-region averaging on cropped regions of
`frames1/frame_020.png`, 360x640 source resolution):

| Hex | Role (measured location) |
|---|---|
| `#E85953` | coral-red keyword-highlight box behind emphasized caption words (avg of ~450 masked pixels in the highlight-box region) |
| `#3894B1` | teal-blue lower-third channel watermark logo ("IFAL") |
| `#EFC833` | golden-yellow bold section-title card text ("ACQUISITION") |
| `#D6DCE8` | pale blue-lavender background of the CTA end-card |
| `#141022` | near-black navy of the CTA end-card's dark UI block |
| `#594838` / `#2F261A` | warm brown/dark-olive tones from warehouse B-roll (dominant-color quantization of `frame_004.png`) |
| `#C49F51` / `#DACBA2` | warm amber/tan product-photography midtones (dominant-color quantization of `frame_020.png`/`frame_021.png`) |

Caption body text itself is plain white fill with a black stroke/outline
(standard high-contrast burned-in caption treatment), confirmed visually in
`crop_bottom.png`.

**Cross-reference:** both palettes independently converge on a warm
red/orange/amber accent against a dark or high-contrast neutral base — this
recurrence across an aspirational dashboard shot and a real, currently-live
business-Shorts channel is the basis for the accent-color recommendation
below.

## Typography Tokens

- Dribbble shots are rendered as flattened video/image assets — no CSS or
  font metadata is exposed via Firecrawl's markdown/HTML scrape, so **exact
  typeface family cannot be verified** for reference #2/#4 (flagged in Open
  Gaps). Visually the dashboard shot uses a clean geometric sans for both
  large bold KPI numerals and smaller regular-weight secondary labels — a
  standard SaaS-dashboard hierarchy (bold headline metric + regular
  supporting label), typical of the fintech-product-design genre.
- From the downloaded Short (measured directly on 360x640 frame pixels via
  crop bounding boxes, `crop_bottom.png` / `crop_title.png`):
  - Caption line ("To its credit," style burned-in captions): cap-height
    ≈ 16–20px of a 640px-tall frame ⇒ **≈ 2.5–3% of frame height**. Bold
    sans, white fill, black outline, normal tracking.
  - Section-title card text ("ACQUISITION"): cap-height ≈ 35–40px of the
    same frame ⇒ **≈ 5.5–6.5% of frame height**. Bold/condensed sans,
    solid golden-yellow fill (`#EFC833`), no outline, tight tracking.
  - Measured scale ratio between the two tiers: **≈ 2:1** (title text is
    roughly double the cap-height of caption text).
- Exact font family for the Short's captions/title cards is also not
  verifiable (burned-in/rasterized text, no embedded font metadata) —
  flagged in Open Gaps.

## Spacing Tokens

- Caption block horizontal inset, measured on `frame_020.png`: text begins
  roughly 20px from the left edge of a 360px-wide frame ⇒ **≈ 5–6% left
  margin**, consistent with a title-safe inset.
- Lower-third watermark logo sits in the bottom **≈12–15%** of frame height,
  right-of-center — positioned to avoid the caption block directly above it.
- Standard 9:16 Shorts/Reels platform convention (not independently
  re-measured here, cited as general platform knowledge rather than a
  Firecrawl-sourced claim) reserves roughly the bottom ~20% of the frame for
  platform UI (like/comment/share rail). The observed captions in this
  reference stay clear of that zone, consistent with the convention.
- No dedicated 8px/4px-style spacing grid could be confirmed from a single
  compressed video reference — flagged in Open Gaps.

## Motion/Pacing Notes

Cut frequency was measured directly, not estimated: the first 20 seconds of
`ref1_eBZyBNVP6YQ.mp4` were re-extracted at 4fps (`frames_fine/`, 80 frames)
and visually reviewed via `cutcheck_sheet.png`.

- **Hard cuts observed in the first 20s:** 3 — at ≈3.5s, ≈8.25s, ≈16.0s.
- **Shot lengths measured:** ≈3.5s (Del Monte warehouse exterior),
  ≈4.75s (static product/can shot), ≈7.75s (warehouse interior with slow
  camera pan), then a new shot continuing past the 20s sample window.
- **Average shot length:** ≈5.3s across the 3 measured cuts ⇒ **≈320
  frames at a normalized 60fps** — a notably unhurried pace compared to
  rapid meme-cadence Shorts (sub-1s cuts). Some "shots" contain a slow
  Ken-Burns zoom/pan on a still photo rather than being fully static,
  adding motion without a cut.
- **Caption/text-overlay cadence is decoupled from and faster than the
  visual cut rate:** new caption text chunks (1–3 words) change roughly
  every 0.75–1.5s regardless of whether the underlying B-roll has cut,
  based on caption-text changes visible across the fine-sampled frames
  (e.g. "Del Monte one" → "of the most" → "recognized names" inside a
  single ≈4.75s product shot). Emphasized words get the coral
  keyword-highlight box (`#E85953`) treatment progressively, i.e. a
  karaoke/progressive-reveal caption style layered independently on top of
  slower-cut B-roll.
- No elastic/bounce/overshoot easing was detected on caption pop-ins at
  4fps (250ms) sampling resolution — captions appear to hard-cut/appear
  rather than spring in. This sampling rate cannot rule out a fast (<250ms)
  eased entrance; flagged in Open Gaps.
- Choreography/timing best-practice grounding: Motion.dev's public docs
  (motion.dev/docs/easing-functions, motion.dev/docs/spring) distinguish
  tween/easing-curve animation from physics-based spring animation as the
  two standard toolkits for this kind of UI/caption motion — cited here as
  the timing-vocabulary reference per the research brief's instruction,
  not as a claim about this specific Short's implementation.

## Motion-Personality Direction

Three dials, each grounded in what was actually observed above (not
invented):

- **Layout variance: medium.** The analyzed Short rotates between three
  recurring composition types shot-to-shot — full-bleed B-roll, a
  blurred-fill vertical background behind a centered sharp product shot,
  and a bold flat-color title-card interstitial ("ACQUISITION") — while
  keeping caption placement and safe-zone position fixed across all three.
  Recommend the same approach for Venture Forge: rotate between full-bleed
  stock/B-roll, data/stat callout cards, and bold title-card interstitials
  from shot to shot, but keep the caption band and lower-third position
  constant so the format reads as consistent across an automated pipeline.
- **Motion intensity: medium-low.** No spring/overshoot easing was
  observed on captions (hard appear/cut), and camera movement was limited
  to slow Ken-Burns zoom/pan rather than aggressive whip-pans or snap
  zooms; average shot length (~5.3s) is unhurried. This is reinforced by
  the Dribbble fintech dashboard reference's own stated intent — "smooth,
  easy-to-follow animations" (quoted from the shot's project description)
  rather than aggressive motion. Recommend restrained eases (standard
  ease-out tweens, no heavy spring overshoot) for Venture Forge — the
  "sharp, energetic" tone should come from caption density, cut selection,
  and copy, not from exaggerated spring physics.
- **Visual density: medium-high.** Captions are near-continuous (new text
  every ~1s) layered over B-roll, plus a persistent lower-third watermark
  and periodic bold-color title/stat cards — multiple simultaneous
  information layers. The dashboard reference shows the same instinct in a
  different medium (dense multi-metric dark-UI layout using color contrast,
  not negative space, to direct the eye). Recommend medium-high density for
  Venture Forge: constant caption presence plus periodic data-callout
  cards, using one restrained accent color (a coral/amber pulled from the
  observed and published palettes above) to direct focus rather than
  empty space.

## Open Gaps

- Exact typeface/font family for both the Dribbble dashboard shot and the
  analyzed Short's captions/title cards could not be verified (rasterized
  video/image assets expose no font metadata via Firecrawl scrape or frame
  extraction). Treat "geometric sans, bold for emphasis" as a directional
  description, not a specified typeface.
- The two Awwwards listing URLs (#6, #7 above) were fetched via `search`
  only (title/description snippets); individual "site of the day" case
  study pages were not deep-scraped within the ~15-call budget, so no
  Awwwards-sourced color/typography tokens are included above.
- Only one video reference was downloaded and analyzed with a full contact
  sheet. A second reference (the brief allows "1-2") was not produced —
  the five additional real Shorts URLs listed under Source References were
  confirmed to exist via Firecrawl search but not downloaded/frame-analyzed.
- Caption pop-in easing curve could not be confirmed at sub-250ms
  resolution; a native-30fps frame-by-frame pass would be needed to
  measure exact entrance timing/easing.
- No fine-grained 4px/8px layout grid could be confirmed from a single
  compressed, re-encoded (YouTube-transcoded) video source — spacing
  percentages above are frame-relative measurements, not confirmed design-
  tool grid values.
