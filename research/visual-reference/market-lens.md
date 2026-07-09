# Market Lens — Visual Reference Moodboard (Phase 1)

Channel: **Market Lens** — economics, markets, policy, trade, current trends.
Tone target: sharp, analytical, macro-explainer.

All findings below trace to a URL actually fetched with Firecrawl (REST API,
`research/frames_tmp/market-lens/s*.json` holds the raw responses) or to a
video actually downloaded with yt-dlp and processed with ffmpeg/PIL
(`research/frames_tmp/market-lens/`). Firecrawl usage for this channel:
15 calls (9 `/v1/search`, 6 `/v1/scrape`), within the ~15-call budget.

## Source References

Motion-design galleries (Dribbble / Behance / Awwwards):
- https://dribbble.com/search/data-motion
- https://dribbble.com/search/data-visualization-motion
- https://dribbble.com/search/financial-data
- https://dribbble.com/search/animated-data
- https://dribbble.com/search/dynamic-chart
- https://dribbble.com/search/finance-motion
  (Dribbble search-result pages only — individual shot pages are behind
  client-side rendering Firecrawl's markdown scrape didn't resolve within
  budget; see Open Gaps.)
- https://www.behance.net/search/projects/animated%20chart%20finance%20animation
- https://www.behance.net/search/projects/Financial%20animation%20infographic
- https://www.behance.net/search/projects/animated%20infographics
- https://www.behance.net/search/projects/animated%20charts
- **https://www.behance.net/gallery/78074399/Motion-design-video-for-Financial-Services-Company**
  (scraped in full — Animazzio/Eugene Kukharsky project, After Effects +
  Illustrator, financial-services explainer with animated line charts,
  icon build-ons, and outline-style infographics; embeds
  https://www.youtube.com/watch?v=9PC8kXKxmNU)
- **https://www.awwwards.com/websites/data-visualization/** (scraped in full
  — current 2026 Data Visualization collection; notable real entries
  observed: "People's Audit", "Negotiated Intelligence",
  "Obama Presidency Oral History", "World Cup 2026, simplified.",
  "CryptOwl", "ashMeteo")

Currently-circulating economics/markets short-form video (Shorts/Reels),
used both as topic signal (Phase 2) and visual/motion signal (Phase 1):
- https://www.instagram.com/reel/DBhduCKq3kk/ — tariffs explainer, on-screen
  stat callouts ("TARIFFS = TAXES ON IMPORTS")
- https://www.instagram.com/reel/DYTMglyBdi8/?hl=en — Fed/Warsh inflation
  explainer with chart-style captions
- https://www.instagram.com/reel/DUZicIjkSsM/?hl=en — AI-bubble market
  sell-off, "ZOOM OUT" callout style
- https://www.instagram.com/reel/DZycGgQiLiF/ — SF AI-boom real estate reel
- https://www.instagram.com/reel/DMYGKtyR8p9/ — "#Tariffs explained in 60
  seconds" (download attempted, failed — see Open Gaps)
- **https://www.youtube.com/shorts/5BZDu9oQyhU** — "What are tariffs and how
  do they affect the economy? TCU professor explains" — **downloaded via
  yt-dlp, frames extracted, contact sheet built** (see below)

Choreography/easing reference (per brief instruction, no packaged
motion-design skill exists here, so citing Motion.dev's own public docs
directly):
- https://motion.dev/docs/easing-functions
- https://motion.dev/docs/spring
- https://motion.dev/docs/react-transitions

TTS/voice and music-sourcing citations are listed in the companion Phase 2
file, not repeated here.

## Video Reference → Contact Sheet

Downloaded: `youtube.com/shorts/5BZDu9oQyhU` ("What are tariffs and how do
they affect the economy? TCU professor, Rishav Bista, explains it.")
- Source file: `research/frames_tmp/market-lens/clips/clip1.mp4`
- Verified via ffprobe: 360×640 (9:16 vertical), ~24fps (24000/1001),
  61.99s duration
- Frames extracted every 3s with `ffmpeg -vf fps=1/3` →
  `research/frames_tmp/market-lens/frames_clip1/frame_001.png` … `frame_021.png`
  (21 frames)
- Contact sheet assembled with PIL (script:
  `research/frames_tmp/market-lens/build_contact_sheet.py`) →
  `research/frames_tmp/market-lens/contact_sheet_1.png` (6-column grid,
  timestamp labels, gitignored working copy)
- Committed copy (compressed JPEG, ~270KB, same contents) for reference
  from this doc: `research/visual-reference/market-lens-contact-sheet-1.jpg`

A second video reference (`instagram.com/reel/DMYGKtyR8p9/`) was attempted
via yt-dlp twice and failed both times — Instagram's session/anti-bot layer
reset the connection before the post could be fetched. No second contact
sheet was produced; this is disclosed rather than papered over (see Open
Gaps). One contact sheet meets the brief's stated minimum of "at least 1-2."

## Extracted Color Tokens

All hex values below were sampled directly with PIL from the actual
extracted frames of `clip1.mp4` (not estimated by eye), via
`research/frames_tmp/market-lens/extract_colors.py` and follow-up targeted
pixel samples. Source frame/coordinates noted per token.

| Token | Hex | Source |
|---|---|---|
| Brand/bumper purple (gradient) | `#58347A` → `#815EA9` | frame_001.png (opening "TARIFFS EXPLAINED IN 60 SECONDS" title card), sampled at 4 corner/edge points |
| Data/chart background (near-black) | `#000000`–`#010000` | frame_009.png (stock-chart b-roll behind presenter, t=24s) |
| Data-chart grid/accent blue | `#265DBA` | frame_009.png, dot-grid/line accent over chart background |
| US flag blue field | `#3369BC` | frame_017.png (t=48s, flag+cash b-roll) |
| Presenter wardrobe navy | `#34394A` | frame_008.png, shirt fabric sample |
| Checklist positive/checkmark green | `#238325` | frame_014.png (t=39s "✅ market volatility" build-up list) |
| Caption/label chip (near-white neutral) | `#D1D0D5` | frame_014.png, translucent text-background chip |

Not hex-confirmed: a red "up-arrow" accent is clearly visible by eye in the
contact sheet on the "↑ retail prices" callout (t≈15–18s row), but its
on-screen window fell between the 3s-interval extraction and a supplemental
targeted frame grab at t=16s, so no pixel sample landed on it. Treat as
"observed, not hex-confirmed" — do not treat any specific red hex as
sourced.

## Typography Tokens

Described structurally from the contact sheet (no font-identification
tool available in this environment, so family names are not claimed):

- **Headline / bumper text** ("TARIFFS EXPLAINED IN 60 SECONDS," closing
  logo card): bold, heavily condensed sans-serif, slight italic slant,
  all-caps, stacked 2–3 lines, tight leading (~0.9x), large scale
  (~15–18% of frame height per line) — high-impact title-card treatment.
- **Overlay stat labels** ("↑ retail prices," "↓ consumption," "domestic
  industries," "INPUT PRICE," "PRODUCTION COST"): bold sans-serif, mixed
  case for lower-third callouts / all-caps for chart-overlay labels, short
  icon glyph prefix (arrow or emoji), white text on a dark or translucent
  rounded chip, medium scale (~5–6% of frame height).
- **Checklist items** ("✅ international retaliation," "✅ market
  volatility" …): bold sans-serif, sentence case, green-checkmark prefix,
  left-aligned, additive stacking (new line added rather than text
  replaced), consistent line height.

## Spacing Tokens

Observed from frame composition (approximate, as fractions of the 360×640
frame):

- Overlay callouts anchor to the **upper third**, ~8–10% margin from the
  top edge, ~5% margin from the left edge.
- The checklist block anchors to the **lower-left quadrant**, ~5% left
  margin, ~4–5% vertical gap between stacked items.
- The presenter cutout is horizontally centered and occupies roughly the
  middle 60% of frame height, acting as a fixed compositional anchor while
  background/overlay layers change.
- Title/bumper cards use a centered vertical stack with generous
  whitespace (~15–20% of frame height above and below the headline block).

## Motion/Pacing Notes

- Source clip: 24fps native, 61.99s total, vertical 9:16.
- Sampling at 3s intervals (72 native frames per interval) shows a
  background/overlay change at nearly every sample point through the first
  ~35s (t=0,3,6,9,12,15,18,21,24,27,30,33s all show a distinct visual
  change — new b-roll, new stat callout, or both), then the pace relaxes to
  ~9–15s holds during the checklist build-up section (t=36–45s) and the
  closing card (t=54–60s).
- The checklist section uses an **additive reveal** pattern — a new
  checkmarked line is added roughly every 3s while prior lines persist,
  rather than a cut-and-replace pattern.
- Converting the observed ~3s beat cadence to the 60fps reference the brief
  asks for: 3s × 60fps = **~180 frames per overlay/cut beat** during the
  fast section — a brisk pace typical of retention-optimized explainer
  Shorts, though not a rapid-fire meme-cut pace (which would run
  closer to 30–60 frames/beat).
- The presenter/cutout element itself is nearly motion-static (arms folded,
  minimal gesture) — the background plates and text/icon overlays do
  essentially all of the "motion" work. This is a directly relevant
  precedent for a faceless/automated channel: a single static or
  slow-drifting base layer (a b-roll loop, a chart, a map) can carry a full
  Short if the overlay layer is doing frequent, punchy work on top of it.
- Motion.dev's own docs (cited above) describe spring-based easing
  (stiffness/damping/mass, not fixed-duration curves) as the mechanism for
  the kind of snappy, slightly-overshooting settle seen in UI/data-reveal
  animation — consistent with the "pop in, settle" character of the
  checkmark and stat-callout reveals in the reference clip and in the
  Animazzio finance-explainer project (chart-line and icon build-ons).

## Motion-Personality Direction

Grounded in the TCU Shorts explainer (fast overlay cycling, additive
checklist, static presenter anchor), the Animazzio/Behance finance motion
project (chart-line reveals, icon build animations), and the Instagram
Reel examples (bold caption-driven stat callouts):

- **Layout variance: Medium.** Compositions shift meaningfully between
  b-roll/chart backdrop and lower-third callouts from beat to beat, but a
  fixed anchor (the presenter cutout in the reference; for Market Lens,
  a consistent title-safe grid — headline zone / chart-or-visual zone /
  caption zone) stays put shot to shot. Recommendation: vary the
  background content (chart, ticker, map, icon set) on nearly every beat
  to sustain attention, but keep the safe-zone grid itself constant so a
  viewer never has to re-locate where captions or the "main visual" will
  appear.
- **Motion intensity: Medium-high.** The reveals observed (checkmarks
  popping in, chart lines extending, stat callouts sliding/scaling in) read
  as snappy and slightly overshooting rather than slow or cinematic —
  consistent with spring-based easing per Motion.dev's docs. Recommendation:
  use spring/overshoot easing on data reveals (counters, bars, arrows,
  checkmarks) to sell the "sharp, analytical" read; keep any camera-style
  moves (pans/zooms on the base layer) restrained, since the reference's
  base layer itself stayed close to static while overlays carried the
  energy.
- **Visual density: Medium-high.** The reference frequently stacks 2–4
  simultaneous text/icon elements (multi-item checklist, dual stat
  callouts) against an already-busy chart or archival-photo backdrop.
  Recommendation: allow layered data callouts (a headline stat plus one
  supporting micro-label) but cap concurrent on-screen text blocks at
  ~3, matching the point in the checklist reference where a 4th–5th
  stacked line starts to feel cluttered on a small phone screen.

## Open Gaps

- Dribbble shot pages (individual shots, not search-listing pages) were
  not scraped — Dribbble's search-result pages returned by Firecrawl are
  category listing pages, and following into individual client-rendered
  shot pages was not attempted in order to stay inside the ~15-call
  budget. The Behance project page and the downloaded video contact sheet
  substitute as the grounded visual sources instead.
- Second video reference (`instagram.com/reel/DMYGKtyR8p9/`) could not be
  downloaded — two yt-dlp attempts both failed with a connection reset
  from Instagram's session layer. Only one contact sheet was produced.
- The red "up-arrow" accent color visible by eye in the contact sheet
  (retail-prices callout) is not hex-confirmed — flagged above rather than
  invented.
- Exact typeface family names for the headline/caption type could not be
  identified — no font-recognition tool is available in this environment;
  typography tokens above are structural descriptions only, not font names.
