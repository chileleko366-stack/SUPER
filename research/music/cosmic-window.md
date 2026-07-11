# Cosmic Window — Music Bed Sourcing

## Track

- **Title**: "Space X-plorers"
- **Artist**: Kevin MacLeod
- **Source**: incompetech.com
- **Track page**: https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100064&Search=Search
- **ISRC**: USUAN1100064
- **Catalog feel tags**: Relaxed, Mysterious, Epic
- **Duration**: 1:42 (102.2s measured via ffprobe on the downloaded file)
- **Composer description (from incompetech's own catalog data, `pieces.json`)**: "Background padding with an open wondrous feel."
- **Local file**: `assets/music/cosmic-window.mp3` (3,493,730 bytes, 102.22s duration, mp3/44.1kHz/stereo — confirmed via ffprobe)

## Why this track

Cosmic Window's tone is "awe-driven but precise science communicator — wonder-forward, not sensationalist" with `motionPersonality.motionIntensity: "low-to-moderate"` and an explicit note to avoid punchy/bouncy moves in favor of calm ambient motion (`channels/cosmic-window.json`). The composer's own description — "an open wondrous feel" — is a near-literal match for "wonder-forward" astronomy content, and the Relaxed/Mysterious/Epic feel tags land on ambient-with-scale rather than aggressive or comedic, appropriate for a "precise" (not sensationalist) science register.

## License

- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **License text**: https://creativecommons.org/licenses/by/4.0/
- **Source confirmation (quoted, fetched directly from incompetech.com/music/royalty-free/faq.html this session)**: in answer to whether the music can be used commercially and in monetized YouTube videos, the FAQ states verbatim: **"Yes, AND you can monetize the videos. Be sure to credit me."**
- **Monetization-safe**: **YES** — explicitly confirmed on the source's own FAQ page, not inferred from marketing copy.
- **Attribution required**: **YES**. Required credit text (exact format instructed by incompetech's own track-page rendering of its `pieces.json` catalog data):

```
"Space X-plorers" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/
```

- **Operator action item**: this attribution text must be placed in the YouTube video description.

## Verification method

Downloaded directly via `curl` from `https://incompetech.com/music/royalty-free/mp3-royaltyfree/space%20explorers.mp3` (note: the catalog's internal `filename` field for this ISRC is `space explorers.mp3`, lowercase, differing slightly from the display title — used verbatim as instructed by the source's own download-URL-construction JS). Verified with `ffprobe` — real mp3 audio stream (44.1kHz stereo) with duration matching the catalog's stated 1:42 length.
