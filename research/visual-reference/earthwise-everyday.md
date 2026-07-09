# Earthwise Everyday — Visual Reference Moodboard (Phase 1)

Channel: **Earthwise Everyday** — sustainability / eco habits / environmental concepts.
Tone target: grounded, optimistic, practical eco-living (not preachy, not doom-oriented,
not glossy-corporate-greenwash).

Research method: Firecrawl REST search/scrape (15 calls used, at budget), plus direct
(non-Firecrawl) downloads of public CDN images and one public YouTube Short via yt-dlp,
frame-extracted with ffmpeg and assembled into a contact sheet with PIL. All claims below
trace to a URL actually hit or a file actually produced in this session — see Open Gaps
for anything that could not be verified.

## Source References (URLs actually fetched)

**Firecrawl search calls:**
- `sustainability eco motion graphics animation Dribbble shots` → surfaced
  https://dribbble.com/search/eco-animation, https://dribbble.com/search/earth-day-animation,
  https://dribbble.com/search/eco-friendly, https://dribbble.com/search/sustainability-3d,
  https://dribbble.com/search/3d-sustainability
- `sustainability infographic motion design Behance case study` → surfaced
  https://www.behance.net/search/projects/motion%20study,
  https://www.behance.net/gallery/55651635/P3P510-A-Case-Study-in-Motion-Design
  (generic motion-design case study; no eco-specific Behance gallery surfaced — see Open Gaps)
- `eco tips sustainable living YouTube Shorts viral 2025 2026` and
  `site:youtube.com/shorts eco friendly tips sustainable living` → surfaced the Shorts URLs
  listed in the companion topics/voice/music doc, several of which double as visual references
  below.
- `Motion.dev easing spring animation documentation` → surfaced
  https://motion.dev/docs/easing-functions (scraped for choreography citation, see Motion/Pacing Notes)

**Firecrawl scrape calls:**
- https://dribbble.com/search/eco-animation — scraped for real shot listings (not just the
  generic color-filter widget, which is Dribbble UI chrome, not actual design data and was
  discarded). Real shots surfaced, each with a working shot URL:
  - https://dribbble.com/shots/26960030-Ecovise-Branding-Animation-Green-Tech-Brand-Identity
    ("Ecovise" — green-tech brand identity / branding animation)
  - https://dribbble.com/shots/26699868-EcoSun-Smart-Solar-Monitoring-App
    (solar-monitoring dashboard UI)
  - https://dribbble.com/shots/21897326-Crypto-eco-site-animation-desktop
    (eco-brand site animation, desktop)
  - https://dribbble.com/shots/7886741-Eco-Bebe (eco baby-products brand animation)
  - https://dribbble.com/shots/26639742-E-commerce-website-for-eco-brand-Homepage-Animation
- https://motion.dev/docs/easing-functions — scraped in full for named easing/spring
  reference (`easeIn`/`easeOut`/`easeInOut`, `backIn`/`backOut`, `anticipate`, `steps`,
  `cubicBezier`), used as the choreography vocabulary below in lieu of the unavailable
  LottieFiles/Motion.dev skill.

**Direct (non-Firecrawl) downloads, grounding the extracted tokens in real pixels/frames:**
- Three Dribbble CDN stills downloaded directly and analyzed with PIL
  (`research/frames_tmp/earthwise-everyday/stills/ecovise.webp`,
  `ecosun.webp`, `cryptoeco.webp`) — these are the actual preview images from the three
  shot URLs above (Ecovise, EcoSun, Crypto-eco).
- One YouTube Short downloaded via yt-dlp:
  **https://www.youtube.com/shorts/kvuzP1F4f1U** — "5 Easy Sustainable Swaps for a
  Low-Waste Routine" (360×640, 30fps, 46.78s, h264/aac). Frames extracted with ffmpeg at
  2fps (93 frames), a 24-frame subset assembled into a contact sheet with PIL.
  Saved to `research/frames_tmp/earthwise-everyday/contact_sheet_1.png` (gitignored temp
  dir per brief; commit only if the operator wants the PNG tracked).

## Extracted Color Tokens

Two distinct real palettes emerged — a **branded/graphic-design** cluster (Dribbble) and a
**real-world UGC** cluster (the downloaded Short). Both are grounded in PIL median-cut
quantization of actual downloaded pixels, not guessed.

**Branded eco/green-tech motion design (Dribbble shots, dominant swatches by pixel weight):**
- Ecovise (green-tech brand identity): `#00130d`, `#093027`, `#136f57`, `#49cfaa` —
  near-black forest green ground, deep teal-green mid-tone, mint/teal accent.
- EcoSun (solar dashboard UI): `#f0ede8`, `#2b2d32`, `#dfdbcf`, `#fcfcfa`, `#c2b7aa`,
  `#efbf4a` — warm off-white/taupe neutrals with a dark slate UI-chrome color and one
  amber/gold "sun energy" accent.
- Crypto-eco site animation: `#faf8f6`, `#e0f1da`, `#98c991` — warm near-white ground with
  a soft sage-green accent.

Pattern across all three: **deep forest/teal green + warm neutral (off-white or taupe)
base + one saturated accent** (mint-teal or amber-gold). None of the three references use
a bright/saturated "Kelly green" — the green is consistently desaturated toward
teal or near-black.

**Real-world UGC eco Short (contact sheet, dominant swatches by pixel weight):**
`#a6a6a0`, `#585147`, `#867568`, `#d6cfc4`, `#959087`, `#775948`, `#372720`, `#caa994` —
warm greige/taupe neutrals (marble countertop, skin tones, wood, kraft packaging). No
graphic brand-green appears at all in the highest-performing UGC reference — the palette
is entirely photographic/environmental, not designed.

**Implication for Earthwise Everyday:** use the branded-motion-design green/teal/amber
palette for on-screen graphic elements (title cards, lower-thirds, icon accents) but let
B-roll/live-action backgrounds stay in the warm-neutral UGC register rather than forcing
green into every frame — that's what the actually-high-performing reference does.

## Typography Tokens

Grounded only in what is visually legible in the contact sheet and shot stills; no font
was identified via a font-detection tool, so names below are descriptive, not literal
typeface IDs (flagged in Open Gaps).

- **Caption/title-card text (contact sheet, frame 1-2):** heavy-weight, condensed-neutral
  grotesque sans-serif, set in white with a dark outline/drop-shadow for legibility over
  variable backgrounds — the standard high-contrast Shorts-caption treatment. The numeral
  "5" is rendered at roughly 2x the scale of the accompanying words as a visual anchor,
  positioned upper-left/upper-third, clear of the bottom safe zone.
- **UI headline text (EcoSun dashboard still):** clean, ungrooved grotesque sans at
  medium/bold weight for headings, lighter weight for body/labels — standard SaaS-dashboard
  type hierarchy (2-3 weights, no display/serif mixed in).
- No serif or script typefaces appeared in any of the five references.

## Spacing Tokens

- **Branded web/UI shots (EcoSun, Crypto-eco):** generous whitespace, card-based grouping,
  rounded-corner containers, comfortable padding around numerals/icons — consistent with
  a calm, uncluttered "eco-clean" design convention rather than dense dashboards.
- **UGC Short (contact sheet):** full-bleed 9:16 vertical framing, single subject
  (hand + product) centered per shot, no on-screen UI chrome beyond the caption text,
  caption kept inside the top ~20% of frame — leaving the bottom safe zone (where
  platform UI overlays sit) clear.

## Motion/Pacing Notes

Measured directly from the downloaded Short (not estimated): 46.78s total runtime, native
30fps, vertical 360×640. Sampling the extracted frames (2fps → 93 frames, visualized as a
24-cell contact sheet at every-4th-frame) shows:
- A ~4s title-card open ("5 Sustainable Swaps I Have Made") before the first product beat.
- Each of the 5 "swap" segments runs roughly **6-10 seconds** (≈180-300 frames at 30fps),
  itself containing 2-3 internal hard cuts to different angles of the same product
  (roughly one cut every 2-3s / 60-90 frames within a segment).
- All transitions observed are **hard cuts** — no wipes, no zoom-punch transitions, no
  visible speed-ramping. This is a talking-hands/product-demo pacing, not a fast-cut
  meme-style edit.

The Dribbble references are static stills, so no cut-frequency or easing-curve data could
be measured from them directly (flagged in Open Gaps) — for choreography vocabulary this
moodboard instead cites Motion.dev's documented easing set
(https://motion.dev/docs/easing-functions): named eases (`easeIn`/`easeOut`/`easeInOut`),
`backIn`/`backOut` (overshoot), `circIn`/`circOut`, `anticipate`, and `steps` (discrete/
snap motion) — plus `cubicBezier` for custom curves. Given the calm, uncluttered register
observed in every actual reference in this niche, `easeOut`/`easeInOut` and gentle
duration-based springs are the appropriate default; `backOut`/`anticipate` overshoot
should be reserved for rare emphasis beats, not general use.

## Motion-Personality Direction

Three-dial direction, grounded in the above (not invented from nothing):

- **Layout variance: low-to-moderate.** Every reference — the three branded Dribbble
  shots and the UGC Short alike — reuses one consistent compositional template
  (centered card / centered hand-and-product) rather than varying framing shot-to-shot.
  Earthwise Everyday should lock a consistent caption position and product/subject
  framing across a video's shots, varying only angle/zoom slightly, rather than
  reinventing layout each cut. Consistency reads as trustworthy/grounded, which matches
  the target tone.
- **Motion intensity: low.** The one measured video reference uses hard cuts exclusively,
  no overshoot, no speed ramps. The branded stills (by genre convention, not
  frame-measured — flagged as inferred) favor smooth confident reveals, not punchy
  bounce. Default to `easeOut`/`easeInOut`, reserve `backOut`/`anticipate` overshoot for
  rare single-beat emphasis (e.g. a number counting up), never for routine cuts.
- **Visual density: low-to-moderate.** Every reference favors one focal subject and
  generous negative space over multi-element clutter (EcoSun's dashboard whitespace,
  Crypto-eco's soft neutral ground, the UGC short's single-product framing). Keep on-screen
  text to one short caption line (+ optional numeral/icon), avoid stacking multiple
  graphic elements in one frame.

## Open Gaps

- **Awwwards** was not independently searched/verified — the brief's "Dribbble/Behance/
  Awwwards-style" was covered via Dribbble (verified, real shots) and a generic Behance
  motion-design case study (verified, but not eco-specific — no eco-specific Behance
  project surfaced in the one search call spent on Behance). If a dedicated Awwwards eco
  reference is required, it was **not found** in this session's budget.
- Only **one** video reference was downloaded and contact-sheeted (the brief allows "1-2").
  A second Instagram Reel or TikTok reference was surfaced by search
  (e.g. https://www.instagram.com/reel/DS2p6TZgA6J/ , https://www.tiktok.com/@livingplanetfriendly/video/7581559275894377783)
  but not downloaded — Instagram/TikTok are typically harder for yt-dlp to pull without
  auth/cookies, and the remaining Firecrawl/time budget was prioritized toward the
  voice-licensing investigation in the companion doc (see that doc — it surfaced a real
  licensing gotcha worth the trade-off). Treat "second contact sheet" as **not done**,
  not skipped-and-hidden.
- No font-identification tool was used, so typeface names above are descriptive
  observations, not verified typeface IDs.
- Cut-frequency/easing data for the branded Dribbble references could not be measured
  (they are static preview stills, not video) — the Motion/Pacing Notes section is
  explicit about which claims are measured vs. inferred from genre convention.
