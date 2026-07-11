# Echoes of Ages — Music Bed Sourcing

## Track

- **Title**: "Americana"
- **Artist**: Kevin MacLeod
- **Source**: incompetech.com
- **Track page**: https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1200092&Search=Search
- **ISRC**: USUAN1200092
- **Catalog feel tags**: Epic, Uplifting
- **Duration**: 3:22 (202.21s measured via ffprobe on the downloaded file)
- **Composer description (from incompetech's own catalog data, `pieces.json`)**: "Starts out simply on the plains with cellos and winds, becomes disrupted bit a bit and piles on the grandiose with a lot of brass!"
- **Local file**: `assets/music/echoes-of-ages.mp3` (8,090,770 bytes, 202.21s duration, mp3/44.1kHz/stereo — confirmed via ffprobe)

## Why this track

Echoes of Ages' tone is "epic, documentary-narrator gravitas" for history/civilizations content (`channels/echoes-of-ages.json`). "Americana" is an orchestral piece (cellos, winds, brass) that builds from a simple, spare opening to a grandiose full-orchestra close — a genuinely epic, documentary-appropriate arc, and its Epic/Uplifting tags avoid the Dark/Eerie/Unnerving register that dominates most other "Epic"-tagged tracks in this catalog (those read more as horror/thriller scoring, which would clash with this channel's gravitas-not-dread tone). Deliberately screened out tracks like "Epic Unease" (Dark, Eerie, Unnerving) for this reason.

## License

- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **License text**: https://creativecommons.org/licenses/by/4.0/
- **Source confirmation (quoted, fetched directly from incompetech.com/music/royalty-free/faq.html this session)**: in answer to whether the music can be used commercially and in monetized YouTube videos, the FAQ states verbatim: **"Yes, AND you can monetize the videos. Be sure to credit me."**
- **Monetization-safe**: **YES** — explicitly confirmed on the source's own FAQ page, not inferred from marketing copy.
- **Attribution required**: **YES**. Required credit text (exact format instructed by incompetech's own track-page rendering of its `pieces.json` catalog data):

```
"Americana" Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/
```

- **Operator action item**: this attribution text must be placed in the YouTube video description.

## Verification method

Downloaded directly via `curl` from `https://incompetech.com/music/royalty-free/mp3-royaltyfree/Americana.mp3`. Verified with `ffprobe` — real mp3 audio stream (44.1kHz stereo) with duration matching the catalog's stated 3:22 length.

## Note on concurrent work

This channel's caption rendering (`src/remotion/primitives/KineticCaption.tsx`) and its topic-sourcing config (`channels/echoes-of-ages.json`) were being independently fixed by other agents at the time this music was sourced. See this channel's VERIFICATION.md in the new run-id directory for whether those fixes had landed by render time and were spot-checked.
