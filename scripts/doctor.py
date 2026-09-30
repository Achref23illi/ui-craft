#!/usr/bin/env python3
"""Check a ui-craft install and say which mode it runs in.

  python3 scripts/doctor.py            install check
  python3 scripts/doctor.py --refs     also check that every sheet named in refs/patterns.md and
                                       every screen cited in refs/recipes.md exists
"""
import glob
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def count(pattern):
    return len(glob.glob(os.path.join(ROOT, pattern), recursive=True))


def main():
    ok = True
    print(f"ui-craft at {ROOT}\n")
    for f in ["SKILL.md", "refs/patterns.md", "refs/recipes.md", "refs/notes.md", "refs/lessons.md", "refs/ux-research.md", "refs/screens-index.csv"]:
        present = os.path.exists(os.path.join(ROOT, f))
        ok &= present
        print(f"  {'ok ' if present else 'MISSING'}  {f}")

    print(f"\n  python {sys.version.split()[0]}")
    try:
        import PIL  # noqa: F401

        print("  ok   Pillow (scripts/sheet.py can build contact sheets)")
    except ImportError:
        print("  --   Pillow missing: python3 -m pip install pillow  (only needed for scripts/sheet.py)")

    sheets = count("refs/sheets/*.jpg")
    lessons = count("refs/lessons-img/*.jpg")
    examples = count("examples/before-after/*.jpg")
    screens = count("refs/screens/*/*.jpg")
    apps = len(glob.glob(os.path.join(ROOT, "refs", "screens", "*")))
    print(f"\n  contact sheets in refs/sheets/   {sheets}")
    print(f"  screens in refs/screens/         {screens} ({apps} apps)")
    print(f"  lesson screenshots               {lessons}")
    print(f"  before/after examples            {examples}")

    tools = [t for t in ["xcrun", "adb", "npx"] if shutil.which(t)]
    print(f"  screenshot tools on PATH         {', '.join(tools) if tools else 'none found'}")

    print("\nMode:")
    if sheets:
        print("  FULL — reference sheets are local. Start every design or review with")
        print('  python3 scripts/refs.py "<pattern>" and Read two or three of the sheets it lists.')
    else:
        print("  RULES — no local screen library. The skill works from the rules, notes, lessons")
        print("  and published examples. To add references, see README › Build a reference library.")
    if "--refs" in sys.argv and sheets:
        sys.path.insert(0, os.path.join(ROOT, "scripts"))
        import re  # noqa: E402

        from refs import find_sheet, refs_in_line, screen_file, sheet_index  # noqa: E402

        idx = sheet_index()
        missing = []
        for line in open(os.path.join(ROOT, "refs", "patterns.md"), encoding="utf-8"):
            if not line.startswith("- "):
                continue
            for app, n in refs_in_line(line):
                if not find_sheet(idx, app, n):
                    missing.append(f"{app} {n:02d}  ←  {line.strip()[:70]}")
        print(f"\nPattern references: {len(missing)} unresolved")
        for m in missing:
            print("  " + m)
        ok &= not missing

        recipes = os.path.join(ROOT, "refs", "recipes.md")
        if os.path.exists(recipes):
            bad, total = [], 0
            for cite in re.findall(r"\(([^()]*\d{2}·\d[^()]*)\)", open(recipes, encoding="utf-8").read()):
                app = None
                for part in re.split(r"[,;]\s*", cite):
                    m = re.match(r"^(.*?)\s*(\d{2})·(\d)$", part.strip())
                    if not m:
                        continue
                    app = m.group(1).strip() or app
                    total += 1
                    if not app or not screen_file(f"{app} {m.group(2)}·{m.group(3)}"):
                        bad.append(f"{app} {m.group(2)}·{m.group(3)}")
            print(f"Recipe citations: {total} checked, {len(bad)} unresolved")
            for b in bad[:20]:
                print("  " + b)
            ok &= not bad
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
