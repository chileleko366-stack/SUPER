"""Procedural placeholder-image generation for KenBurnsCard beats.

Real stock-photo/b-roll sourcing (e.g. a licensed image API) is not wired
in this pilot -- that is a real gap, documented here rather than silently
faking a sourcing pipeline that doesn't exist. These generated images are
single-subject, low-clutter abstract gradient cards, matching the moodboard's
observed b-roll density (see research/visual-reference/mind-mosaic.md,
Spacing Tokens: "single-subject, uncluttered frames").
"""
import hashlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


def _hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def generate_broll_card(seed_text: str, accent_hex: str, base_hex: str, out_path: Path,
                         size: tuple[int, int] = (1080, 1920)) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    base = _hex_to_rgb(base_hex)
    accent = _hex_to_rgb(accent_hex)

    img = Image.new("RGB", size, base)
    draw = ImageDraw.Draw(img)

    # Deterministic-but-varied radial blob position from the segment text,
    # so different beats produce visibly different (not random-looking)
    # single-subject compositions.
    seed = int(hashlib.sha256(seed_text.encode()).hexdigest(), 16)
    cx = size[0] * (0.3 + 0.4 * ((seed % 100) / 100))
    cy = size[1] * (0.3 + 0.4 * (((seed // 100) % 100) / 100))
    radius = min(size) * 0.32

    bbox = [cx - radius, cy - radius, cx + radius, cy + radius]
    draw.ellipse(bbox, fill=accent)

    img = img.filter(ImageFilter.GaussianBlur(radius=90))
    img.save(out_path, format="PNG")
    return out_path
