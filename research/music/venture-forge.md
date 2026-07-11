# Venture Forge — Music Bed Sourcing

## Track

- **Title**: "Hustle"
- **Artist**: Kevin MacLeod
- **Source**: incompetech.com
- **Track page**: https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100793&Search=Search
- **ISRC**: USUAN1100793
- **Catalog feel tags**: Bouncy, Bright, Driving
- **Duration**: 2:01 (120.56s measured via ffprobe on the downloaded file)
- **Composer description (from incompetech's own catalog data, `pieces.json`)**: "The bass guitar plays a familiar rolling Blues riff, while accompanied by organ, acoustic guitar, and drums. A toe-tapping beat plays throughout, and can be used as the background music for a fast-paced game or scene, or as the intro to a scene full of bustling people."
- **Local file**: `assets/music/venture-forge.mp3` (4,824,325 bytes, 120.56s duration, mp3/44.1kHz/stereo — confirmed via ffprobe)

## Why this track

Venture Forge's tone is "sharp, energetic, builder-to-builder" for startup/founder content, with the moodboard explicitly noting that its "sharp, energetic" feel should come from "caption density, cut selection, and copy — not from exaggerated spring physics" (`channels/venture-forge.json`'s `motionPersonality.easingNote`). "Hustle" is a toe-tapping, blues-rock-organ instrumental literally composed for "fast-paced... scene[s] full of bustling people" — its title and description are a direct match for startup/builder "hustle" culture, and its Driving-but-not-Aggressive energy provides the track's own forward motion without requiring bouncy on-screen physics.

## License

- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **License text**: https://creativecommons.org/licenses/by/4.0/
- **Source confirmation (quoted, fetched directly from incompetech.com/music/royalty-free/faq.html this session)**: in answer to whether the music can be used commercially and in monetized YouTube videos, the FAQ states verbatim: **"Yes, AND you can monetize the videos. Be sure to credit me."**
- **Monetization-safe**: **YES** — explicitly confirmed on the source's own FAQ page, not inferred from marketing copy.
- **Attribution required**: **YES**. Required credit text (exact format instructed by incompetech's own track-page rendering of its `pieces.json` catalog data):

```
"Hustle" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/
```

- **Operator action item**: this attribution text must be placed in the YouTube video description.

## Verification method

Downloaded directly via `curl` from `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Hustle.mp3`. Verified with `ffprobe` — real mp3 audio stream (44.1kHz stereo) with duration matching the catalog's stated 2:01 length.
