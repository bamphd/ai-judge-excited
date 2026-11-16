"""ai-excited-01 entry: hand the judge one image.

The image lives beside this file as entry.png (JPEG bytes under the
entry.png name, which the gate tells apart by its magic bytes). The
program copies those exact bytes to /output/entry.png.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "entry.png"
if not SRC.is_file():
    print(f"error: source image not found: {SRC}", file=sys.stderr)
    raise SystemExit(1)

OUT_DIR.mkdir(parents=True, exist_ok=True)
dst = OUT_DIR / "entry.png"
shutil.copyfile(SRC, dst)
if dst.stat().st_size != SRC.stat().st_size:
    print(
        f"error: copied size mismatch: {dst} is {dst.stat().st_size} bytes, "
        f"expected {SRC.stat().st_size}",
        file=sys.stderr,
    )
    raise SystemExit(1)
