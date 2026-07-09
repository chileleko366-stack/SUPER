#!/usr/bin/env python3
"""Per-channel content pipeline: Firecrawl topic sourcing -> NVIDIA NIM
script generation -> Piper TTS -> asset resolution (local caching, no
remote hits during render) -> props.json for Remotion.

Parameterized by --channel so it is reusable across all 10 channels, not
Mind-Mosaic-specific -- per Phase 7 pilot instructions. Channel-specific
behavior (tokens, voice, shot grammar) all comes from channels/<slug>.json,
not from code branches on the channel name.
"""
import argparse
import json
import math
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import firecrawl_client, nim_client, tts_piper, assets_gen  # noqa: E402

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
3 short (1-4 word) keyword/phrase items, not full sentences."""


def build_script_prompt(channel: dict, topic: dict) -> str:
    beats = channel["shotGrammar"]
    beat_desc = "\n".join(
        f'- beat "{b["beat"]}" (primitive: {b["primitive"]})' for b in beats
    )
    schema_fields = ", ".join(f'"{b["beat"]}"' for b in beats)
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

Return JSON with this exact shape (keys: {schema_fields}):
{{
  "hook": {{"text": "...", "emphasisWord": "onewordfromtext"}},
  "concept_card": {{"text": "short headline", "traits": ["kw1", "kw2", "kw3"]}},
  "bridge": {{"text": "..."}},
  "example": {{"text": "short caption for a b-roll still"}},
  "explanation": {{"text": "..."}},
  "mechanism": {{"text": "short headline", "traits": ["kw1", "kw2", "kw3"]}},
  "conclusion": {{"text": "actionable one-line takeaway"}}
}}"""


def generate_script(channel: dict, topic: dict) -> dict:
    prompt = build_script_prompt(channel, topic)
    return nim_client.generate_json(SCRIPT_SYSTEM_PROMPT, prompt)


def resolve_accent(beat_cfg: dict) -> str:
    return beat_cfg["accent"]


def synthesize_music_bed(out_path: Path, duration_s: float) -> Path:
    """PLACEHOLDER music bed: a soft synthesized pad, NOT a sourced trending
    or royalty-free-library track. Real music sourcing per the Copyright
    Risk Flag in research/channels/mind-mosaic-topics-voice-music.md is an
    explicit operator decision, not resolved by this pipeline. This exists
    only so the audio-ducking system has something real to duck under for
    verification purposes."""
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

    print("[3/5] Synthesizing voiceover (Piper TTS) + resolving assets...")
    voice_model = ROOT / ".voices" / "en_US-libritts_r-medium.onnx"
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
        duration_s = tts_piper.synthesize(text, voice_model, wav_abs, speaker_id=0)
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

        segments.append(seg)
        print(f"      [{beat}] {duration_s:.2f}s -> {duration_frames}f  \"{text[:60]}\"")

    print("[4/5] Copying SFX + generating placeholder music bed...")
    used_sfx = {seg["cutSfx"].split("/")[-1] for seg in segments}
    for name in used_sfx:
        src = sfx_dir / name
        if not src.exists():
            raise RuntimeError(f"Missing vendored SFX file: {src}")
        dst = public_dir / "sfx" / name
        dst.write_bytes(src.read_bytes())

    total_duration_s = sum(s["durationInFrames"] for s in segments) / FPS
    music_rel = "audio/music_bed.wav"
    synthesize_music_bed(public_dir / music_rel, total_duration_s)

    tokens = {
        "background": channel["visualTokens"]["background"],
        "moodAccents": channel["visualTokens"]["moodAccents"],
        "captionEmphasis": channel["visualTokens"]["captionEmphasis"],
        "captionDefault": channel["visualTokens"]["captionDefault"],
        "fontStack": channel["typography"]["captionFallbackFontStack"],
    }

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
