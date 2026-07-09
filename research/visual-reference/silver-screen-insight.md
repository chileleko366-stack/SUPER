# Visual Reference Moodboard — Silver Screen Insight

Channel: film analysis / cinematic technique / cultural impact. Persona: cinephile,
articulate, visually literate critic. This document is Phase 1 of the per-channel
research protocol in `docs/RESEARCH_BRIEF.md`.

Firecrawl budget used for this channel: 15/15 calls (10 `/v1/search`, 3 `/v1/scrape`
successful, 1 `/v1/scrape` blocked/403 — see Open Gaps). yt-dlp and ffmpeg were used
in addition to Firecrawl, per the brief, and do not count against the Firecrawl budget.

## Source References

**Firecrawl — scraped (full page content fetched):**
- https://www.awwwards.com/sites/cinema-typography — "Cinema Typography," Awwwards
  Honorable Mention (Feb 9, 2026). An independent archive celebrating typography's
  role in cinema opening titles. Full markdown fetched; color palette and structural
  element list extracted (see tokens below).
- https://dribbble.com/search/film-ui — Dribbble "film ui" search results page. Full
  markdown fetched; 47 distinct shot links extracted (see selection below).
- https://github.com/rhasspy/piper — used for Phase 2 voice research, listed here
  for completeness since it was fetched in this channel's session.

**Firecrawl — attempted, blocked:**
- https://www.youtube.com/@filmalysis/videos — returned a JS-gated/403 shell page
  with no usable video listing via Firecrawl scrape. Abandoned in favor of yt-dlp
  (see below) for this channel's actual video data.

**Firecrawl — search results (titles/descriptions/URLs returned by Firecrawl
`/v1/search`, not deep-scraped):**
- https://dribbble.com/search/movie-video
- https://dribbble.com/search/video-assets
- https://dribbble.com/search/video-review-ui
- https://dribbble.com/search/film-video
- https://www.awwwards.com/websites/film-tv/?page=4
- https://www.awwwards.com/awwwards/collections/typography-in-web-design/
- https://www.awwwards.com/websites/animation/
- https://www.instagram.com/reel/DYbE8pIp4Xp/ — "Motion meets atmosphere" cinematic
  animated hero reel (search snippet only; not deep-fetched)
- https://www.behance.net/search/projects/kinetic%20typography
- https://www.behance.net/gallery/71745989/Kinetic-Typography-Case-Study-01
- https://www.behance.net/gallery/90601433/Kinetic-Typography-Case-Study-02
- https://motion.dev/docs/easing-functions — Motion.dev easing-function reference
  (approximating the "no packaged motion-design skill" gap per the brief)
- https://motion.dev/docs/spring — Motion.dev spring-animation reference
- https://www.reddit.com/r/criterion/comments/13efrq0/good_film_analysis_youtube_channel/
- https://www.youtube.com/c/indepthcine — In Depth Cine (cinematography breakdown
  channel; also used directly via yt-dlp below)
- https://blog.suitestudios.io/article/15-youtube-channels-decode-mysteries-movie-magic
- https://www.storybench.org/the-art-of-fear-how-the-youtube-channel-spikima-movies-made-film-analysis-its-own-cinematic-experience/
- https://www.youtube.com/@filmalysis — Filmalysis channel (search snippet; see
  yt-dlp section for its actual current video titles/URLs)
- https://www.youtube.com/channel/UCXcTkcC_H4XeDGfJ7rQGJaw — "Lucas Blue" channel
  (search snippet; used directly via yt-dlp below)

**yt-dlp — actually queried (flat-playlist listing of real, current video titles
and URLs, no Firecrawl cost):**
- https://www.youtube.com/@filmalysis/shorts
- https://www.youtube.com/channel/UCXcTkcC_H4XeDGfJ7rQGJaw/shorts (Lucas Blue)
- https://www.youtube.com/c/indepthcine/shorts (In Depth Cine)
- (attempted) https://www.youtube.com/@SpikimaMovies/shorts — returned no results
  under this handle; dropped, see Open Gaps.

**yt-dlp + ffmpeg — actually downloaded for contact sheets:**
- https://www.youtube.com/shorts/3Xdq562RjqM — In Depth Cine, "How To Light A
  Cinematic Night Interior #Shorts" (360x640, 24000/1001 fps, 59.28s)
- https://www.youtube.com/shorts/oXBFyHwdGgI — Lucas Blue, "The SYMBOLS of
  Midsommar" (360x640, 30fps, 25.05s)

## Extracted Color Tokens

From the Awwwards "Cinema Typography" reference (scraped color-palette block):
- `#0D0D0D` — near-black canvas/background
- `#E72A00` — red-orange accent (single accent color against the near-black field)

From programmatic dominant-color extraction (PIL median-cut quantization, 5 colors
per frame) on actual sampled frames of the two downloaded reference clips:

Clip 1 (In Depth Cine, tungsten-lit interior + diagram inserts):
- `#180E06`, `#321E0A`, `#593F17` — near-black to dark-umber shadow range
- `#CEA180`, `#956C3D` — warm tungsten skin/highlight tones
- `#F2F2A3`, `#F9F9BA` — pale acid-yellow caption/graphic block overlay color
  (used as a full-bleed highlight bar, not as text-on-transparent)

Clip 2 (Lucas Blue, Midsommar analysis, overcast daylight + stone-carving inserts):
- `#3B4C5C`, `#202A35` — cool desaturated blue-grey (shadow/interior cutaways)
- `#90857A`, `#BBA592`, `#A19886`, `#AFACB1` — bleached, low-saturation daylight
  neutrals (overcast Scandinavian daylight palette, consistent with the source
  film's cinematography)
- `#EAE0DB`, `#D3BDB0` — warm off-white (floral crowns, linen costumes)
- Bright arterial red appears on-screen (blood on carved stone) but was not
  captured as a top-5 dominant color at the sampled frames' scale — visually
  confirmed in the contact sheet, not numerically sampled; treat as an accent
  only, not a dominant token.

**Working palette for Silver Screen Insight** (synthesized from the above, not
invented): near-black canvas (`#0D0D0D`–`#120D08`) as the dominant field, one hot
accent in the red-orange family (`#E72A00`, echoing both the Awwwards reference and
the blood-red accent visually observed in Clip 2) used sparingly for emphasis/CTA
elements, warm tungsten amber (`#CEA180`/`#956C3D`) for "film still / quote" inserts,
and a desaturated cool neutral (`#3B4C5C`/`#90857A`) for analytical/diagram
interludes — mirroring how both reference clips code "footage" vs. "explanation"
moments with distinct temperature.

## Typography Tokens

- Awwwards "Cinema Typography" reference is explicitly typography-led (an archive
  of cinema title-card type), but the scraped page did not expose specific font
  family/weight metadata (no font-loader or "fonts used" block was present in the
  fetched markdown) — **specific typeface: not found**, flagged in Open Gaps.
- From the two contact sheets (directly observed, not inferred):
  - Clip 2 (Lucas Blue) uses two caption registers: (1) a heavy, all-caps or
    title-case **display burst** for hook/verdict lines ("IN THE MOVIE MIDSOMMAR",
    "NO SPOILERS", "EVERY RUNE") — bold geometric sans, white fill, dark
    edge/shadow for legibility over live footage, centered, 2-4 words per card;
    (2) a lighter-weight **annotation label** style for connective/pointer text
    ("For example", "Rebirth", "Dark Journey", "Journey", "Prosperity") set in
    mixed case, paired with a thin hand-drawn-style directional arrow graphic
    pointing at the referenced object in frame.
  - Clip 1 (In Depth Cine) uses a full-bleed flat-color caption bar (pale
    acid-yellow, see color tokens) rather than text-on-transparent; at the sampled
    resolution the caption glyphs inside the bar were not legible, so exact
    typeface/weight for that channel's captions is **not found** — only the
    color-block treatment is confirmed.
- Working direction: a single bold grotesque/geometric sans for hook lines (high
  legibility at small Shorts scale, thumb-stopping weight) plus a lighter-weight
  companion cut for annotation/connective text — directly modeled on the two-tier
  caption hierarchy observed in Clip 2, which is the faster-paced, higher
  information-density of the two references.

## Spacing Tokens

- Both references keep one caption idea on screen at a time — never more than one
  headline caption and one annotation arrow simultaneously (Clip 2) — reinforcing
  a "one beat, one message" rhythm rather than dense multi-label overlays.
- Clip 2's annotation arrows are placed with near-zero offset from their target
  object (arrow tail touches or nearly touches the subject being called out),
  i.e. spacing is used to *bind* label to referent, not to create general
  breathing room.
- Clip 1's full-bleed color caption bars occupy roughly the top third or bottom
  third of the 9:16 frame in the sampled frames, consistent with a lower/upper
  safe-third placement that avoids the center third where the subject sits.
- Awwwards Cinema Typography reference is a minimal, single-page, generous-negative-
  space layout (categorized by Awwwards itself under "Minimal," "Single page,"
  "Gallery," "Typography") — reinforces a low-clutter canvas as the resting state
  between caption beats.

## Motion/Pacing Notes

Cut points were detected with ffmpeg scene-change detection
(`select='gt(scene,0.35)'`) on both downloaded clips, not estimated by eye.

**Clip 1 — In Depth Cine, "How To Light A Cinematic Night Interior" (native
23.976fps, 59.28s total):**
- 10 detected cuts → 11 shots.
- Average shot length: 5.39s (≈129 frames at native 24fps; ≈323 frames if
  normalized to 60fps).
- Range: shortest shot ≈2.04s (≈49 native frames / ≈122 frames @60fps), longest
  ≈13.6s (≈326 native frames / ≈816 frames @60fps) — the longest shot is a single
  static instructional take (hand holding a light bulb to camera), not a cut-heavy
  moment.
- Cut frequency: ≈11.1 cuts/minute. Pacing style: technique-explainer with long
  static demonstration holds punctuated by diagram/graphic inserts.

**Clip 2 — Lucas Blue, "The SYMBOLS of Midsommar" (native 30fps, 25.05s total):**
- 12 detected cuts → 13 shots.
- Average shot length: 1.93s (≈58 native frames; ≈116 frames if normalized to
  60fps).
- Cut frequency: ≈31.1 cuts/minute — roughly 3x the cut rate of Clip 1.
- Pacing style: fast, caption-driven analysis; visual cuts and caption changes are
  tightly coupled to voiceover cadence, matching the two-tier caption system noted
  above.

These two references bracket a real observed range for the niche: ~11–31 cuts/min,
~58–129 native frames per shot (~116–323 frames @60fps-equivalent), with the faster
end associated with the more overtly "analysis/reveal" format (Clip 2) and the
slower end with instructional/demonstration format (Clip 1).

## Motion-Personality Direction

Grounded in the above, not invented:

- **Layout variance — Medium.** Compositions should alternate between full-bleed
  footage/quote inserts and centered caption-over-footage layouts (the pattern in
  both references), but should not swing into high-variance multi-panel or
  UI-heavy layouts. The Awwwards reference's minimal/single-page ethos and the
  restrained, dark, editorial Dribbble "dark portfolio" results argue for a
  composed, editorial rhythm befitting an "articulate critic" persona rather than
  meme-paced panel-hopping.
- **Motion intensity — Medium-high.** Cut cadence should trend toward Clip 2's
  faster ~2s/shot, ~31 cuts/min pace for retention, since that is the format
  explicitly built around analytical reveals (this channel's core content), while
  preserving occasional longer holds (4-6s) for cinematography quote/clip moments
  as in Clip 1. Caption/annotation entrances should snap in with a fast ease-out
  and low or no bounce/overshoot (per Motion.dev's easing-function and spring
  references) — precise and controlled, matching the tight arrow-to-object binding
  observed in Clip 2, not cartoonish or bubbly, to stay consistent with the critic
  tone.
- **Visual density — Low-medium.** At most one headline caption plus one
  annotation/diagram element on screen at a time (the "one beat, one message" rule
  observed in both clips); resting state between beats should return to a clean,
  near-black or full-bleed footage canvas, echoing the Awwwards reference's minimal
  negative-space canvas rather than a busy dashboard-style overlay stack.

## Open Gaps

- Exact typeface/font family for the Awwwards "Cinema Typography" reference was
  not exposed in the scraped markdown (no font-loader/"fonts used" data present)
  — not found.
- Clip 1's in-bar caption typography (color block confirmed, glyphs not legible at
  sampled resolution) — exact typeface/weight not found.
- Behance kinetic-typography case studies
  (behance.net/gallery/71745989, /90601433) were found via Firecrawl search but
  not deep-scraped (Firecrawl budget fully allocated to higher-priority
  scrapes) — color/type tokens from those pages not verified.
- The `@SpikimaMovies` yt-dlp shorts lookup returned no results (likely incorrect
  handle) and was dropped rather than guessed.
- Bright arterial-red accent visually present in Clip 2 (blood on stone) was not
  captured by the top-5 dominant-color extraction at the sampled frame scale;
  it is confirmed only by visual inspection of the contact sheet, not by numeric
  sampling.
- No Instagram Reels content was directly downloadable/analyzable within budget;
  the one Instagram Reel surfaced by search (DYbE8pIp4Xp) was cited from its
  search snippet only, not deep-fetched or downloaded.

Contact sheets referenced above are stored at:
`research/frames_tmp/silver-screen-insight/contact_sheet_1.png` and
`contact_sheet_2.png` (gitignored working copies), with committed copies at
`research/visual-reference/silver-screen-insight/contact_sheet_1.png` and
`contact_sheet_2.png`.
