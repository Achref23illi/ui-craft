#!/usr/bin/env python3
"""Contact sheets from any folder of screenshots: six screens per image.

Reading one sheet shows an agent six screens in a single image read, which is
what makes a review fast. Use it on your own app's screenshots before a review,
or on screenshots you have the right to keep, to build a local reference
library under refs/sheets/.

  python3 scripts/sheet.py shots/                      -> shots/sheets/sheet-01.jpg …
  python3 scripts/sheet.py shots/ --out review/ --cols 4 --rows 2
  python3 scripts/sheet.py refs/library/Linear --out refs/sheets --name 900-Linear

Requires Pillow (pip install pillow).
"""
import argparse
import glob
import os
import re
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # pragma: no cover
    sys.exit("Pillow is missing: run  python3 -m pip install pillow")

EXTS = (".png", ".jpg", ".jpeg", ".webp")


def natural(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="folders or image files")
    ap.add_argument("--out", help="output folder (default: <first folder>/sheets)")
    ap.add_argument("--name", default="sheet", help="file name prefix (default: sheet)")
    ap.add_argument("--cols", type=int, default=3)
    ap.add_argument("--rows", type=int, default=2)
    ap.add_argument("--width", type=int, default=300, help="width of each screen in the sheet, px")
    args = ap.parse_args()

    files = []
    for item in args.inputs:
        if os.path.isdir(item):
            files += [f for f in glob.glob(os.path.join(item, "*")) if f.lower().endswith(EXTS)]
        elif item.lower().endswith(EXTS):
            files.append(item)
    files = sorted(set(files), key=natural)
    if not files:
        sys.exit("No screenshots found.")

    out = args.out or os.path.join(args.inputs[0] if os.path.isdir(args.inputs[0]) else ".", "sheets")
    os.makedirs(out, exist_ok=True)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 15)
    except Exception:
        font = ImageFont.load_default()

    per = args.cols * args.rows
    first = Image.open(files[0])
    w = args.width
    h = int(first.height * w / first.width)
    pad, label = 10, 24
    written = []
    for n in range(0, len(files), per):
        sheet = Image.new("RGB", (args.cols * (w + pad) + pad, args.rows * (h + pad + label) + pad), (28, 28, 30))
        draw = ImageDraw.Draw(sheet)
        for k, path in enumerate(files[n : n + per]):
            try:
                im = Image.open(path).convert("RGB")
            except Exception:
                continue
            im = im.resize((w, int(im.height * w / im.width)))
            x = pad + (k % args.cols) * (w + pad)
            y = pad + (k // args.cols) * (h + pad + label)
            sheet.paste(im.crop((0, 0, w, min(h, im.height))), (x, y + label))
            draw.text((x, y + 4), os.path.basename(path)[:38], fill=(235, 235, 235), font=font)
        dest = os.path.join(out, f"{args.name}-{n // per + 1:02d}.jpg")
        sheet.save(dest, quality=82)
        written.append(dest)
    print(f"{len(files)} screens -> {len(written)} sheet(s)")
    for d in written:
        print(d)


if __name__ == "__main__":
    main()
