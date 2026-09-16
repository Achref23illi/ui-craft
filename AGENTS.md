# ui-craft for any coding agent

This repository is a skill for designing and reviewing mobile UI. Claude Code loads
`SKILL.md` automatically; other agents (Codex, Cursor, Gemini CLI, Windsurf, Aider…)
should read `SKILL.md` before any mobile UI work and follow its "Start here" section.

The short version:

1. **References first.** `python3 scripts/refs.py "<pattern>"` lists the reference
   contact sheets to open (one image, six real screens) and the matching notes. Open
   two or three before designing (three at most for a fast review). `--list` shows
   the pattern names.
2. **Rules as numbers.** Apply the rules and measurements in `SKILL.md`. When sources
   disagree: the project's own tokens, then the rules, then the recipes, then the
   per-app notes.
3. **Lessons.** Read "Lessons at a glance" in `SKILL.md`; `refs/lessons.md` has the
   details with screenshots.
4. **Verify on a render.** Screenshot the running app, build a contact sheet with
   `python3 scripts/sheet.py <folder>` and read it; measure on the original
   screenshots with `python3 scripts/measure.py <shot.png>` (`--col`/`--row` in pt);
   run the checklist; report at most ten findings as a table (screen · rule · problem
   with measurement · fix with number).

Setup for each agent, a hand-run fast review and troubleshooting are in `README.md`.
`python3 scripts/doctor.py` checks the install (`--refs` also checks the reference index).
