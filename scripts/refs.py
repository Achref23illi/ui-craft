#!/usr/bin/env python3
"""Find the references to look at before designing or reviewing a screen.

  python3 scripts/refs.py "video editor"
  python3 scripts/refs.py settings profile --max 4
  python3 scripts/refs.py --list

  python3 scripts/refs.py --screen "Wise 03·2"      the screen file behind a citation, to measure it

Prints, best first:
  1. local contact sheets (refs/sheets/*.jpg) for the apps that do the pattern well,
     if a local library is present (read each one: six screens per image);
  2. the matching lines of refs/patterns.md, the closest measured recipes of
     refs/recipes.md and the notes of refs/notes.md;
  3. published images that apply (refs/lessons-img/, examples/before-after/).

No third-party dependencies.
"""
import argparse
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SYNONYMS = {
    "home": ["root", "rails", "feed", "library"],
    "library": ["rails", "grid", "home"],
    "feed": ["feed", "stories", "video feed", "post"],
    "detail": ["detail", "media"],
    "player": ["player", "now playing", "mini player"],
    "editor": ["editor", "tool", "timeline", "panel"],
    "camera": ["camera", "tool", "capture"],
    "settings": ["rows", "grouped", "forms", "settings", "profile"],
    "profile": ["rows", "grouped", "settings", "profile"],
    "form": ["forms", "fields", "segmented", "publish"],
    "publish": ["forms", "publish", "share"],
    "onboarding": ["onboarding", "welcome", "permission"],
    "paywall": ["paywall", "plan"],
    "search": ["search", "empty"],
    "empty": ["empty", "no results"],
    "sheet": ["sheet", "menu", "dialog"],
    "menu": ["menu", "sheet", "context"],
    "comments": ["comments", "replies", "messaging"],
    "chat": ["chat", "composer", "messaging"],
    "tab": ["tab bar", "tabs"],
    "create": ["create", "record", "capture", "source", "invite"],
    "record": ["record", "recording", "studio", "capture"],
    "import": ["import", "source", "picker"],
    "invite": ["invite", "share", "role"],
    "account": ["settings", "profile", "grouped"],
    "toast": ["toast", "confirmation"],
    "list": ["rows", "lists"],
    "money": ["money", "balance", "amount", "transaction", "send"],
    "bank": ["money", "balance", "transaction"],
    "wallet": ["money", "balance", "crypto"],
    "fintech": ["money", "balance", "amount", "chart"],
    "send": ["amount", "send", "money", "keypad"],
    "payment": ["checkout", "money", "amount", "pay"],
    "transfer": ["amount", "send", "money"],
    "chart": ["charts", "stats", "dashboard", "graph"],
    "stats": ["charts", "stats", "progress", "dashboard"],
    "dashboard": ["charts", "stats", "dashboard", "home"],
    "shop": ["commerce", "product", "cart", "checkout", "grid"],
    "store": ["commerce", "product", "cart"],
    "product": ["commerce", "product", "grid"],
    "cart": ["cart", "checkout", "commerce"],
    "checkout": ["checkout", "cart", "commerce", "payment"],
    "order": ["checkout", "cart", "tracking"],
    "map": ["maps", "location", "place", "route"],
    "location": ["maps", "location", "place"],
    "route": ["maps", "route", "navigation"],
    "calendar": ["calendar", "scheduling", "date", "timeline"],
    "schedule": ["calendar", "scheduling", "timeline"],
    "event": ["event", "calendar", "ticket"],
    "task": ["task", "list", "rows", "calendar"],
    "todo": ["task", "list", "rows"],
    "login": ["sign", "account", "security", "passcode"],
    "signin": ["sign", "account", "security"],
    "signup": ["sign", "onboarding", "account"],
    "auth": ["sign", "account", "security", "passcode", "code"],
    "otp": ["code", "passcode", "sign"],
    "workout": ["workouts", "timers", "live", "session"],
    "fitness": ["workouts", "timers", "stats"],
    "timer": ["timers", "live", "session"],
    "ai": ["assistants", "voice", "chat", "composer"],
    "assistant": ["assistants", "voice", "chat"],
    "voice": ["voice", "assistants", "record"],
    "article": ["reading", "articles", "news"],
    "news": ["reading", "articles", "news", "feed"],
    "reader": ["reading", "articles", "book"],
    "book": ["reading", "book"],
    "notification": ["notifications", "inbox"],
    "inbox": ["inbox", "notifications", "mail"],
    "mail": ["inbox", "mail", "rows"],
    "loading": ["loading", "skeletons", "errors"],
    "skeleton": ["loading", "skeletons"],
    "error": ["errors", "loading", "empty"],
    "delete": ["destructive", "confirmation", "dialog"],
    "confirm": ["confirmation", "destructive", "dialog", "toast"],
    "dialog": ["dialogs", "confirmation", "destructive", "sheet"],
    "filter": ["filters", "sort", "segmented"],
    "sort": ["filters", "sort"],
    "header": ["headers", "navigation", "title"],
    "navigation": ["headers", "navigation", "tab bar"],
    "weather": ["charts", "stats", "dashboard"],
    "dating": ["cards", "swipe", "profile"],
    "recipe": ["reading", "grid", "timers"],
}

LESSON_IMAGES = [
    (("motion", "transition", "animation", "animate", "tab", "search"), "refs/lessons-img/01-motion-search-rise.jpg"),
    (("glow", "gradient", "grain", "brand", "background", "home", "library"), "refs/lessons-img/02-glow-grain.jpg"),
    (("button", "buttons", "cta", "compact", "publish", "form"), "refs/lessons-img/03-buttons-compact.jpg"),
    (("status", "sync", "icon", "icons", "tag", "badge", "settings", "list", "rows"), "refs/lessons-img/04-status-icons.jpg"),
    (("editor", "panel", "tool", "text"), "refs/lessons-img/05-tool-panel.jpg"),
    (("dark", "night", "theme", "community", "social", "tab", "second"), "refs/lessons-img/06-night-stage.jpg"),
    (("reaction", "reactions", "emoji", "like", "feed", "social"), "refs/lessons-img/07-reactions-fire.jpg"),
]

EXAMPLES = [
    (("home", "library", "rails", "grid"), "examples/before-after/01-library.jpg"),
    (("create", "source", "import", "capture"), "examples/before-after/02-create.jpg"),
    (("detail", "media", "video"), "examples/before-after/03-media.jpg"),
    (("editor", "timeline", "tool"), "examples/before-after/04-editor.jpg"),
    (("publish", "form", "share", "destination"), "examples/before-after/05-publish.jpg"),
    (("social", "feed", "community", "dark", "night"), "examples/before-after/06-social-home.jpg"),
]


def words(text):
    return re.findall(r"[a-zà-ÿ]+", text.lower())


def stem(w):
    return w[:5]


def expand(query):
    """The words typed, and the words their synonyms add (kept apart: typed words weigh more)."""
    typed = set(words(" ".join(query)))
    extra = set()
    for w in typed:
        for key, more in SYNONYMS.items():
            if w.startswith(key) or key.startswith(w):
                extra.update(words(" ".join(more)))
    return typed, extra - typed


def norm(name):
    """Compare app names without punctuation: '(Not Boring) Camera' == 'Not Boring Camera'."""
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def sheet_index():
    idx = []
    for path in glob.glob(os.path.join(ROOT, "refs", "sheets", "*.jpg")):
        m = re.match(r"^(\d{3})-(.+)-(\d{2})\.jpg$", os.path.basename(path))
        if m:
            idx.append((norm(m.group(2)), int(m.group(3)), path))
    return idx


def app_matches(app, name):
    a = norm(app)
    return bool(a) and (name.startswith(a) or a in name)


def find_sheet(sheets, app, n):
    """The sheet for 'App NN': an exact name first ('Uber' is not 'Uber Eats'), then the closest partial match."""
    hits = [(name, path) for name, num, path in sheets if num == n and app_matches(app, name)]
    if not hits:
        return None
    exact = [p for name, p in hits if name == norm(app)]
    return exact[0] if exact else min(hits, key=lambda h: len(h[0]))[1]


def refs_in_line(line):
    """'Spotify 01–02, Apple Music 01, 03; TIDAL 01' -> [('Spotify',1),('Spotify',2),('Apple Music',1),…]"""
    body = line.rsplit(": ", 1)[1] if ": " in line else line  # ratios like 16:9 stay in the description
    body = re.sub(r"\([^)]*\)", " ", body)  # parenthetical notes hold numbers that are not sheets
    out, app = [], None
    for m in re.finditer(r"(?:([A-Za-z(][\w.'&+() ]*?)\s+)?(?<![\d/.])(\d{2})(?![\d/])(?:\s*[–-]\s*(\d{2}))?", body):
        if m.group(1):
            app = m.group(1).strip()
        if not app:
            continue
        a = int(m.group(2))
        b = int(m.group(3)) if m.group(3) else a
        out += [(app, n) for n in range(a, min(b, a + 5) + 1)]
    return out


def screen_file(ref):
    """'Wise 03·2' (or 'Wise 03.2') -> the screen file and its source, from refs/screens-index.csv."""
    import csv
    m = re.match(r"^\s*(.+?)\s+(\d{2})\s*[·.\-/ ]\s*(\d)\s*$", ref)
    path = os.path.join(ROOT, "refs", "screens-index.csv")
    if not m or not os.path.exists(path):
        return None
    app, sheet, pos = m.group(1), int(m.group(2)), int(m.group(3))
    n = (sheet - 1) * 6 + pos
    rows = [r for r in csv.DictReader(open(path, encoding="utf-8")) if int(r["n"]) == n and app_matches(app, norm(r["app"]))]
    if not rows:
        return None
    exact = [r for r in rows if norm(r["app"]) == norm(app)]
    return (exact or sorted(rows, key=lambda r: len(r["app"])))[0]


def recipe_hits(typed_s, extra_s, limit=3):
    path = os.path.join(ROOT, "refs", "recipes.md")
    if not os.path.exists(path):
        return []
    sections = open(path, encoding="utf-8").read().split("\n## ")[1:]
    best = []
    for sec in sections:
        head, _, body = sec.partition("\n")
        if head.startswith("How to use"):
            continue
        hw = {stem(w) for w in words(head)}
        for line in body.splitlines():
            if line.startswith("- **"):
                label = line.split("**:", 1)[0]
                lw = {stem(w) for w in words(label)}
                score = 3 * len(typed_s & hw) + 2 * len(typed_s & lw) + len(extra_s & (hw | lw)) + len(typed_s & {stem(w) for w in words(line)}) / 2
                if score >= 2:
                    best.append((score, head, line))
    best.sort(key=lambda b: -b[0])
    return best[:limit]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="*", help="pattern words, e.g. 'video editor', 'settings', 'paywall'")
    ap.add_argument("--max", type=int, default=6, help="max sheets to list")
    ap.add_argument("--list", action="store_true", help="list pattern headings")
    ap.add_argument("--screen", help="print the screen file behind a citation like 'Wise 03·2', to measure it")
    args = ap.parse_args()

    if args.screen:
        row = screen_file(args.screen)
        if not row:
            raise SystemExit(f"no screen found for {args.screen!r} (use 'App NN·k', k = 1–6 left to right, top to bottom)")
        print(os.path.join("refs", "screens", row["app_id"], row["file"]))
        if row.get("label"):
            print(f"label: {row['label']}")
        if row.get("refero_url"):
            print(f"source: {row['refero_url']}")
        print(f"measure: python3 scripts/measure.py refs/screens/{row['app_id']}/{row['file']}")
        return

    patterns = open(os.path.join(ROOT, "refs", "patterns.md"), encoding="utf-8").read().splitlines()
    if args.list or not args.query:
        for line in patterns:
            if line.startswith("## "):
                print(line[3:])
        return

    typed, extra = expand(args.query)
    typed_s, extra_s = {stem(w) for w in typed}, {stem(w) for w in extra}
    heading, scored = "", []
    for line in patterns:
        if line.startswith("## "):
            heading = line[3:]
            continue
        if not line.startswith("- "):
            continue
        head = {stem(w) for w in words(heading + " " + line.rsplit(": ", 1)[0])}
        body = {stem(w) for w in words(line)}
        score = 3 * len(typed_s & head) + len(extra_s & head) + len(typed_s & body)
        if score >= 2:
            scored.append((score, heading, line))
    scored.sort(key=lambda s: -s[0])
    terms = typed | extra

    sheets = sheet_index()
    print(f"# references for: {' '.join(args.query)}\n")
    listed, seen = 0, set()
    if sheets:
        print("## local contact sheets (Read each: six screens of one app; look for the ones that match)")
        wanted = []
        for _, _, line in scored:
            for app, n in refs_in_line(line):
                path = find_sheet(sheets, app, n)
                if path and path not in seen:
                    wanted.append((norm(app), path))
                    seen.add(path)
        # one sheet per app first, then the rest, so a short list shows several apps
        first, rest, apps_seen = [], [], set()
        for app, path in wanted:
            (rest if app in apps_seen else first).append(path)
            apps_seen.add(app)
        for path in (first + rest)[: args.max]:
            print(os.path.relpath(path, ROOT))
            listed += 1
        if not listed:
            print("(no sheet matched these words: try `--list` for pattern names, or other words)")
        print()
    else:
        print("## no local screen library")
        print("(refs/sheets/ is empty. Work from the patterns and notes below, and read at most two of")
        print(" the published images listed at the end. To restore the library: git checkout -- refs/sheets)\n")

    print("## patterns")
    for _, heading, line in scored[:6]:
        print(f"[{heading}] {line[2:]}")

    recipes = recipe_hits(typed_s, extra_s)
    if recipes:
        print("\n## measured recipes (refs/recipes.md; `--screen \"App NN·k\"` gives the file to measure)")
        for _, head, line in recipes:
            print(f"[{head}] {line[2:]}")

    apps = []
    for _, _, line in scored[:3]:
        for app, _ in refs_in_line(line):
            if norm(app) not in [norm(x) for x in apps]:
                apps.append(app)
    notes_path = os.path.join(ROOT, "refs", "notes.md")
    if apps and os.path.exists(notes_path):
        sections = open(notes_path, encoding="utf-8").read().split("\n## ")
        hits = [sec for sec in sections if any(norm(sec.split("\n", 1)[0]).startswith(norm(a)) for a in apps[:3])]
        if hits:
            print("\n## notes (measurements observed in those apps; the rules in SKILL.md win where they differ)")
            for sec in hits[:3]:
                lines = sec.strip().splitlines()
                text, total = [], 0
                for l in lines:
                    if total + len(l) > 1400:
                        text.append("  (more in refs/notes.md)")
                        break
                    text.append(l)
                    total += len(l)
                print("## " + "\n".join(text))

    local = [p for p in glob.glob(os.path.join(ROOT, "refs", "user-refs", "*")) if any(t in os.path.basename(p).lower() for t in typed)]
    if local:
        print("\n## your own local references (refs/user-refs/)")
        for p in local[:6]:
            print(os.path.relpath(p, ROOT))

    q = typed | terms
    imgs = [p for keys, p in LESSON_IMAGES + EXAMPLES if q & set(keys) and os.path.exists(os.path.join(ROOT, p))]
    if imgs:
        print("\n## published images (one real app before/after and the lessons behind it;")
        print("   take the principle, not the layout, colours or branding)")
        for p in imgs[:5]:
            print(p)


if __name__ == "__main__":
    try:
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # quiet when piped into head
    except (AttributeError, ValueError):
        pass
    main()
