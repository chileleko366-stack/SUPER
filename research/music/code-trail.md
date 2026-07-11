# Code Trail — Music Bed Sourcing

## Track

- **Title**: "Aitech"
- **Artist**: Kevin MacLeod
- **Source**: incompetech.com
- **Track page**: https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100336&Search=Search
- **ISRC**: USUAN1100336
- **Catalog feel tags**: Grooving, Bright
- **Duration**: 2:30 (150.9s measured via ffprobe on the downloaded file)
- **Composer description (from incompetech's own catalog data, `pieces.json`)**: "Hard rock beat with electronic elements grooving in."
- **Local file**: `assets/music/code-trail.mp3` (3,728,372 bytes, 150.91s duration, mp3/44.1kHz/stereo — confirmed via ffprobe)

## Why this track

Code Trail's tone is "crisp, technical, dev-to-dev" with `motionPersonality.motionIntensity: "moderate"` and an explicit note to avoid bounce/overshoot in favor of restrained, technical energy (`channels/code-trail.json`, `research/visual-reference/code-trail.md`). "Aitech" is an electronica/rock-hybrid instrumental with a driving-but-controlled groove and no vocals — reads as clean/technical rather than lifestyle or cinematic, and its title is a direct (coincidental but fitting) match for an AI/programming channel.

## License

- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **License text**: https://creativecommons.org/licenses/by/4.0/
- **Source confirmation (quoted, fetched directly from incompetech.com/music/royalty-free/faq.html this session)**: in answer to whether the music can be used commercially and in monetized YouTube videos, the FAQ states verbatim: **"Yes, AND you can monetize the videos. Be sure to credit me."**
- **Monetization-safe**: **YES** — explicitly confirmed on the source's own FAQ page, not inferred from marketing copy.
- **Attribution required**: **YES**. Required credit text (from the track's own page, rendered from incompetech's `pieces.json` catalog data — this is the exact format incompetech instructs creators to use):

```
"Aitech" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/
```

- **Operator action item**: this attribution text must be placed in the YouTube video description (incompetech's FAQ specifies description or on-screen credit is acceptable for YouTube/Vimeo).

## Verification method

Downloaded directly via `curl` from `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Aitech.mp3` (the exact download URL incompetech's own track-detail page constructs from its `pieces.json` catalog, confirmed by reading the page's rendering JS). Verified with `ffprobe` — real mp3 audio stream (44.1kHz stereo) with duration matching the catalog's stated 2:30 length, not an HTML error page saved with a `.mp3` extension.
