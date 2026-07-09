"""Piper TTS wrapper. Self-hostable, CPU-only, no cloud dependency --
per each channel's voice-provider research doc. Voice model files are
pre-downloaded (see .voices/) so rendering itself makes no remote calls,
matching the "asset resolution: local caching, no remote hits during
render" requirement.
"""
import subprocess
import wave
from pathlib import Path


def synthesize(text: str, model_path: Path, out_wav: Path, speaker_id: int | None = None) -> float:
    """Runs Piper CLI, returns duration in seconds of the produced wav."""
    out_wav.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["python", "-m", "piper", "-m", str(model_path), "-f", str(out_wav)]
    if speaker_id is not None:
        cmd += ["-s", str(speaker_id)]
    proc = subprocess.run(cmd, input=text, capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        raise RuntimeError(f"piper synthesis failed: {proc.stderr[-800:]}")
    with wave.open(str(out_wav), "rb") as w:
        frames = w.getnframes()
        rate = w.getframerate()
        return frames / float(rate)
