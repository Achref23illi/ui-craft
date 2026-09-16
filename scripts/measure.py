#!/usr/bin/env python3
"""Measure a screenshot in points, so a review can quote real numbers.

  python3 scripts/measure.py shot.png                 size, scale, width in pt, side gutters
  python3 scripts/measure.py shot.png --col 60        elements met going down the line x = 60 pt
  python3 scripts/measure.py shot.png --row 420       elements met going across the line y = 420 pt
  python3 scripts/measure.py shot.png --col 60 --from 100 --to 500

Each run prints spans as `start–end (size)` in points, and the gap before each one,
which is how you read paddings, gaps between sections, row heights and button
heights. Background is taken from the first pixel of the line; anything that differs
from it by more than --tol counts as content.

Scale: phones are shot at 3x (1170, 1179, 1206, 1284, 1290, 1320 px wide) or 2x
(750, 828). Override with --scale.

Requires Pillow (pip install pillow).
"""
import argparse
import sys

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("Pillow is missing: run  python3 -m pip install pillow")


def guess_scale(width):
    if width >= 1100:
        return 3
    if width >= 700:
        return 2
    return 1


def spans(values, bg, tol, min_px):
    out, start = [], None
    for i, v in enumerate(values):
        diff = max(abs(v[0] - bg[0]), abs(v[1] - bg[1]), abs(v[2] - bg[2]))
        if diff > tol and start is None:
            start = i
        elif diff <= tol and start is not None:
            if i - start >= min_px:
                out.append((start, i))
            start = None
    if start is not None and len(values) - start >= min_px:
        out.append((start, len(values)))
    return out


def fmt(pairs, scale, offset):
    lines, prev = [], None
    for a, b in pairs:
        s, e = (a + offset) / scale, (b + offset) / scale
        gap = f"   gap {s - prev:5.1f}" if prev is not None else ""
        lines.append(f"  {s:6.1f}–{e:6.1f}  ({e - s:5.1f}){gap}")
        prev = e
    return "\n".join(lines) if lines else "  (no content on this line)"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image")
    ap.add_argument("--col", type=float, help="x in points: walk down this vertical line")
    ap.add_argument("--row", type=float, help="y in points: walk across this horizontal line")
    ap.add_argument("--from", dest="start", type=float, default=0, help="start of the walk, pt")
    ap.add_argument("--to", dest="end", type=float, help="end of the walk, pt")
    ap.add_argument("--scale", type=float, help="pixels per point (default: guessed from width)")
    ap.add_argument("--tol", type=int, default=18, help="colour difference that counts as content (0–255)")
    ap.add_argument("--min", dest="min_pt", type=float, default=1.0, help="ignore spans thinner than this, pt")
    args = ap.parse_args()

    im = Image.open(args.image).convert("RGB")
    w, h = im.size
    scale = args.scale or guess_scale(w)
    px = im.load()
    min_px = max(1, int(args.min_pt * scale))
    print(f"{args.image}: {w}×{h} px · scale {scale:g}x · {w / scale:g}×{h / scale:g} pt")

    if args.col is None and args.row is None:
        # Side gutters: the most common left and right content edges over the screen's middle.
        lefts, rights = {}, {}
        for y in range(int(h * 0.12), int(h * 0.85), max(1, int(4 * scale))):
            row = [px[x, y] for x in range(w)]
            sp = spans(row, row[0], args.tol, min_px)
            if sp and sp[0][0] > 0 and sp[-1][1] < w:
                l, r = round(sp[0][0] / scale), round((w - sp[-1][1]) / scale)
                lefts[l] = lefts.get(l, 0) + 1
                rights[r] = rights.get(r, 0) + 1
        top = lambda d: ", ".join(f"{k} pt ×{v}" for k, v in sorted(d.items(), key=lambda kv: -kv[1])[:3])
        print(f"left content edges:  {top(lefts) or 'none'}")
        print(f"right content edges: {top(rights) or 'none'}")
        print("(the most frequent value is usually the gutter; full-bleed rows are skipped)")
        return

    if args.col is not None:
        x = min(w - 1, int(args.col * scale))
        y0 = int(args.start * scale)
        y1 = min(h, int(args.end * scale)) if args.end else h
        line = [px[x, y] for y in range(y0, y1)]
        print(f"down x = {args.col:g} pt, from {args.start:g} pt:")
        print(fmt(spans(line, line[0], args.tol, min_px), scale, y0))
    if args.row is not None:
        y = min(h - 1, int(args.row * scale))
        x0 = int(args.start * scale)
        x1 = min(w, int(args.end * scale)) if args.end else w
        line = [px[x, y] for x in range(x0, x1)]
        print(f"across y = {args.row:g} pt, from {args.start:g} pt:")
        print(fmt(spans(line, line[0], args.tol, min_px), scale, x0))


if __name__ == "__main__":
    main()
