# ui-craft — an agent skill for mobile UI that looks like a real app

**By [Achref Arabi](https://github.com/Achref23illi).**

A skill for Claude Code (and any agent that reads `SKILL.md`) built from a study of
44 shipped iOS apps — Spotify, Airbnb, Instagram, TikTok, Apple Music, Apple TV,
Netflix, VSCO, Halide, Denim, Photoshop, Riverside, Moises, Playground, Revolut,
Linear, Notion, ChatGPT, Claude, Uber and more — 2,600 screens read for how they
spend space, how few things they show, and how each element earns its place.

What you get:

- **`SKILL.md`** — ten rules with the numbers behind them, a table of reusable
  measurements for a 390-pt screen, nine screen recipes (home with rails, media
  detail, player, editor, publish form, settings, comments, paywall, onboarding),
  a done-checklist and the anti-patterns that separate cheap screens from real ones.
- **`refs/notes.md`** — per-app observations with measurements, app by app.
- **`refs/patterns.md`** — pattern → which apps and sheets to look at.
- **`refs/INDEX.md`** — the 44 apps and what each is good for.
- **`refs/dl.sh`, `refs/sheets.py`** — the pipeline that builds a local contact-sheet
  library so the agent can *look* at the real thing before drawing.

## Install

```bash
git clone https://github.com/Achref23illi/ui-craft ~/.claude/skills/ui-craft
```

Claude Code picks it up on the next session. Invoke with `/ui-craft` or just
work on a mobile screen; the description triggers it.

## Building the screenshot library (optional, local only)

The rules and notes work on their own. The contact sheets make them concrete.
Screens come from [Refero](https://refero.design) and are the app makers'
copyrighted UI, so they are **not** in this repo; build them locally with your
own Refero account:

1. On a Refero app page, collect the screenshot ids (see the comment at the top
   of `refs/dl.sh` for the expected `appId:id,id,…;` format).
2. `refs/dl.sh ids.txt` downloads thumbnails into `refs/screens/<appId>/`.
3. `python3 refs/sheets.py` builds six-up contact sheets into `refs/sheets/`
   (needs Pillow). `refs/apps.json` maps ids to app names.

## Credits

Study, notes, rules and pipeline by **Achref Arabi** (2026). Screens referenced
belong to their respective apps; Refero is the catalogue they were studied from.

MIT licensed.
