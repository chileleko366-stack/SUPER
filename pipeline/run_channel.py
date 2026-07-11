#!/usr/bin/env python3
"""Per-channel content pipeline: Firecrawl topic sourcing -> NVIDIA NIM
script generation -> Piper TTS -> asset resolution (local caching, no
remote hits during render) -> props.json for Remotion.

Parameterized by --channel so it is reusable across all 10 channels, not
Mind-Mosaic-specific -- per Phase 7 pilot instructions. Channel-specific
behavior (tokens, voice, shot grammar) all comes from channels/<slug>.json,
not from code branches on the channel name.

DataChart accuracy handling (deliberate choice, documented rather than
hidden): NVIDIA NIM is not a reliable source of real-time financial/economic
figures. This pipeline does NOT ask NIM for "real" numbers and does not
scrape a second factual source per topic to back-fill DataChart beats
either (that's a real, disclosed gap -- see each channel's VERIFICATION.md).
Instead, the script-generation prompt (see `build_script_prompt`'s
`chart_note`) explicitly instructs NIM to produce clearly-illustrative
EXAMPLE figures for teaching a concept (e.g. "if you save $50/month..."
style hypothetical math), and to phrase the spoken line so a viewer
understands the numbers are illustrative, not reported statistics.
`resolve_chart_data` then validates structure (labels + numeric values)
but cannot and does not verify factual accuracy -- illustrative-by-design,
not fabricated-and-passed-off-as-real.
"""
import argparse
import json
import math
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import firecrawl_client, nim_client, tts_piper, tts_kokoro, assets_gen  # noqa: E402

ROOT = Path(__file__).parent.parent
FPS = 60
MIN_SEGMENT_FRAMES = 60  # 1s floor so no beat is imperceptibly short

CUT_SFX_CYCLE = ["click1.mp3", "click2.mp3", "chime1.mp3", "click1.mp3", "click2.mp3", "chime1.mp3", "click1.mp3"]
HOOK_SFX = "whoosh1.mp3"


def load_channel_config(slug: str) -> dict:
    path = ROOT / "channels" / f"{slug}.json"
    if not path.exists():
        raise SystemExit(f"No channel config at {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def source_topic(channel: dict) -> dict:
    """Real Firecrawl call -- picks the first fresh result for one of the
    channel's configured query patterns. Falls back through patterns if a
    query returns nothing."""
    for query in channel["firecrawlQueryPatterns"]:
        results = firecrawl_client.search(query, limit=5)
        if results:
            top = results[0]
            return {"query": query, "title": top.get("title", ""), "url": top.get("url", ""),
                     "description": top.get("description", "")}
    raise RuntimeError("No Firecrawl search results across any configured query pattern")


SCRIPT_SYSTEM_PROMPT = """You write short-form (45-70 second) faceless YouTube Shorts scripts.
Voice/tone is set by the operator. Output ONLY valid JSON, no prose, no markdown fences.
Every beat's "text" field is a short spoken line (8-20 words) suitable for text-to-speech
narration and on-screen kinetic captions -- not a written essay. Beats with "traits" get
3 short (1-4 word) keyword/phrase items, not full sentences. Beats with "timelineEvents"
get 3 to 5 objects, each with a short (1-4 word) "label" and a "date" field holding a
REAL, historically plausible year/date for the actual topic being scripted, in correct
chronological order -- these are read by a downstream renderer as literal on-screen date
badges, so invented, anachronistic, or internally-inconsistent dates are a hard failure,
not a stylistic choice. If you are not confident of an exact year, use the most
specific date range that is still historically defensible (e.g. "c. 1289" or "1450s")
rather than fabricating false precision. You do not have access to real-time data. For
any beat requiring "chartData", invent clearly-illustrative EXAMPLE numbers to teach a
concept (e.g. simple hypothetical savings/growth math) -- never invent numbers and
present them as real reported statistics. Beats with "codeLines" get a real, syntactically
correct, runnable code snippet -- you are a careful software engineer writing this
snippet, not improvising fake syntax. Double-check indentation, matching brackets/parens,
and correct keyword spelling for the language you choose before answering."""

CODE_BLOCK_GUIDANCE = (
    ' Also include "codeLines": an array of 6-10 short lines (each under 46 characters, '
    "using 2-space indentation, no tabs) of a real, syntactically correct, working code "
    "snippet in a well-known mainstream language (Python or JavaScript preferred) that "
    "implements a simple, well-known algorithm or pattern relevant to the topic (e.g. a "
    "classic sort, a common one-liner, a basic data-structure operation). Do not invent "
    'syntax; write only code you are confident actually compiles/runs. Also include '
    '"language": the lowercase language name (e.g. "python", "javascript"). "text" for '
    "this beat is still a short spoken line (6-10 words, e.g. \"Here's binary search in "
    "six lines of Python\") -- it is read aloud by TTS AND shown as the on-screen snippet "
    "title, so keep it short enough to fit one line."
)


def _example_for_beat(beat_cfg: dict) -> dict:
    """Builds an illustrative example object for one beat, shaped by its
    primitive (and, for two conventional beat names with no distinguishing
    primitive of their own, by beat name) -- keeps the prompt's example JSON
    in sync with whatever beat names/primitives a channel actually
    configures (channels/<slug>.json), instead of hardcoding one channel's
    beat names into every prompt."""
    beat, primitive = beat_cfg["beat"], beat_cfg["primitive"]
    example: dict = {"text": "short spoken line, 8-20 words"}

    if primitive == "InfoCard":
        example["text"] = "short headline"
        example["traits"] = ["kw1", "kw2", "kw3"]
    elif primitive == "KenBurnsCard":
        example["text"] = "short caption for a b-roll still"
    elif primitive == "TimelineReveal":
        example["emphasisWord"] = "onewordfromtext"
        example["timelineEvents"] = [
            {"label": "short event name", "date": "a real plausible year, e.g. 1289"},
            {"label": "short event name", "date": "a later real plausible year"},
            {"label": "short event name", "date": "a later real plausible year"},
        ]
    elif primitive == "DataChart":
        example["text"] = (
            "spoken line that clearly frames the numbers as an illustrative example, "
            "e.g. 'say you save $50 a month' -- NOT a claimed real statistic"
        )
        example["chartData"] = [
            {"label": "Month 1", "value": 50},
            {"label": "Month 6", "value": 300},
            {"label": "Month 12", "value": 600},
        ]
    elif primitive == "CodeBlock":
        example["text"] = "Here's binary search in six lines"
        example["language"] = "python"
        example["codeLines"] = [
            "def binary_search(arr, target):",
            "  lo, hi = 0, len(arr) - 1",
            "  while lo <= hi:",
            "    mid = (lo + hi) // 2",
            "    if arr[mid] == target:",
            "      return mid",
            "    if arr[mid] < target:",
            "      lo = mid + 1",
            "    else:",
            "      hi = mid - 1",
            "  return -1",
        ]
    elif beat == "hook":
        example["emphasisWord"] = "onewordfromtext"
    elif beat == "conclusion":
        example["text"] = "actionable one-line takeaway"

    return example


def build_script_prompt(channel: dict, topic: dict) -> str:
    beats = channel["shotGrammar"]
    beat_desc = "\n".join(
        f'- beat "{b["beat"]}" (primitive: {b["primitive"]})'
        + (CODE_BLOCK_GUIDANCE if b["primitive"] == "CodeBlock" else "")
        for b in beats
    )
    example = {b["beat"]: _example_for_beat(b) for b in beats}
    example_json = json.dumps(example, indent=2)

    chart_note = ""
    if any(b["primitive"] == "DataChart" for b in beats):
        chart_note = """

IMPORTANT for any beat with primitive DataChart: you do not have access to real,
current financial/economic data. Do NOT invent numbers and present them as real
statistics. Produce clearly-illustrative EXAMPLE figures that teach the underlying
concept (e.g. hypothetical "if you save $X a month" math, a simple made-up
before/after comparison, or round illustrative percentages), 3-5 chartData points,
and make the spoken "text" for that beat say something like "let's say" / "for
example" / "imagine" so viewers understand these are illustrative numbers, not
reported real-world data."""

    return f"""Channel: {channel['displayName']} -- {channel['niche']}
Tone: {channel['tone']}
Hook formula: {channel['hookFormula']}
Narrative structure: {channel['narrativeStructure']}

Topic sourced live via Firecrawl just now:
Title: {topic['title']}
Description: {topic['description']}
URL: {topic['url']}

Write a script with exactly these beats, in this order:
{beat_desc}
{chart_note}

Return JSON with exactly this shape (the values below are illustrative
placeholders describing what each field is for -- replace every one with
real content written for the topic above):
{example_json}"""


def generate_script(channel: dict, topic: dict) -> dict:
    prompt = build_script_prompt(channel, topic)
    has_code_beat = any(b["primitive"] == "CodeBlock" for b in channel["shotGrammar"])
    max_tokens = 1300 if has_code_beat else 900
    return nim_client.generate_json(SCRIPT_SYSTEM_PROMPT, prompt, max_tokens=max_tokens)


def resolve_accent(beat_cfg: dict) -> str:
    return beat_cfg["accent"]


def resolve_chart_data(beat_script: dict, beat: str) -> list[dict]:
    """Validates the NIM-produced chartData for a DataChart beat. This is
    the one enforcement point standing between "NIM hallucinated a number"
    and it silently landing on screen as a rendered chart: every point must
    have a real label and a numeric value, and there must be at least 2
    points, or the pipeline fails loudly instead of rendering a broken/empty
    chart. It does NOT and cannot verify the numbers are factually accurate
    -- see the DataChart accuracy-handling note in run_channel.py's module
    docstring and each channel's VERIFICATION.md for why illustrative
    figures (not claimed real data) are this pipeline's chosen approach."""
    raw = beat_script.get("chartData")
    if not isinstance(raw, list) or len(raw) < 2:
        raise RuntimeError(
            f"NIM script missing usable chartData for DataChart beat '{beat}' "
            f"(need a list of >=2 {{label, value}} points, got {raw!r})"
        )
    out = []
    for item in raw:
        if not isinstance(item, dict):
            raise RuntimeError(f"NIM chartData item for beat '{beat}' is not an object: {item!r}")
        label = str(item.get("label", "")).strip()
        if not label:
            raise RuntimeError(f"NIM chartData item for beat '{beat}' missing a label: {item!r}")
        try:
            value = float(item["value"])
        except (KeyError, TypeError, ValueError):
            raise RuntimeError(f"NIM chartData item for beat '{beat}' has a non-numeric value: {item!r}")
        out.append({"label": label, "value": value})
    return out


def synthesize_vo(text: str, channel: dict, out_wav: Path) -> float:
    """Dispatches to the TTS engine named in the channel's own voice
    research (channels/<slug>.json -> voice.engine), so each channel can use
    the engine its own licensing/persona research actually recommended
    instead of one hardcoded engine for every channel."""
    voice_cfg = channel["voice"]
    engine = voice_cfg.get("engine", "piper")

    if engine == "piper":
        model_path = ROOT / ".voices" / f"{voice_cfg['checkpoint']}.onnx"
        if not model_path.exists():
            raise RuntimeError(
                f"Piper voice model not found at {model_path} -- download it first: "
                f"python -m piper.download_voices {voice_cfg['checkpoint']}"
            )
        return tts_piper.synthesize(text, model_path, out_wav, speaker_id=voice_cfg.get("speakerId", 0))

    if engine == "kokoro":
        return tts_kokoro.synthesize(text, voice_cfg["checkpoint"], out_wav, lang_code=voice_cfg.get("langCode", "a"))

    raise ValueError(f"Unknown voice engine {engine!r} in channel config")


def synthesize_music_bed(out_path: Path, duration_s: float) -> Path:
    """PLACEHOLDER music bed: a soft synthesized pad, NOT a sourced trending
    or royalty-free-library track. This is the fallback used only when a
    channel has no real sourced track under assets/music/<slug>.<ext> yet
    (see resolve_music_bed) -- exists only so the audio-ducking system has
    something real to duck under for verification purposes in that case."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-f", "lavfi", "-i", f"sine=frequency=110:duration={duration_s}",
        "-f", "lavfi", "-i", f"sine=frequency=165:duration={duration_s}",
        "-filter_complex",
        f"[0]volume=0.5[a];[1]volume=0.3[b];[a][b]amix=inputs=2:duration=longest,"
        f"afade=t=in:st=0:d=1,afade=t=out:st={max(duration_s-1.5,0):.2f}:d=1.5",
        str(out_path),
    ]
    subprocess.run(cmd, capture_output=True, check=True, timeout=60)
    return out_path


REAL_MUSIC_EXTS = ("mp3", "m4a", "ogg", "flac")


def resolve_music_bed(channel_slug: str, audio_dir: Path, duration_s: float) -> str:
    """Real sourced music bed, replacing the synthesized placeholder wherever
    one has actually been sourced and licensed. Looks for a pre-downloaded,
    committed master track at assets/music/<slug>.<ext> (mp3/m4a/ogg/flac --
    deliberately never .wav, since .gitignore blanket-ignores *.wav and a
    real master stored as .wav would silently fail to be tracked by git).
    Each such file has a matching research/music/<slug>.md documenting the
    track's title/artist/source/license terms (verified to explicitly permit
    commercial + monetized-YouTube use) and required attribution text.

    AudioMix.tsx already loops whatever musicSrc points at
    (`<Audio ... loop />`), so the sourced master does not need to be
    trimmed or regenerated to match this run's exact duration -- it is
    simply copied byte-for-byte into this run's audio/ dir under the name
    props.json's musicSrc expects.

    Falls back to the synthesized placeholder (see synthesize_music_bed)
    only if no real track has been sourced for this channel yet, so the
    pipeline still produces a playable, ducking-compatible music bed for
    any not-yet-sourced channel rather than failing outright.

    Returns the path relative to the per-run public dir (e.g.
    "audio/music_bed.mp3"), for direct use as props.json's musicSrc suffix.
    """
    music_library = ROOT / "assets" / "music"
    for ext in REAL_MUSIC_EXTS:
        src = music_library / f"{channel_slug}.{ext}"
        if src.exists():
            dst_rel = f"audio/music_bed.{ext}"
            dst = audio_dir.parent / dst_rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(src.read_bytes())
            return dst_rel

    dst_rel = "audio/music_bed.wav"
    dst = audio_dir.parent / dst_rel
    synthesize_music_bed(dst, duration_s)
    return dst_rel


def run(channel_slug: str, run_id: str | None = None) -> Path:
    channel = load_channel_config(channel_slug)
    run_id = run_id or time.strftime("%Y%m%d-%H%M%S")

    out_dir = ROOT / "out" / channel_slug / run_id
    public_dir = ROOT / "public" / "generated" / channel_slug / run_id
    (out_dir).mkdir(parents=True, exist_ok=True)
    (public_dir / "audio").mkdir(parents=True, exist_ok=True)
    (public_dir / "images").mkdir(parents=True, exist_ok=True)
    (public_dir / "sfx").mkdir(parents=True, exist_ok=True)

    print(f"[1/5] Sourcing topic via Firecrawl for {channel_slug}...")
    topic = source_topic(channel)
    (out_dir / "topic.json").write_text(json.dumps(topic, indent=2), encoding="utf-8")
    print(f"      topic: {topic['title'][:80]}")

    print("[2/5] Generating script via NVIDIA NIM...")
    script = generate_script(channel, topic)
    (out_dir / "script.json").write_text(json.dumps(script, indent=2), encoding="utf-8")

    print(f"[3/5] Synthesizing voiceover ({channel['voice'].get('engine', 'piper')} TTS) + resolving assets...")
    sfx_dir = ROOT / "soundfx.d"

    segments = []
    for i, beat_cfg in enumerate(channel["shotGrammar"]):
        beat = beat_cfg["beat"]
        beat_script = script.get(beat, {})
        text = beat_script.get("text", "").strip()
        if not text:
            raise RuntimeError(f"NIM script missing text for beat '{beat}'")

        wav_rel = f"audio/{i:02d}_{beat}.wav"
        wav_abs = public_dir / wav_rel
        duration_s = synthesize_vo(text, channel, wav_abs)
        duration_frames = max(MIN_SEGMENT_FRAMES, math.ceil(duration_s * FPS) + 12)

        seg = {
            "beat": beat,
            "primitive": beat_cfg["primitive"],
            "text": text,
            "accent": resolve_accent(beat_cfg),
            "voAudioSrc": f"generated/{channel_slug}/{run_id}/{wav_rel}",
            "durationInFrames": duration_frames,
            "cutSfx": f"generated/{channel_slug}/{run_id}/sfx/{Path(HOOK_SFX if i == 0 else CUT_SFX_CYCLE[i % len(CUT_SFX_CYCLE)]).name}",
        }
        if "emphasisWord" in beat_script:
            seg["emphasisWord"] = beat_script["emphasisWord"]
        if "traits" in beat_script:
            seg["traits"] = beat_script["traits"]
        if beat_cfg["primitive"] == "CodeBlock":
            code_lines = beat_script.get("codeLines") or []
            if not code_lines:
                raise RuntimeError(f"NIM script missing codeLines for CodeBlock beat '{beat}'")
            seg["codeLines"] = code_lines
            seg["language"] = beat_script.get("language", "")
            # A code beat needs enough hold time to read every revealed line,
            # not just enough time for the (short) spoken title -- floor it at
            # ~0.9s/line on top of the VO-derived duration.
            code_floor_frames = math.ceil(len(code_lines) * 0.9 * FPS) + 30
            duration_frames = max(duration_frames, code_floor_frames)
            seg["durationInFrames"] = duration_frames
        if beat_cfg["primitive"] == "KenBurnsCard":
            accent_hex = (
                channel["visualTokens"]["moodAccents"][seg["accent"]].get("primary")
            )
            img_rel = f"images/{i:02d}_{beat}.png"
            img_abs = public_dir / img_rel
            assets_gen.generate_broll_card(
                text, accent_hex, channel["visualTokens"]["background"]["explanationBase"], img_abs
            )
            seg["imageSrc"] = f"generated/{channel_slug}/{run_id}/{img_rel}"
        if beat_cfg["primitive"] == "TimelineReveal":
            events = beat_script.get("timelineEvents")
            if not events or len(events) < 2:
                raise RuntimeError(
                    f"NIM script missing/insufficient timelineEvents for beat '{beat}' "
                    f"(TimelineReveal needs at least 2 dated events, got {events!r})"
                )
            for ev in events:
                if not ev.get("label") or not ev.get("date"):
                    raise RuntimeError(f"NIM timelineEvents entry missing label/date in beat '{beat}': {ev!r}")
            seg["timelineEvents"] = events
        if beat_cfg["primitive"] == "DataChart":
            seg["chartData"] = resolve_chart_data(beat_script, beat)

        segments.append(seg)
        print(f"      [{beat}] {duration_s:.2f}s -> {duration_frames}f  \"{text[:60]}\"")

    print("[4/5] Copying SFX + resolving music bed...")
    used_sfx = {seg["cutSfx"].split("/")[-1] for seg in segments}
    for name in used_sfx:
        src = sfx_dir / name
        if not src.exists():
            raise RuntimeError(f"Missing vendored SFX file: {src}")
        dst = public_dir / "sfx" / name
        dst.write_bytes(src.read_bytes())

    total_duration_s = sum(s["durationInFrames"] for s in segments) / FPS
    music_rel = resolve_music_bed(channel_slug, public_dir / "audio", total_duration_s)
    if music_rel.endswith(".wav"):
        print(f"      WARNING: no sourced track at assets/music/{channel_slug}.<ext> -- using synthesized placeholder")
    else:
        print(f"      music bed: assets/music/{channel_slug}.{music_rel.rsplit('.', 1)[-1]} (see research/music/{channel_slug}.md for license)")

    # DataChart's motion (calm ease-out vs. energetic spring-overshoot) is
    # driven by the channel's own motionPersonality.motionIntensity research
    # finding, not hardcoded -- "high"/"medium-high" opts into the
    # spring/overshoot data-reveal treatment; anything else keeps the
    # no-bounce default every other primitive in this pipeline uses.
    motion_intensity = channel.get("motionPersonality", {}).get("motionIntensity", "").lower()
    chart_motion = "energetic" if "high" in motion_intensity else "calm"

    tokens = {
        "background": channel["visualTokens"]["background"],
        "moodAccents": channel["visualTokens"]["moodAccents"],
        "captionEmphasis": channel["visualTokens"]["captionEmphasis"],
        "captionDefault": channel["visualTokens"]["captionDefault"],
        "fontStack": channel["typography"]["captionFallbackFontStack"],
        "chartMotion": chart_motion,
    }
    # Optional: only channels using TimelineReveal (e.g. Echoes of Ages)
    # define this block in visualTokens.
    if "timeline" in channel["visualTokens"]:
        tokens["timeline"] = channel["visualTokens"]["timeline"]

    props = {
        "channelSlug": channel_slug,
        "tokens": tokens,
        "segments": segments,
        "musicSrc": f"generated/{channel_slug}/{run_id}/{music_rel}",
        "musicPolicy": channel["music"]["policy"],
    }
    props_path = out_dir / "props.json"
    props_path.write_text(json.dumps(props, indent=2), encoding="utf-8")

    print(f"[5/5] Wrote props to {props_path}")
    print(f"      Total runtime: {total_duration_s:.1f}s ({sum(s['durationInFrames'] for s in segments)} frames @ {FPS}fps)")
    return props_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", required=True)
    parser.add_argument("--run-id", default=None)
    args = parser.parse_args()
    run(args.channel, args.run_id)
