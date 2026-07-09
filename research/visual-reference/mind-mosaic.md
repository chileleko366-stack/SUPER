# Visual Reference Moodboard — Mind Mosaic

Channel: psychology / cognitive biases / emotions / self-improvement. Persona: warm,
insightful, non-clinical psychology communicator. This document is Phase 1 of the
per-channel research protocol in `docs/RESEARCH_BRIEF.md`.

Firecrawl budget used for this channel (shared across Phase 1 + Phase 2 of this
document set): **15/15 calls** — 9 `/v1/search`, 6 `/v1/scrape`, all 15 returned
HTTP 200. yt-dlp and ffmpeg were used in addition, per the brief, and do not count
against the Firecrawl budget.

## Source References

**Firecrawl — scraped (full page content fetched):**
- https://www.awwwards.com/sites/motion-ed — "Motion.ed" by Zajno, Awwwards Site of
  the Day (May 22, 2023). Full markdown fetched; 2-color palette block extracted
  (see tokens below). Chosen as a general motion-design quality benchmark, not
  psychology-specific.
- https://dribbble.com/shots/26486088-Mood-Tracker-A-Color-Driven-Mental-Health-UI —
  "Mood Tracker: A Color-Driven Mental Health UI" by Reliqio. Full markdown fetched;
  8-color palette with explicit emotion-to-color mapping extracted (directly
  relevant to an emotions/psychology channel — see tokens below).

**Firecrawl — search results (titles/descriptions/URLs returned by Firecrawl
`/v1/search`, not deep-scraped):**
- https://dribbble.com/search/bias
- https://dribbble.com/search/cognitive%20bias
- https://dribbble.com/tags/cognitive?page=2
- https://dribbble.com/search/cognitive
- https://medium.com/@beerad/cognitive-bias-in-motion-graphics-943df46ad26f
- https://www.instagram.com/reel/DAlIQYlRN3K/?hl=en
- https://www.awwwards.com/academy/courses/motion
- https://www.youtube.com/watch?v=J6aNMFZogyk — "Motion Design: Where, How And When
  To Use It," Louis Paquet talk
- https://www.awwwards.com/inspiration/motion-design-submission-67c97fe8169fe855608251
- https://www.behance.net/search/projects/kinetic%20typography
- https://www.behance.net/gallery/87781367/Motion-Design-Kinetic-Typography
- https://www.behance.net/search/projects/kinetic%20typography%20motion%20design
- https://www.behance.net/gallery/176934835/Kinetic-typography-(motion-graphics)
- https://www.behance.net/gallery/23664789/Kinetic-Typography
- https://dribbble.com/search/psychologist-app
- https://dribbble.com/shots/26941426-Mindfulness-Mental-Health-App-UI-Calm-Meditation-Experience
- https://dribbble.com/shots/25941922-AI-Mental-Health-Mobile-App-Design-Showreel
- https://dribbble.com/search/mental-health-resources
- https://www.tiktok.com/@donnellycss/video/7271683053246893345 — "Understanding the
  Halo Effect" (search snippet only, see yt-dlp note below)
- https://www.tiktok.com/@veritasium/video/7609332204602182926
- https://www.instagram.com/reel/DCCtqCjiJXs/
- https://www.tiktok.com/discover/cognitive-bias
- https://www.tiktok.com/@distilledscience/video/7110319980004019502
- https://www.youtube.com/shorts/8NOceZyOK6Q
- https://www.youtube.com/watch?v=QlEROiyNpyw
- https://www.youtube.com/shorts/F4H56kZH5oc
- https://www.youtube.com/shorts/9XSMm2mrVqg — downloaded and analyzed, see below
- https://www.youtube.com/shorts/d2Pye-De5lQ — download attempted, see Open Gaps
- https://www.youtube.com/shorts/2_XYM1rxJjU

**yt-dlp + ffmpeg — actually downloaded and analyzed for a contact sheet:**
- https://www.youtube.com/shorts/9XSMm2mrVqg — "The Hidden Cognitive Bias Even Smart
  People Suffer From," uploader Stephen Petro, 10,207 views. 360x640, 30fps,
  60.73s duration, 1822 native frames. Downloaded via `yt-dlp -f "best[height<=720]"`,
  frames extracted via `ffmpeg -vf "fps=1/2.5"` (24 frames), contact sheet
  assembled via PIL (6 cols x 4 rows, labeled with timestamps).

**yt-dlp — attempted, failed (stated explicitly per the brief rather than
silently dropped):**
- https://www.tiktok.com/@donnellycss/video/7271683053246893345 — yt-dlp reached the
  TikTok extractor and solved the JS challenge, but the requested video format was
  not available (likely region/format restriction on this specific upload).
  Not downloaded.
- https://www.youtube.com/shorts/d2Pye-De5lQ — yt-dlp reported a successful 60s/30fps
  download, but the resulting file was only 26KB and ffmpeg failed to decode it
  ("Invalid data found when processing input") — a truncated/corrupted download.
  Not usable; discarded rather than treated as a second data point.

## Extracted Color Tokens

**From programmatic dominant-color extraction (PIL, top-5 colors per 60x60
downsample) on actual frames of the downloaded reference clip
(`research/frames_tmp/mind-mosaic/frames_1/`):**
- `#0B1132`–`#131941` — dark navy background of the on-screen "personality trait"
  infographic card (t=5.0s–14.8s segment)
- `#1E1E1E`–`#2B2B2B` — near-black charcoal background of the animated brain/network
  data-visualization cutaway (t=35.0s–37.5s segment)
- `#1F3B30`–`#213D34` — dark forest-green, from the bookshelf background behind the
  talking-head host (environmental/set color, not a designed brand color, but
  present in the majority of frames since most of the video is talking-head)
- `#EFD300`–`#F5E10A` (measured via targeted pixel scan for yellow-family pixels,
  frame `frame_012.png`, t=27.5s) — the saturated gold-yellow used to highlight a
  single emphasized word in the caption ("BASE", "MEDICAL DIAGNOSES", "RATES ARE"
  were each highlighted this way at different timestamps), alternating with plain
  white for non-emphasized caption words

**From the Dribbble "Mood Tracker: A Color-Driven Mental Health UI" case study
(Reliqio) — an explicit, designer-articulated emotion-to-color system, directly
relevant to an emotions/psychology channel:**
- `#EDF3F2` — near-white/pale mint neutral (base/background)
- `#0A0606` — near-black (text/contrast)
- `#DACF8D` — muted gold
- `#B2E196` — soft green — mapped by the designer to **inspiration, joy, feeling
  fulfilled**
- `#F0A98B` — soft coral/peach — mapped to **lightness, playfulness, energy**
- `#E2726C` — coral-red — mapped to **tension, anger, anxiety**
- `#84BD60` — mid green
- `#47452F` — olive-dark
- (Blue, described in the case study text as mapped to **calm, gratitude, balance**,
  was named in the write-up but did not appear as one of the 8 swatched hex values
  on the page — noted rather than invented; see Open Gaps.)

**From the Awwwards "Motion.ed" Site of the Day reference (general motion-design
quality benchmark, not psychology-specific):**
- `#FDFCFA` — near-white
- `#0C0B0B` — near-black
- (A deliberately minimal 2-color palette, used here only as evidence that premium
  motion sites often rely on near-monochrome fields punctuated by motion rather than
  color variety — informs the density/restraint recommendation below.)

**Working palette direction for Mind Mosaic** (synthesized from the above, not
invented): a near-black/charcoal resting canvas (`#141414`–`#0C0B0B` family, echoing
both the brain-visualization cutaway and the Awwwards near-black) as the default
"explanation" mode background, with a **mood-mapped accent system** borrowed
directly from the Reliqio case study's logic — cool green/mint (`#84BD60`/`#EDF3F2`
family) for calm/insight beats, warm coral/gold (`#F0A98B`/`#DACF8D` family) for
"lightness/energy" beats, and coral-red (`#E2726C`) reserved for tension/anxiety/bias
topics — plus the observed saturated gold-yellow (`#EFD300`) as the single-word
caption emphasis color, matching what was actually seen in the reference Short.

## Typography Tokens

- Captions in the downloaded reference clip are set in a heavy, all-caps (or
  near-all-caps) grotesque/geometric sans, white fill, revealed word-by-word or in
  short 1-3 word phrases roughly every 1-2 seconds (directly observed: distinct
  caption text appeared in nearly every one of the 24 frames sampled at a 2.5s
  interval). A two-tier emphasis system is used: plain white for most words, the
  measured gold-yellow (`#EFD300`) for one emphasized keyword per caption beat.
  **Exact typeface/font family: not found** — Firecrawl scraping cannot recover
  font-file metadata from a rendered video frame, and no font-loader data was
  available since this is a video, not a scraped web page. Visually it resembles a
  heavy weight in the Montserrat/Poppins/Archivo Black family common to
  caption-generator tools, but this is a visual impression, not a verified claim.
- The "personality trait" infographic card (t=5.0s–14.8s) uses a bold sans headline
  ("Quiet Introspective Detail-oriented") in a warm yellow/gold on navy, stacked
  center-aligned, with small flat-style icons revealed one at a time beneath each
  trait word as the card progresses — a staggered-reveal pattern (see Spacing
  Tokens).
- The Awwwards "Motion.ed" reference did not expose specific font-family metadata in
  the fetched markdown (no explicit typography block was present) — **not found**
  for that reference either.

## Spacing Tokens

- Captions in the reference clip sit in the lower-middle third of the 9:16 frame,
  consistently positioned just above a decorative animated-microphone graphic that
  anchors the bottom of the frame in every talking-head shot — a fixed "caption
  safe zone" rather than captions moving frame to frame.
- The infographic card (t=5.0s–14.8s) reveals its icon row progressively: at t=10.0s
  one icon is visible under the trait list; by t=12.5s a second icon has been added
  alongside it. This is a **staggered/incremental reveal**, not all elements
  appearing at once — content density increases in discrete steps synced to speech.
- Full-frame b-roll cutaways (stock footage of people, library/office scene, brain
  visualization) are composed as single-subject, uncluttered frames with no caption
  text overlaid during those specific sampled frames — density drops to near-zero
  during pure b-roll beats, then returns when the host or caption reappears.
- The Awwwards "Motion.ed" reference is one of Awwwards' own "Minimal" / "Single
  page" categorized sites, reinforcing a low-clutter resting state as a broader
  motion-design norm, not just an artifact of this one Short.

## Motion/Pacing Notes

Cut points were detected with ffmpeg scene-change detection
(`select='gt(scene,0.35)',showinfo`) on the downloaded reference clip, not estimated
by eye.

**Reference clip — "The Hidden Cognitive Bias Even Smart People Suffer From"
(native 30fps, 60.73s total):**
- Raw scene-change timestamps (deduplicated, adjacent detections <0.5s apart merged
  as a single cut): 3.87s, 14.80s, 18.17s, 21.67s, 25.03s, 35.13s, 40.53s.
- 7 detected cuts → 8 shots.
- Shot durations: 3.87s, 10.93s, 3.37s, 3.50s, 3.36s, 10.10s, 5.40s, 20.20s.
- Average shot length: **7.59s** (≈228 native frames at 30fps; ≈455 frames if
  normalized to 60fps).
- Cut frequency: **≈6.9 cuts/minute** — noticeably slower than a hyper-edited
  meme-paced Short.
- Range: shortest shot ≈3.36s, longest ≈20.2s (final segment — a long,
  uninterrupted talking-head monologue closing the video; the scene-change
  detector found no hard cut here even though caption text continued to change
  underneath it, since caption overlays alone don't register as a full-frame scene
  change).
- Qualitative pattern (cross-checked against the contact sheet): talking-head
  opening (0–3.9s) → full-bleed infographic card with staggered icon reveal
  (3.9–14.8s) → brief talking-head bridge (14.8–18.2s) → stock b-roll of people in
  a field (18.2–21.7s) → single-subject office/library b-roll (21.7–25.0s) →
  extended talking-head explanation (25.0–35.1s) → animated brain/network data-viz
  (35.1–40.5s) → extended talking-head close (40.5–60.7s).
- A secondary, continuous (non-cut) motion source was also observed: a decorative
  animated gradient orb at the base of the on-screen microphone graphic
  continuously cycles hue (green, purple, orange, teal observed across different
  sampled frames) even during long uncut talking-head holds — ambient motion is
  used to keep static shots visually alive between hard cuts.

Only one reference clip yielded usable pacing data this session (see Open Gaps for
the second attempt's failure), so this single data point should be treated as
indicative, not a verified range, for future channel work.

## Motion-Personality Direction

Grounded in the above, not invented:

- **Layout variance — Medium.** The reference alternates among four distinct
  compositional templates (talking-head, full-bleed infographic card, single-subject
  stock b-roll, abstract data-visualization) across 8 shots in 60s, following clear
  content-beat logic (hook → concept card → supporting explanation → example →
  mechanism visualization → conclusion) rather than either a single static template
  or constant novel layouts. This matches a psychology-explainer format that needs
  to visually distinguish "here's a concept," "here's an example," and "here's the
  mechanism" from one another.
- **Motion intensity — Low-medium.** Cut cadence is moderate-to-slow (≈6.9
  cuts/minute, well below hyper-edited pacing), and caption entrances in the
  reference read as simple word-by-word appearance/cuts rather than bouncy
  overshoot — consistent with a calm, credible, non-clinical communicator tone
  rather than a hyperactive meme-style edit. The one clearly "designed" motion
  element observed — the continuously hue-cycling ambient orb — suggests intensity
  should live in slow, continuous ambient movement during holds rather than in
  aggressive cut frequency or spring/overshoot easing. (No dedicated Motion.dev
  easing-curve reference was scraped this session — see Open Gaps — so specific
  easing-curve recommendations beyond "avoid bounce/overshoot" are not independently
  verified.)
- **Visual density — Low.** One caption line with at most one emphasized keyword at
  a time; the infographic card reveals icons incrementally rather than all at once;
  pure b-roll beats drop to zero on-screen text. This is reinforced by the Awwwards
  "Motion.ed" reference's own minimal/single-page categorization and its 2-color
  palette — premium motion work in this general design space favors restraint over
  density, and the one psychology-specific reference clip actually analyzed follows
  the same low-density, one-beat-at-a-time principle.

## Open Gaps

- Second reference clip download (youtube.com/shorts/d2Pye-De5lQ) produced a
  corrupted/truncated 26KB file that ffmpeg could not decode; no second contact
  sheet or cross-check pacing data point was obtained. Only one clip's motion
  timing data is available.
- TikTok reference (@donnellycss, Halo Effect video) could not be downloaded —
  yt-dlp reached TikTok's extractor but the requested format was unavailable.
  Not analyzed.
- No Instagram Reels content was directly downloadable/analyzable within budget;
  the Instagram Reel surfaced by search (DCCtqCjiJXs) was cited from its search
  snippet only, not deep-fetched or downloaded.
- Exact typeface/font family for both the reference clip's captions and the
  Awwwards "Motion.ed" site: not found (video frames and the fetched markdown
  do not expose font metadata).
- The Reliqio Dribbble case study's text names "blue" as mapped to calm/gratitude/
  balance, but no blue hex value appeared among the 8 swatched palette colors on
  the scraped page — flagged rather than invented; if a blue token is needed, treat
  as unverified.
- No dedicated Motion.dev easing/spring documentation page or 12-principles-of-
  animation writeup was scraped this session (Firecrawl budget was prioritized
  toward psychology-specific references and Phase 2 requirements); the Awwwards
  Academy motion course and the Louis Paquet YouTube talk were surfaced by search
  but not deep-scraped. Easing-curve specifics in the Motion-Personality Direction
  above are therefore qualitative (from the one analyzed clip), not sourced from a
  dedicated animation-timing reference.
- Behance kinetic-typography results (behance.net/gallery/87781367,
  /176934835, /23664789) were found via Firecrawl search but not deep-scraped;
  color/type tokens from those specific pages are not verified.

Contact sheet referenced above is stored at:
`research/frames_tmp/mind-mosaic/contact_sheet_1.png` (gitignored working copy),
with a committed copy at `research/visual-reference/mind-mosaic/contact_sheet_1.png`.
