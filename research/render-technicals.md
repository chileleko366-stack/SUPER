# Render Technicals — 60fps / 1080x1920 on GitHub Actions

Shared across all 10 channels. Sourced from Remotion's own docs via Firecrawl
(scraped 2026-07-09) plus a search pass on real-world GitHub Actions render
reports.

## Sources
- https://www.remotion.dev/docs/renderer/render-media (renderMedia API, codec/audio options)
- https://www.remotion.dev/docs/config (remotion.config.ts)
- https://www.remotion.dev/docs/quality (CRF, resolution/pixel-density, JPEG quality, color space)
- https://www.remotion.dev/docs/encoding (codec/CRF ranges)
- https://www.remotion.dev/docs/cli/render (CLI flags: --concurrency, --video-bitrate, --color-space)
- https://github.com/remotion-dev/remotion/issues/4300 (CPU-core utilization/concurrency caveats)
- https://github.com/remotion-dev/remotion/issues/4783 ("Remotion is too slow" thread — real production teams moved off Lambda to custom containers/render hosts for cost/predictability reasons)
- https://github.com/yuvraj108c/Remotion-Matrix-Renderer (existing OSS example of a GitHub Actions matrix workflow rendering Remotion compositions — confirms the matrix-per-composition pattern is a known, working approach, not novel to this project)

## Composition config

```ts
export const FPS = 60;
export const WIDTH = 1080;
export const HEIGHT = 1920;
```

- fps=60 must be set on the `<Composition>` (or `Config.Rendering` in
  `remotion.config.ts` for CLI defaults) — Remotion does not upsample; every
  `interpolate()`/`spring()` call in primitives must be written against 60fps
  frame counts (e.g. a 12-frame in-cut is 0.2s, not 0.4s as it would be at 30fps).
- 1080x1920 is native device resolution for Shorts/Reels/TikTok — no upscale
  needed. Per the Quality Guide, text sharpness on high-density viewer
  displays is a separate concern from encode resolution; since Shorts are
  viewed full-bleed on phone screens (which are already >1080px logical
  width at 2-3x density), consider `--scale=1.5` output scaling if text-heavy
  primitives look soft on review, at a proportional render-time/file-size cost.

## Encoding settings

| Setting | Recommendation | Why |
|---|---|---|
| Codec | `h264` | Universal compatibility, YouTube/TikTok/IG all transcode h264 uploads cleanly; no reason to use vp8/prores for a delivery-only pipeline. |
| CRF | 18–23 | Remotion's CRF docs: lower = higher quality/larger file. 18 is visually lossless for h264, 23 is default libx264 quality. For fast-cut, high-motion-graphics content (hard cuts, no crossfades per spec), use nearer 18–20 since motion+text is where h264 macroblocking is most visible. |
| Pixel format | `yuv420p` | Default, universally compatible with platform players. |
| Color space | `bt709` | Explicitly pass `--color-space=bt709` per Remotion's own quality guide — it becomes default in Remotion 5.0 but isn't yet; without it, colors can look washed out/shifted on some players. |
| Image format (frame capture) | `jpeg`, quality 80 (default) | `png` is "slower" per docs; with hard cuts and duotone/flat color fields (per Phase 3 visual spec) JPEG artifacting is low-risk. Bump to `--jpeg-quality=90` if a channel's moodboard shows banding on flat gradient duotone backgrounds. |
| Audio codec | default for chosen video codec (Remotion picks automatically per renderMedia docs) | No need to override unless we need uncompressed intermediate; final delivery doesn't need `pcm-16`. |

## Concurrency / render time on GitHub Actions runners

- **Correction from the Mind Mosaic pilot run (job 86182420980,
  2026-07-09)**: ffmpeg is **not** preinstalled on `ubuntu-latest` runners,
  contrary to this doc's original assumption -- a real workflow run failed
  at `ffmpeg -version` with "command not found." Every workflow must run
  `sudo apt-get update && sudo apt-get install -y ffmpeg` as an explicit
  step before any ffmpeg-dependent pipeline code runs.
- Standard GitHub-hosted `ubuntu-latest` runners: 2 vCPU, 7GB RAM, no GPU.
  Remotion rendering is CPU-bound (headless Chrome frame capture + ffmpeg
  encode); GPU is not required for h264 encode at this resolution.
- `--concurrency` controls parallel browser tabs rendering frames
  simultaneously. On a 2-vCPU runner, concurrency above 2 gives diminishing/
  negative returns (per issue #4300, Remotion doesn't always saturate cores
  cleanly) — set concurrency to `2` (or leave default, which auto-detects
  CPU count) rather than hand-tuning higher.
- **Rough time budget**: a 60fps, ~45-60s Short (2700-3600 frames) with
  moderate-complexity 2D motion graphics (text, shape, chart primitives —
  not 3D/WebGL-heavy) typically renders on a 2-vCPU CI runner in the
  5-12 minute range, well inside GitHub Actions' default 6-hour job timeout
  and comfortably inside free-tier per-job minutes for a twice-daily
  10-channel matrix. Actual number must be confirmed with a real timed
  render in the Verification phase — this is a planning estimate, not a
  measured fact, and should be corrected once the first real render lands.
- File size: h264 CRF 18-20 at 1080x1920/60fps for a 45-60s clip lands
  roughly in the 15-40MB range depending on motion complexity (higher cut
  frequency and duotone flat-color content compress well vs. photographic
  content). Comfortably under all platform upload limits.

## Open gap
No actual timed render of a real composition has been performed yet — the
time/file-size figures above are estimates from Remotion's documented
behavior and general h264 encoding characteristics, not a measurement. The
Verification agent must render one real test clip per channel and record
actual wall-clock time and file size before these numbers are treated as
confirmed.
