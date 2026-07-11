# Silver Screen Insight — Music Bed Sourcing

## Track

- **Title**: "Highlight Reel"
- **Artist**: Kevin MacLeod
- **Source**: incompetech.com
- **Track page**: https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100205&Search=Search
- **ISRC**: USUAN1100205
- **Catalog feel tags**: Driving
- **Duration**: 2:55 (175.96s measured via ffprobe on the downloaded file)
- **Composer description (from incompetech's own catalog data, `pieces.json`)**: "Not pure rock, it has jazz and funk characteristics. Reminds me of the under music for a sports highlights telecast. Rock beat, a few guitars, and a nice electric bass."
- **Local file**: `assets/music/silver-screen-insight.mp3` (6,721,927 bytes, 175.96s duration, mp3/44.1kHz/stereo — confirmed via ffprobe)

## Why this track

Silver Screen Insight's tone is "cinephile, articulate, visually literate critic" with `motionPersonality.motionIntensity: "medium-high"` and an explicit note for "fast ease-out entrances with low/no bounce or overshoot... precise and controlled, not cartoonish" (`channels/silver-screen-insight.json`). "Highlight Reel" is a jazz/funk/rock-hybrid instrumental composed as "under music for a highlights telecast" — a sophisticated, editorially-controlled groove rather than a generic beat, fitting a critic voiceover format without being cartoonish or aggressive.

## License

- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **License text**: https://creativecommons.org/licenses/by/4.0/
- **Source confirmation (quoted, fetched directly from incompetech.com/music/royalty-free/faq.html this session)**: in answer to whether the music can be used commercially and in monetized YouTube videos, the FAQ states verbatim: **"Yes, AND you can monetize the videos. Be sure to credit me."**
- **Monetization-safe**: **YES** — explicitly confirmed on the source's own FAQ page, not inferred from marketing copy.
- **Attribution required**: **YES**. Required credit text (exact format instructed by incompetech's own track-page rendering of its `pieces.json` catalog data):

```
"Highlight Reel" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/
```

- **Operator action item**: this attribution text must be placed in the YouTube video description.

## Verification method

Downloaded directly via `curl` from `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Highlight%20Reel.mp3`. Verified with `ffprobe` — real mp3 audio stream (44.1kHz stereo) with duration matching the catalog's stated 2:55 length.
