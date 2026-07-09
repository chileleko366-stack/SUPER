# Mind Mosaic Pilot — Adaptation Note

The one reference clip analyzed for Mind Mosaic's Phase 1 moodboard
(`research/visual-reference/mind-mosaic.md`) is a **talking-head** video —
a host on camera, four shot templates: talking-head, full-bleed infographic
card, single-subject b-roll, abstract data-viz cutaway.

This build is **faceless** (no on-camera host, no video of a person — this
is a stated hard constraint of the whole project). The talking-head shot
type has no direct equivalent here, so it's explicitly substituted rather
than silently dropped:

| Reference shot type | Faceless substitute used in `shotGrammar` |
|---|---|
| Talking-head hook | `KineticCaption` — bold kinetic-type hook line, same caption-emphasis system observed in the reference (gold keyword highlight) |
| Full-bleed infographic card, staggered icon reveal | `InfoCard` — same staggered/incremental reveal pattern, adapted content (bias/concept keywords instead of personality traits) |
| Talking-head bridge | `KineticCaption` — continuation of kinetic captions rather than a face reappearing |
| Single-subject b-roll | `KenBurnsCard` — a slow pan/zoom still (procedurally generated, see pipeline Open Gap on real stock-photo sourcing) standing in for "single-subject, uncluttered" b-roll density |
| Extended talking-head explanation | `KineticCaption` |
| Animated brain/network data-viz | `InfoCard` (abstract variant) |
| Talking-head close | `KineticCaption` |

What **is** carried over faithfully because it's format-independent:
- Cut cadence (~6.9 cuts/min, ~7.59s avg shot — scaled to frames at 60fps)
- Two-tier caption emphasis (white default, `#EFD300` gold keyword)
- Low visual density (one caption line, staggered reveals, not all-at-once)
- Ambient continuous motion (hue-cycling orb) during any held shot, avoiding
  bounce/overshoot easing per the moodboard's motion-intensity finding

This is a judgment call, not a research finding — flagged here so it's
auditable rather than an invisible drift from the moodboard doc.
