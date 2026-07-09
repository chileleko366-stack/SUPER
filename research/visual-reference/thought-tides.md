# Thought Tides — Visual Reference Moodboard (Phase 1)

Channel: **Thought Tides** — philosophy, ethics, classic and modern schools of
thought. Tone: contemplative, calm, thought-provoking. Format: YouTube Shorts
(vertical 9:16).

All findings below trace to a URL actually fetched via Firecrawl (`/v1/search`
or `/v1/scrape`) on 2026-07-09, or to frames/data actually produced from a
downloaded reference clip via `yt-dlp` + `ffmpeg` + PIL. Nothing here is
invented.

## Source References

Motion design / typography galleries (Dribbble, Behance, Awwwards):

- https://dribbble.com/search/quote-animation — searched
- https://dribbble.com/search/motion-typography — scraped (shot listing)
  - https://dribbble.com/shots/26893688-Text-Reveal-Animation-Motion-Typography
  - https://dribbble.com/shots/26942691-Kinetic-Promo-Bold-Fashion-Typography
  - https://dribbble.com/shots/26662044-Digital-Typography-Animation
  - https://dribbble.com/shots/14188781-A-game-of-highs-and-lows (Neue Haas
    Grotesk kinetic type study)
  - https://dribbble.com/shots/22152842-ac-typo (kinetic typography, Neue
    Haas Grotesk)
- https://dribbble.com/search/minimal-text-animation — searched
- https://www.awwwards.com/websites/minimal/?ads=1&page=38 — searched
  (Best Minimal Websites index)
- https://www.awwwards.com/websites/black/ — searched (Best Black Websites
  index — dark-background editorial sites)
- https://www.awwwards.com/websites/Editorial%20New/ — searched (sites using
  Editorial New serif typography)
- https://www.behance.net/search/projects/black%20and%20white%20motion —
  scraped (project listing)
  - https://www.behance.net/gallery/246953053/Black-White-Short-Animations
  - https://www.behance.net/gallery/252095651/In-Passing
  - https://www.behance.net/gallery/244099737/Moir-patterns-Study
  - https://www.behance.net/gallery/251449051/Exploring-Photography-Through-Light-and-Motion
- https://www.behance.net/search/projects/minimalist%20motion%20graphic —
  searched

High-performing philosophy Shorts/Reels (niche reference):

- https://www.youtube.com/shorts/LFHYTObcbNc — "Stoicism: Become
  Undefeatable" — **downloaded via yt-dlp, used for contact sheet below**
- https://www.instagram.com/reel/DZIFhayjKht/ — Johnathan Bi, "Nietzsche:
  Stoicism is a Coping Mechanism" (established philosophy-explainer creator,
  IG Reels format)
- https://www.youtube.com/watch?v=vH1yx0Dlvbs — "My Method to Making Viral
  Stoic Shorts" (creator-side breakdown of the format's production pattern)
- https://www.youtube.com/watch?v=1zGgW7BS-QQ — "How To Create VIRAL Stoic
  Youtube Shorts" (production-pattern reference)

Motion/easing reference (choreography vocabulary, cited directly per the
brief since no packaged easing skill exists here):

- https://motion.dev/docs/easing-functions
- https://motion.dev/docs/spring

## Extracted Color Tokens

Colors below were **not** taken from Dribbble's generic UI color-filter
swatches (those are search-facet chips, not per-shot extracted data — using
them would not be a grounded observation). Instead they were extracted
programmatically with PIL (median-cut quantization, 6 colors/frame, bucketed
to the nearest 16) across all 27 evenly-sampled frames of the downloaded
reference clip (`research/frames_tmp/thought-tides/frames/frame_*.png`).
Ranked by pixel-weighted frequency:

| Hex | Role (observed) |
|---|---|
| `#000000` | Dominant background/shadow — near-full-frame black in text-card and silhouette shots |
| `#202020` | Near-black secondary — caption-pill background, shadow gradients |
| `#101010` | Near-black tertiary — vignette falloff |
| `#001020` / `#000010` | Cool near-black blue — night cityscape / ocean-at-dusk shots |
| `#907060` | Warm muted tan — skin tone / candlelit object close-ups |
| `#605030` | Warm muted olive-brown — golden-hour crowd and ruins shots |
| `#302020` / `#100000` | Warm near-black — shadow side of warm-lit shots |

Reading: this is a **teal/cyan-and-amber cinematic grade over a
near-black base** — shadows pushed cool (teal/blue), highlights pushed warm
(amber/tan), consistent with the color-graded stock footage seen across the
whole clip (ocean, ruins, night skyline, golden-hour crowds — see contact
sheet). It is not a flat minimal palette; it is a moody, high-contrast
grade. This matches the "Best Black Websites" dark-UI direction found on
Awwwards and the black-and-white/high-contrast Behance motion pieces cited
above, generalized to a warm/cool duotone rather than strict monochrome.

## Typography Tokens

Read directly off frames of the downloaded reference clip (not inferred):

- **Caption typeface**: bold, condensed, all-caps grotesk/impact-style sans
  (visually consistent with the "Neue Haas Grotesk" kinetic-type family
  called out by tag on Dribbble shots 14188781 and 22152842 above — exact
  font file not verifiable from video pixels alone, flagged in Open Gaps).
- **Weight**: heavy/bold only — no lighter secondary weight appears on
  screen at any sampled frame.
- **Case**: ALL CAPS throughout, no sentence case captions observed.
- **Color/contrast treatment**: solid white text (`#FFFFFF`-ish) on a
  semi-transparent dark rounded-rectangle pill (roughly `#000000` at ~70-80%
  opacity), giving legibility over any background without a full lower-third
  bar.
- **Line length**: short — 3 to 6 words per caption card (e.g. "SOCRATES AND
  OTHER GREAT", "TRULY MATTER TO YOU.", "OUT OF ZENO'S OR"), chunked to
  narration phrasing rather than full sentences or single words.
- **Scale**: single fixed caption size throughout the sample — no
  hierarchy/size variation observed within this clip (no separate
  title-card treatment distinct from body captions in this particular
  reference).

## Spacing Tokens

Observed from the same frames (all at 360×640 source / 9:16):

- Caption pill is horizontally centered, with roughly 8-10% of frame width
  as left/right padding inside the pill (tight, not full-bleed text).
- Caption vertical position sits at roughly 65-72% down the frame (lower-
  middle third) — clear of both the very bottom (native UI/engagement bar
  safe zone) and the top third (title-safe zone for thumbnails).
- Single caption card visible at a time — no stacked/multi-line caption
  blocks in this reference, reinforcing a low-density, one-idea-per-beat
  reading rhythm.
- Rounded-rectangle pill corner radius is small/subtle, not pill-shaped
  (roughly matches the caption text block height rather than a large stadium
  shape).

## Motion/Pacing Notes

Two independent passes were run against the downloaded reference clip
(`research/frames_tmp/thought-tides/ref_clip_1.mp4`, 360×640, 30fps,
duration 2:41):

1. **Regular-interval sampling** (`ffmpeg -vf fps=1/6`) → 27 frames,
   assembled into `research/visual-reference/thought-tides/contact_sheet_1.jpg`
   (source PNG kept in `research/frames_tmp/thought-tides/`, gitignored).
2. **Scene-change detection** (`ffmpeg -vf "select='gt(scene,0.35)'"`) → 31
   detected cut points across the 161-second clip.

From pass 2, computed directly (not estimated):

- **Average shot length**: ~5.2 seconds (≈156 frames at 30fps source ≈ 312
  frames at a 60fps-equivalent timeline).
- **Shot length range**: 0.4s (fast punch-in cut) to 20.1s (held
  establishing shot).
- **Cut frequency**: ~11.5 cuts/minute.
- Visual read from the contact sheet confirms this: broll shifts fully
  (coastline → ocean swell → smoke/cloud texture → silhouette at sunset →
  walking crowd → columns/ruins → night skyline → close-up hands) roughly
  every one-to-two caption cards, i.e. the edit changes the shot at a
  similar cadence to the caption-phrase changes, not independently of them.
- No fast-zoom or shake/glitch transitions were visible at any sampled
  frame; cuts read as straight hard cuts on stock broll, with the caption
  card holding continuity across some of the shorter cuts.

Motion.dev's public documentation (https://motion.dev/docs/easing-functions,
https://motion.dev/docs/spring) is cited here as the choreography-vocabulary
reference per the brief (no packaged easing/spring skill exists in this
environment): it defines the standard eased/spring vocabulary (`easeIn`,
`easeOut`, `circIn/Out`, `backIn/Out`, spring `stiffness`/`damping`) that
should be used when specifying caption-in/caption-out and broll-transition
timing for this channel, since none of that easing detail is visible from
static frame extraction — flagged in Open Gaps below.

## Motion-Personality Direction

Grounded in the observations above (contact sheet + scene-cut data + Awwwards
dark/editorial + Behance black-and-white motion references):

- **Layout variance: low.** The caption composition (centered pill, fixed
  lower-middle-third position, single line, one card at a time) never
  changes shot-to-shot in the reference clip. For Thought Tides this should
  stay low — a contemplative, calm tone benefits from a single predictable
  "reading anchor" the viewer can rest on, rather than restaged captions
  bouncing around the frame. Variance budget should go into the *broll*
  (which changes fully each cut), not the text layout.
- **Motion intensity: low-to-moderate.** The reference clip uses hard cuts
  on broll with no visible overshoot/bounce/glitch on the caption itself —
  consistent with a calm register. Recommend simple fade/short-ease
  caption-in and caption-out (per Motion.dev's `easeOut`/`easeInOut`
  vocabulary, no `backOut`/spring-overshoot) rather than punchy
  spring-overshoot typography moves that read as energetic/motivational
  (that register belongs to higher-arousal niches, not to a contemplative
  ethics/philosophy channel).
  ~5.2s average shot length / ~11.5 cuts-per-minute observed here is faster
  than a purely meditative pace but still well below the sub-1s hyper-cut
  pacing seen in high-arousal Shorts formats — this mid pace is
  recommended as the starting point: enough movement to hold attention,
  slow enough to let a line of philosophy land before the cut.
- **Visual density: low.** Single caption card, no on-screen chrome besides
  the caption pill, no icons/lower-third logo/graphic overlays observed in
  the reference. This matches the dark, uncluttered Awwwards "Best Black
  Websites" and Behance black-and-white-motion references pulled above.
  Recommend keeping Thought Tides to broll + one caption card + (optionally)
  a small persistent channel mark — no multi-element compositions, no
  simultaneous stat/quote/caption stacks.

## Open Gaps

- Exact caption font file/family could not be verified — it is visually
  consistent with a bold condensed grotesk (Neue Haas Grotesk-style, per
  Dribbble shot tags) but no font-identification tool was available; this
  should be verified against actual licensed fonts at implementation time,
  not assumed from this doc.
- Only one reference clip was successfully downloaded and analyzed
  (`youtube.com/shorts/LFHYTObcbNc`). The brief allows 1-2; a second
  clip (e.g. the Johnathan Bi Instagram Reel) was not downloaded because
  Instagram Reels are not reliably retrievable via yt-dlp without
  authenticated cookies in this environment, and pulling a second public
  YouTube Short would have spent Firecrawl/time budget better used on
  Phase 2 topic sourcing — flagged rather than skipped silently.
  Color/typography/spacing tokens above should be treated as directionally
  representative of the niche, not as a multi-source statistical average.
- Exact easing curve values (cubic-bezier numbers or spring
  stiffness/damping) used in the reference clip's caption transitions could
  not be measured from static PNG frames — Motion.dev's public vocabulary is
  cited as the naming/choreography reference, but specific curve values for
  Thought Tides should be chosen at implementation time, informed by the
  "low-to-moderate intensity" direction stated above.
- Dribbble/Behance color-filter swatches seen in the raw scrape output were
  intentionally excluded from the Extracted Color Tokens table since they
  are generic search-facet UI, not colors actually present in a specific
  reference shot — noting this so it's clear why the palette above is
  sourced entirely from the downloaded video, not from the gallery scrapes.
