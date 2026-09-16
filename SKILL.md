---
name: ui-craft
description: How successful mobile apps are actually built — spacing, hierarchy, components and screen patterns distilled from 2,600 real iOS screens (44 apps). Use before designing or restyling any mobile screen, when reviewing a screen for "does this look like a real app", or when you need a reference for a specific pattern (player, editor, feed, sheet, paywall, empty state…).
---

# UI craft — what real apps do

By Achref Arabi · https://github.com/Achref23illi/ui-craft

A skill built from a study of 44 shipped iOS apps (Spotify, Airbnb, Instagram, TikTok,
Apple Music, Apple TV, Netflix, VSCO, Halide, Denim, Photoshop, Riverside, Moises,
Playground, Revolut, Linear, Notion, ChatGPT, Claude, Uber…). 2,602 screens were
studied; about 270 were read closely and annotated. The point of the skill is not a
style. It is the discipline these apps share: where they spend space and where they
don't, how few things they show, and how every element earns its place.

## How to use this skill

1. **Before designing a screen**, find its pattern in `refs/patterns.md`: it names the apps
   and screens that do it well. If a local screen library is present, open two or three of
   the listed contact sheets with Read (`refs/sheets/<id>-<App>-<nn>.jpg`, six screens
   each). Look at the real thing before drawing.
2. **Apply the rules below** as numbers, not vibes. If a screen violates one, it is the
   screen that changes, not the rule, unless the brand brief says otherwise.
3. **After building**, run the checklist at the end on a device screenshot.
4. Per-app observations live in `refs/notes.md`; the app index in `refs/INDEX.md`.

## The rules (with the numbers behind them)

1. **Content carries the screen; chrome is nearly invisible.** Artwork, video, photos and
   the user's words fill the frame. Headers are one title (15–17/600 centred, or 28–34/700
   left) and at most two 24-pt glyphs. No decorative bars, no dividers between sections;
   a title and 12 pt of air are the divider. (Spotify, Apple TV, VSCO, Sora)

2. **One primary action per screen state, pinned where the thumb is.** A full-width pill
   or 12–16 pt-radius button, 48–56 pt tall, at the bottom with 16 pt side gutters; the
   secondary is text or an outlined/grey pill under it. Never two filled buttons side by
   side except as a strict pair (Play · My List, Submit · Retake). (Airbnb, Revolut,
   Headspace, Netflix)

3. **Titles are close to their content and far from each other.** Section title 20–22/700
   with 12 pt to its rail; 24–28 pt between sections. Screen title 28–34/700 with 8–12 pt
   to the first control. Body 15–16 with a 1.4 line height, never wider than the gutter.
   (Apple Music, Spotify, Denim, Superlist)

4. **Rows are 44–56 pt and carry three things at most**: a leading visual (24 icon, 40
   avatar, 40–48 thumbnail), a title 15/500–600 with an optional 13 grey sub-line, and one
   trailing element (chevron, ⋯, value in grey, a 32–36 pt pill). Hairlines inset from the
   label, or none at all inside a card. Grouped screens put rows in white 12-pt cards on a
   grey ground; flat screens put them on white with hairlines. (Apple Music, Uber, Notion,
   Rewind, Opal)

5. **Rails and grids have one geometry per screen.** Rail tiles are square 112–160 pt or
   16:9 at 160–180 wide, 12–20 pt corners, 8 pt gaps, with a 13–14 label and a 12 grey
   meta line under; 3 to 3.5 visible plus a peek. Grids are 2 columns with 8 pt gaps for
   browsing, 3 columns with 2–4 pt gaps for archives. Posters are 2:3, video 16:9, social
   4:5. (Spotify, Apple TV, Denim, Pinterest, VSCO, Sora)

6. **Tool UIs live on black with the picture at its own ratio.** Editors, players and
   cameras: pure black stage, controls in bands below the picture (never over it except
   guides), tool labels 11 pt uppercase or 12–13 sentence case, the selected tool as a
   white or accent pill, the primary shutter/play as a 56–72 white disc, and one accent
   colour for "selected" or "has a value". Panels rise as sheets to about half the screen
   and never push the picture off. (Halide, Moises, Riverside, Denim, Photoshop, Analog)

7. **Colour is a signal, not paint.** One accent for the action (brand colour), one state
   colour at most (record red, live green), everything else ink and greys. Artwork
   supplies colour: dark players tint the top of the screen from the art. Brand colour
   on the tab bar's active item is enough branding. (Spotify, Netflix, Apple Music, Moises)

8. **Sheets are the app's second surface.** Anything transient rises as a sheet with a
   grabber, a 15–20/700 title, and an × disc: menus, pickers, filters, comments, share.
   Actions in a sheet are plain rows (icon 24 + label 15–16, ~56 pt), destructive last in
   red, "Cancel" as text. Alerts are centred dark/white cards with 15/600 title and two
   pills. (Spotify, Airbnb, Instagram, Threads, Riverside, Sora)

9. **Empty, loading and error states are one sentence and one move.** Centred, a 15–17
   /600 line plus a 13 grey line, optionally a 48–64 pt glyph or small illustration, and
   at most one button. No paragraphs, no decoration. Toasts are dark pills (top or bottom)
   with 14/600 text and an optional trailing action. (TikTok, Meta AI, Notion, Pinterest)

10. **Type does the hierarchy, not boxes.** Two weights (500–600 for labels, 700–800 for
    titles), grey for the second line, mono or tabular figures only for numbers and
    readouts. Tracked uppercase only on 11–12 pt tool labels and eyebrows, never on
    titles. Cards are for objects (a place, an item, a plan), not for grouping text.

11. **The tap budget: five choices in the first viewport, one of them primary.** Count
    every tappable control above the fold except the tab bar and back. Five or fewer
    (W3C cognitive pattern), one filled primary, the rest as content (tiles, rows) or
    behind one clearly named "more" at most two levels deep (NN/g progressive
    disclosure). Two similar buttons side by side is the fastest way to make a user
    hesitate. Sources and numbers in `refs/ux-research.md`. **Tool screens are the
    exception**: an editor counts per band, not per screen. Header (back · undo · redo ·
    primary), transport (play · full screen · timecode), timeline, and one scrollable
    band of 5–6 labelled tools that changes with the selection. Hiding tools there reads
    as "this app can't do it" (Splice, Instagram Reels, VN).

12. **Every action icon carries a visible label.** Only home, search, back and close
    stand alone; tab bars are always labelled; tool rows use icon + 10–11 pt label.
    Eleven studies over nineteen years and NN/g say the same thing: users match
    labels, not pictures, and rely on position for the rest. Tap targets 44 pt,
    48 pt at the screen edges, with padding between neighbours.

13. **Buttons are compact, and most screens need the smallest one.** The main action is
    44 pt (full width only where the screen exists to make one decision: intro, export,
    publish, paywall); dark buttons 40; everything else 36, hugging its label; chips 30
    with 13-pt labels; tertiary actions are 15/600 text in the accent. Discs: 56 for
    source choices, 44 for media actions. Anything under 44 pt keeps a 44-pt touch
    area with hitSlop. Two big buttons on consecutive screens means one of them is a
    step, not a decision. Lessons in `refs/lessons.md` (§2, §7).

14. **Motion follows the kind of screen, one animation per change.** Places you drill
    into slide in from the right and follow the back swipe; tasks you open and close
    (search, editor, sign-in, import, forms) rise from the bottom and swipe down; tabs
    cross-fade in ~180 ms. Never let a container fade its content while the navigator
    also animates. Tiles, cards and big round actions ease to ~96 % and spring back;
    sheets ease out; panels rise. No bounce on the tab bar. Reduce Motion turns it all
    off. (`refs/lessons.md` §5)

15. **Brand atmosphere comes from one glow, not from paint.** A vertical gradient of
    the brand colour under the status bar (~34 % → 0 over ~380 pt) with a light-and-dark
    film grain masked to the same fade. Rows over it are transparent, fields are
    frosted white, and a status-bar backdrop fades in once content scrolls under the
    clock. A diagonal gradient leaves a seam; a white-only grain vanishes on white.
    (`refs/lessons.md` §6)

16. **States are icons; problems are words.** Synced, local, uploading, cloud-only,
    downloaded, preview-only, export: one icon at the row's trailing edge, the word
    for the screen reader. Conflicts, unsupported files and offline waits keep a word
    next to the warning icon. Tool panels follow the same idea: formatting choices are
    icon segments and steppers, and a panel fits without scrolling. (§8, §9)

17. **A second space in the product is the same family on a different stage.** Same
    typeface, icons, radii, grain and components; a different ground (a night palette)
    and its second brand colour as the action. It gets its own tab bar (its sections as
    tabs, the way back to the main space as the first tab with the main logo),
    illustrated icons for its main places and a plain outline for the profile. Its
    logo reuses the main wordmark's letter construction. Implement it as a theme scope
    that components read, never as forked components. (§10)

18. **Own the expressive details, and give only one of them a big moment.** Reactions
    drawn in the brand gradients instead of system emoji, each with its own small tap
    motion; one reaction (fire) gets the full-post effect. (§11)

## Measurements to reuse (390-pt screen)

| Element | Value |
|---|---|
| Screen gutter | 16 (20 for editorial reading) |
| Header height | 44 + safe area; title 17/600 centred or 28–34/700 left |
| Section title → content | 12 · section → section 24–28 |
| List row | 44 (dense) · 52–56 (with sub-line) · 64 (with 48 thumb) |
| Card radius | 12 (rows, small cards) · 16–20 (artwork, sheets) · 24 (large sheets) |
| Button | main 44 · dark 40 · others 36 (hug label) · text 15/600 accent · 44-pt touch area via hitSlop |
| Disc | 56 source choice · 44 media action · 32–36 row pill |
| Editor | header 44 (back · undo · redo · primary) · transport row 44 · ruler 11 mono · video track 56–64 · audio track 40 · tool band 5–6 × (icon 22 + 11 label), scrolls, contextual |
| Pill chip | 30 tall, 12 padding, 13/600, grey fill · selected ink (or the space's accent) |
| Icon | 24 in headers and rows · 20 in tool rows · 28–32 in feed rails |
| Avatar | 24 inline · 32–36 in rows · 44–48 in lists · 64 stories · 96 profile |
| Rail tile | 112–160 square · 160–180 × 16:9 · gap 8 · corner 12–20 |
| Grid | 2 col gap 8 · 3 col gap 2–4 |
| Tab bar | 49 + safe area; icon 24 + label 10/500; or icons only |
| Mini player | 56 above the tab bar, art 40 |
| Sheet | grabber 36×4, title 15–20/700, × disc 28–32 |
| Toast | 40–48 pill, 14/600 |
| Tool label | 11 uppercase mono/sans with 0.06 em, or 12–13 sentence case |
| Big readout | 30–44/700 tabular (timecode, percentage, price) |
| Motion | push: slide from right + back swipe · task: rise from bottom, swipe down · tabs: cross-fade 180 ms · press: 96 % + spring (not on tabs) |
| Brand glow | vertical brand gradient 34 % → 15 % (30 %) → 6 % (60 %) → 0 over ~380 pt + light/dark grain masked; transparent rows, frosted fields, scroll backdrop |
| Tap budget | ≤ 5 choices in the first viewport (tab bar and back excluded) · 1 primary · "more" ≤ 2 levels |
| Typeface | one family with high x-height, open apertures, tabular figures, ≥ 5 weights; free with an Expo package (Plus Jakarta Sans, Figtree, DM Sans, Onest, Geist, Public Sans) or the system face; mono only for readouts |
| Icons | one SVG set on a 24 grid (Phosphor: outline inactive / fill active; or Lucide 2-px); labelled except home · search · back · close |

## Screen recipes

- **Home with rails**: title 28–34/700 (or wordmark 14 + title) · optional search pill 44 grey
  · sections of [title 20–22/700 + "See all" 14/600 accent] + rail · 24 between sections ·
  tab bar. Nothing else above the first rail.
- **Media detail**: picture edge to edge at its ratio · title 17–20/700 · one 13 grey meta line ·
  a row of 3–4 equal actions (44 discs with 12 labels, or 48 outlined buttons) · related list.
  Sharing lives in the header or the ⋯ menu.
- **Player / Now playing**: dark, artwork square with 16 gutters · title 22–24/700 + 15–16 grey
  · thin progress with 11 times · 5-control row with a 64 disc · tertiary icon row · lyrics /
  queue as a peeking card.
- **Editor**: black stage · header (back · undo · redo · primary pill 32) · picture at its
  ratio · transport row (play centred, full screen right, timecode mono) · ruler with 2-s
  ticks · playhead line · video track 56–64 (thumbnails, selected with a 2-pt accent
  outline, trim handles) · audio track 40 (name + duration on a colour) · mute discs at
  the left · tool band of 5–6 labelled tools that scrolls and changes with the selection
  · tool panels as sheets with Cancel · title · Apply and a Reset in the header, each
  fitting without scrolling, formatting choices as icon segments and steppers.
- **Publish / form**: title 28/700 · destination tiles or radio cards · one field at a time with a
  13 grey label · "More options" disclosure · pinned CTA with a 12 grey line under it.
- **Settings / profile**: avatar 44–56 row · grouped cards of 44–52 rows · section titles 15/600
  · footer links 12 grey. Destructive row last, in red.
- **Comments / replies**: sheet with "N replies" 20/700 · rows avatar 28–32 + handle 13/600 +
  time grey + body 14 + heart right · composer pill 44–48 docked · replies indented 40.
- **Paywall**: rail of what you get (artwork) or 3 benefit rows (icon 24 + 15/600 + 13 grey) ·
  two plan cards with the selected outlined in the accent · one CTA with the price · 12 grey
  legal links.
- **Onboarding**: one image or illustration · title 24–28/700 · one sentence 15–17 grey · dots ·
  one pill. Permission explainers use a dark overlay with two "why / control" rows.

## Checklist before calling a screen done

- Can you name the one thing this screen is for, and is it the only filled button?
- Is the title within 12 pt of what it titles, and is there ≥ 24 pt before the next section?
- Is the gutter 16 everywhere, including inside sheets?
- Do rows carry ≤ 3 elements, and is the trailing one the only interactive one?
- Is there any box, border or divider that a change of ground or 12 pt of air could replace?
- Are all tiles in a rail the same size, corner and label style?
- Is the accent used ≤ 3 times on the screen (action, active tab, selection)?
- Are there ≤ 5 tappable choices in the first viewport (per band on a tool screen), and does every action icon have a label?
- Are buttons 44 / 40 / 36 with 44-pt touch areas, and is the only full-width one at a flow's end?
- Does each transition animate once (slide, rise or cross-fade), with no bounce on the tab bar?
- Are states shown as icons, with words only for problems, and does every tool panel fit without scrolling?
- Do empty, loading and error states exist, each as one line + one move?
- Is every number tabular, every timecode mono, every uppercase label ≤ 12 pt?
- Does the tool UI (if any) sit on black with the picture untouched?
- Does it read the same at 400-pt width and with Larger Text on?

## Anti-patterns seen in weaker screens

Cards inside cards; three shadows on one screen; titles with an eyebrow, a title and a
subtitle stacked; a segmented control and a chip row and tabs on the same screen; icons
with labels everywhere; gradient buttons next to flat ones; centred body text; more than
one accent; "Learn more" links in the middle of a flow; a header that repeats the tab
label; all-caps 14-pt headings; toasts that need to be dismissed.

## Files

- `refs/INDEX.md` — the 44 apps, counts, and what each is good for.
- `refs/patterns.md` — pattern → apps and screens to look at.
- `refs/notes.md` — per-app measurements and observations.
- `refs/ux-research.md` — sourced findings on choices per screen, icon labels, tap targets, typefaces and icon systems.
- `refs/lessons.md` — what changed when the research met real screens, then the product owner's review (motion, glow, compact buttons, status icons, a second space, own reactions).
- `refs/lessons-img/` — screenshots for each lesson (logos blurred).
- `examples/before-after/` — the same app before and after the skill, screen by screen.
- `refs/sheets/` — optional local screen library (six-up contact sheets), used when present.
