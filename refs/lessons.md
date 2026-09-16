# Lessons from applying the research — VEDYX, September 2026

What changed when the sourced findings in `ux-research.md` met twelve real screens
and a round of founder feedback. Recorded so the next brief starts here, not at the
articles. By Achref Arabi.

## 1 · The tap budget works on browsing screens, not on tool screens

Counting choices in the first viewport cut the home, media, publish and feed screens
without losing anything: extras went into one ⋯, into the content (a tile is the
action), or into a gesture. On the editor the same count produced a toy. Real editors
(Splice, Instagram Reels, VN, CapCut and layout editors) show 5–6
labelled tools in one scrollable band plus undo · redo · save in the header, a play
and full-screen pair, a timecode ruler and a multi-track timeline. Users expect that
density; hiding it reads as "this app can't do it".

Rule that came out of it: **on a tool screen the budget applies per band, not per
screen.** One header band (back · undo · redo · primary), one transport band (play ·
full screen · timecode), one timeline, one tool band of 5–6 labelled tools that
scrolls and **changes with the selection** (nothing selected: Media · Music · Text ·
Split · Delete; clip selected: Trim · Speed · Rotate · Filters · Duplicate). Panels
for a tool rise as a sheet with Cancel · title · Apply and a Reset in the header.

## 2 · Buttons have three sizes and most screens need the small one

Feedback after the first pass: "the buttons are big, some screens don't need this".
The 48–56 pill is right only where the screen exists to make one decision: intro,
export, publish, paywall. Everywhere else it shouts.

- **Hero 48–52**: one per flow end (Commencer, Exporter, Publier, Essayer).
- **Compact 36–40 pill**, 13/600, hugging its text or half width: actions inside a
  browsing screen (Créer une Battle, Participer, Tout voir, Ouvrir).
- **Text 15/600** in the accent: tertiary (Réglages avancés, J'ai déjà un compte).
- **Discs**: 56 for source choices (Filmer · Importer), 44 for media actions (Lire ·
  Modifier · Publier), 32–36 for row pills.

If two screens in a row both end in a hero button, one of them is a step, not a
decision, and it should be compact.

## 3 · What survived unchanged

- Labels on every action icon, tab bar always labelled. No pushback, immediate clarity.
- Plus Jakarta Sans at 500/600/700/800 with JetBrains Mono only for readouts.
- Two levels of disclosure at most. When a third appeared in a draft (Publier ›
  Plus d'options › Visibilité › Qui peut voir) the option moved next to the destination
  tile instead.
- One filled primary per screen state. On the editor that is the header's Save.

## 4 · Things that looked right in the article and wrong on the phone

- "Remove the See all link, the title is tappable": true, but only once the title
  has a chevron. A bare title was not discovered in the simulator.
- "Long-press for the other reactions": fine on a feed, wrong on a Battle where the
  vote must be one obvious tap on the video itself.
- Hiding undo behind a shake on an editor: the reference editors all show undo and
  redo in the header. Undo is not a rare action in a tool; it is the safety net.
