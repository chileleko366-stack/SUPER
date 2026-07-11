# Market Lens — Music Bed Sourcing

## Track

- **Title**: "Shiny Tech"
- **Artist**: Kevin MacLeod
- **Source**: incompetech.com
- **Track page**: https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100078&Search=Search
- **ISRC**: USUAN1100078
- **Catalog feel tags**: Driving, Action, Intense, Uplifting, Bright
- **Duration**: 3:42 (222.67s measured via ffprobe on the downloaded file)
- **Composer description (from incompetech's own catalog data, `pieces.json`)**: "Electronica (techno-pop dance). This is a fast and energetic piece polished almost to a fault. Lots of synth, and a happy clave."
- **Local file**: `assets/music/market-lens.mp3` (9,014,582 bytes, 222.67s duration, mp3/44.1kHz/stereo — confirmed via ffprobe)

## Why this track

Market Lens's tone is "sharp, analytical, macro-explainer" with `motionPersonality.motionIntensity: "medium-high"` and a channel-specific note that spring/overshoot easing IS appropriate here (its DataChart beats use "pop in, settle" bar-growth), unlike most other channels in this pipeline (`channels/market-lens.json`). "Shiny Tech" is a Driving/Intense/Uplifting/Bright electronica track — polished, propulsive energy that matches the channel's above-average motion intensity and analytical-but-energetic register, without tipping into the Dark/Aggressive tracks elsewhere in the catalog that would clash with "sharp, analytical" (as opposed to menacing).

## License

- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **License text**: https://creativecommons.org/licenses/by/4.0/
- **Source confirmation (quoted, fetched directly from incompetech.com/music/royalty-free/faq.html this session)**: in answer to whether the music can be used commercially and in monetized YouTube videos, the FAQ states verbatim: **"Yes, AND you can monetize the videos. Be sure to credit me."**
- **Monetization-safe**: **YES** — explicitly confirmed on the source's own FAQ page, not inferred from marketing copy.
- **Attribution required**: **YES**. Required credit text (exact format instructed by incompetech's own track-page rendering of its `pieces.json` catalog data):

```
"Shiny Tech" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/
```

- **Operator action item**: this attribution text must be placed in the YouTube video description.

## Verification method

Downloaded directly via `curl` from `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Shiny%20Tech.mp3`. Verified with `ffprobe` — real mp3 audio stream (44.1kHz stereo) with duration matching the catalog's stated 3:42 length.
