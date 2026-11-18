"""Crop a single-frame image in source pixels without resampling its colors."""

import argparse
from io import BytesIO
import json
from pathlib import Path

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--box", nargs=4, type=int, required=True, metavar=("L", "T", "R", "B"))
    parser.add_argument("--scale", type=int, choices=range(1, 17), default=1)
    args = parser.parse_args()
    if args.output.suffix.lower() != ".png":
        parser.error("output must end in .png")
    l, t, r, b = args.box
    size = ((r - l) * args.scale, (b - t) * args.scale)
    data = BytesIO()
    try:
        with Image.open(args.source) as source:
            w, h = source.size
            if getattr(source, "n_frames", 1) != 1:
                parser.error("provide a single-frame PNG, JPEG, or other still image")
            if not (0 <= l < r <= w and 0 <= t < b <= h):
                parser.error(f"box must lie inside {w}x{h} source pixels")
            if size[0] * size[1] > 16_000_000:
                parser.error("output exceeds 16 million pixels; reduce the box or scale")
            result = source.crop((l, t, r, b))
            if result.mode in {"CMYK", "YCbCr"}:
                result = result.convert("RGB")
                result.info.pop("icc_profile", None)
            result.resize(size, Image.Resampling.NEAREST).save(data, format="PNG")
        with args.output.open("xb") as stream:
            stream.write(data.getbuffer())
    except (OSError, ValueError, Image.DecompressionBombError) as error:
        parser.exit(1, f"{error}\n")
    print(json.dumps({"source_size": [w, h], "box": args.box, "scale": args.scale,
                      "output_size": size, "output": str(args.output)}, ensure_ascii=True))


if __name__ == "__main__":
    main()
