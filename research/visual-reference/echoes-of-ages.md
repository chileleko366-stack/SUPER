# Echoes of Ages — Visual Reference Moodboard (Phase 1)

Channel: **Echoes of Ages** — historical events, civilizations, turning points,
timelines/maps. Tone: epic, documentary-narrator gravitas.

All findings below trace to a URL actually fetched with Firecrawl, a page
actually fetched with WebFetch, or a clip actually downloaded with yt-dlp and
processed with ffmpeg/PIL on this machine. Nothing here is invented.

## Source References

**Firecrawl `/v1/search` calls (results actually returned):**
- Query "historical map animation motion design dribbble behance" →
  https://www.behance.net/search/projects/map%20animation?locale=en_US ,
  https://dribbble.com/search/location-history ,
  https://dribbble.com/search/motion-map ,
  https://www.behance.net/search/projects/animated%20map?locale=en_US ,
  https://dribbble.com/search/map-motion ,
  https://dribbble.com/search/map-history
- Query "ancient civilization timeline infographic motion graphics awwwards
  showcase" →
  https://www.awwwards.com/inspiration/history-timeline-cosimo-digital ,
  https://www.awwwards.com/inspiration/history-timeline-alvic-1 ,
  https://www.awwwards.com/inspiration/our-history-timeline-hutstuf ,
  https://www.awwwards.com/inspiration/homepage-carvico ,
  https://www.awwwards.com/inspiration/histography-timeline-of-history
- Query "history facts youtube shorts channel viral million views" →
  https://www.youtube.com/@WeirdHistory ,
  https://youtube.fandom.com/wiki/Most-viewed_YouTube_shorts ,
  https://www.instagram.com/reel/DXfUX5lSpHg/?hl=en (candidate examples
  surfaced; not all used as final references — see below)

**Firecrawl `/v1/scrape` calls (full markdown fetched):**
- https://www.awwwards.com/inspiration/histography-timeline-of-history —
  Awwwards showcase entry for [histography.io](http://histography.io), an
  interactive data-viz timeline of history (linked as external resource,
  itself not scraped — see Open Gaps).
- https://www.behance.net/search/projects/animated%20map?locale=en_US —
  returned real, currently-listed Behance projects: "ANIMATED ILLUSTRATED MAP
  OF KYIV" (Serhii Tereshchenko), "MAP — Lodes", "EXPO 2025 | Osaka",
  "Political Map" (Shuja Rehman), "BATTLEFIELD 2042 | MAPS + INTERFACE" —
  useful as confirmation of current motion-graphics-map conventions (colour-
  coded territory fills, camera push-ins on cartography) even though none are
  history-documentary-specific.

**WebFetch (outside Firecrawl budget, used for supplementary grounding):**
- https://motion.dev/docs/easing-functions — Motion's public easing
  reference: named presets `easeIn`/`easeOut`/`easeInOut`, `backIn`/
  `backOut`/`backInOut`, `circIn`/`circOut`/`circInOut`, `anticipate`,
  `linear`, `steps`, plus `cubicBezier` for custom curves. No default
  duration values are published on that page.

**WebSearch (outside Firecrawl budget, used to locate a downloadable
reference channel):**
- Query "best history YouTube Shorts channel epic maps timelines
  civilizations 2026" surfaced **Epic History TV**
  (https://www.youtube.com/@EpichistoryTv/shorts) as a channel combining
  animated-map storytelling with an epic/documentary tone.

**Downloaded video reference (yt-dlp + ffmpeg + PIL):**
- Channel: Epic History TV — confirmed via yt-dlp metadata at 3,120,000
  subscribers (`channel_follower_count`), a genuinely high-performing channel
  in this niche.
- Video: "Rise of the Ottoman Empire: From Nothing to Superpower"
  https://www.youtube.com/watch?v=0XBMx9RNBGk (this specific upload had
  51,695 views at fetch time; channel-level reach is what qualifies it as
  "high-performing" — see Open Gaps for the caveat on this specific video's
  own view count).
- Downloaded with `python -m yt_dlp -f "best[height<=1080]"` → source format
  18, 360×640, 94.04s, ~25fps. Saved to
  `research/frames_tmp/echoes-of-ages/ref_epichistory_ottoman.mp4`
  (gitignored, not committed).
- Frames extracted with `ffmpeg -vf "fps=0.5"` (one frame every 2s, 47
  frames total) into `research/frames_tmp/echoes-of-ages/frames1/`, plus a
  finer `fps=4` pass over a 10s window (`frames_fine/`) to measure caption
  cadence precisely.
- Contact sheet assembled with PIL (`build_contact_sheet.py` /
  `build_contact_sheet2.py` in the same folder):
  - Full 47-frame sheet: `research/frames_tmp/echoes-of-ages/contact_sheet_1.png`
    (2.8MB, gitignored, kept locally only).
  - Committed, size-reduced 24-frame sheet (4s spacing, 780×988px, ~837KB):
    **`research/visual-reference/echoes-of-ages-contact-sheet-1.png`** — this
    is the citable contact sheet for this moodboard.

## Extracted Color Tokens

All hex values below were sampled directly with PIL from pixels in the
downloaded/decoded frames (not estimated from thumbnails).

| Token | Hex | Sampled from |
|---|---|---|
| `--brand-red` | `#D13832` (also read `#D43837` on a second sample) | "EPIC HISTORY" logo lockup fill, pinned top-of-frame throughout |
| `--brand-lettering-cream` | `#D0BBA3` | Cream/off-white lettering inside the red logo box (not pure white — warmed to match the parchment palette) |
| `--parchment-bg` | `#C3B2AA` (range `#DFCBBB`–`#E0CCBC` in lighter/vignette areas) | Base map paper color |
| `--map-water` | `#1A3240` | Ocean/sea fill on the animated map |
| `--territory-fill` | `#8B8B70` (olive-sage; broader sampled range `#84A860`–`#909C60` across frames as the map re-colors per era) | Empire/territory highlight overlaid on the parchment map as it expands |
| `--year-badge-bg` | `#0C1A25` (near-black navy) | Small rounded-pill date badge, top-right of the map (e.g. "1289", "1330") |
| `--caption-white` | `#FFFFFF` | Default (non-emphasized) caption word fill |
| `--caption-outline` | `~#141414` (near-black, slight blue tint from blur bleed) | Stroke/drop-shadow around every caption glyph |
| `--emphasis-yellow` | `#FDFC00` | Karaoke-style keyword highlight, e.g. "ILKHANATE", "ANATOLIA" |
| `--emphasis-green` | `#00FF20` | Alternate karaoke-style keyword highlight, e.g. "EMERGE", "EMPIRE" |

Palette read: warm, desaturated parchment/map neutrals (cream, tan, ink-navy,
olive) for the "documentary" base layer, punched through by one saturated
brand red (logo) and two neon caption-highlight colors (yellow/green) that
exist purely to drive Shorts-native readability/retention — those two neons
are clearly a caption-tool convention layered on top of an otherwise muted,
archival color story, not part of the "epic" palette itself.

## Typography Tokens

Observed directly in the contact sheet and zoomed crops (no font-matching
tool available, so these are visual descriptions, not confirmed family
names):

- **Logo lockup ("EPIC HISTORY")**: heavy, condensed, all-caps grotesque/
  display sans (visually close to families like Anton/Oswald ExtraBold —
  not confirmed), red fill box, cream lettering, fixed top-safe-zone
  position for the entire 94s clip.
- **Caption/subtitle track**: heavy condensed sans, all-caps, white fill with
  thick black stroke + soft drop shadow (the common "auto-caption burn-in"
  style seen across most caption tools) — visually similar to the default
  bold caption style used by CapCut/Opus-Clip-style auto-captioners, not a
  bespoke typeface. Two to three words per on-screen caption card. Keyword
  emphasis is conveyed by fill-color swap (yellow or green), not by
  weight/size change.
- **Map/chapter labels** ("GOLDEN HORDE", "ISLAMISATION OF BALKANS"): a
  narrower, semi-transparent cream serif/slab label overlaid directly on the
  map surface, styled like vintage cartography lettering — lower contrast
  and lower prominence than the caption track, meant to be read as "map
  ink" rather than as UI text.
- **Year badge numerals**: small serif/slab numerals in cream, centered
  inside the dark rounded-pill badge.
- No typographic scale (multiple weight/size steps for headings vs. body)
  was observed — this format uses exactly two text roles (logo lockup,
  caption track) plus incidental map-ink labels, consistent with a
  single-continuous-shot Short rather than a multi-scene explainer.

## Spacing Tokens

Derived from pixel measurement against the 360×640 source frame (all
proportions, since the committed reference was downloaded at 360p — see Open
Gaps):

- Logo lockup: pinned to the top ~14% of frame height, consistent inset
  margin on all sides, never repositioned across the 94s clip.
- Caption zone: consistently centered horizontally, vertically anchored in
  the lower-middle third (roughly 69–87% of frame height), i.e. clear of
  both the very-bottom UI-safe zone and the map content above it.
  Caption line height ≈ font-cap-height × 1.3 (single line only; no
  multi-line captions observed in the sample).
  Same vertical anchor is held for the entire clip — this is a fixed
  caption-safe-zone, not a per-shot recomposition.
- Year badge: top-right of the map area, small consistent margin from map's
  own frame edge, roughly 8% of frame width in badge width.
- Overall composition keeps a large open negative-space field (the map
  itself) with only two UI layers on top (logo + caption) at any time —
  read together with Visual Density below.

## Motion/Pacing Notes

- **Shot structure**: the reference clip is a **single continuous shot** for
  its full 94s duration — there is no hard scene-to-scene cutting. The
  camera performs a slow, continuous Ken-Burns-style pan/zoom across a
  static map asset; the map's territory-fill color animates in as the
  narrative timeline advances (new date badge + new territory fill roughly
  every 8–20s, e.g. 1289 → 1300 → 1330 → 1450 → 1453). One full-bleed
  interlude (a circular ornamental crest/emblem, ~t=26–46s) is the only
  genuine compositional break in the entire clip.
- **Caption cadence (measured directly, not estimated)**: a finer `fps=4`
  ffmpeg sample across a 10s window (t=14s–24s) showed caption text changing
  roughly **every 0.5–0.75s** (2–3 word groups per card), i.e. roughly
  30–45 frames at a 60fps-equivalent timeline. This is the dominant "cut
  frequency" viewers actually perceive in the format — it lives entirely in
  the text layer, not in shot changes.
- **Keyword emphasis rhythm**: within each caption card, exactly one word is
  usually color-punched (yellow or green, alternating with no fixed pattern
  observed), landing on the narratively "loaded" word (a proper noun or a
  strong verb: "EMERGE", "ILKHANATE", "MUSLIM EMPIRE").
- **Easing**: could not be measured directly from pixel data (no visible
  overshoot/bounce artifacts in the sampled frames — the map pan/zoom reads
  as smooth ease-in-out or linear, consistent with Motion.dev's documented
  `easeInOut`/`linear` presets rather than the more aggressive `backIn`/
  `anticipate` presets in that same reference doc).

## Motion-Personality Direction

Grounded in the observations above, the three dials for **Echoes of Ages**:

- **Layout variance: LOW.** The reference holds one composition (map fills
  frame, logo pinned top, caption pinned lower-third) for the entire runtime.
  Compositional change is gradual (continuous pan/zoom + map re-coloring),
  not shot-to-shot recomposition. Only rare full-bleed interludes (crest,
  chapter card) break the frame — these should be used sparingly, as
  punctuation for a new era/chapter, not as a per-beat device.
- **Motion intensity: LOW-TO-MODERATE, and asymmetric.** The visual bed
  (map, camera) moves with restrained, unhurried eases — no bounce, no
  overshoot — which is what reads as "gravitas" rather than "hype." All of
  the format's kinetic energy is deliberately concentrated in the caption
  layer, which hard-cuts every 0.5–0.75s with a snap-in (no fade) on each
  new word group. This split (calm visuals, punchy text) is the specific
  mechanism that lets a documentary-narrator tone stay watchable at Shorts
  attention spans — Echoes of Ages should copy this split rather than making
  the map/camera itself aggressive.
- **Visual density: LOW.** At any instant there are at most two active UI
  elements (logo lockup + one caption card) plus incidental map-ink labels.
  Negative space (open map/parchment) dominates the frame. Density should
  spike only briefly, at chapter-card or crest moments, then return to the
  restrained baseline.

Overall: Echoes of Ages should read as **one continuous, slow-moving,
archival "camera"** (map pans, territory fills, muted parchment/ink/navy
palette, one brand-red accent) **carrying a fast, punchy, high-contrast
caption layer** (white/black/yellow/green, 2–3 word cards, sub-second
cadence) — restraint in the visual bed, energy in the text, which is what
separates "epic documentary" from either a static slideshow or a hyperactive
meme-cut format.

## Open Gaps

- **histography.io itself was not scraped** — the Awwwards entry linking to
  it was scraped, but the live interactive timeline site
  (http://histography.io/) was not fetched directly (would have required an
  additional Firecrawl call against a JS-heavy site of uncertain scrape
  value). Its inclusion here is as a *named prior-art reference for
  "timeline as data visualization"*, not as a source of verified color/type
  tokens.
- **Only one reference clip was downloaded and contact-sheeted** (the brief
  allows 1-2). A second clip from a different channel (e.g. to check whether
  the "continuous single shot + punchy captions" pattern holds across
  creators, or whether some Echoes-of-ages-adjacent channels use harder
  scene cuts) was not pulled, to conserve time/budget. Treat the Motion/
  Pacing findings as representative of one strong exemplar (Epic History TV,
  3.12M subs), not as a cross-channel statistical average.
- **The specific downloaded video (51,695 views)** is not itself a top-
  performing individual Short — the channel's overall subscriber base
  (3.12M) is what establishes "high-performing in this niche," not this
  particular upload's view count. A view-count-verified individual viral
  Short was not separately identified within budget.
- **Exact font family names are not confirmed** — typography tokens above
  are visual descriptions (weight, case, condensation, stroke treatment),
  not verified family/foundry names, since no font-identification tool was
  available.
- **Dribbble/Behance results returned were search-listing pages, not deep
  individual-shot scrapes** (one Behance listing was scraped in full; the
  five Dribbble search URLs were only search-result URLs from the `/search`
  endpoint, not scraped project pages) — sufficient to confirm current
  motion-map conventions exist and are active, insufficient to extract
  further color/type tokens from that gallery side without spending
  additional Firecrawl budget.
