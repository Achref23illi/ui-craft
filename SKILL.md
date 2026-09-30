---
name: ui-craft
description: Make a mobile UI look and feel like a shipped app. Rules with numbers, 29 screen recipes (plus 200 measured ones), a fast screenshot review and lessons from a real redesign, grounded in 4,500 iOS screens from 78 apps (Spotify, Airbnb, Instagram, Apple Music, Wise, Coinbase, Google Maps, Uber Eats, Halide, Notion…). Use before designing or restyling any mobile screen (React Native, Expo, SwiftUI, Flutter, mobile web), when reviewing screenshots for "does this look like a real app", or when you need a reference for a pattern (feed, player, editor, sheet, paywall, settings, onboarding, empty state, money home, checkout, map, calendar, sign-in, AI chat, workout).
---

# UI craft — what real apps do

By Achref Arabi · https://github.com/Achref23illi/ui-craft

A skill built from a study of 78 shipped iOS apps (Spotify, Airbnb, Instagram, TikTok,
Apple Music, Apple TV, Netflix, VSCO, Halide, Denim, Photoshop, Riverside, Moises,
Revolut, Wise, Coinbase, PayPal, Linear, Notion, Cron, ChatGPT, Gemini, Claude, Uber,
Uber Eats, Google Maps, Apple Books, The Athletic, Nike Training Club…). 4,536 screens
in 760 contact sheets; every sheet was read and the key screens measured in points.
The point of the skill is not a style. It is the discipline these apps share: where
they spend space and where they don't, how few things they show, and how every element
earns its place.

## Start here

Paths below are relative to this skill's folder (the one holding this file). The
scripts need Python 3; `scripts/sheet.py` also needs Pillow.

**1. Pick the job.**

| The ask | Mode | Go to |
|---|---|---|
| Design or build a new screen | Design | steps 2–5 |
| "Does this look right?", screenshots to judge | Fast review | § Fast review |
| Restyle a whole app | Whole-app pass | § Whole-app pass |

**2. References first, every time.** Run
`python3 scripts/refs.py "<pattern words>"` (for example `"video editor"`,
`"settings"`, `"paywall"`). It lists, best first, the local contact sheets to read
(each is one image with six screens of one app: look for the ones that match), the
matching patterns, measurements observed in those apps, and published before/after
images, plus the closest measured recipes from `refs/recipes.md` (about 200, by screen
type, each citing a screen as `App NN·k`). Read two or three sheets before drawing
anything. `refs.py --list` prints the pattern names when you are unsure which words to
use; `refs.py --screen "Wise 03·2"` gives a cited screen's file to measure with
`scripts/measure.py`. If it reports no local library, work from the patterns and notes
it prints and read at most two of the published images it lists; the rules below still
hold. The published before/after images show
one app's result: take the principle from them, never copy their layout, colours or
branding into another product, and do not score a review by how closely a screen
resembles them.

**3. Apply the rules as numbers, not vibes.** If a screen breaks one, the screen
changes, not the rule. When sources disagree, this order wins:

1. the project's own design system and tokens (read them in code when you have it);
2. the rules and measurements in this file;
3. the screen recipes (here, then the measured ones in `refs/recipes.md`);
4. the per-app notes, which record what those apps do, not targets.

When you only have screenshots, you cannot see the project's tokens: report a
deviation with its number and add "unless this is a deliberate token".

**4. Use what the last redesign taught.** Read "Lessons at a glance" below; open
`refs/lessons.md` and `refs/lessons-img/` when the screen involves motion, brand
background, buttons, status indicators, tool panels, a second product space or
reactions.

**5. Verify on a real render.** Screenshot the running app (iOS Simulator
`xcrun simctl io booted screenshot shot.png`, Android `adb exec-out screencap -p > shot.png`,
web a headless browser at 390 px wide), put several shots in one contact sheet with
`python3 scripts/sheet.py <folder>`, read it, and run the checklist. Judge the render,
never the code.

## Fast review

For "review these screens" in minutes rather than an hour. No need to run
`doctor.py`.

1. **Collect** screenshots of every screen in scope in one folder: same device, same
   data, tidy status bar. iOS Simulator:
   `xcrun simctl status_bar booted override --time 9:41 --batteryState charged --batteryLevel 100 --wifiBars 3 --cellularBars 4`
   then `xcrun simctl io booted screenshot shots/01-home.png`. Android emulator:
   `adb shell settings put global sysui_demo_allowed 1` then
   `adb exec-out screencap -p > shots/01-home.png`.
2. **See everything at once**: `python3 scripts/sheet.py shots` writes six screens per
   image into `shots/sheets/`; read the sheets, not the files, to judge layout,
   hierarchy and consistency.
3. **Measure on the originals, not the sheets** (sheets are too small for numbers):
   `python3 scripts/measure.py shots/01-home.png` gives the scale, the width in points
   and the side gutters; `--col <x pt>` and `--row <y pt>` list what a vertical or
   horizontal line crosses, with sizes and gaps in points (paddings, section gaps, row
   and button heights). The numbers in this file are for a 390-pt screen and hold from
   375 to 430 pt.
4. **References, three at most in fast mode**: pick the two or three screens with the
   biggest problems, run `scripts/refs.py` with several words at once, and read one
   sheet per pattern. Skip references for screens that already follow a recipe. For a
   screen type the recipes below do not cover, the measured recipe `refs.py` prints is
   the benchmark to quote.
5. **Score against the checklist**, global issues first: typeface and type scale,
   gutter, button sizes, icon set and labels, placeholder content, status bar. A global
   fix repairs every screen at once.
6. **Report as a table**, most important first, one line per finding:

   | # | Screen | Rule | What is wrong (with the measurement) | Fix (with the number) |
   |---|---|---|---|---|

   Cap it at the ten findings that matter most; say what is already good in one line;
   end with what to fix first (usually the shared components).

## Whole-app pass

1. Shared layer first: tokens (type, colour, spacing, radii), icon set, buttons, chips,
   fields, rows, headers, sheets, tab bar. Most screens then fix themselves.
2. Replace placeholder art with real pictures before judging anything.
3. Sweep every route: screenshot all of them and read them as contact sheets; list what
   is still off; fix in batches; sweep again.
4. Then the key screens by hand, each against its recipe.
5. Show the owner on a device and turn each note into a rule for the next pass (as
   `refs/lessons.md` round 2 did).

## Lessons at a glance

From applying this skill to a real app and its owner's review (details, with
screenshots, in `refs/lessons.md`):

- Tool screens (editors) are counted per band, not per screen; hiding their tools
  reads as a weak product. Tool panels fit without scrolling and use icon controls.
- Buttons were still too big at 48–52: the owner settled on 44 / 40 / 36, chips 30,
  with 44-pt touch areas.
- No transitions made a polished app feel like a prototype: slide for drill-down,
  rise for tasks, cross-fade for tabs, one animation per change, no bounce on tabs.
- A brand glow with grain gave identity without painting surfaces; it needs a
  vertical gradient, dark-and-light grain, transparent rows and a scroll backdrop.
- Status tags (synced, local, cloud, export…) are noise; icons are understood.
  Problems keep words.
- One owner's choices that worked well as defaults, not laws: a second space
  (community, marketplace) as a different stage of the same family with its own tab
  bar and a fixed way back; an own reaction set with one signature effect, not four.
- Replace striped placeholders with real images early; they hide spacing problems.
- A status bar style set by one dark screen lingers: set it per route.

## The rules (with the numbers behind them)

1. **Content carries the screen; chrome is nearly invisible.** Artwork, video, photos and
   the user's words fill the frame. Headers are one title (15–17/600 centred, or 28–34/700
   left) and at most two 24-pt glyphs. No decorative bars, no dividers between sections;
   a title and 12 pt of air are the divider. (Spotify, Apple TV, VSCO, Sora)

2. **One primary action per screen state, pinned where the thumb is.** A 44-pt pill at
   the bottom with 16 pt side gutters, full width only when the screen exists to make
   that one decision (rule 13); the secondary is text or a grey pill under it. Never two
   filled buttons side by side except as a strict pair (Play · My List, Submit · Retake).
   (Airbnb, Revolut, Headspace, Netflix)

3. **Titles are close to their content and far from each other.** Section title 20–22/700
   on root and browsing screens, 17/700 for a section inside a detail screen, 13/600 grey
   for a group label above settings rows; 12 pt to its content (8 for group labels);
   24–28 pt between sections. Screen title 28–34/700 with 8–12 pt to the first control.
   Body 15–16 with a 1.4 line height, never wider than the gutter. A section that follows
   a list gets about double the air (≈46, Apple Podcasts). One gutter per product: 16 is
   the default; Apple's own apps, Luma and TIDAL use 20; Airbnb, Coinbase and Nike
   Training Club 24; long reading goes to 24–38 (The Athletic, Bear, Apple Books). Hands-
   busy reading (a cooking step, a workout cue) may run 20–22 text.
   (Apple Music, Spotify, Denim, Superlist)

4. **Rows are 44–56 pt and carry three things at most**: a leading visual (24 icon, 40
   avatar, 40–48 thumbnail), a title 15/500–600 with an optional 13 grey sub-line, and one
   trailing element (chevron, ⋯, value in grey, a 32–36 pt pill). Hairlines inset from the
   label, or none at all inside a card. Grouped screens put rows in white 12-pt cards on a
   grey ground; flat screens put them on white with hairlines. The height follows the
   row's class, measured across 78 apps: settings 44–54; with a sub-line 52–64; commerce
   and people 60–64; money and price rows with a sparkline or two-line figure 72–80; media
   rows with a 16:9 thumbnail 80–106; mail 85; editorial headline + thumbnail ≈120; data
   tables 32 when every figure is tabular and right-aligned. A row that is taller than its
   class for no content (The Athletic's 78-pt account rows) reads as empty.
   (Apple Music, Uber, Notion, Rewind, Opal, Gmail, Coinbase, Target)

5. **Rails and grids have one geometry per screen.** Rail tiles are square 112–160 pt or
   16:9 at 160–180 wide, 12–20 pt corners, 8 pt gaps, with a 13–14 label and a 12 grey
   meta line under; 3 to 3.5 visible plus a peek. Wide tiles (3:2 headlines, balance cards
   ≈208, store tiles ≈230) show 2–2.2 plus a peek with 12–15 gaps. Grids are 2 columns with
   8 pt gaps when they read as one grid, 12–16 (the gutter) when each tile is its own card
   (Asos, Kitchen Stories, Headspace, VSCO), 3 columns with 2–4 pt gaps for archives.
   Posters are 2:3, video 16:9, social and fashion 4:5, recipes 3:4; book covers stay at
   their own ratio, bottom-aligned (Apple Books). (Spotify, Apple TV, Denim, Pinterest,
   VSCO, Sora)

6. **Tool UIs live on black with the picture at its own ratio.** Editors, players and
   cameras: pure black stage, controls in bands below the picture (never over it except
   guides), tool labels 11 pt uppercase or 12–13 sentence case, the selected tool as a
   white or accent pill, the primary shutter/play as a 56–72 white disc, and one accent
   colour for "selected" or "has a value". Panels rise as sheets to about half the screen
   and never push the picture off. Image and design editors may use a light grey canvas
   (Photoshop, Playground): the bands hold, the black does not have to. A full-screen
   video player's pause can grow to 88 with 62 skip discs (Apple TV). A tool control takes
   the accent only once its value differs from the default, with "Reset" appearing then
   (Moises, Luminar). (Halide, Moises, Riverside, Denim, Photoshop, Analog)

7. **Colour is a signal, not paint.** One accent for the action (brand colour), one state
   colour at most (record red, live green), everything else ink and greys. Artwork
   supplies colour: dark players tint the top of the screen from the art. Brand colour
   on the tab bar's active item is enough branding. When a product needs more than one
   hue, give each exactly one meaning and never let two mean "act": PayPal (black acts,
   blue links, green is incoming money), Claude (terracotta acts, violet only upgrades),
   Coinbase (blue acts, red and green only inside numbers), Cron (orange only for today,
   selection and send; even the + disc is grey). Repeating the accent on every row
   (ten orange Follow pills, Substack) turns it into noise; so does one red for brand,
   price, back arrow and button at once (Target). (Spotify, Netflix, Apple Music, Moises)

8. **Sheets are the app's second surface.** Anything transient rises as a sheet with a
   grabber, a 15–20/700 title, and an × disc: menus, pickers, filters, comments, share.
   Actions in a sheet are plain rows (icon 24 + label 15–16, 48–64 pt: tighter with no
   dividers, taller on a full-screen blur), destructive last in red, isolated in its own
   group, "Cancel" as text. A sheet that edits one property can drop the big title: a 13
   grey label with Clear · Done pills is enough (Superlist). Alerts are centred dark/white
   cards ≈290 wide with 15/600 title, one line, and two stacked pills (destructive red or
   red-tinted on top). Destructive confirms say the consequence in the button ("Yes,
   delete permanently"); if the button is not red, its words must carry the danger.
   (Spotify, Airbnb, Instagram, Threads, Riverside, Sora, Notion, Meta AI)

9. **Empty, loading and error states are one sentence and one move.** Centred, a 15–17
   /600 line plus a 13 grey line, optionally a 48–64 pt glyph or small illustration, and
   at most one button. No paragraphs, no decoration. Inside a sheet with a search field,
   "no results" is one left-aligned grey line, no glyph (Instagram). Loading is a skeleton
   of the final layout (Airbnb, Uber Eats, Wise), not a spinner in a void; an AI step is
   one grey line with a small spinner where the answer will appear (Structured, Wispr
   Flow). Errors name the cause and give one move (Retry), never a raw provider message
   (Luma) or "Something went wrong · Done" (Uber, Headspace). Toasts are pills or bars
   40–54 tall (dark, or white on dark stages) with 14/600 text and an optional trailing
   Undo; they never need dismissing. A confirmation about one object can sit on that
   object as a small capsule instead of a toast (Threads). (TikTok, Meta AI, Notion,
   Pinterest, Gmail, Substack)

10. **Type does the hierarchy, not boxes.** Two weights (500–600 for labels, 700–800 for
    titles), grey for the second line, mono or tabular figures only for numbers and
    readouts. Tracked uppercase only on 11–12 pt tool labels and eyebrows, never on
    titles. Cards are for objects (a place, an item, a plan), not for grouping text.
    A serif, when the brand has one, is for display lines only (titles, quotes, stat
    counts) and the sans runs every control and row (Wispr Flow, Apple Books, The
    Athletic, Claude, Atoms). All-caps chrome at 13–15 (Asos, SSENSE, Duolingo) is a
    brand choice that only holds when every screen does it; never mix it in.

11. **The tap budget: five choices in the first viewport, one of them primary.** Count
    what makes a decision or starts an action above the fold (buttons, text links,
    chips, fields, toggles), except the tab bar and back. A set of options answering one
    question (a radio list, a segmented control, a set of destinations) counts as one.
    Content that opens an item (a tile, a row, a post) does not count. Five or fewer
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
    48 pt at the screen edges, with padding between neighbours. Many famous apps ship
    unlabelled bars (TIDAL, Notion, Linear, Substack tab bars; ChatGPT and Gemini's row of
    6 glyphs under each answer; X's 8-icon composer toolbar): they survive on repetition
    and habit, and they are the most frequent weakness in the study. Flag them on any
    screen a user sees once; accept them only for a row repeated under every item and
    for system-like keyboards. A capsule tab bar keeps its labels (WhatsApp, Wispr Flow).

13. **Buttons are compact, and most screens need the smallest one.** The main action is
    44 pt (full width only where the screen exists to make one decision: intro, export,
    publish, paywall); dark buttons 40; everything else 36, hugging its label; chips 30
    with 13-pt labels; tertiary actions are 15/600 text in the accent. Discs: 56 for
    source choices, 44 for media actions. Anything under 44 pt keeps a 44-pt touch
    area with hitSlop. Two big buttons on consecutive screens means one of them is a
    step, not a decision. Lessons in `refs/lessons.md` (§2, §7). For the record, the
    78 apps measure their single decision button at 44–57 (Target and Halide 44, Apple
    50–51, Wise 49–54, Coinbase and Revolut 56, Uber 57) while their secondaries hug at
    32–38 (X, BeReal, Netflix, YouTube). This skill keeps 44 by design; use a taller one
    only when the project's tokens say so, and never for a step. Row actions are chips:
    Follow is 30–33 × ≈89 and keeps its size in the "Following" state so the row never
    shifts (Instagram, TikTok).

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

17. **If the product has a second space (a community, a marketplace), make it the same
    family on a different stage.** These are defaults from one product's review; adapt
    them to yours. Same typeface, icons, radii, grain and components; a different
    ground (a night palette) and its second brand colour as the action. It gets its own
    tab bar (its sections as tabs, and a way back to the main space in a fixed place,
    for example the first tab with the main logo), illustrated icons for its main
    places and a plain outline for the profile. Its
    logo reuses the main wordmark's letter construction. Implement it as a theme scope
    that components read, never as forked components. (§10)

18. **When the product has expressive details, own them, and give only one a big
    moment.** For example reactions drawn in the brand gradients instead of system
    emoji, each with a small tap motion, and one of them (fire, in the case study) with a
    full-post effect. Optional; worth it for social and consumer products. (§11)

19. **On money, data and stats screens the number is the content.** One figure per
    screen is the hero at 28–40/700 tabular (balance, price, amount, score, temperature),
    its label 11–13 grey above or below, and change as a small coloured value or pill
    (13, green/red) — colour lives inside the number, never on the buttons. One chart per
    screen, edge to edge, no gridlines, a range control under it (1D · 1W · 1M · 1Y · All,
    13, the selected as a tinted pill). Amount entry is a centred figure of 40 or more
    over a bare keypad (digits ≈28/400 on a ≈64 pitch, no key shapes) with the one
    action under it.
    Statuses (pending, paid, paused) are one disc + one word under the figure. (Coinbase,
    Acorns, Wise, PayPal, Copilot, Revolut, CARROT Weather, The Athletic)

20. **Selected, disabled and done must read differently at a glance.** Selected = a 2-pt
    ink or accent outline (or a fill) plus a check; disabled = neutral grey fill with a
    grey label (or ~40 % opacity), with a reason nearby when it is not obvious; done = a
    check in the state colour. A disabled
    primary that is only a paler tint of the enabled one reads as missing (Structured,
    Coinbase); a "Following" pill in grey-on-grey reads as disabled (VSCO). Answer
    lists that advance on tap need no Next (Nike Training Club); lists that need a Next
    keep it disabled until a choice is made (Revolut, Todoist).

21. **Maps are the stage; everything else floats or rises.** A search pill 44–48 at the
    top (inset 8–16), round 40–56 discs stacked at the right edge (locate, layers,
    directions), chips 32 under the search, and content in a sheet with a grabber and
    three stops (peek ≈ a third, half, full). The sheet carries a 17–22 title, one line
    of 13 grey meta and one hugging action pill 40 (Start, Save, Directions) while the
    user is browsing; a full-width button appears only for the one decision the screen
    exists for (Confirm pickup, Choose ride; Uber). Pins are small white pills with the
    value (price, rating), black when selected. (Google Maps, Uber, Airbnb, komoot,
    Flighty, Tripsy, Uber Eats)

22. **Stay native through the whole journey.** Help, legal, sign-in, payment and
    "manage account" steps that drop into a web view with another type scale, ground or
    button style were the single most common break in the study (Halide, Craft, Luma,
    Netflix, Cron, ten ten, The Athletic, Todoist, Coinbase, Instagram). Keep those
    screens in the app's own components; when a web page is unavoidable, open it as a
    sheet with the app's header. Legal copy under a CTA is at most two 11–12 grey lines
    with links; everything longer lives one tap away.

23. **Secondary text stays readable.** 13 grey on white is the floor for meaning; 11–12
    only for timestamps, legal and tool labels. On dark, tinted or photo grounds keep
    secondary text ≥ 13 and ≥ ~60 % white, or add a scrim; 11–13 grey on black, blurred
    art or a gradient (Sora, BeReal, Calm, Dropset, Not Boring Camera) was a recurring
    failure. Never set prices, actions or tab labels under 10 (SSENSE's 8–9-pt caps).

## Measurements to reuse (390-pt screen; the same numbers hold from 375 to 430 pt)

| Element | Value |
|---|---|
| Screen gutter | 16 default · 20 (Apple-style, editorial) · 24 (spacious marketplaces, fintech) · 24–38 long reading · one per product |
| Header height | 44 + safe area; title 17/600 centred or 28–34/700 left |
| Section title | root/browsing 20–22/700 · inside a detail 17/700 · settings group label 13/600 grey |
| Section title → content | 12 (8 for group labels) · section → section 24–28 |
| List row | 44 (dense, settings 44–54) · 52–56 (with sub-line) · 60–64 (commerce, people, 48 thumb) · 72–80 (money rows with a figure or sparkline) · 80–106 (16:9 video thumb) · ≈120 (headline + thumb) · 32 (data table) |
| Card radius | 12 (rows, small cards) · 16–20 (artwork, sheets) · 24 (large sheets) |
| Button | main 44, full width only at a flow's decision · dark 40 · others 36 (hug label) · text 15/600 accent · 44-pt touch area via hitSlop |
| Disc | 56 source choice · 44 media action · 32–36 row pill |
| Editor | header 44 (back · undo · redo · primary) · transport row 44 · ruler 11 mono · video track 56–64 · audio track 40 · tool band 5–6 × (icon 22 + 11 label), scrolls, contextual |
| Pill chip | 30 tall, 12 padding, 13/600, grey fill · selected ink (or the space's accent) |
| Icon | 24 in headers and rows · 20 in tool rows · 28–32 in feed rails |
| Avatar | 24 inline · 32–36 in rows · 44–48 in lists · 64 stories · 96 profile |
| Rail tile | 112–160 square · 160–180 × 16:9 · gap 8 · corner 12–20 |
| Grid | 2 col gap 8 (one grid) or 12–16 (separate cards) · 3 col gap 2–4 · tiles 160–167 wide on a 375–390 screen |
| Tab bar | 49 + safe area; icon 24 + label 10/500 · or a floating capsule 52–59 inset 16–24, labels kept · 3–5 items, the main action may be the centre item as a 42–44 disc |
| Mini player | 56 above the tab bar, art 40 |
| Sheet | grabber 36×4, title 15–20/700, × disc 24–32 · or a floating card inset 8–16, radius 24–32 · three stops over maps |
| Toast | 40–54 pill or bar, inset 8–16, 14/600, optional trailing Undo · or a 30-pt capsule on the object |
| Alert | card ≈270–295 wide, radius 14–20, title 15–17/600, one line 13, stacked pills 40–44 |
| Money figure | hero 28–40/700 tabular · label 11–13 grey · change 13 in green/red · keypad digits ≈28/400 on a ≈64 pitch |
| Chart | one per screen, full width, 150–250 tall, no gridlines · range chips 13, selected as a tinted pill |
| Map | search pill 44–48 inset 8–16 · side discs 40–56 · chips 32 · sheet stops ≈⅓ · ½ · full · pins as value pills 13/700 |
| Filters sheet | title 17/700 · sections 17–20/600 · chips 32–42 · stepper discs 30–32 · footer: "Clear all" text + one button with the live count |
| Plan cards (paywall) | 2 cards ≈160×80 side by side or 60–86-tall rows · selected = 2-pt accent outline + check · discount chip 11 |
| Calendar | month grid cells 38–44 · today outlined or accent 28–32 · selection filled disc · range as a tinted band |
| Skeleton | grey blocks in the final layout (same radii, same rows) · no spinner unless an AI step (one grey line + spinner) |
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
  a row of 3–4 equal actions (44 discs with 12 labels, or 36 grey buttons) · related list.
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
  13 grey label · "More options" disclosure · pinned 44 CTA with a 12 grey line under it.
- **Settings / profile**: avatar 44–56 row · grouped cards of 44–52 rows · group labels 13/600 grey
  · footer links 12 grey. Destructive row last, in red.
- **Comments / replies**: sheet with "N replies" 20/700 · rows avatar 28–32 + handle 13/600 +
  time grey + body 14 + heart right · composer pill 44–48 docked · replies indented 40.
- **Paywall**: rail of what you get (artwork) or 3 benefit rows (icon 24 + 15/600 + 13 grey) ·
  two plan cards with the selected outlined in the accent · one 44 CTA with the price · 12 grey
  legal links.
- **Onboarding**: one image or illustration · title 24–28/700 · one sentence 15–17 grey · dots ·
  one 44 pill at the bottom. Permission explainers use a dark overlay with two "why / control" rows.

The screens below were added in v2 from the 34 new apps; each has measured versions with
sources in `refs/recipes.md` (the section name is in brackets).

- **Money home** [Money home, send and status]: avatar 32 + one header chip + bell · title
  28/700 or a balance card (figure 24–40/700 + 11 grey label) · balance cards ≈208 wide with a
  peek, or one card · "Send again" avatar rail 48–56 with 11 names · activity rows 64–80 (disc
  40 · 15/600 + 13 grey · amount 15/600 right, green only for incoming) · "See all" 15/600 ·
  tab bar with the main money action as the centre item. (Wise 01, PayPal 01, Coinbase 01)
- **Send / amount entry** [Money home, send and status]: back + 13–15/600 title · recipient
  avatar 56–62 + name · amount 40+/600 centred or in a 76 outlined field with the currency as
  a chip · fee and arrival lines 13 with the key value bold · bare keypad or keyboard · one
  Continue 44, or Request · Send as a strict pair. (Wise 03, PayPal 05)
- **Asset / metric detail** [Dashboards, charts and stats]: back · name 15/600 · star · share
  · price 28/700 + change 13 coloured · one line chart full width, no axes · range chips 13
  (selected tinted) · 5 labelled action discs 42 or one pair · "About" 20/700 · label/value
  rows 15. (Coinbase 03, Acorns 04, CARROT Weather 02–03)
- **Transaction or order status**: status disc 56 + one word 13 grey · amount 28/700 · tag
  chip · "Details" 20/700 + label/value rows 15 · one outlined 44 action (View order, Get
  help). (Wise 10, Acorns 10)
- **Product grid** [Grids, browse lists and libraries]: back · title or brand 13–17 centred ·
  SORT | FILTER split bar 44 + count 11 grey · 2 columns 160–165 wide at 4:5 (or 3:4), gap
  8–15, 12 corners or none · heart on the image · price 14–15/700 · name 12–13 grey, two lines.
  (Asos 02, Kitchen Stories 01, SSENSE 01)
- **Product page** [Product, booking and event pages]: pictures edge to edge with dots or a
  counter · brand 13 + name 15–17 + price 15/700 (sale red + struck) · variant thumbs 48 or
  size chips · one pinned add-to-bag 44 + wishlist heart or text · details as label rows.
  (SSENSE 02–03, Asos 04, Airbnb 09)
- **Cart and checkout** [Cart and checkout]: title + "N items · subtotal" 13 grey · rows 64–73
  (thumb 60–73 · 15/600 · 13 grey · trash · n · + stepper) · "+ Add items" grey pill · sections
  (address, delivery, payment) on grey bands or cards, "Change" as text · total row 17/600 ·
  one checkout button pinned, Apple Pay as its strict pair. (Uber Eats 05, Target 04, Asos 07)
- **Filters sheet** [Search, filters and sort]: × + "Filters" 17/700 · sections 17–20/600 with
  20–24 above · one control type per section (chips 32–42, stepper 30, range slider with a
  histogram) · sticky footer: "Clear all" text left + one button with the live count
  ("Show 82 homes"). (Airbnb 02, 07, 10; Uber Eats 04; Calm 05)
- **Map with a sheet** [Maps, places and routes]: rule 21 · sheet peek holds title 17–22/700
  + 13 grey meta + one hugging action 40 · half shows 3 labelled action tiles (icon 24 + 13)
  and label/value cards · turn-by-turn uses a banner 88 (arrow 32 · street 24/500) and a red
  "Exit" pill in the sheet. (Google Maps 01, 08, 10; Uber 04–05; komoot 03; Tripsy 06)
- **Calendar / day timeline** [Calendar, timeline and task editors]: month 26–28/700 + chevron
  · week strip (day 11 grey · date 15–16 · today as a 28–32 accent disc) or month grid cells
  40–44 · hour labels 10–11 grey · events as tinted capsules, height = duration, title 15/600 +
  11 grey time · now line 1 pt + 11/600 time · one + disc 48–56. (Cron 01, Structured 01)
- **Event / task editor sheet** [Calendar, timeline and task editors]: small grey kind label +
  Done pill 28 · title 20–22/600 · property rows 40–44 (icon 16–20 grey · value 15 · grey
  qualifier) · toggles in the accent · participants rows avatar 24 · one accent action.
  (Cron 02, Linear 02, Todoist 06, Structured 02)
- **Inbox / mail / task list** [Inbox, task and note lists]: title 22–34/700 or a search pill
  48 · rows 68–85 (avatar 34–40 · 15/600 sender or title + 12 time · 13 subject · 13 grey
  snippet · unread as a 6-pt dot) · swipe to act · one FAB or extended "Compose" pill 47–56
  bottom-right · undo snackbar 48. (Gmail 01, Linear 03, Todoist 01)
- **Sign-in** [Sign-in, sign-up and passcode]: logo 28–48 · one headline 24–28 · provider
  pills 44–54 stacked 12–16 apart (Apple filled, others outlined) or one email field with
  Continue grey until valid and providers under an "or" hairline · 11 grey terms at the foot.
  (Luminar 01, Wispr Flow 10, X 10, ten ten 03)
- **Passcode / code entry**: title 28/700 · 13 grey hint · 6 dots 16 or 6 boxes 44–48 · bare
  keypad 3 × 4 on a ≈64 pitch, the action as an accent disc in the empty cell · error as a
  red line under the boxes, never an alert. (Revolut 04, 06; Netflix 01; Claude 01)
- **Onboarding question** [Onboarding questions]: back + progress bar 4–8 or "1/3" 15/600 ·
  question 22–28/700 left, two lines · one 13–15 grey sentence · answers as full-width pills
  or cards 44–82 tall, 8–12 apart, selected filled ink or outlined accent + check · advance
  on tap, or Continue disabled until chosen · Skip as 13–15 grey text. (Nike Training Club
  02, Opal 05, Todoist 06–07, Revolut 03, 07)
- **Feature intro / pre-permission sheet** [Feature intro and permission sheets]: sheet inset
  8, radius 24–32 · icon disc 48 or illustration 120 · title 20–28/700 centred · one 13–15 grey
  line · 3 rows (icon 20–28 + 15/600 + 13 grey) · one 44 pill + "Not now" text. Ask before the
  system prompt, never after it. (ChatGPT 09, Meta AI 05, TikTok 06, Halide 06)
- **AI assistant chat** [AI assistant chat and voice]: header title 15/500–600 centred ·
  user bubble grey 16–18 radius, right · answer as plain body 15 at ≈23 line height, no
  bubble · one row of labelled or tooltip-backed actions (copy, retry, feedback) · follow-ups
  as rows with ↳, in ink · composer pill 44 + send disc, docked, with a 11 grey disclaimer.
  Voice mode is a black stage, one moving glow, two labelled 64 discs (Hold, End).
  (Google Gemini 02, 04; Meta AI 03; ChatGPT 01)
- **Article / reader** [Reading, articles and news]: serif or large sans headline 22–28 ·
  byline 11–13 grey · hero 16:9 full width · body 17–19 at 1.5 in a 24 gutter (reader
  margins up to 38) · page position 12 grey · text settings in a sheet (size segment,
  theme tiles 3 × 2 with the selected outlined). (The Athletic 01, 09; Apple Books 07, 09)
- **Live session / workout** [Live sessions, workouts and timers]: dark or full-colour
  ground · elapsed or countdown 48–100/700–800 tabular · current step 17–28/700 + next line
  15 grey · list of sets as rows 52 with tabular cells and a done check · one pause disc 40–64
  with a progress ring + a grey Stop pill 36 · finishing needs a hold or a confirm.
  (Dropset 04, 06; Train Fitness 03–04; Nike Training Club 06)
- **Destructive confirm** [Choice sheets, dialogs and confirmations]: centred card ≈290 or a
  sheet with the object (avatar 72 or thumb) · title 17–24/700 naming the object · one 13
  grey line with the consequence · red pill 40–44 with the verb ("Delete 3 photos") over
  Cancel as text or grey. (Threads 04, ten ten 02, Notion 09, Meta AI 08)

## Checklist before calling a screen done

- Can you name the one thing this screen is for, and is it the only filled button?
- Is the title within 12 pt of what it titles, and is there ≥ 24 pt before the next section?
- Is the gutter 16 (or the project's one gutter token) everywhere, including inside sheets?
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
- On a money, data or stats screen: is there one hero figure, tabular, with colour only inside numbers and one chart at most?
- Do selected, disabled and done states differ by shape (outline, fill, check), not only by tint?
- Is every step of the journey (help, legal, sign-in, payment) in the app's own components, with legal ≤ 2 lines under a CTA?
- Is secondary text ≥ 13 and readable on its ground (dark, tinted, photo), with nothing that carries meaning under 11?
- Does loading show a skeleton of the final layout, and does every error name its cause and offer one move?

## Anti-patterns seen in weaker screens

Cards inside cards; three shadows on one screen; titles with an eyebrow, a title and a
subtitle stacked; a segmented control and a chip row and tabs on the same screen; icons
beside every heading or row label as decoration (action icons do carry labels, rule 12);
gradient buttons next to flat ones; centred body text; more than one accent; "Learn
more" links in the middle of a flow; a small centred header title repeating the large
title right under it; all-caps 14-pt headings; toasts that need to be dismissed.

Seen again and again in the 78 apps (sources in `refs/notes.md` and `refs/recipes.md`):
help, legal or sign-in pages that switch to a web view with another type system; the
accent repeated on every row (ten identical Follow or Send pills) or one colour for brand,
price, navigation and action at once; three or more action colours on one screen (a
five-colour action row, a gradient CTA beside a solid one); a raw error string or
"Something went wrong" with only "Done"; ten-line legal blocks under the CTA; centred
paragraphs of five lines in intros and dialogs; the same upsell four ways in one flow
(PRO tags, in-card pills, a chip and a sheet); a disabled button that is only a paler
tint; unlabelled rows of 5–12 tool icons over the picture; menus of 10–12 actions in one
card; rows that repeat ⋯ and + on every line; chips or tags repeated on every row until
the list is a wall of grey; tables that clip columns with no scroll hint; floating buttons
that cover the next item or text; a promo card between content sections; mixed button
languages (Material uppercase text actions beside iOS pills); tab bars that spend a slot
on "Premium".

## Files

- `scripts/refs.py` — references for a pattern: local sheets to read, patterns, measured recipes, app notes, published images; `--screen "App NN·k"` gives a cited screen's file.
- `scripts/sheet.py` — contact sheets (six screens per image) from any folder of screenshots.
- `scripts/measure.py` — sizes, gutters and gaps in points from a screenshot.
- `scripts/doctor.py` — checks an install; `--refs` also checks every sheet named in `refs/patterns.md` and every screen cited in `refs/recipes.md`.
- `refs/patterns.md` — 500 patterns under 29 headings → apps and sheets that do it well.
- `refs/recipes.md` — about 200 measured screen recipes in 28 screen types, each citing its screen (`App NN·k`).
- `refs/notes.md` — per-app measurements and observations, 78 apps.
- `refs/INDEX.md` — the 78 apps and what each is good for.
- `refs/screens-index.csv` — every screen: app, sheet, position, file, label, source.
- `refs/ux-research.md` — sourced findings on choices per screen, icon labels, tap targets, typefaces and icon systems.
- `refs/lessons.md` and `refs/lessons-img/` — what changed when the rules met a real app and its owner's review.
- `examples/before-after/` — that app before and after, screen by screen.
- `refs/sheets/` (760 contact sheets), `refs/screens/` (4,536 screens of 78 apps, 375-pt iPhones at 488 px), `refs/user-refs/` (editor references): the reference library.
