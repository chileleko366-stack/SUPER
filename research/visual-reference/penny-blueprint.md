# Penny Blueprint — Visual Reference Moodboard (Phase 1)

Channel: **Penny Blueprint** — budgeting, investing, taxes, debt reduction,
practical wealth-building. Tone target: practical, trustworthy, no-hype
personal finance (not aspirational fintech marketing, not shouty
get-rich-quick content).

All findings below trace to a URL actually fetched with Firecrawl (REST API,
raw JSON responses cached in `research/frames_tmp/penny-blueprint/fc/`... —
note: this session's Firecrawl responses were saved under the session
scratchpad and are not repo-tracked; every source URL actually hit is listed
below) or to a video actually downloaded with yt-dlp and processed with
ffmpeg/PIL (`research/frames_tmp/penny-blueprint/`). Firecrawl usage for
this channel: **12 calls** (5 `/v1/search`, 7 `/v1/scrape`), within the
~15-call budget.

## Source References

Motion-design galleries (Dribbble / Behance):
- https://dribbble.com/search/budget-app
- https://dribbble.com/tags/budget-app
- https://dribbble.com/search/budget-management
- https://dribbble.com/search/spending-dashboard
- https://dribbble.com/search/budget-progress
- https://dribbble.com/search/finance-motion
  (search-result listing pages, scraped for links)
- **https://dribbble.com/shots/26922283-FlowPay-Finance-in-Motion** —
  scraped in full (markdown + screenshot). "FlowPay — Finance in Motion" by
  Ali Asadi: futuristic fintech dashboard concept, glassmorphism balance
  card, dark hero layout. Real hex palette pulled directly from the shot's
  published color-tag list (see Color Tokens).
- **https://dribbble.com/shots/27033915-Smart-Budget-Management-Animation-Finance-Motion-Design**
  — scraped in full (markdown). "Smart Budget Management Animation |
  Finance Motion Design" by Pixelvi: minimal/smooth budget-flow animation
  concept. Real hex palette pulled directly from the shot's published
  color-tag list.
- Other real shot URLs surfaced in the listing scrape but **not**
  individually scraped (budget-conserving; listed for the operator's later
  reference, not examined further — see Open Gaps):
  https://dribbble.com/shots/26833979-Vaulta-credit-card-3d-animation ,
  https://dribbble.com/shots/26627197-Paygo-Logo-Animation ,
  https://dribbble.com/shots/26923113-Finance-Motion-Explainer
- https://www.behance.net/search/projects/fintech%20app%20design%20case%20study
  (search-result listing page, scraped for links)
- **https://www.behance.net/gallery/248327829/LedgerX-Personal-Finance-Management-App-Website**
  — scraped in full. "LedgerX – Personal Finance Management App & Website"
  by Orbillo (UI/UX & Branding Agency, Bangladesh), published April 27,
  2026. Concept dashboard for tracking income/expenses/financial health —
  directly on-niche for a personal-finance (not generic fintech) product.

Currently-circulating personal-finance Shorts/Reels (used both as a topic
signal for Phase 2 and a visual/motion signal for Phase 1):
- https://www.youtube.com/watch?v=-oMMjE_a7h8 — "Things didn't go as
  planned, my first personal spending | June 2026 Update" (Personal Finance
  with Leila – Debt Over It). Checked via yt-dlp metadata: 1338s, **not** a
  Shorts-format video — used only as a channel-discovery pointer, not
  downloaded.
- **https://www.youtube.com/watch?v=YtCRwOQZ3xg** — "5 Simple Budgeting
  Tips for Beginners #shorts" (The Abundance Academy), 49s vertical Short —
  **downloaded via yt-dlp, frames extracted, contact sheet built** (see
  below). Found via a direct `yt-dlp ytsearch` query (not Firecrawl), then
  duration-filtered for genuine sub-65s Shorts.
- https://www.youtube.com/watch?v=rDCJZr92gR4 — "5 smart budgeting tips for
  first time savers" (The Grind Corner), 65s Short, surfaced by the same
  yt-dlp search, not downloaded.
- https://www.youtube.com/watch?v=hm6vdF2hPbQ — "Budget vs Forecast
  Explained in 60 Seconds #Shorts" (AI Finance Hub), 42s Short, surfaced by
  the same search, not downloaded.
- https://suitsmecard.com/blog/5-financial-youtubers-that-will-help-you-manage-your-money
- https://due.com/best-youtube-channels-for-finance/
- https://makingmomentum.net/best-personal-finance-youtube-channels/

Choreography/easing reference (per brief instruction — no packaged
motion-design skill exists in this environment, so citing Motion.dev's own
public docs directly):
- https://motion.dev/docs/easing-functions — scraped in full. Documents
  Motion's built-in easing set (`easeIn`/`easeOut`/`easeInOut`,
  `backIn`/`backOut`/`backInOut`, `circIn`/`circOut`/`circInOut`,
  `anticipate`, `cubicBezier`, `steps`) and modifiers (`reverseEasing`,
  `mirrorEasing`) — used below as shared vocabulary for describing observed
  motion, not as evidence of what any specific reference actually used.
- https://motion.dev/docs/spring (search result only, not scraped —
  referenced from the search snippet for spring-based
  stiffness/damping/mass framing, not independently fetched in full this
  pass)

TTS/voice and music-sourcing citations are listed in the companion Phase 2
file, not repeated here.

## Video Reference → Contact Sheet

Downloaded: `youtube.com/watch?v=YtCRwOQZ3xg` ("5 Simple Budgeting Tips for
Beginners #shorts", The Abundance Academy).
- Source file: `research/frames_tmp/penny-blueprint/ref_clip1.mkv`
- Verified via ffprobe: 48.36s duration; container is a pillarboxed
  1280×720 canvas with the real vertical (9:16) content occupying
  roughly x=437–843 (406px wide) of that canvas — cropped accordingly
  before building the contact sheet.
- Frames extracted at 1fps with `ffmpeg -vf fps=1` →
  `research/frames_tmp/penny-blueprint/frames1/frame_001.png` …
  `frame_048.png` (48 frames)
- Contact sheet assembled with PIL (script:
  `research/frames_tmp/penny-blueprint/make_contact_sheet.py`) → an 8×6
  grid, gitignored working copy at
  `research/frames_tmp/penny-blueprint/contact_sheet_1.png`
- Committed copy (compressed JPEG, ~460KB, same contents) for reference
  from this doc: `research/visual-reference/penny-blueprint/contact_sheet_1.jpg`
- A second, finer-grained extraction (`fps=12` over the 10.6–12.2s window
  spanning the "Tip 1 → Tip 2" cut) was pulled specifically to inspect
  whether text overlays animate in with an eased transition — see Motion
  section below. Working copy:
  `research/frames_tmp/penny-blueprint/frames_fine/` and
  `research/frames_tmp/penny-blueprint/contact_sheet_2_finegrain.png`;
  committed copy:
  `research/visual-reference/penny-blueprint/contact_sheet_2_finegrain.jpg`

Only one video reference was downloaded and frame-analyzed this pass (two
other real, on-niche Shorts URLs were identified and are listed above but
not downloaded, to conserve time/budget) — this meets the brief's stated
minimum of "at least 1-2" but is a sample of one; see Open Gaps.

## Extracted Color Tokens

Two source families, kept separate because they represent different design
registers observed in the references (see Motion-Personality Direction for
how that split informs the recommendation):

**A. Aspirational fintech-concept register** (hex values taken directly
from the published color-tag lists on the two scraped Dribbble shots —
these are the designers' own stated palettes, not eyeballed):

| Token | Hex | Source |
|---|---|---|
| Near-black navy background | `#010103` | FlowPay shot |
| Slate-navy panel | `#273757` | FlowPay shot |
| Pale lavender-grey (secondary text) | `#D4D9E3` | FlowPay shot |
| Muted blue-grey | `#A2AEBB` | FlowPay shot |
| Vivid indigo accent (CTA/highlight) | `#393ED8` | FlowPay shot |
| Dusty blue | `#5D6D94` | FlowPay shot |
| Neutral grey | `#C4C4C4` | Smart Budget Management shot |
| Near-black navy (alt.) | `#030324` | Smart Budget Management shot |
| Amber/orange accent | `#D38317` | Smart Budget Management shot |
| Dark slate-purple | `#3A3754` | Smart Budget Management shot |
| Gold/amber (secondary) | `#BA8125` | Smart Budget Management shot |
| Warm brown | `#81665B` | Smart Budget Management shot |

**B. Real-world high-performing-Short register** (hex values sampled
directly with PIL from `frame_010.png` of the downloaded reference clip,
via `Image.crop(...).getcolors()` dominant-color extraction — not
eyeballed):

| Token | Hex | Source |
|---|---|---|
| Overlay title text | `#000000` | title-highlight-bar crop, dominant color |
| Title highlight-bar fill (translucent warm off-white over background) | `#D9D0C7` | title-highlight-bar crop, 2nd/4th-ranked colors, `(217,208,199)`/`(218,208,199)` |
| Caption bar background | `#FFFFFF` | caption-bar crop, dominant color (7600/8823 px) |
| Caption/narration text | `#000000` | caption-bar crop, 3rd-ranked color |
| Warm tan/khaki flat-lay desk surface | `#A58E78` | background-desk crop, dominant color, `(165,142,120)` |

Register A reads as cool, dark-mode, blue/indigo-accented "product" fintech.
Register B — the actual measured high-performing Short — reads as warm,
neutral, high-contrast black-on-white/tan, tangible (real desk, real cash,
real calculator) rather than screen-UI. This contrast is a real, grounded
finding, not a stylistic guess, and is the central input to the
motion-personality direction below.

## Typography Tokens

No font-identification tool is available in this environment, so family
names are not claimed — described structurally, split by register:

**Register A (FlowPay Dribbble shot, visual estimate from the fetched
screenshot** — proportions eyeballed against the 1690×1266px image, not
programmatically measured, flagged as approximate):
- Hero headline ("Your Money, Moving Smarter"): large bold grotesque/
  geometric sans, ~6% of image height per cap-line, with the closing word
  set in an italic, gradient-filled (blue→indigo) treatment for emphasis.
- Subhead: regular weight, ~2.5–3% of image height, reduced-opacity white.
- Card figure ("$22,720.40"): bold, tabular-figure numerals, ~4–4.5% of
  image height.
- Micro-labels ("Total balance," "In," "Out"): regular/medium weight,
  small, ~1.2–1.5% of image height, housed in rounded pill/chip shapes.

**Register B (downloaded Short, pixel-measured from `frame_010.png`'s
406×720 cropped content region):**
- Title/hook text ("Tip 1: Understand your income"): bold grotesque
  sans-serif, black fill, all two-line instances measured at ~11% of frame
  height total (≈5.5% per line), left-aligned, tight leading, sitting on a
  semi-opaque warm off-white highlight block sized tightly to the text (not
  full-bleed). A small color emoji is appended inline after each tip title
  (💰 📊 🎯 ✏️ 🔄) functioning as a per-section icon/bullet rather than a
  designed icon system.
- Caption/narration text ("Calculate your total monthly earnings after
  taxes."): medium-weight sans, black on a solid white rounded-rect bar,
  centered, max 2 lines, measured at ~5.6% of frame height for the bar
  (text itself smaller, sitting inside that bar with visible padding).
- Outro card: centered italic serif script logotype ("The Abundance
  Academy") on a pure-white background — the single serif/script
  typographic accent in an otherwise all-sans system, used only for the
  brand moment, not for informational text.

## Spacing Tokens

Register B, measured as percentages of the 406×720 cropped content region
in `frame_010.png` (resolution-independent, so portable to any export
resolution):
- Title block: left inset ≈23% of frame width, top offset ≈4% of frame
  height, block width ≈62% of frame width, block height ≈11% of frame
  height for two lines (≈5.5%/line).
- Caption bar: left/right inset ≈11–13% each side (bar width ≈76% of frame
  width), positioned ≈90% down from the top (bottom safe zone), bar height
  ≈5–8% of frame height depending on 1 vs. 2 caption lines.
- Both blocks avoid the outer ~10% edge margin on all sides — consistent
  with standard 9:16 Shorts/Reels safe-zone practice (platform UI chrome —
  like/comment/share rail, caption/username block — typically occupies the
  right edge and bottom ~12–15% on-platform).

Register A (FlowPay, visual estimate, not pixel-measured): generous
vertical rhythm between the hero text block and the balance card (roughly
one card-height of whitespace), consistent card internal padding that
reads as a generous, even inset on all sides, and clearly rounded corners
(soft, "friendly fintech" card language) rather than sharp rectangles.

## Motion/Pacing Notes

- Source clip: 48.36s, downloaded MP4/MKV, pillarboxed 1280×720 container
  around 406×720 real vertical content.
- Scene-cut detection via `ffmpeg -vf scdet=threshold=6` found **6 hard
  cuts** at t = 4.667s, 10.967s, 26.3s, 33.367s, 41.9s, 44.567s → **7
  shots** total. Shot durations: 4.67s, 6.30s, 15.33s, 7.07s, 8.53s, 2.67s,
  3.79s.
- Average shot length = 48.36s / 7 = **6.91s ≈ 414 frames at a 60fps
  reference rate.** One shot (the "Tip 2 / track your expenses" b-roll,
  15.33s) is a clear outlier; the **median** shot length is 6.3s ≈ **378
  frames at 60fps**, arguably the more representative "typical beat"
  number.
- **Fine-grain check (12fps sampling across the 10.6–12.2s window,
  spanning the t=10.967s cut):** the title-card text and the underlying
  b-roll swap **instantly** between two consecutive 1/12s samples (≤83ms) —
  no crossfade, no visible scale/opacity ramp, no motion blur on the text
  itself. In Motion.dev's vocabulary (cited above), this reads as a
  zero-duration hard cut on the text/graphic layer, not an eased
  entrance (no `easeOut`/`backOut`/spring-overshoot signature was
  observed on the actual measured clip). The only continuous motion
  present is a slow, roughly-linear handheld pan/zoom drift in the
  underlying stock b-roll footage — camera drift, not programmed easing.
- Net read: this reference's pacing is driven almost entirely by **cut
  frequency** (a new tip + new b-roll roughly every 6–7s on average, one
  outlier stretch to 15s) rather than by within-shot animation choreography.
  Text/graphics appear fully-formed on the cut; nothing animates in gradually.

## Motion-Personality Direction

Grounded in the measured Short (hard-cut pacing, static text overlays, slow
b-roll drift, warm/tangible color register) contrasted against the two
Dribbble "aspirational fintech" concepts and the LedgerX Behance case study
(cool/dark, glassmorphism, "smooth animations… calm interactions" per the
FlowPay project description — note that description is the designer's own
marketing copy, not something independently measured, since Firecrawl
returned a static screenshot, not the underlying animation file):

- **Layout variance: Medium-low.** The one real measured Short keeps a
  very consistent 2-zone template (top-left title+icon block, bottom
  caption bar) across all 7 shots — low structural variance shot-to-shot
  *within* a video. The Dribbble/Behance concepts show high variety
  *across different projects* (dashboard, hero, card, chart layouts) but
  that's a portfolio spanning many different products, not evidence for
  variance within a single piece of content. Recommendation: keep
  Penny Blueprint's title/caption scaffold highly consistent within an
  episode — viewers pattern-match fast finance-tip content quickly — while
  rotating 3–4 alternate b-roll/data-viz compositions (bar-chart callout,
  calculator/number card, checklist-build) across the library, echoing the
  range seen across the Dribbble shots without changing the core scaffold.
- **Motion intensity: Low.** The one reference actually measured on a
  frame-by-frame basis shows **zero** eased/spring text animation — hard
  cuts only, calm b-roll drift. Given the "practical, trustworthy, no-hype"
  tone target, and that the flashier, more aggressively-eased fintech
  concepts in Register A are static product-marketing stills (their motion
  claims are unverified copy, not measured behavior), recommend low motion
  intensity: fast (≤150–200ms) hard cuts or minimal fades between tip
  cards, no cartoonish bounce/overshoot on numbers or text. Reserve at most
  one moderate `easeOut`/`backOut`-style "pop" (Motion.dev vocabulary) for
  the single most important number in a video (e.g., a debt-payoff total
  or savings milestone) as one clear emphasis beat, not a constant motif.
- **Visual density: Low-to-medium.** The measured Short keeps each screen
  to one title-line pair + one caption-line pair + one b-roll subject —
  never more than ~3 text/graphic elements on screen simultaneously. The
  Register A dashboard concepts are denser (multiple cards/charts at once),
  but those are static product-marketing stills optimized for a portfolio
  page, not for 9:16 scroll consumption. Recommendation: cap concurrent
  on-screen text blocks at 2 (headline/tip + caption) plus one visual
  anchor (chart, calculator, cash, checklist), matching the measured
  reference and the "no-hype, practical" tone — avoid multi-card dashboard
  layouts crammed into a single Short frame.

## Open Gaps

- No Awwwards-style gallery was independently searched/scraped this pass —
  Dribbble (2 shots scraped in full) and Behance (1 case study scraped in
  full) were judged sufficient coverage of "motion design galleries" within
  the ~15-call budget; this is a real gap against the brief's example list,
  disclosed rather than papered over with an invented Awwwards citation.
- Exact on-screen easing-curve values (bezier coordinates, spring
  stiffness/damping) for the Dribbble/Behance concepts could not be
  measured — Firecrawl's scrape returned a static screenshot and
  descriptive text for FlowPay ("smooth animations," "calm interactions"),
  not the underlying video/Lottie file, so Register A's motion claims are
  the designer's own marketing description, not independently verified
  motion data. Only Register B (the downloaded Short) has directly-measured
  motion behavior in this doc.
- Only one video reference was downloaded and frame-analyzed (budget/time);
  two other real, on-niche sub-65s Shorts URLs were identified
  (`rDCJZr92gR4`, `hm6vdF2hPbQ`) but not downloaded, so the pacing/motion
  conclusions above rest on a sample of one measured video plus one static
  fintech-concept screenshot, not a larger corpus.
- The three additional real Dribbble shot URLs surfaced in the listing
  scrape (Vaulta, Paygo, Finance-Motion-Explainer) were not individually
  scraped for their own color/typography data — listed as available
  leads, not examined.
- Native fps of the downloaded Short beyond the ffprobe-confirmed duration
  was not independently pinned down; the "frames at 60fps" conversion above
  is derived from wall-clock cut timestamps (a resolution/fps-independent
  measurement), not from a directly observed 60fps source — this is stated
  explicitly rather than implying a native 60fps capture.
