# Code Trail — Visual Reference Moodboard (Phase 1)

Channel: **Code Trail** — programming, algorithms, project builds. Tone:
crisp, technical, dev-to-dev. Format: YouTube Shorts (vertical 9:16).

All findings below trace to a URL actually fetched via Firecrawl (`/v1/search`
or `/v1/scrape`) on 2026-07-09, or to frames/data actually produced from a
downloaded reference clip via `yt-dlp` + `ffmpeg` + PIL. Nothing here is
invented.

## Source References

Motion design / code-editor / dashboard UI galleries (Dribbble, Behance,
Awwwards):

- https://dribbble.com/search/edit-animation — searched
- https://dribbble.com/tags/code-editor — searched, then **scraped**
  (233 shots listed); representative shots pulled from the scrape:
  - https://dribbble.com/shots/26647433-moora-Collaborative-coding-platform
  - https://dribbble.com/shots/26699238-moora-team-collaboration-for-developers
- https://dribbble.com/search/web-code-editor — searched
- https://dribbble.com/search/animation-editor — searched
- https://dribbble.com/search/code-editor-illustration — searched
- https://dribbble.com/search/sorting-algorithm — searched
- https://www.toptal.com/developers/sorting-algorithms — surfaced via search
  (classic sorting-algorithm animation reference site, not scraped for
  markdown — visual style noted from the search snippet only)
- https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html —
  surfaced via search (academic sorting-visualization reference, noted, not
  scraped)
- https://www.awwwards.com/websites/developer/ — searched (Awwwards
  "Developer" site-of-the-day category index)
- https://www.awwwards.com/websites/portfolio/ — searched
- https://github.com/topics/awwwards?l=javascript&o=desc&s=forks — searched
  (GSAP/Awwwards-style dev-portfolio build repos, adjacent signal)
- https://www.behance.net/search/projects/dark%20mode%20design%20ui%20dashboard — searched
- https://www.behance.net/search/projects/ui%20motion%20study — searched
- https://www.behance.net/search/projects/dashboard%20ui%20ux%20case%20study — searched
- https://www.behance.net/search/projects/real-time%20dashboard%20ux%20ui%20animation — searched
- https://www.behance.net/search/projects/motion%20graphics%20intro%20case%20study — searched

High-performing programming Shorts/Reels (niche reference):

- https://www.instagram.com/reel/DWeyTGOFEq4/?hl=en — **thebrainmaze**,
  "Visualizing Sorting Algorithms" (posted March 29 2026, 185 likes at time
  of search) — **downloaded via yt-dlp, used for the contact sheet below**.
- https://www.youtube.com/watch?v=kPRA0W1kECg — "15 Sorting Algorithms in 6
  Minutes" (classic algorithm-visualization/"audibilization" reference,
  surfaced via search; not downloaded — budget was spent on the Instagram
  reel instead, see Open Gaps).
- https://www.youtube.com/c/Fireship — searched; the dominant high-performing
  channel format in this niche ("100 Seconds of Code" and news-explainer
  Shorts).
- https://www.youtube.com/watch?v=cYoY_WbqNSw — "Fireship in 100 Seconds" —
  **download attempted via yt-dlp, failed** (YouTube bot-check block in this
  environment: "Sign in to confirm you're not a bot"). Logged in Open Gaps
  rather than skipped silently.
- https://read.engineerscodex.com/p/how-fireship-became-youtubes-favorite —
  **scraped**. Secondary-source article characterizing Fireship's editing
  style directly (quoted in Motion/Pacing Notes below) since the primary
  clip could not be downloaded.
- https://www.youtube.com/watch?v=7IWIQJKdCGU — "How I Make My Successful
  Coding Shorts On YouTube" (creator-side breakdown of the format).
- https://www.youtube.com/playlist?list=PL43pGnjiVwgTW6FwMbDCWMRLkH_Vm5tSn —
  "Programming shorts" playlist, surfaced via search (topic/format sampling,
  not analyzed frame-by-frame).

Motion/easing reference (choreography vocabulary, cited directly per the
brief since no packaged easing skill exists here):

- https://motion.dev/docs/easing-functions — searched, then **scraped**
  (full function list: `cubicBezier`, `easeIn`/`easeOut`/`easeInOut`,
  `backIn`/`backOut`/`backInOut`, `circIn`/`circOut`/`circInOut`,
  `anticipate`, `linear`, `steps`).
- https://motion.dev/docs/spring — searched (spring-physics API, not scraped
  for markdown — function signature noted from the search snippet only).

## Extracted Color Tokens

Colors below were sampled with PIL (`Image.getpixel`) directly from frames
of the downloaded reference clip
(`research/frames_tmp/code-trail/frames1/frame_*.png`, 30 frames, one every
4 seconds across the 121-second clip), not from Dribbble/Behance generic
UI color-filter chips (those are search-facet swatches, not observed colors
from a specific shot).

| Hex | Role (observed) |
|---|---|
| `#090909` – `#121212` | Base background — near-black, full-bleed behind both the header table and the chart |
| `#16170b` – `#1e1f17` | Panel/table background — slightly warmer near-black with a faint olive-green cast, brushed-metal texture visible under compression |
| `#ffffff` | Grid divider rules — pure white, ~2px hairlines bounding the header table rows |
| `#940d00` | Saturated red — low end of the hue-mapped data sweep (early frames, "Insertion Sort") |
| `#5e5106` / `#445f09` | Olive/yellow-green — mid-low hue band |
| `#757e1c` | Yellow-green — mid hue band (later in the same run) |
| `#35935b` | Teal-green — mid-high hue band (transition toward "Cocktail Sort") |
| `#20009e` | Saturated violet-blue — high hue band (late frames, "Merge Sort"/"Counting Sort") |
| `#120062` | Deep indigo — final-frame center value, darkest point of the hue sweep |

Reading: this is a **near-black dashboard base with a single saturated,
continuously hue-rotating accent** (red → olive → green → teal → blue →
violet, i.e., a value-to-hue rainbow ramp typical of algorithm/data
visualizations) plus **pure-white UI chrome** (grid lines, labels) for
structure. There is no secondary/tertiary brand color — all color budget
goes into the data itself, and the UI chrome stays strictly
black-and-white. This matches the "dark mode dashboard" and "real-time
dashboard animation" Behance search categories cited above, and is
consistent with the terminal/dark-IDE convention long associated with
programming content.

## Typography Tokens

Read directly off frames of the downloaded reference clip:

- **Label typeface**: clean UI sans-serif / grotesk (humanist, not
  geometric — visible curve terminals on lowercase letters), medium
  weight for both the algorithm-name label ("Insertion Sort") and the
  numeric readout ("Iterations: 2393"). Exact font family not
  identifiable from video pixels alone — flagged in Open Gaps.
- **Case**: mixed/Title Case for algorithm names ("Insertion Sort",
  "Cocktail Sort"), sentence case for the metric label ("Iterations:") —
  **not** all-caps, distinct from the caption-card convention seen in
  other niches' Shorts.
- **Weight**: single medium weight throughout the sampled frames; no
  bold/light hierarchy contrast observed within the header band itself.
- **Color/contrast**: white/off-white text directly on the near-black
  brushed-panel background, no pill or card behind the text — contrast is
  carried by luminance alone, not by a background chip.
- **Scale**: small relative to frame — the entire header band (logo +
  2-row table) occupies roughly the top 15-17% of the 640px-tall frame,
  leaving the large majority of vertical space to the visualization itself.
  This is a **data-dense, not caption-dense** typographic hierarchy —
  the opposite emphasis from a quote/caption-card niche.
- **Wordmark**: a small bold sans-serif monogram ("TBM") plus an icon
  mark inside a white square, pinned top-left — a persistent, low-key
  channel-brand element rather than a large logo treatment.

## Spacing Tokens

Observed from the same frames (720×1280 source, 9:16):

- Header band (logo + 2-row data table) is pinned to the top of frame,
  bounded top and bottom by pure-white 2px horizontal rules, occupying
  roughly the top 15-17% of frame height.
- Table columns are added incrementally left-to-right as each new
  algorithm's run starts — empty/reserved cells are visible for
  algorithms not yet run, so the grid's column count grows over the
  video's runtime rather than being fixed from frame one.
- The large data visualization (a full-bleed radial/pie chart) fills
  essentially all remaining vertical space below the header band, and
  is close to full frame width — very little unused margin around the
  focal visual once the header is accounted for.
- Small consistent margin (~3% of frame width) between the logo mark and
  the top-left frame edge; no other UI chrome (no bottom-third caption,
  no side icons) appears anywhere in the sampled frames.
- Single-viewport, single-layer-below-the-header layout throughout — no
  stacked cards, no scroll, no secondary overlay competing with the main
  visualization.

## Motion/Pacing Notes

Analysis is based on the downloaded reference clip
(`research/frames_tmp/code-trail/ref1_sorting_ig.mp4`, 720×1280, 30fps,
duration 121.02s), sampled at a regular interval
(`ffmpeg -vf fps=1/4,scale=360:-1`) into 30 frames, assembled into
`research/visual-reference/code-trail/contact_sheet_1.jpg` (source PNG kept
in `research/frames_tmp/code-trail/`, gitignored).

Directly observed from the contact sheet and full-resolution frame
inspection:

- **Zero hard cuts** across the entire 121-second clip — it is a single
  continuous, uninterrupted real-time simulation/take. As a literal
  "shot length" measurement: 1 shot, ~121s (≈3,631 frames at 30fps
  source, ≈7,261 frames at a 60fps-equivalent timeline), 0 cuts/minute.
- In place of cuts, the clip's rhythm is carried by two continuous
  micro-motion sources: (1) **smooth per-frame color interpolation** of
  the hue-mapped data sweep (never a discrete jump), and (2) **live
  incrementing counters** ("Iterations: N") that update every frame —
  a "live metrics ticking" motif that reads as motion even without any
  cut or camera move.
- **Macro-beat cadence**: new algorithm columns are added to the header
  table at roughly t≈20s ("Bubble Sort"), t≈68s ("Cocktail Sort"),
  t≈96s ("Merge Sort"), and t≈112s ("Counting Sort") — i.e., a new
  "chapter" beat roughly every 25-30 seconds, marked by a UI-state change
  (new column appears) rather than an edit cut.
- **Contrast case (not frame-measured — cited from a secondary source)**:
  Fireship, the dominant high-performing channel in this niche, is
  independently described as running "fast-paced, snappy" editing with
  frequent meme/reaction-image cutaways
  (https://read.engineerscodex.com/p/how-fireship-became-youtubes-favorite:
  "fast-paced, humorous, meme-filled videos"; "Keep videos fast-paced. It
  boosts retention and keeps viewers watching."). An actual Fireship clip
  (https://www.youtube.com/watch?v=cYoY_WbqNSw) could not be downloaded in
  this environment (yt-dlp hit a YouTube bot-check wall), so its exact cut
  frequency/avg shot length could **not** be measured directly — this
  characterization is qualitative only, sourced from the article, not from
  frame data. Flagged in Open Gaps.
- Motion.dev's public documentation
  (https://motion.dev/docs/easing-functions, https://motion.dev/docs/spring)
  is cited as the choreography-vocabulary reference per the brief (no
  packaged easing/spring skill exists in this environment): it defines the
  standard eased/spring vocabulary (`easeIn`/`easeOut`/`easeInOut`,
  `backIn`/`backOut`/`backInOut`, `circIn`/`circOut`, `steps`, spring
  `stiffness`/`damping`) that should be used when specifying transition
  timing for Code Trail, since no specific curve values are visible from
  static frame extraction.

## Motion-Personality Direction

Grounded in the observations above (measured continuous-shot data-viz
reference + Behance dashboard-UI search categories + the Fireship
secondary-source contrast case):

- **Layout variance: low-to-moderate.** The reference clip's own
  compositional chrome (fixed header band position, fixed
  full-bleed-visualization body) never restages itself even as its
  *content* changes dramatically — this is a stable "dashboard" frame
  that lets highly dynamic content read clearly. For Code Trail, keep a
  consistent safe-zone layout *within* a single video (code/diagram
  region, small persistent metric/label region) so technical content
  stays legible, but allow moderate variance *across* videos/topics
  (terminal-style dashboard vs. diagram/architecture-style vs.
  graph/algorithm-style) so a high-volume automated channel doesn't feel
  visually monotonous. Do not restage the core layout mid-video the way a
  meme-cutaway format does — that would fight legibility of code/diagrams.
- **Motion intensity: moderate.** The measured reference sits at one
  extreme (zero cuts, purely continuous/hypnotic motion) and the
  documented Fireship format sits at the other (frequent cuts, meme
  cutaways, explicitly optimized for retention via pace). A crisp,
  technical, dev-to-dev tone should land in between: enough cut/beat
  frequency to hold Shorts-native attention (aim for a new visual beat
  roughly every 2-4 seconds — faster than the ~25-30s macro-beat cadence
  measured in the reference, much slower than a hyper-cut meme edit), but
  simple eased transitions (`easeOut`/`easeInOut` per Motion.dev's
  vocabulary) rather than bouncy `backOut`/spring-overshoot moves, which
  would read as playful/lifestyle rather than technical. Reserve any
  overshoot/punch easing for a single hook moment at the very start of
  each video, not throughout.
- **Visual density: moderate-to-high.** The reference keeps a data table,
  live counters, and a large animated visualization on screen
  simultaneously at all times, organized into exactly two clear zones
  (fixed header band vs. large visualization body) — dense but not
  cluttered, and never more than two simultaneous layers. This suits a
  technical/dev-to-dev audience that can process more on-screen
  information than a lifestyle niche. Recommend one persistent
  "dashboard chrome" element (e.g., a running metric, file name, or
  step counter, echoing the iteration counter observed here) plus one
  large focal visualization (code diff, algorithm animation, terminal
  output, architecture diagram) — a firm two-layer density ceiling, not
  three-plus simultaneous stat/quote/caption stacks.

## Open Gaps

- Exact typeface family for the header/label UI could not be verified —
  it reads as a clean humanist/grotesk UI sans, but no font-identification
  tool was available; verify against a specific licensed font
  (e.g., Inter, IBM Plex Sans, JetBrains Mono for any code-body text) at
  implementation time rather than assuming from this doc.
- A second reference clip could not be obtained: the Fireship "100
  Seconds" video (https://www.youtube.com/watch?v=cYoY_WbqNSw) failed to
  download via yt-dlp in this environment (`ERROR: [youtube] ...: Sign in
  to confirm you're not a bot`). Its fast-cut/meme-cutaway style is
  therefore documented qualitatively from a secondary source
  (engineerscodex article) only, not measured from frames — cut
  frequency, average shot length, and any easing/overshoot values for
  that format remain unverified. The classic "15 Sorting Algorithms in 6
  Minutes" video (youtube.com/watch?v=kPRA0W1kECg) was also not
  downloaded — Firecrawl/time budget was prioritized toward Phase 2 topic
  sourcing once one working contact sheet was secured, per the brief's
  "at least 1-2" minimum being satisfied by the Instagram reel.
- Only one reference clip was successfully downloaded and frame-analyzed
  (the thebrainmaze Instagram Reel). Color/typography/spacing tokens above
  should be treated as directionally representative of the
  "algorithm/data-visualization" sub-style within programming content, not
  as a statistical average across the whole niche (which also includes
  code-editor-screen-recording style and meme/commentary style, per the
  Fireship contrast case above).
- Exact easing curve values (cubic-bezier numbers or spring
  stiffness/damping) used by either reference could not be measured from
  static PNG frames — Motion.dev's public vocabulary is cited as the
  naming/choreography reference; specific curve values for Code Trail
  should be chosen at implementation time, informed by the "moderate
  intensity" direction stated above.
- Dribbble/Behance color-filter swatches seen in raw search/scrape output
  were intentionally excluded from the Extracted Color Tokens table since
  they are generic search-facet UI, not colors actually present in a
  specific reference shot — the palette above is sourced entirely from the
  downloaded video's frames.
