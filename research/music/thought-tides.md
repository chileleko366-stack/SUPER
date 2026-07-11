# Thought Tides — Music Bed Sourcing

## Track

- **Title**: "Deliberate Thought"
- **Artist**: Kevin MacLeod
- **Source**: incompetech.com
- **Track page**: https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100261&Search=Search
- **ISRC**: USUAN1100261
- **Catalog feel tags**: Calming, Relaxed
- **Duration**: 2:57 (177.46s measured via ffprobe on the downloaded file)
- **Composer description (from incompetech's own catalog data, `pieces.json`)**: "Calming round electronic music with a nice delay... and a choir."
- **Local file**: `assets/music/thought-tides.mp3` (7,224,606 bytes, 177.46s duration, mp3/48kHz/stereo — confirmed via ffprobe)

## Why this track

Thought Tides' tone is "contemplative, calm, thought-provoking philosophy communicator" with `motionPersonality.motionIntensity: "low-to-moderate"` and an explicit note to avoid bounce/overshoot in favor of a "contemplative register" (`channels/thought-tides.json`). "Deliberate Thought" is a Calming/Relaxed ambient-electronic piece with a choir pad — its very title doubles as a fitting descriptor for a philosophy channel, and its calm, unhurried texture matches the contemplative, non-punchy register the moodboard calls for.

## License

- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **License text**: https://creativecommons.org/licenses/by/4.0/
- **Source confirmation (quoted, fetched directly from incompetech.com/music/royalty-free/faq.html this session)**: in answer to whether the music can be used commercially and in monetized YouTube videos, the FAQ states verbatim: **"Yes, AND you can monetize the videos. Be sure to credit me."**
- **Monetization-safe**: **YES** — explicitly confirmed on the source's own FAQ page, not inferred from marketing copy.
- **Attribution required**: **YES**. Required credit text (exact format instructed by incompetech's own track-page rendering of its `pieces.json` catalog data):

```
"Deliberate Thought" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/
```

- **Operator action item**: this attribution text must be placed in the YouTube video description.

## Verification method

Downloaded directly via `curl` from `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Deliberate%20Thought.mp3`. Verified with `ffprobe` — real mp3 audio stream (48kHz stereo — this track's source master is 48kHz, unlike most of the other catalog entries downloaded this session which are 44.1kHz; both are standard rates ffmpeg/Remotion handle natively) with duration matching the catalog's stated 2:57 length.
