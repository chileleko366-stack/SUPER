# Visual Reference Moodboard — Cosmic Window

Channel: astronomy, space missions, celestial objects, discoveries. Persona: an
awe-driven but precise science communicator — wonder-forward, not sensationalist.
Format: YouTube Shorts (vertical 9:16). This document is Phase 1 of the
per-channel research protocol in `docs/RESEARCH_BRIEF.md`.

Firecrawl budget used for this channel: 16/~15 calls (7 `/v1/search`, 9
`/v1/scrape`, all successful — no 403s or failures). One call over the
approximate budget was spent deliberately on the Motion.dev easing-doc lookup
the brief explicitly asks for (choreography vocabulary); everything else
stayed inside budget. `yt-dlp`, `ffmpeg`, and PIL were used in addition, per
the brief, and do not count against the Firecrawl budget.

## Source References

**Firecrawl `/v1/search` (query → what it returned):**
- "space astronomy motion graphics Dribbble shots" — returned Dribbble tag/
  search pages for astronomy, astronomy-app, astronomy-website, star-space,
  cosmic.
- "awwwards space exploration website design award" — returned
  awwwards.com/sites/the-space-that-makes-us-human, awwwards.com/sites/
  spaceforce-com, awwwards.com/sites/in-space-we-trust.
- "best astronomy space youtube shorts channel viral 2025 2026" — returned
  https://www.youtube.com/shorts/qF7pm_h7DpQ ("The Only Astronomy YouTube
  Channels Actually Worth Watching") plus several astronomy-YouTuber list
  articles (feedspot, Reddit r/askastronomy).
- "space news discoveries July 2026 NASA ESA" — used for Phase 2 topics (see
  that file) but also confirmed esawebb.org and esahubble.org as the live,
  currently-updating primary-source galleries for this niche.
- "dribbble shot space exploration kinetic typography motion design" —
  returned dribbble.com/tags/kinetic_typography, dribbble.com/search/
  animation-space, a Jordan Hughes kinetic-typography project page.
- "Piper TTS open source neural text to speech license CPU GitHub" — Phase 2,
  see that file.
- "motion.dev easing spring animation principles documentation" —
  https://motion.dev/docs/easing-functions, https://motion.dev/docs/spring.

**Firecrawl `/v1/scrape` (full page fetched):**
- https://www.awwwards.com/sites/the-space-that-makes-us-human — Awwwards
  Site of the Day (Karman Project interactive space platform). Full markdown
  + metadata fetched; color palette extracted (see tokens below).
- https://www.awwwards.com/sites/in-space-we-trust — Awwwards SOTD (space
  history art project). Full markdown fetched; color palette extracted.
- https://esawebb.org/news/archive/year/2026/ — ESA/Webb 2026 press-release
  archive. Full markdown fetched; 15 dated JWST releases with titles/URLs
  extracted, used for both moodboard tone-reading and Phase 2 topics.
- https://esahubble.org/news/ — ESA/Hubble press-release index. Full markdown
  fetched; 20 dated Hubble releases extracted (492 total in archive, first
  page fetched).
- https://dribbble.com/tags/astronomy?page=8 — Dribbble astronomy tag page.
  Full markdown fetched; 20 shot titles/links extracted (Solar System
  Simulation, Staring into Space / Data Visualization, Messier - Astronomy
  App Concept, React Telescope, etc.).
- https://dribbble.com/shots/10902978-Solar-System-Simulation — individual
  Dribbble shot (mobile "Online Space Encyclopedia" concept). Full markdown
  fetched; **per-shot extracted hex palette** (Dribbble's own color-tag data
  for this specific shot, not a generic search-facet swatch) captured.
- https://github.com/rhasspy/piper — Phase 2.
- https://github.com/OHF-Voice/piper1-gpl — Phase 2.
- https://huggingface.co/rhasspy/piper-voices — Phase 2 (page is JS-rendered;
  little usable markdown returned, flagged in Open Gaps there).

**Video reference downloaded and analyzed:**
- https://www.youtube.com/shorts/qF7pm_h7DpQ — "The Only Astronomy YouTube
  Channels Actually Worth Watching in ..." — downloaded via `yt-dlp`
  (format 18, 360×640, 25fps, 46.6s), frames extracted every 2s with
  `ffmpeg -vf fps=1/2` (23 frames), assembled into a contact sheet with PIL.
  Saved to `research/frames_tmp/cosmic-window/contact_sheet_1.png` (raw,
  gitignored) and committed at
  `research/visual-reference/cosmic-window/contact_sheet_1.jpg` (compressed,
  referenced by this doc). This is a compilation-style video that itself
  cuts between stock astronomy b-roll (radio telescope silhouette, rocket
  launch, starfields, nebula plates) with karaoke-style word captions — it
  functions here as a direct sample of current-format astronomy Shorts
  editing, not as a single narrative reference clip.

No second video reference was downloaded — see Open Gaps.

## Extracted Color Tokens

Two independent kinds of evidence, kept separate and then cross-checked:

**A. Per-site/per-shot palettes as published by Awwwards/Dribbble** (their own
extracted-color-tag data for that specific work, not generic UI swatches):

| Source | Hex swatches |
|---|---|
| Awwwards — "The Space that makes us Human" (Karman Project) | `#000000`, `#DF6C4F`, `#FFFFFF` |
| Awwwards — "In Space We Trust" | `#2779A7`, `#49C5B6`, `#DF6C4F` |
| Dribbble — "Solar System Simulation" | `#030203`, `#29344A`, `#5B2011`, `#BFBEBC`, `#5D5E5E`, `#993117`, `#B85434`, `#467E75` |

**B. Programmatic pixel sampling** (PIL, dominant/filtered-color extraction)
from the downloaded reference clip's frames — not eyeballed:

| Hex | Role (observed) |
|---|---|
| `#000B24` / `#010A1D` | Dominant near-black navy — night-sky/void background, radio-telescope shot |
| `#020202` / `#030303` | Pure black — deep-space starfield shot background |
| `#100415` / `#120518` | Near-black violet — nebula/end-card background |
| `#005181` / `#024D7C` | Teal-blue atmosphere gradient — rocket-launch sky |
| `#FFD700` | Bold gold/yellow — karaoke-style caption text (isolated by color-filtering all frame pixels for r>180,g>140,b<110; this is a caption-styling convention, not a "space" brand color — see reading below) |
| `#6B4A84` / `#453B89` | Violet/mauve nebula wisp (upper cloud layer) |
| `#7C5C4A` | Warm sand/amber nebula wisp (lower cloud layer) |

**Reading:** both evidence sources converge independently on the same
structure: a **near-black navy/void base** (every one of the three site/shot
palettes and every one of the five sampled video frames has a near-black or
near-black-navy dominant swatch) plus a **warm burnt-orange/rust accent**
(`#DF6C4F` appears in *two separate* Awwwards sites; Dribbble's palette has
`#993117`/`#B85434`/`#5B2011` in the same rust family) plus a **cooler
teal/cyan secondary accent** (`#49C5B6`, `#467E75`, `#005181`/`#024D7C` — all
independently in the same blue-green band) plus **white/light-grey text**
(`#FFFFFF`, `#BFBEBC`). The gold caption color (`#FFD700`) sampled from the
actual Short is a distinct, separate finding: it reads as a general
high-visibility Shorts/Reels caption convention (bold gold-on-dark-stroke)
rather than part of the "space" brand palette itself — recommend treating it
as a caption-chrome color, not mixing it into the background/accent palette.

Recommended token set for Cosmic Window, grounded in the above:
- Background/void: `#050914` (near-black navy, averaged from the sampled
  frame values)
- Primary accent (warm): `#DF6C4F` (directly attested twice)
- Secondary accent (cool): `#49C5B6`
- Tertiary accent (nebula depth): `#6B4A84` (violet), `#7C5C4A` (amber)
- Text/high-contrast: `#FFFFFF` / `#BFBEBC`

## Typography Tokens

Read directly off frames of the downloaded reference clip (weights/sizes as
seen, not inferred), cross-checked against the Dribbble kinetic-typography
search results:

- **Caption typeface**: bold, rounded-sans, all letters solid-filled with a
  visible dark stroke/outline separating text from busy backgrounds
  (necessary against starfields and nebula footage where a plain-color word
  would lose contrast). Visually consistent with the general "bold rounded
  grotesk + stroke" family seen across the Dribbble kinetic-typography tag
  results, though the exact font file is not verifiable from video pixels
  alone (flagged in Open Gaps).
- **Weight**: heavy/bold only — no lighter secondary weight appears on
  screen in the sampled frames.
- **Case**: Sentence case observed on individual caption words in this
  reference ("with", "isn't", "go for", "Engineering", "Spacetime",
  "cosmology.") — not forced all-caps, unlike some other Shorts formats.
- **Word-level pacing**: this reference uses **karaoke/word-by-word
  captioning** — one word (occasionally a short 2-3 word phrase) highlighted
  per ~2-second sample interval, changing on roughly every beat of narration.
- **Color/contrast treatment**: solid gold/yellow fill (`#FFD700`) with a
  dark navy/black stroke outline — no background pill or bar, the stroke
  alone carries legibility over the video.
- **Scale**: single fixed caption size throughout the sampled clip; no
  separate title-card treatment distinct from body captions was observed in
  this particular reference.

## Spacing Tokens

Observed from the same frames (360×640 source, 9:16):

- Caption words sit low-center, roughly 78-92% down the frame — clear of the
  very top (thumbnail/title-safe zone) and low enough to sit just above the
  native platform UI safe zone without touching it.
- Single word/phrase visible at a time — no stacked multi-line caption
  blocks in this reference, reinforcing a low-density, one-beat-at-a-time
  reading rhythm typical of narrated-fact Shorts.
- No lower-third bar, logo watermark, or persistent chrome observed in any
  sampled frame of this particular reference clip (its only persistent
  element is the single caption word).
- Full-bleed b-roll throughout — no letterboxing, no side padding/margins on
  the video itself; all "spacing" in this format is caption-position spacing
  against otherwise edge-to-edge footage.

## Motion/Pacing Notes

From the 23-frame, 2-second-interval contact sheet
(`research/visual-reference/cosmic-window/contact_sheet_1.jpg`, source clip
46.6s at 25fps):

- **Shot-hold pattern** (visually read off the contact sheet, not
  scene-detected): the radio-telescope shot holds for ~6s (t=0-4s across 3
  sampled frames plus surrounding), the rocket-launch shot holds for ~8s
  (t=12-18s, 4 sampled frames), starfield/galaxy-plate shots hold ~6-8s each,
  and nebula-plate shots hold ~6s each. This reads as **moderate-length
  holds on high-production stock b-roll**, not rapid hard-cutting — the edit
  lets a single striking image breathe under 2-4 caption words before
  switching.
- **Caption cadence**: a new caption word/phrase appears roughly every 2
  seconds (measured directly — this is the sampling interval and every
  sampled frame carries a different caption), independent of the underlying
  shot hold — i.e. one b-roll shot typically carries 2-4 caption beats before
  the visual cuts, meaning caption pacing is faster than shot pacing.
- Estimated **average shot length**: ~6-7 seconds ≈ 360-420 frames at a
  60fps-equivalent timeline (based on the visually-read hold pattern above;
  this is an estimate from an 11-sample contact sheet, not a frame-accurate
  scene-cut detector pass — flagged in Open Gaps).
- No zoom/shake/glitch transitions are visible at any sampled frame; shot
  changes read as straight hard cuts between distinct high-production stock
  clips.

Motion.dev's public documentation
(https://motion.dev/docs/easing-functions, https://motion.dev/docs/spring) is
cited here as the choreography-vocabulary reference per the brief (no
packaged easing/spring skill exists in this environment): its standard
eased/spring vocabulary (`easeOut`, `easeInOut`, spring
`stiffness`/`damping`) should be used when specifying caption-in/caption-out
timing for this channel. Exact curve values were not measurable from static
PNG frames (flagged in Open Gaps).

## Motion-Personality Direction

Grounded in the observations above (pixel-sampled contact sheet + shot-hold
reading + the three independently-sourced color palettes + Awwwards'
space-themed sites leaning toward immersive, slow-reveal WebGL/scroll
experiences rather than frenetic UI):

- **Layout variance: low.** Across every sampled frame the caption occupies
  the same low-center position with the same single-word/phrase treatment —
  it never restages. For Cosmic Window this should stay low: an
  awe-driven, precise science-communicator tone is served by a stable
  "reading anchor" the viewer can trust, while the *b-roll* (real
  telescope imagery, mission footage, simulated fly-throughs) carries all
  the visual variety. Do not bounce captions around the frame shot-to-shot;
  reserve movement for the imagery itself.
- **Motion intensity: low-to-moderate.** The reference shows moderate-length
  holds (~6-8s) on striking stock/real imagery with straight hard cuts and no
  visible overshoot, shake, or glitch transitions — consistent with letting
  genuinely awe-inspiring source imagery (real JWST/Hubble frames, real
  launch footage) do the emotional work rather than aggressive editing
  tricks. Recommend simple fade or short `easeOut`/`easeInOut` caption-in/out
  (per the Motion.dev vocabulary cited above), and avoid spring-overshoot
  "punchy" typography moves — those read as hype/energetic, which undercuts
  the "precise" half of this channel's tone. Caption *cadence* (~2s/word)
  can still be brisk even while caption *motion* stays restrained: the
  energy should come from pacing of information, not from bouncy easing.
- **Visual density: low.** Single caption word/phrase, no lower-third bar,
  no logo watermark, no simultaneous stat/label overlays observed in the
  reference, and the Awwwards space sites researched favor large, uncluttered
  full-bleed imagery with minimal UI chrome over dense dashboard-style
  layouts. Recommend keeping Cosmic Window to full-bleed real/simulated
  space imagery + one caption word/phrase at a time + (optionally) a small
  persistent channel mark — reserve any data-overlay elements (distance,
  scale, timestamp callouts) for moments where they add genuine precision
  rather than decorative clutter, since "precise" is part of this channel's
  stated tone.

## Open Gaps

- Exact caption font file/family could not be verified from video pixels —
  it reads as a bold rounded grotesk with stroke, consistent with the
  Dribbble kinetic-typography search results, but no font-identification
  tool was available in this environment; verify against actually-licensed
  fonts at implementation time.
- Only one reference clip was successfully downloaded and analyzed
  (`youtube.com/shorts/qF7pm_h7DpQ`). The brief allows 1-2; a second clip
  was not pulled because this session's remaining Firecrawl/time budget was
  prioritized for Phase 2 topic sourcing (which needed several scrapes of
  live press-release archives to get real, dated, cited topics). The color/
  typography/motion tokens above should be treated as directionally
  representative of current astronomy-Shorts editing conventions, not as a
  multi-clip statistical average.
- Shot-length/cut-frequency figures in Motion/Pacing Notes are read visually
  off an 11-distinct-shot, 23-frame (2s-interval) contact sheet, not computed
  from an `ffmpeg` scene-change-detection pass (`select='gt(scene,X)'` was
  not run in this session). Treat the ~6-7s average shot length as an
  estimate, not a frame-accurate measurement.
- Exact easing curve values (cubic-bezier numbers or spring
  stiffness/damping) used in any real reference could not be measured from
  static frames — the Motion.dev vocabulary is cited as the naming/
  choreography reference; specific values should be chosen at implementation
  time per the "low-to-moderate intensity" direction above.
- The Awwwards SpaceForce.com result (from the initial search) was not
  scraped for a color palette — two Awwwards space sites plus one Dribbble
  shot were judged sufficient corroboration for the converged palette
  direction and the remaining budget was redirected to Phase 2. If a third
  independent web palette is wanted, https://www.awwwards.com/sites/spaceforce-com
  is the next candidate (not yet fetched — do not treat any color claim
  attributed to it, since it was not scraped).
