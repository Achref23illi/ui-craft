# ui-craft — an agent skill for mobile UI that looks like a real app

**By [Achref Arabi](https://github.com/Achref23illi).**

A skill for Claude Code (and any agent that reads `SKILL.md`) built from a study of
44 shipped iOS apps — Spotify, Airbnb, Instagram, TikTok, Apple Music, Apple TV,
Netflix, VSCO, Halide, Denim, Photoshop, Riverside, Moises, Playground, Revolut,
Linear, Notion, ChatGPT, Claude, Uber and more — 2,600 screens read for how they
spend space, how few things they show, and how each element earns its place.

What you get:

- **`SKILL.md`** — the rules with the numbers behind them, a table of reusable
  measurements for a 390-pt screen, nine screen recipes (home with rails, media
  detail, player, editor, publish form, settings, comments, paywall, onboarding),
  a done-checklist and the anti-patterns that separate cheap screens from real ones.
- **`refs/notes.md`** — per-app observations with measurements, app by app.
- **`refs/ux-research.md`** — sourced findings: choices per screen, icon labels, tap targets, typefaces, icon systems.
- **`refs/lessons.md`** — what changed when the research met real screens.
- **`refs/patterns.md`** — pattern → which apps and screens to look at.
- **`refs/INDEX.md`** — the 44 apps and what each is good for.

## Install

```bash
git clone https://github.com/Achref23illi/ui-craft ~/.claude/skills/ui-craft
```

Claude Code picks it up on the next session. Invoke with `/ui-craft` or just
work on a mobile screen; the description triggers it.

## Free for everyone

Made for the community by **Achref Arabi** (2026). Use it, fork it, change it and
ship with it, in personal or commercial work. Issues and pull requests are welcome.

MIT licensed.
