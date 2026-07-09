# Shared Research Brief — Read Before Starting Any Channel Research

This governs every per-channel research agent. Do not skip steps or invent
citations. Every claim in your output must trace to a URL you actually
fetched with Firecrawl or yt-dlp/ffmpeg output you actually produced.

## Tooling available to you

- **Firecrawl** (REST API, not an installed MCP tool — call it with curl).
  Key is in `C:\Users\CC\SUPER\.env` as `FIRECRAWL_API_KEY`. NEVER print the
  raw key value in any file you write, and NEVER write `.env` contents into
  a tracked file. Load it per-call:
  ```bash
  export $(cat /c/Users/CC/SUPER/.env | xargs)
  curl -s -X POST https://api.firecrawl.dev/v1/search \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" -H "Content-Type: application/json" \
    -d '{"query":"...","limit":5}'
  curl -s -X POST https://api.firecrawl.dev/v1/scrape \
    -H "Authorization: Bearer $FIRECRAWL_API_KEY" -H "Content-Type: application/json" \
    -d '{"url":"...","formats":["markdown"]}'
  ```
  **Budget: max ~15 Firecrawl calls for your channel** (shared pool of 1020
  credits across 10 channels this billing period — stay economical, batch
  queries, don't re-scrape the same URL twice).

- **NVIDIA NIM** (cloud LLM API): `NVIDIA_NIM_API_KEY` in the same `.env`.
  Use only if you need to synthesize/summarize findings, not as a source of
  facts about current design trends — those must come from Firecrawl results.

- **yt-dlp** (`python -m yt_dlp`) + **ffmpeg** + **Python/PIL**: for
  downloading any reference Shorts/Reels clips you find and extracting
  frames into contact sheets. Only download clips that are clearly
  reference/analysis use; save nothing large into git — write frames/contact
  sheets to `research/frames_tmp/<channel>/` (gitignored) and only commit
  the final contact-sheet PNGs referenced by your moodboard doc if small.

## No packaged "motion design" or "taste" skills exist in this environment

The build brief references a LottieFiles motion-design-skill, a Motion.dev
easing/spring reference skill, and a taste-skill dial framework. None are
installed here. Approximate them yourself:
- For choreography/timing: research actual current best-practice sources
  (e.g. Motion.dev's own public easing docs, established 12-principles-of-
  animation writeups) via Firecrawl and cite them directly.
- For taste/decision framework: don't import any library. Just make and
  state explicit decisions on 3 dials — **layout variance** (how much
  compositions shift shot-to-shot), **motion intensity** (how aggressive
  eases/overshoots are), **visual density** (how much is on screen at once)
  — as a short paragraph per channel, justified by what you saw in the
  references, not invented from nothing.

## Phase 1 protocol (produce `research/visual-reference/<slug>.md`)

1. Firecrawl-search + scrape real motion design galleries (Dribbble,
   Behance, Awwwards-style sites) AND currently high-performing Shorts/
   Reels in your niche. List every source URL you actually fetched.
2. For at least 1-2 video references you can obtain via yt-dlp, extract
   frames at a regular interval with ffmpeg and assemble a contact sheet
   with PIL. Save to `research/frames_tmp/<slug>/contact_sheet_N.png`.
   If a reference can't be downloaded (private/DRM/no video), say so
   explicitly rather than skipping the citation.
3. From the frames/screenshots, extract structured tokens: hex color
   palette, typography scale (weights/sizes as seen), spacing rhythm,
   motion timing (cut frequency, avg shot length in frames at 60fps).
4. State the chosen motion-personality direction (the 3-dial paragraph
   above) grounded in what was observed.
5. Output file must have these sections: Source References (URL list),
   Extracted Color Tokens, Typography Tokens, Spacing Tokens, Motion/Pacing
   Notes, Motion-Personality Direction, Open Gaps (anything you couldn't
   verify).

## Phase 2 protocol, channel-specific parts (produce `research/channels/<slug>-topics-voice-music.md`)

- **Topics**: 8-10 real current topic examples in the niche sourced via
  Firecrawl (news/trend sites, not invented), each with a source URL.
- **Voice provider**: pick ONE open-source TTS engine for this channel's
  persona. It must be (a) self-hostable, (b) runnable on a GitHub Actions
  ubuntu runner with no GPU within a normal job timeout, (c) have a license
  permitting commercial use. Name the specific model/checkpoint, state
  license, and give rough CPU inference time for a ~150-word script.
- **Music sourcing**: describe the concrete method to identify trending
  tracks in this niche AND how stems/instrumentals would be obtained.
  Then write an explicit **Copyright Risk Flag** paragraph: stem-separated
  instrumentals of trending copyrighted songs still carry real Content ID /
  takedown risk on monetized automated content — removing vocals does not
  clear the underlying composition's copyright. Present the
  trending-but-risky vs. royalty-free-but-safer tradeoff plainly. Do NOT
  pick one for the operator — flag it as a decision the human must make.

## Hard rules

- No fabricated sources. If you can't find something, say "not found" —
  don't fill the gap with plausible-sounding invention.
- Cite every URL you actually hit.
- Stay within your channel's Firecrawl budget.
