"""Kokoro-82M TTS wrapper (Apache-2.0, github.com/hexgrad/kokoro). Used by
channels whose research doc recommended Kokoro over Piper for licensing
reasons (e.g. Penny Blueprint -- Piper's actively-maintained engine repo is
GPL-3.0, Coqui XTTS v2 is non-commercial-licensed; Kokoro's weights are
Apache-2.0). Requires the `kokoro` pip package plus the `espeak-ng` system
package (used for English out-of-dictionary fallback) -- both installed as
explicit CI steps, not assumed present.
"""
import wave
from pathlib import Path

import numpy as np


def synthesize(text: str, voice: str, out_wav: Path, lang_code: str = "a") -> float:
    """Runs Kokoro inference in-process (unlike Piper's CLI wrapper, kokoro
    is used as a Python library), returns duration in seconds."""
    from kokoro import KPipeline  # imported lazily: heavy (torch) import,
    # and channels that only use Piper shouldn't pay this cost.

    out_wav.parent.mkdir(parents=True, exist_ok=True)
    pipeline = KPipeline(lang_code=lang_code)
    generator = pipeline(text, voice=voice)

    chunks = [audio for _, _, audio in generator]
    if not chunks:
        raise RuntimeError(f"Kokoro produced no audio for voice={voice!r}")
    full_audio = np.concatenate(chunks)

    sample_rate = 24000
    pcm16 = (np.clip(full_audio, -1.0, 1.0) * 32767).astype(np.int16)
    with wave.open(str(out_wav), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        w.writeframes(pcm16.tobytes())

    return len(full_audio) / float(sample_rate)
