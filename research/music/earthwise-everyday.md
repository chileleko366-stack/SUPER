# Earthwise Everyday — Music Bed Sourcing

## Track

- **Title**: "Morning"
- **Artist**: Kevin MacLeod
- **Source**: incompetech.com
- **Track page**: https://incompetech.com/music/royalty-free/index.html?isrc=USUAN2300003&Search=Search
- **ISRC**: USUAN2300003
- **Catalog feel tags**: Bright, Calm, Relaxed
- **Duration**: 2:33 (153.31s measured via ffprobe on the downloaded file)
- **Composer description (from incompetech's own catalog data, `pieces.json`)**: "This piece of music is based on the old-timey concept of calm, beautiful, renewing mornings."
- **Local file**: `assets/music/earthwise-everyday.mp3` (3,068,475 bytes, 153.31s duration, mp3/44.1kHz/stereo — confirmed via ffprobe)

## Why this track

Earthwise Everyday's tone is "grounded, optimistic, practical eco-living communicator — not preachy, not doom-oriented, not glossy-corporate-greenwash" with `motionPersonality.motionIntensity: "low"` and a preference for calm, uncluttered register (`channels/earthwise-everyday.json`). "Morning" is explicitly composed around "calm, beautiful, renewing mornings" — directly aligned with grounded optimism rather than urgency or doom, and its Bright/Calm/Relaxed tags avoid both the "preachy" and "corporate-greenwash" traps the channel's own tone notes flag.

## License

- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **License text**: https://creativecommons.org/licenses/by/4.0/
- **Source confirmation (quoted, fetched directly from incompetech.com/music/royalty-free/faq.html this session)**: in answer to whether the music can be used commercially and in monetized YouTube videos, the FAQ states verbatim: **"Yes, AND you can monetize the videos. Be sure to credit me."**
- **Monetization-safe**: **YES** — explicitly confirmed on the source's own FAQ page, not inferred from marketing copy.
- **Attribution required**: **YES**. Required credit text (exact format instructed by incompetech's own track-page rendering of its `pieces.json` catalog data):

```
"Morning" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/
```

- **Operator action item**: this attribution text must be placed in the YouTube video description.

## Verification method

Downloaded directly via `curl` from `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Morning.mp3`. Verified with `ffprobe` — real mp3 audio stream (44.1kHz stereo) with duration matching the catalog's stated 2:33 length.
