# Study notes — one block per app (iOS). By Achref Arabi.

What each app does, measured from its screens: observations, not targets. Screen
references in parentheses are (sheet·position): (07·3) is `refs/sheets/<id>-<App>-07.jpg`,
third screen (positions run 1–6, left to right, top to bottom). Where a number here
differs from `SKILL.md` (many apps use 48–56-pt buttons, for example), the rules and
measurements in `SKILL.md` win, and the project's own tokens win over both.

## Spotify (001) · dark media player
- Stage #121212; the top of a screen takes a colour tint sampled from the artwork, fading to the stage within ~40% of the height. Header text sits on the tint.
- Now Playing: 16pt gutter, square artwork full width, title 24/700 + artist 16 grey, thin 2pt progress with time labels 11pt, control row of 5 (shuffle · prev · big filled play 64 · next · device), then a quiet tertiary row (cast, share, queue). "Lyrics" panel peeks at the very bottom as a card.
- Context menu (⋯): blurred artwork behind, small artwork centred, title + subtitle, then a plain list of actions (icon 24 + label 16, rows ~56pt), no card, "Close" text button at the bottom. Premium items carry a trailing pill badge.
- Queue: section labels 16/700, rows with a radio circle leading and a drag handle trailing; transport controls persist at the bottom.
- Rows: title 16/400 + subtitle 13 grey, ⋯ trailing at 24. ~52-56pt tall, no dividers.
- Rails: 3 items visible + a peek, artwork square, label 14 below, meta 12 grey. Section titles 22/700 with 12pt to the rail.
- Tab bar: 4 items icon+label 10pt; a mini-player (56pt, artwork 40) docks above it.
- Share: preview card centred on a flat colour, three round action buttons (56) with labels under.
- Toasts: white pill with dark text, 14pt, with a trailing action ("Change").
- *From the full library (sheets 01–10):*
  - Context menu rows measure a 64-pt pitch, not ~56: icons at y 473 · 537 · 601 · 672 pt; icon 24 + label 15, Premium pill trailing; on long menus the art and title scroll away and the Shuffle · Repeat · Go to queue toggles (icon 24 + 11 label) shrink into a strip under the status bar (01·2, 06·2).
  - Queue: × left, context name 13/700 centred; "Now Playing" and "Next In Queue" section titles 15/700; outlined "Clear queue" pill ≈28 on the section line; rows ≈64 pt (radio 20 leading, title 15 + 13 grey, drag handle trailing); transport row pinned at the bottom. Selecting rows swaps the transport for a text bar "REMOVE · ADD TO QUEUE" 13 caps (01·3, 02·2, 09·3).
  - Add to playlist is a full-screen dark sheet: Cancel 13 · title 15/700 centred; white "New playlist" pill ≈48 hugging, centred; one row with 49-pt thumb and a green check; green "Done" pill ≈50 hugging, centred at the bottom (06·3).
  - Naming a playlist: dark sheet with × disc, prompt 15/700 centred, the input itself ≈32/700 centred on a 1-pt hairline, green "Create" pill ≈40 hugging under it, keyboard up; default text arrives pre-selected (08·2, 08·6).
  - Premium upsell as a half sheet over the dimmed page: art tile 93, title 17/700, two lines 15 grey, green "Explore Premium" pill 36 tall hugging its label, "Stay on Spotify Free" 13/700 text under (07·1).
  - Artist page: photo full-bleed to ~288 pt with the name ≈48/800 on its lower-left edge, "10,654,701 monthly listeners" 13 grey, outlined "Following" pill ≈28 + ⋯, green play disc ≈52 on the right; the collapsed header keeps the play disc straddling its bottom edge (10·2, 10·1).
  - Sleep timer and Connect: full-screen blur of the art, "Stop audio in" 17/700, durations as plain 15 labels at a 64-pt pitch, "Close" centred at the foot; device sheet: "Current device" 20/700 + green 15 sub, rows icon 24 + 15, volume slider pinned at the bottom (10·4, 03·5, 07·3).
  - Confirmations come in two forms: a white full-width bar ≈40 above the mini player with a green trailing action ("Added to Liked Songs · Change"), and a dark 112-pt square HUD with a large check for timers and copied links (03·2, 10·3, 03·6, 04·3).

## Airbnb (002) · light marketplace
- White canvas; the only accent is coral red, used for the active tab, the price emphasis, and the Reserve button.
- Search header is a pill (56pt) with two-line text (title 15/600, sub 13 grey) and a trailing filter disc with a count badge.
- Result cards: image 4:3 with 12pt corners, overlay chips top-left ("Guest favorite" white pill 13/600) and a heart top-right; below: title 15/600 + rating right-aligned, 2 lines of 14 grey, dates, price 15/600 with strikethrough previous. Card gap 24.
- Map view: price pills (white, 13/700, black on selected), bottom sheet with "6 homes" grabber, card inside.
- Filters sheet: title 18/700 left; sections 17/700 with 20pt above; steppers as 32pt outlined circles (− value +); amenity chips as outlined pills with icon (40pt); a range slider with a histogram above; sticky footer "Clear all" text + black filled button with the live count ("Show 82 homes").
- Calendar: month title 15/600, day cells 40pt, selected as a black disc, range as light grey; quick chips under (± 3 days) as outlined pills.
- Detail: hero photo edge to edge, sheet with 24pt radius slides over it; title 24/600 centred; meta 14 grey; sticky footer: price left (strikethrough + bold), Reserve button right (coral, 48).
- Segmented control: 3 text options in a grey pill; selected is white with shadow.
- Tab bar 5 items, icon 24 + label 10, coral for active, red dot for badges.
- *From the full library (sheets 01–10):*
  - Gutter is 24, not 16: home rails, detail and every filters sheet start content at 24 pt (rail x 23.8, "Clear all" x 24.6, footer button right edge 351) (04·3, 02·6).
  - Home rails: category icon tabs (Homes · Experiences · Services, 36 icons + 11 labels, NEW badge) over near-square tiles 159 × ≈151, gap 11, two visible + a 12-pt peek; section title 20/600 with a trailing ›; overlay "Guest favorite" chip 11/600 and heart on the photo (04·3).
  - Stepwise search: collapsed steps as white 56-pt cards (grey label left, value right); the open step is a card inset 12 from the edges with a 26/700 title, a 41-pt segmented control (Dates · Months · Flexible) and a 3-D dial for months; footer "Reset" underlined + ink "Next" 130×46 (01·1, 05·5, 08·3).
  - Who step: 4 stepper rows at 73-pt pitch, 30-pt outlined circles, disabled "−" in light grey, 11 grey age line under each label; footer "Clear all" + coral "Search" 46 with a magnifier (08·2).
  - No results: map with "No exact matches" sheet, then one 13 grey sentence and a wrap of outlined "Remove <filter>" chips 42 tall with 8-pt gaps, one per active filter (02·3, 05·4, 10·5).
  - Loading: a skeleton (grey pill header, grey sheet title bar and grey card) instead of a spinner (09·5); detail title shows at once with a three-dot loader under it (01·3).
  - Confirmations are anchored to the footer: a white floating pill "✓ Coupon claimed · View details" 44 sits just above the Reserve bar (05·6); the promo that triggers it is a white card with × and a grey full-width "Claim" 36 (04·4, 08·4).
  - Destination suggestions: rows at ≈70 pitch with a ≈52 tinted tile holding a line illustration, 15/500 title + 13 grey reason ("Because your wishlist has stays in Cleveland") (04·2, 06·2).

## Headspace (004) · warm illustrated wellness
- White canvas, section title 22/700 ("Start your day"), timeline rail on the left (dot + dashed line) linking cards.
- Cards: white with 1pt border and 12pt radius, content left (title 17/700, two meta lines with small icons 12), illustration right in a fixed 120×90 box. Lock glyph inline in the title for gated content.
- Dark theme variant keeps identical geometry; only surfaces change.
- Paywall: big illustration, title 24/700, 4 check lines, two plan cards (selected filled orange with a "Best value" chip), full-width blue pill CTA 56 at the bottom.
- Empty search: small mascot illustration, "No results for 'x'" 15/600, one grey line, nothing else.
- Explore: full-width coloured banner tiles 64pt tall with a title 15/700 and an illustration bleed on the right; 8pt gaps.
- Tab bar 3 items only.
- *From the full library (sheets 01–10):*
  - Content detail: illustration hero inset 8 pt with rounded corners (~240 tall), back as a 32 white disc over it; title ≈28/700 + heart right; one 12 grey meta line with a type glyph; body 15 grey; "Related" 17/700 with 2-up tiles; pinned blue pill 50 tall at 23-pt gutters ("Play", or "🔒 Start My Free Trial" when locked) (09·5, 01·4, 03·4).
  - Explore root: outlined search field 56 tall at 16 gutter; a scrolling row of 40-pt grey chips (walk, relax, happy…) clipped at the edge; 2×2 category tiles 164×73 with 16-pt gaps, label ≈17/700 white centred; then a programme card ("Guided Program" outlined 11 tag, three 12 meta lines with icons, portrait bleeding off the right) (09·2, 06·4).
  - Favorites / Recent: header 17/600 centred, then a cream band with one 13 grey centred sentence ("Find all your favorite meditations…"); rows on a 79-pt pitch with 85×57 (3:2) thumbs, title 15/600 with inline heart and lock glyphs, 12 grey meta, chevron. Empty Recent is only that band sentence, nothing else (02·6, 06·6).
  - Audio player: full-bleed illustration, × top-left and volume top-right; centred play/pause glyph ≈40 flanked by ↺10 / ↻10 glyphs ≈30; thin scrubber near the bottom with elapsed left and "−0:39" remaining right in 11 grey; AirPlay and ⋯ above it at the right (04·6, 08·3).
  - Animation player uses a story-style segmented progress bar at the top plus subtitles as dark caption chips over the art; "BUFFERING…" in 11 tracked caps under the stage while loading (03·1, 09·1, 05·3).
  - My progress: filter chips "stress / anxiety" ≈30 outlined with a colour dot, selected dark; the empty chart is a blank month grid with an outlined card over it ("Start tracking your stress over time with monthly check-ins" 13) and one full-width blue "Check in" pill 44 below (04·5, 06·5).
  - Coachmark: dark card with a pointer to the bell icon, title 14/700 + 13 body + × right, laid over the home timeline (08·1).
  - Loading: a detail screen shows its skeleton (grey rounded bars in the title/body positions, hero block) with the CTA pill kept and a spinner inside it; other routes show a lone centred spinner on white (08·5, 03·2, 06·1).

## Duolingo (005) · playful learning
- One lesson screen = progress bar (8pt, rounded, green) + close × on the left + hearts count on the right; then an eyebrow chip ("NEW WORD" 12/700 purple with icon), then the question 20/700, then the exercise. Nothing else.
- Buttons: full-width 48–52pt, 16pt radius, all-caps 15/700 label with letter-spacing, a 3–4pt darker bottom edge for depth; disabled state is grey with grey text. Word tokens are 40pt chips with a 2pt border and the same bottom edge.
- Selection cards (pick an image): 2×2 grid, 16pt radius, 2pt border, illustration on top, label 15 below; selected turns blue.
- Streak/celebration screens: one big illustration centred, headline in colour 22/700, one card of context, CTA at the bottom.
- List (courses): white card with dividers, flag 32 + label 16/700, 56pt rows.
- Home path: nodes 64pt discs on a vertical path, locked nodes grey; top bar shows currency chips.
- *From the full library (sheets 01–10):*
  - Answer feedback rises as a tinted bottom band ≈160 tall (green "Nicely done!", red "Incorrect", yellow "We'll skip…"): title ≈20/700 in the state colour with a ✓/× disc, "Correct Answer:" 15/700 + answer 15, share · discuss · flag icons 20 top-right, and the 49-pt CTA recoloured to the state ("CONTINUE", "GOT IT") (04·5, 07·2, 06·4).
  - Session summary: illustration ≈260 tall, "Lesson complete!" ≈24/800 in yellow, then 3 stat tiles 94 wide with 27 gaps (≈80 tall, 2-pt coloured outline, a filled eyebrow tab 10/800 caps "TOTAL XP" / "COMMITTED" / "GOOD", value 15/700 with icon), CTA 49 pinned at the bottom (06·6, 03·4).
  - Sign-up is one question per screen: back arrow + 8-pt progress bar, question 20/700, one grey field ≈44 with a 2-pt border and a blue check when valid, NEXT 49 placed 12 under the field when no keyboard is up; the password step pins "CREATE PROFILE" low with a 13 grey legal line centred under it (02·4, 07·6, 04·3).
  - Goal picker: 4 options in one outlined card, rows ≈62 pitch, label 15/700 left + adjective 15 grey right; selected row tinted pale yellow with a 2-pt orange border and a check badge on its corner; mascot + speech bubble below states the payoff ("7x more likely") with the number in orange (03·5, 04·1).
  - Out-of-hearts blocker: the lesson dims and a white bottom panel (≈270) rises: title 20/700 centred, 2 lines 15 grey, one blue CTA 49 "REFILL FOR FREE"; no Cancel, the × stays in the dimmed header (10·1).
  - Discussion thread: rows avatar 32, name 15/700 blue, body 15, score 13 grey + up/down chevrons 20; replies step right ≈16 per level with a grey rail in the gutter; the prompt card at the top (speaker disc 32 + sentence 15/700 + translation 15) and "748 comments" 13 grey (08·6, 02·5).
  - Loading: mascot ≈80, "LOADING..." 13/700 caps grey tracked, one tip 15 grey centred, tab bar kept (05·5).
  - Course switcher drops down under the green stat bar: flag tiles ≈64×44 with 13/700 labels, selected with a 2-pt blue border, "+ Course" outlined; the path behind is dimmed grey (01·3, 06·3).

## Pinterest (008) · image grid
- Masonry 2 columns with 8pt gap, 16pt corner radius on every pin, ⋯ under each pin bottom-right at 12pt.
- Top: tiny logo + two text tabs ("Browse / Watch") with a 2pt underline.
- Toasts: black rounded pill at the top with white 14/600 text, optional leading thumbnail and trailing "Edit" chip; feed toasts are inline dark cards replacing a pin with "Undo".
- Long-press: radial menu of 44pt white discs around the touch point, the primary (save) is the red disc, with a big "Save" label.
- Selection mode: "1 selected" 24/700 centred, selected pin gets a 3pt black border with a check; bottom tool row of 4 grey 44pt discs.
- Forms (Create board): field label 13 grey, value 17, toggle rows with a 13 grey sub-line; primary "Create" as a red pill 40pt top-right.
- Contact lists: avatar 40, name 16/700 with the matched part bold, red "Send" pill 36pt trailing.
- Tab bar 5 icons with 10pt labels; the centre "+" is just another icon, not raised.
- Error dialogs: white sheet from the bottom with title 22/700, body 15, one red pill button.
- *From the full library (sheets 01–10):*
  - Board page: title ≈30/700 centred, collaborator avatar stack 32 + "+" disc, "Secret board" 13 grey with a lock; three grey rounded-square action tiles 68×72 (icon 24 + 11 label) with 12 gaps; "1 Pin" 17/700 with 12 to a 2-col grid of 178-wide tiles at a 7-pt edge; floating white "+" disc ≈56 bottom centre (08·5, 03·3).
  - Send Pin: outlined search pill 44 inset only 8 from the edge; rows pitch 60, avatar 44, name 17 with the matched part bold, red "Send" pill 58×45 at an 18 right edge; sent state turns the pill grey "Sent"; an unreachable email row greys both label and pill (01·4, 06·2, 07·2).
  - Report Pin: flat list, title ≈17/600 + 13 grey reason, chevron trailing, pitch 59 with a one-line reason and 69–78 with two, no dividers, × + 15/600 centred title (10·4).
  - Move and filter sheets: plain text rows 17/600 with no icons, 13 grey group labels ("Your boards", "Filter by type", "Set view as"), check trailing on the selected row, and a grey "Close" pill ≈44×64 centred at the foot instead of an × (08·6, 09·6, 07·3).
  - Reorder mode: "Select or reorder" 22/700 centred, tiles with a white "=" handle top-right, grey "Select all" pill top-right; the bottom row of 4 discs 36 stays pale grey until something is selected, then turns black (02·2, 03·1, 10·5).
  - Notes editor: title 28/700 ("Add a title" placeholder), checklist rows with a 20 checkbox, a toolbar above the keyboard (Aa · add pin · checklist · trash right); "Done" red pill 36 is grey while empty (01·1, 02·6, 04·6).
  - Tune home feed sheet: × + 15/600 title, text chips Boards · History · Topics with a grey pill on the selected one; topic tiles 2-col with white overlay labels and a grey full-width "Remove" pill 36 under each (06·1, 08·3).
  - Empty board notes: "No notes on this board (yet)" 22/700 centred, a 13 grey paragraph of 4 lines, red pill "Create your first note" ≈40 low on the screen (09·2).

## Apple Music (026) · iOS native reference
- Playlist: numbered rows (number 15 grey, title 15/400 caps for this album, ⋯ trailing), 44pt rows with hairline insets; the playing row is tinted with the accent surface and the number becomes a star. Header: back chevron red, title 17/600 centred, + and ⋯ as small grey discs.
- Browse: section titles 20/700 with a chevron ("Hip-Hop ›") and 12pt to a 2-up rail of 16:9 videos with 8pt corners, title 15 + artist 13 grey under.
- Mini player docked above the 5-item tab bar: artwork 40, title 15/600, one-line eyebrow "2 LISTENING" 11 caps grey, play/forward icons. Tab bar uses red for active.
- Empty search: "No Results" 17 grey centred, nothing else. Error: one grey line and an outlined "Try Again".
- Feature page: hero illustration on a colour, then title 34/700 and running body 17/400 with 24pt line height.
- *From the full library (sheets 01–10):*
  - Curated playlist header: full-bleed artwork to ~390 pt with a glass search field and glass back/download/⋯ discs over it; centred title 17/600 + curator 17 grey + "UPDATED FRIDAY" 11 caps; two grey pills Play · Shuffle 157×48 with a 21-pt gap on a 20-pt gutter; 2-line description 13 grey ending in "MORE"; rows start right under (05·6).
  - Top Songs chart: large title 34/700 with "All Genres" as red 15 text top-right; rows 56 pt = thumbnail 48 + rank number 15 + title 15 + artist 12 grey + ⋯, hairline inset from the title; the Charts root shows 4 ranked rows then a City Charts rail (05·5, 08·6).
  - Search root: title 34/700 + avatar 32 right, grey field 36, "Browse Categories" 20/700, 2-column tiles 163×113 with 8-pt gaps, 12-pt corners, label 13/600 white bottom-left on the image, no caption under (05·4).
  - Radio: title 34/700 + avatar; station heading 20/700 + 13 grey tagline + a 28 calendar disc right; hero card 335×325, 12-pt corners, bottom band holds "LIVE · 4–6AM" 11 caps, show title 15/600, 2-line 13 and a 28 play disc (08·5).
  - Context menu (glass card ~200 wide under the ⋯ disc): rows 44 = label 15 + trailing glyph 20, groups split by 8-pt grey bands; "Sort By" opens inline as a nested list with a check; destructive "Delete from Library" sits first, in red (09·3, 03·3, 07·2).
  - Empty Library: no glyph, a 3-line 15 grey sentence centred and one red filled button 292×50 "Browse Apple Music" 41 pt below; "Edit" as red text top-right (06·5).
  - Confirmations are tiny white pills (~110×36, glyph + 13/600 "Loved", "Added to Library") centred over the list, not full toasts (06·1, 03·4).
  - Delete confirm is an iOS action sheet: 13 grey question, red "Delete Playlist", separate white card "Cancel" 17/600, 8-pt inset from the edges (10·3).

## Halide (027) · pro camera, dark
- Viewfinder fills the screen; overlays are 1pt yellow guides and a small histogram. Controls live in two black bands: a thin band of 3 tiny icons, then the main band (rotate, mode disc, +; exposure ruler with a 0.5 readout 13/700; thumbnail 56, shutter 72 white ring, "2×" lens disc).
- Settings: grouped forms on black; radio cards (checked = green disc), option rows 44pt with a 1pt divider, section labels 13 grey, explanatory 13 grey text between groups. Tech readout: icon 20 + label grey + value right-aligned 15/600.
- Support list: icon 24 + title 17/600, 13 grey description under, 1pt dividers.
- Photo review: black stage, format chips (HEIC · DNG) as 1pt outlined tags 11 mono-ish, meta right (date, place), a row of three readouts (1/833 · ISO 25 · 26mm) with hairline separators, then three icons (heart, share, trash).
- Yellow is the only accent: selected RAW+ chip, exposure marker, subscribe button.
- *From the full library (sheets 01–10):*
  - Edit-exit bar replaces the quickbar: two stacked full-width pills 44.6 tall, inset 36 from each edge, 16 gap; "Done" light grey #e6e6e6 with ink label over "Discard Changes" #373737 with white label, on a #121212 band (01·3, 07·1).
  - Settings root is a sheet over the camera with a chevron grabber: a promo card first ("What you can do with Halide", illustration 56 + 17/600 + 13 grey), then "Settings" group rows icon 30 + 15/600 + 13 grey two-line description at a 77-pt pitch, then "Information" rows single-line ≈48 with icon 24 (03·6, 06·2).
  - Manual-mode explainer: white card inset 20 over the blurred live view, radius ≈24, "M" glyph in an 80 ring, title 17 tracked caps, 15 grey paragraph, three gesture rows (grey tile 48 + 17/600 + 13 grey), outlined "Continue" pill ≈44 (06·3).
  - Mode switch appears as a vertical stack of three dark rounded tiles (≈64) on the viewfinder's right edge: yellow outline glyph + 10 tracked-caps label (AUTO · MANUAL · ZEBRAS) (04·5, 08·2).
  - Transient state is one word in 11-pt tracked caps grey centred in the control band ("DAYLIGHT", "FLASH ENABLED", "WAVEFORM"); white balance swaps the quickbar in place for 5 preset glyphs with a two-line "WHITE BALANCE" caps label left and "AWB" in yellow (03·5, 07·5, 08·3).
  - Photo info: the review sheet drags up into 11–13 key-value rows, label 13 grey left, value 13 white right, ≈24 pitch, no dividers, over a blurred copy of the photo (05·3, 06·6).
  - Alternate icon picker (membership perk): sheet #1a1a1a, "Set Icon" 15 centred, icon ≈120 centred, name 17 tracked caps, one 13 grey line, 6 page dots, "Cancel" text over a white "Set Icon" pill ≈48 at 12 gutter (03·3, 10·4); membership page: "Active Member" card 95 tall #2c2c2c, two light-grey pills ≈54 stacked 7 apart (09·1).
  - Technical readout: device illustration, "IPHONE XS" 20 tracked caps, section eyebrows 9 caps with a lens glyph, rows ≈40 tall = grey icon 20 + label 13 grey + value 13 white right, hairlines (02·6, 09·3).

## ChatGPT (029) · quiet assistant
- Canvas white; header is just a menu glyph + title 17/600 + compose glyph. No dividers.
- Messages: user bubble grey #F2F2F2 with 18pt radius right-aligned, assistant text as plain body 16/400 on the canvas with 24pt line height; action icons row (copy, speak, up, down, share) at 20pt grey under each answer. Bold inline for labels ("When:").
- Composer docked at the bottom: "+" disc 40 grey, pill field 44 grey with placeholder, mic icon inside, black disc 36 for voice on the right.
- Voice mode: full white screen, one animated blue sphere, two 56pt discs at the bottom (mute, close).
- Drawer: search field, three entries with icons, then plain 16pt text history rows 40pt tall, account row pinned at the bottom.
- Cards inside answers: 1pt border, 12pt radius, title 15/600 + 13 grey + progress line + outlined "Details" pill.
- Search suggestions: title 16 + one 13 grey line with the match bold.
- *From the full library (sheets 01–10):*
  - Composer states: idle = "+" disc 44 grey + pill field ≈45 (placeholder 15 grey, mic glyph inside) + ink voice disc 36; recording = stop square disc left, waveform inside the field, ink send-arrow disc right; transcribing = spinner + "Transcribing" 15 grey, send disc greyed (03·2, 04·6).
  - Mode and quote chips live inside the composer: the field grows into a grey card with a blue "Study ×" chip or a "↪ Soviet President Gorbac… ×" quote chip above the text line; no separate bar (04·1, 09·6).
  - Tools sheet from "+": grabber, "Photos" 15/600 + blue "Show All", rail of ≈80 square thumbnails with a grey camera tile first and a select ring on each, hairline, then 6 plain rows (icon 20 + label 15) on a 48-pt pitch, no chevrons, no dividers (05·4).
  - Long-running research shows as an in-thread card (1-pt border, 12 radius): title 15/600, "24 sources" 13 grey, a 4-pt ink progress bar and an outlined "Details" pill; Details opens a sheet with a grey segmented "Activity · 26 sources" (white selected) and a timeline of icon 16 + 15 lines (01·4, 05·2, 08·1).
  - Explore: header title 17/600 centred + search glyph; chip row 34 tall (selected ink with white text, others grey); section "Featured" 20/700 + 13 grey subtitle; grey 12-radius cards 89–124 tall with 17-pt gaps (icon disc 56 + title 15/600 + 13 grey 2 lines + "By …" 12 grey); "Trending" as a numbered list 1–6 with a "See more ⌄" text link (03·6, 07·5).
  - Image viewer: black stage, header × · title 15/600 truncated with › + date 11 grey · ⋯, picture at its ratio, bottom band of 4 labelled tools (icon 24 + 10 label: Edit, Select, Save, Share) (05·3, 07·3).
  - Library: 2-column square grid of ≈187-pt tiles edge to edge with ≈1.5-pt gaps, white canvas fading at the bottom under one floating ink pill "Make Image" (04·2).
  - Feature intro sheets: gradient header holding two sample prompt bubbles, title 28/700 centred, 15 grey line, 3 benefit rows (outline icon 28 + 15/600 + 15 grey), ink pill ≈51 tall at a 24 gutter (09·3); announcement variant with × disc, 24/700 two-line title and an ink "OK" pill (04·4).

## YouTube (035) · dense but ordered
- Shorts: full-bleed video, a vertical stack of 5 actions on the right (icon 28 + count 11 white), creator row (avatar 32 + @handle 14/700 + red "Subscribe" 13/700 pill), caption 14, sound line; tab bar with a big outlined "+" as the centre item.
- Account: eyebrow chip ("Premium" 11 with logo), name 24/700, "Member since" 12 grey, accordion rows 48pt (icon 20 + label 15 + value right + chevron), expanded rows show a 13 grey explanation under.
- Comments sheet: header 17/700 with back and close; rows avatar 28, handle 12 grey + time, body 14, like/dislike row 12; composer at the bottom with the user's avatar.
- Permission explainer: dark overlay screen, two "why / control" rows with icons before the system prompt, one white pill "Continue".
- Feature/paywall: logo, one line 17, blue pill CTA, small print 12 grey centred; legal block 12 grey left-aligned.
- *From the full library (sheets 01–10):*
  - Downloads: summary block "Smart downloads" 15/600 + "151.6 MB Used · Updated today" 12 grey with a gear 24 right; rows on a 106-pt pitch: 16:9 thumbnail ≈144×81 with a duration badge 11 white on black, title 15 on two lines, channel 12 grey, status 12 in blue ("Downloading… 67%", "Waiting to download…"), ⋮ trailing (03·4).
  - Home top: wordmark + 4 header icons, then a chip row: a square compass chip 42 wide first, text chips 32 tall on grey with ≈11 gaps, selected "All" inverted to black/white; Shorts rail tiles 158×262 (≈3:5) at 11-pt gaps and a 12-pt gutter, title 14/600 white on the image + views 12 (04·2).
  - Toasts: dark bar 360×54 inset 8 pt from the sides and sitting ≈8 pt above the tab bar, text 14 white left, optional "Undo" 15/600 blue right ("Video removed", "Video deleted from downloads"); the same bar without action for "Thanks for reporting", "Copied" (04·1, 04·2, 04·6, 10·6).
  - Plan picker: title 17/700 centred, two outlined radio cards 75 and 86 tall at ≈10-pt gaps (plan 15/600 + price 13 + 11 grey note), bottom bar under a hairline with "Cancel" 15 blue text left and a blue "Confirm" pill 38 tall hugging its label right; success is a white centred card with a red check, then a system alert "You're all set." (03·5, 05·1, 09·6).
  - Report dialog: white card inset ≈36, title 17, five radio rows ≈39 pt with two-line labels, "Cancel" / "Report" as right-aligned text buttons, "Report" grey until a radio is picked (03·1, 05·4).
  - Menus over the Shorts player are floating white cards inset 8 from the edges: 3 rows ≈39 pt, icon 20 + label 15, no title, no Cancel (02·5, 06·2, 06·5); Share is the same card with a 17/700 title, app discs 40 with 11 labels and a "Copy link" row with a grey icon disc (06·1).
  - Premium benefits: "Explore benefits and offers" 28/700 on two lines + 15 grey sub, then full-bleed illustration panels each followed by a 20/700 title + 13 grey line; FAQ as an accordion with 15/500 questions and 13 grey answers, chevron right (04·4, 04·5, 08·3).
  - States: Shorts error "Something went wrong" 17 white + "RETRY" 13/600 caps centred over the dimmed frame (04·3); empty downloads = small illustration ≈64 + "Videos you download will appear here" 13 grey (05·3); coach mark = blue speech bubble 13 white pointing at the avatar (10·5).

## Instagram (041)
- Feed: stories rail (avatar 64 with gradient ring, label 11), post header (avatar 32 + name 14/700 + sub 12 grey + ⋯), media edge-to-edge, action row (heart, comment, send left; bookmark right) 24 icons, likes 14/700, caption 14 with the name bold, "View all N comments" 14 grey, composer row.
- Comments sheet: grabber, title 15/700 centred, hairline, rows avatar 32 + handle 13/600 + time grey, body 14, right-aligned heart 16 grey; an emoji quick row above the composer; composer = avatar + pill field + GIF chip.
- Follow list: avatar 44, handle 14/700 + name 13 grey + "Instagram recommended" 12, blue "Follow" 13/700 pill 32pt, × trailing.
- Crop: black stage, 3×3 grid overlay, a single outlined "Rotate" chip bottom-left; Cancel / Done text in the header.
- Meta account centre: icon 24 + label 15/600 rows 48pt, one blue full-width pill at the bottom.
- Success: soft gradient wash background, title 24/700, avatar 128 with a ring, outlined "Edit" chip, a toggle inside a white card with an explanation 13 grey under.
- *From the full library (sheets 01–10):*
  - Reel ⋯ sheet: two grey tiles 163×74 side by side (icon 24 + label 12: Unsave, Remix) 12 apart, then grey 12-radius cards of rows ≈53 pt (icon 24 + label 15), 10 pt between cards, "Report" red inside its group; gutter 18; a dismissible "We've moved things around" tip card sits in the stack (10·5).
  - Discover people: row pitch 82, avatar 56, handle 13/700 + verified badge, name 13 grey, "Instagram recommended" 11 grey, blue Follow pill 89×32 with 13/600, × 16 grey trailing; once followed the pill turns grey "Following" at the same size and the × goes (01·3, 06·4).
  - Followers sheet over the dark reel: title = handle 15/700, three text tabs (Mutual · Followers · Following) with a 1-pt ink underline on the active one, grey search field ≈36, rows avatar 44; empty result is one left-aligned 15 grey line "No users found" under the field, no glyph (06·1, 08·1).
  - Swipe left on a comment reveals two square actions ≈40 wide: grey reply arrow + red trash; after delete a full-width red bar ≈24 tall "1 comment deleted. Tap to undo." 13/600 white docks under the sheet title (10·2, 10·3).
  - Send sheet: search field with an add-people glyph, rows avatar 40 + name 14/600 + handle 13 grey + 24 radio circle; bottom rail of grey discs ≈58 with 11 labels 24 apart (Add to story, Share to…, Copy link, Messages), a white tooltip with a pointer explains the rail on first use (07·6, 09·1).
  - Reply mode: the composer pill grows into a card with "Replying to johnrefero ×" 12 grey on top and a blue "Post" 15/600 text button; the emoji quick row stays above (04·1, 08·6).
  - Pre-permission and "Remember login info?" screens share one template: centred title ≈24/700 on 2–3 lines, 12 grey paragraph, line illustration with the brand-gradient accent, 11 grey fine print, full-width blue 44 "Continue" (or "Remember" + "Not now" blue text); the system alert then appears over the same screen (04·4, 07·2, 10·1).
  - Loading: the GIF picker (nested sheet over comments) shows grey tiles with faint circle glyphs, then a spinner, then a 2-column grid with 4-pt gaps; the feed shows a small spinner between header and stories (05·1, 05·5, 01·4).

## Threads (042) · text-first feed
- Post: avatar 36 + handle 15/600 + verified, time 13 grey right, ⋯; body 15 with 20pt line height; media as 2-up with 8pt corners; action row of 4 outline icons 22 with 24pt gaps; "16 replies · 730 likes" 13 grey; replies indented under a hairline.
- Composer docked: avatar 24 + pill field "Reply to …" 40pt grey.
- Toast: black bar 48pt with check + "Posted" 14/600 and a trailing "View"; a spinner variant "Posting…".
- Share sheet: white rounded cards grouping rows (label 15 left, icon right), 2 groups separated by 8pt.
- Tab bar: 5 outline icons, no labels, active filled.
- *From the full library (sheets 01–10):*
  - Post overflow for someone else's post: sheet with grouped grey cards (rows ≈50, 12 radius, 16 gutter), "Mute" alone in the first card, then "Hide · Block · Report" with Block and Report in red; own-post overflow puts "Who can reply ›" and "Hide like count" in one card and red "Delete" alone in a second (03·1, 08·4).
  - Report flow: tall sheet, title 17/700 centred, question 15/700 + 13 grey paragraph, then 8+ reason rows 61 pt with hairlines and a trailing chevron; the finish is a sheet with a 48 gradient check, title 20/700, two icon + 13 rows and a blue full-width "Next" 44 (06·3, 02·5, 09·1).
  - Block confirmation sheet: 72 avatar disc, "Block pubity?" 24/700 centred, one 13 grey line, three consequence rows (outline icon 24 + 13 text), black full-width button 44 with 16 gutters (04·6).
  - Status confirmations sit on the object, not at the screen edge: a dark 30-pt capsule with 12/600 white text centred on the post's media ("Following", "Reposted", "Blocking", "Deleting…") (04·1, 04·5, 01·5, 07·4).
  - Hidden post leaves a placeholder in place: grey 12-radius bar, "This post has been hidden." 13 grey left + "Undo" 13/600 right, where the post was (04·4, 05·2).
  - Likes list: header "4,217 likes" 17/600 centred, rows 64 pt, avatar 40, handle 14/600 + name 13 grey, outlined "Follow" 104×32 with 8 radius and 13/600 label (10·6).
  - Composer is a modal card over black: "Cancel" 15 left, "Reply"/"New thread" 17/600 centred, avatar 36 + thread line, a paperclip 20 under the field, footer "Anyone can reply" 13 grey left and "Post" 15/600 blue right (faded until there is text) sitting on the keyboard (02·1, 05·3, 09·3).
  - Reply audience: a floating white menu over the keyboard (3 rows 36, no icons) or a sheet "Who can reply" 15/700 with a grouped card of 3 rows ≈42 and trailing radio 22 filled black when selected (02·6, 03·5, 09·4).

## Notion (064) · iOS grouped-form language
- Modal lists: title 17/600 centred, "Done" blue right; rows 44pt with a check trailing, grouped with hairlines.
- Export: settings rows (label + value grey right, toggle) then an action row in blue; the picker rises as a bottom sheet with 44pt rows.
- Page: cover image, emoji 44 + title 28/700, body 15 with 22 line height; a "Subscribed · Undo" black toast; bottom bar with 4 grey icons.
- Empty comments: grey outline icon 40, "No open comments yet" 13/600, one 13 grey line. Segmented "Open / Resolved" pill above.
- Share: tabs with 2pt underline, field, a grey info chip, "People with access" 12 grey label, rows avatar 28 + name 14 + email 12 grey + "Full access ⌄" right, blue full-width button.
- Paywall: logo, title 22/700, 3 benefit rows (icon 24 + title 15/600 + 15 grey), two plan cards with 2pt blue border on the selected one, blue CTA, three grey underlined links.
- *From the full library (sheets 01–10):*
  - Sidebar is the home: workspace row (square avatar 28 "S" + name 15/600 ⇅ + email 12 grey, ⋯ disc 24 right), "Jump back in" 13 grey label, a rail of 144×144 page cards (grey cover top half, icon 24, title 13/600 two lines) with 16 gaps, then "Favorites ⌄" / "Private ⌄ +" group labels 13 grey and tree rows 51 pt pitch (chevron · emoji 20 · title 16/500 · ⋯ · +); gutter 20 (04·4, 05·1, 06·2).
  - Long-press on a page: grabber sheet on grey, page row (icon + 15/600 + "in Recently viewed" 12 grey), then white cards inset 16: "Copy link" alone, then Favorite · Move to · Delete (red, trash icon) with rows ≈41, icon 20 + 15 (07·2, 08·1).
  - Actions page lists 12 rows 46 pt tall (icon 20 + label 15), groups split by 26-pt grey bands, chevrons only where a submenu follows, Delete last; a 12 grey "Last edited by …" footer row (02·1, 05·2, 09·2).
  - Role picker: rows 64 pt (title 15 + 13 grey description), 82 pt when the description wraps, check trailing, "No access" in red as the last row (10·6).
  - Restore dialog: centred white card ≈290 wide, title 15/600 centred, a bordered option card (13/600 + 11 grey + checkbox, border turns blue when checked), then two stacked full-width 40 buttons: red-tinted "Restore" and outlined "Cancel" (06·6, 09·3).
  - Search: grey field 36 + "Cancel" text; results grouped in a white card, rows ≈50 (icon 24 + title 15/500 + "in Reading List" 12 grey); sort opens as a floating card of 5 rows under "Best matches ⌄"; empty is "No pages found" 15/500 + 13 grey hint centred above the keyboard (04·6, 08·6, 06·3).
  - Toasts: dark pill 49 tall inset 31 from each edge above the tab bar, "Moved to Quick Note ›" 15/500 + "Undo" 15/600 right (10·4); a grey "Copied link to clipboard" pill low on the sheet (03·1); long tasks show a small white card "Exporting ◌" over the dimmed page (06·5, 05·5).
  - Cover picker: Remove (blue) · "Page cover" 17/600 · Close; text tabs Gallery · Upload · Link · Unsplash with a 2-pt underline; 12 grey group labels; 4-column grid of 81-pt tiles with 5-pt gaps in 16 gutters (05·6, 09·6).

## Craft (071) · document tool
- Editor: title 22/700 in link colour, body 16 with 24pt line height; a floating toolbar band above the keyboard with 6 glyphs; "Done" as a black pill 36 top-right.
- Space home: title 22/700 with a coloured square avatar 24, text tabs with 2pt underline, a rail of outlined action chips 44pt (icon + label), a grey group card "Recently viewed / Daily notes / Hide" with an empty-state dashed placeholder inside, then 2-up promo cards.
- Sheets: white card with a title 17/700, inputs 44pt grey, explanatory 13 grey, blue full-width button. Role picker sheet: title 15/600 + 13 grey description per option, check trailing, destructive red row last.
- Promo dialog: centred white card 24pt radius over a busy image, title 22/700, body 15 grey, blue button + "Not Now" text.
- *From the full library (sheets 01–10):*
  - Space screen: square space logo 28 + title 20/700, text tabs 15 (grey, active ink) with a 2-pt underline on a hairline; settings rows pitch ≈62 (title 15 + 12 grey sub), value 13 grey + chevron right; group titles 15/600 ("Space Details", "Notifications") with a hairline between groups (06·2, 02·4).
  - Every transient surface is the same floating white card inset 12 pt (card 351 wide), ≈16 radius, title 15/600 left + grey × disc 20 right, hairline under: invite, export format, activity, share, feedback, help (03·5, 07·5, 09·5, 10·2).
  - Option groups inside those cards use grey inner cards with 11 uppercase grey labels ("DAILY NOTES", "EXPORT / IMPORT"), rows 44 with a trailing outline icon 20 (04·2, 06·6, 09·4).
  - Toasts are white cards under the status bar, ≈40 tall, title 13/600 + 11 grey line ("Success · User Role Updated"; "Could not update member role · Current user is the only owner") (05·5, 06·5, 07·4).
  - Loading shows three forms: a spinner over the invite card, a progress card with a thin blue bar and "Item 2 of Total 6" 11 grey, and blurred skeleton rows keeping the member-row shape (01·3, 05·3, 05·6).
  - Primary inside a card is full-width blue ≈44, pale blue while disabled (no member selected, empty invite fields) (04·1, 08·3, 10·5).
  - Feedback card: 5×2 grid of emoji 36, selected ones on a blue disc, "Anything we could do better?" 15/600 + 12 grey, text area, full-width "Send Feedback" grey until filled (04·6, 10·1).
  - Highlight picker: popover of 5×3 colour discs 28 (gradients top row, pastels, "none" slash) above a keyboard toolbar of B · I · S · code · link (05·2, 07·3).

## Figma (072) · minimal tool
- Empty Activity: title 34/700 top-left, then centred "No activity yet" 15/600 + 13 grey. Nothing else; tab bar 4 items with labels.
- Settings: avatar 40 + name/email, section labels 15/600, rows 44 with chevrons, "Log out" plain, floating red record button stack for bug reporting.
- Search: title 34/700, grey field 40, section "Drafts ›" 17/700, 2-up file thumbnails 8pt radius with name 14 + "Drafts" 12 grey.
- Bug report: grey grouped form (label 13 + value 15), attachments as 56pt thumbnails with × badges, bottom sheet of three icon rows.
- *From the full library (sheets 01–10):*
  - Account screen has no grouped cards and no hairlines: avatar 40 + name 15/600 + email 13 grey, section labels 15/500 in black, rows at a 60-pt pitch, blue toggles, "Done" 17/600 blue top-right (07·1).
  - Recents: title 34/700 with a 28 avatar disc top-right; rows at an 81-pt pitch = thumbnail 88×64 (6-pt corner, 1-pt grey border) + name 13/500 + location 12 grey; no dividers (07·2).
  - Report a bug form: grey 44 header band (× · title 17/600 · send glyph blue), fields as label 13 grey over value 15 with full-width hairlines, attachments 64 squares with 16-pt gaps and blue × badges, a bottom sheet of 3 rows at 54 pt (blue icon 20 + label 15) (01·6, 05·3).
  - Screen recording state: stacked red discs bottom-right (mic 40, stop 40, timer 44 "00:12" 13/700 white) over the tab bar; a dark tooltip "Press record when ready" points at the disc (08·2, 04·3).
  - Help chooser: centred white card ~300 wide, "Need help?" 15/600, two option rows = blue glyph 18 + title 15 + 12 grey sub, "Cancel" 15 blue text (07·3).
  - Comment composer: field card on white, a row of 32 grey discs (@, Aa, link) and × + a 28 send disc in the file's colour; the dark canvas variant swaps the row for B / I / S / list format discs when text is selected (09·5, 08·6).
  - Activity with items: "Unread (1)" 13/600 left + "Mark all as read" 13 blue right; rows avatar 32 + bold name + 13 body + 12 grey time, red unread dot on the avatar (08·1).
  - Notification primer inside the file: dark card with a 16:9 illustration, title 15/600, 13 grey line, blue full-width 36 button + outlined 36 "Not now" (10·4).

## Revolut (074) · fintech, confident white
- Titles 28/700 left with 15 grey one-liner under; forms of grey pill fields 56pt with counter "0/50" 11 grey right and "Optional" 11 grey; sticky blue-violet pill CTA 56 at the bottom; secondary as pale tinted pill.
- Plan picker: tabs as text chips (selected white pill with shadow), hero card 16:9 with 16pt radius (title 28/700 white, price 15, tagline 13), "Top features" list in a white card: icon 24 + title 15/600 + 13 grey, 16pt gaps; black pill CTA with price.
- ID capture: full black, document frame with 12pt corners, state pill "Hold still" with spinner, label 20/600 white; result: photo, one line 15, blue "Submit photo" + outlined "Retake".
- Colour swatches: 40pt discs, the selected with a 2pt ring and a 4pt gap.
- Success: white rounded sheet rising with a big check and "Done!" 22/700.
- *From the full library (sheets 01–10):*
  - Yes/No question: title 28/700 three lines left, 15 one-liner, flag illustration centred, bottom strict pair of 56-pt pills at 16 gutter with ≈6 gap: "No" pale blue #e4f0fc with blue label, "Yes" filled blue #0766f4 (03·4).
  - Passcode: title 28/700 centred, 13 grey hint "6 to 12 digits", 6 blue dots ≈16, keypad digits ≈28/400 with no key shapes in 3 columns at ≈64 row pitch; delete glyph left of 0 and a blue 60 disc with → in the right cell once enough digits are entered (04·2, 06·3).
  - Errors: passcode mismatch rises as a floating white sheet inset 12 from the edges with red × 24, title 17/700, 15 grey two lines, one blue ≈52 pill "Change passcode" (07·2); date of birth turns the field pink with a 12 red "ⓘ Incorrect date" under it and the Continue pill goes pale (07·5); a blurry photo shows a red-outlined banner with a red ⓘ disc above the image (04·4).
  - Date of birth: three grey boxes side by side (Month · Day · Year) 58 tall, 11 grey label over 15 value, clear × in the focused box, numeric keypad under (03·6).
  - Use-case chips: 38-pt grey #e1e2e6 pills with emoji 14 + 13/500 label, 8–10 gaps, groups under 17/600 headers ("Everyday needs", "Global spending"); selected chips turn blue fill with white label; Continue floats over the scrolling cloud (07·6, 09·5).
  - Document choice: white card on #f7f7f7, two rows ≈58 = radio 20 (blue when chosen) + tinted icon disc 32 + flag + 15 label; "Continue" pill + blue text link "Change your citizenship" under (04·6).
  - Verification explainer: title 28/700 two lines, 3D face-scan illustration ≈150, a white card with two reassurance rows (icon 20 + 15), blue Continue (08·1); upload and success states are short sheets with a 24 ring or check + one 17/700 word ("Uploading", "Done!") (08·2, 02·4).
  - Search states: address lookup field with Cancel; empty result is a white card with a puzzle glyph and "No result found, enter address manually" link in blue (05·4); invalid input shows a magnifier illustration 56 + 15/600 + 13 grey centred (06·1).

## Opal (076) · dark utility with a gradient CTA
- Black canvas, cards #1C1C1E 14pt radius; row content: icon 24 + label 15 + value grey right + chevron; small info line 12 in violet with an ⓘ.
- The one CTA is a lavender-to-violet gradient pill 56; secondary rows are #2C2C2E pills.
- Idea rail: 3 equal square tiles 96pt (icon + 12 label) then "Work Time · Weekdays" rows with a violet "+ Add" chip.
- Day-of-week picker: 7 circular 36pt toggles, active white.
- Bottom sheets: title 20/700, radio cards with check discs, a nested "Try Opal Pro" card with a white pill.
- Support chat: black, assistant bubble #2C2C2E left, suggestion chips as dark pills above the composer.
- *From the full library (sheets 01–10):*
  - Idea tiles on Blocks are 109×54 pt (3 across with 8-pt gaps at a 16 gutter), not square: icon 20 over a 12 label below the tile (03·4, 01·3).
  - Survey: title 28/700 two lines left; 10 answer pills 44 tall stacked with 8-pt gaps on a #1C fill, 15/500 centred; the selected pill turns white with ink text; white 48 "Continue" pinned, or a "Skip" 13 grey text (05·2, 08·3).
  - Onboarding shows the real product inside an iPhone frame filling the top ~55%, then eyebrow "How does Opal work?" 13 grey, title 24/700, 15 grey body centred, 3 dots and a white pill ≈48 (02·1, 05·4, 07·4).
  - Paywall: 3 stacked plan cards ≈64 tall (name 15 + price 13 grey left, "only $1.92/week" 15 + "Free for 1 week" 12 grey right); the selected card is a lighter fill with a 1-pt white border; a white "80% OFF" badge overlaps its top-right edge; blue CTA ≈50 + "✓ No payment due now!" 13 grey (03·3, 09·2).
  - Live session sheet: hourglass art on a violet glow, "Focus Session" 20/700, "Remaining time 00:19:51" with a tabular value, timeline strip with 11-pt start/end times, two info tiles (11 caps grey label + 13 value), gradient pill 55 "Snooze" and red text "Leave Early" (02·4, 09·4, 10·6).
  - A running session docks as a bar above the tab bar ("Session · 00:19:56" 11 grey over "Focus Session" 15/600, ⌃ right), like a mini player (08·1).
  - Choice sheets use radio cards ≈76 tall with 11-pt gaps: icon tile 32, title 15, 12 grey 2 lines, check disc right; the gated option carries a lavender "PRO" chip 11 and a nested "Try Opal Pro" card with a white pill (06·6, 09·5, 01·6).
  - Support FAQ: title 28/700 two lines "Hey there. How can we help?", uppercase 11 grey eyebrows (FAQS, BROWSE TOPICS), grouped dark cards of ≈47-pt rows with chevrons (05·3).

## VSCO (107) · photographic, black on white
- Everything is type on white with photos: no borders, no cards. Section titles 17/600, tabs as text with 2pt underline, follow buttons as black 32pt rectangles (4pt radius) with 13/600 white.
- People suggestions: overlapping 3-photo collage 4:3 + avatar 88 over it, handle 13/600 + name 12 grey, Follow right.
- Profile grids 2 columns with 8pt gaps, images keep their ratio; handle 12 under.
- Report list: 15 rows 52pt with hairlines and chevrons only where there is a sub-menu.
- Confirmation sheets: title 20/700 two lines, 13 grey body, black pill "Dismiss"/"Report", outlined "Cancel".
- Toasts: full-width electric-blue bar 48pt with white 14 text and a check.
- Tab bar 5 icons, no labels.
- *From the full library (sheets 01–10):*
  - Onboarding interest picker: question 15/600 + "Select all that apply" 12 grey, 7 option rows 48 tall with 8-pt gaps and 24-pt gutters; unselected rows are 1-pt outlined white, selected rows turn grey-filled; black full-width pill 42 "Continue"/"Submit" 45 pt under the list, not pinned (08·1, 08·6, 10·5).
  - Notification permission explainer: black-and-white photo over the top ~60 %, title 20/600 left, 15 body at 24 gutter, black pill "Allow notifications" ≈48 with an outlined "Not now" of the same size under it (01·6).
  - Profile: name 28/700 left with avatar 64 right (a "MEMBER" 9-pt badge under it), grey "Following" and black "Message" pills 28, text tabs 13 with a 2-pt underline, then a 2-column masonry of 164-wide images with a 15-pt gap at 16 gutters (07·4, 02·5, 10·3).
  - Block confirmation is a full-width orange sheet: title 17/600 white, 13 white body, outlined "Cancel" + white filled "Block" pills 44 as a strict pair; the result toast is an orange 44 bar for block and electric blue for unblock (06·1, 08·3, 01·4).
  - Loading: skeleton rows of a grey 44 circle, two bars (72 and 40 wide) and a 60-wide trailing block; the empty version pins "Find people you know" 15/600 + 13 line + outlined 32 "Sync your contacts" above the tab bar (10·6).
  - Promo sheet: title 20/400, 15 body, grey "DISMISS" 13 text left and black "LEARN MORE" pill 40 with 13/600 uppercase right (06·2, 06·3).
  - Discussion sheet: "Discussion" 17/600 centred with × 24, empty state "No responses yet." 17/600 + "Start the discussion." 12 grey centred, grey pill field "Join the discussion…" 40 docked; posted messages are black bubbles right-aligned with "You" 10 under (05·5, 09·2, 05·2).
  - Share options sheet: "Share Options" 15/600, 4 icons 24 with 12 labels in one row, then a plain "Report Journal" row and grey "Cancel" text (02·2).

## TikTok (116)
- Feed: video full-bleed; top text tabs "Following · For You" 15/600 white with the active underlined; right rail avatar 48 with a red + badge, then heart/comment/share 32 with counts 12; bottom-left handle 15/700, caption 14, "Add song" chip; tab bar 5 with a white/coloured "+" pill in the centre.
- Profile: avatar 96 centred, @handle 15/600 + verified, three stats (number 17/700 over label 12 grey), action row of grey pills (Send a 👋 · person icon · ▾), bio 13 centred, tab icons row with underline.
- Share sheet: title 13/600 centred, avatars row (name 11 under), app icons row (48 discs with brand colours, 11 labels), grey utility discs row (Report, Block…).
- QR card: white card 20pt radius on a brand gradient, two grey glass buttons under.
- Empty search: outline icon 64, "No results found" 15/600, 13 grey line.
- Suggestions list: avatar 48, name 15/600, handle 13 grey, meta 12 grey, pink "Follow" 13/600 pill 36×80.
- *From the full library (sheets 01–10):*
  - QR share card: brand gradient ground that cycles on tap ("Tap background to change color" 11 grey); white card 309 wide inset 32 with the avatar 56 straddling its top edge, name 15/600, QR ≈140, caption 11 grey, wordmark; under it two white tiles 150 × ≈70 with 10 gap (icon 24 over 13/500 label: Share profile · Copy link) (02·3, 06·2, 07·3).
  - Pre-permission sheets: white sheet with × 24, illustration ≈120, title 20–22/800 centred, 13 grey sentence, optional toggle row, then a pink pill ≈44 full width minus 32 (x 32–343) (03·2, 06·1). The notification pre-prompt is a card with a strict pair: grey "Not now" + pink "Get notified", each ≈150 × 43 (03·5).
  - Own profile action row: three grey buttons 44 tall, 117 / 131 / 44 wide with 4-pt gaps (Edit profile · Share profile · add-friend icon); "+ Add bio" grey chip ≈18 under; another user's profile swaps in a pink "Follow" 111 × 45 + grey "Message" + ▾ square (02·6, 03·6).
  - Suggested accounts: rows on a 76-pt pitch, avatar ≈56, name 15/600 + handle 13 grey + meta 12 grey, pink "Follow" pill 30 × 89 (13/600); followed rows switch to a grey "Following" pill of the same size (02·4, 04·5).
  - Empty Following feed becomes a carousel of trending creators: dark card ≈225 × 300 playing the creator's video, avatar 56, name 15/700 + handle 12 grey, pink "Follow" ≈36 across the card, × in the corner, neighbours peeking (04·1, 05·4).
  - Send to sheet: grey search field 36, "Find friends" row with a 40 pink disc, recipients with a trailing radio that turns into a pink check, then a message field, an emoji quick-reaction row and a full-width pink "Send" ≈44 (06·5, 09·3).
  - Notification settings sheet: grouped white cards on grey, radio rows ≈42 with a filled pink radio; report flow sheet: back + title 15/700 + ×, reason rows 15/600 with chevrons at ≈40 pitch (08·5, 08·6).
  - Toasts: dark grey pill at the top with a check ("Copied"), text-only variants ("No more suggested accounts"); follow alerts arrive as a white banner card with avatar 36 and a pink "Follow back" text action (05·6, 05·3, 02·1).

## Claude (119) · warm editorial
- Cream #F0EEE6 canvas, serif display (title 30/400 two lines centred), sans body; dark variant #2B2A27 with the same layout.
- Form: pill field 52 grey with a flag, a toggle row inside a grey card ("I am at least 18") 13/600, terracotta button 52 with 15/600, small print 12 grey centred, underlined link. Validation: 12 red under the field, and the button stays.
- Settings: white grouped rows on cream, a dropdown menu card with 13 grey version line, rows with ↗ external icons, red "Log out" with icon.
- Chat: user prompt as a dark pill bubble, assistant as serif 17 with 26pt line height; images as 2-up 96pt thumbnails with the sender name 13/600 above; composer card with three small icons and placeholder "Reply to Claude 3.5 Sonnet".
- *From the full library (sheets 01–10):*
  - Home: wordmark 22 serif centred + 32 avatar disc right; serif greeting ≈32/400 in two centred lines; a 31-pt outlined plan banner ("Limited daily messages on Free plan" 12 + "Upgrade" 13/600 violet); recent chats as cream cards 64 tall, 7-pt gaps, 13 inset, serif title 15 + 11 grey "Last message 13 seconds ago"; composer sheet 88 with a 12 grey limit line above it (02·4, 04·3).
  - Long-press on a chat card blurs the screen, lifts the card and floats a two-row menu (Rename, Delete) with an 11 grey header; Rename opens the iOS alert with a field (03·5, 05·3, 04·2).
  - Errors live in the thread as tinted cards at 16 gutter: 15/600 title in red, 13 body centred, one small grey pill 28 ("× Dismiss", "↻ Retry") (05·4, 08·6).
  - Loading is a lone 64-pt arc spinner centred on the brand ground, no text (01·5, 05·5).
  - Paywall: night violet ground, line illustration ≈120, serif title ≈28 violet, 4 check rows 13, "Auto renews for $20.00 per month" 13 with the amount bold, full-width pill 55 at a 10 gutter, 11 legal links (10·1). Upgrade is violet everywhere, never the terracotta brand (02·1, 09·1).
  - Account form: 13 grey label over a 52-pt white field with a 1-pt border, terracotta "Update Profile" 53, then "Account actions" 13 grey and a plain icon + "Delete Account" 17 row (05·6).
  - Attach sheet: "Add content to chat" 15/600 + 12 grey line, three dark 58-pt rows (icon 20 + 15/600 label), 8-pt gaps, 16 gutter (06·5).
  - Onboarding: serif paragraph 17 left, a field card "Nice to meet you, I'm…", terracotta Continue ≈42 with "You can always change this later" 13 grey; then acknowledgement cards with 24 icons and one "Acknowledge & Continue" (05·2, 06·1, 02·5).

## Uber (124) · black-and-white utility
- Rows: leading grey disc 40 with a star, title 15/600 + 13 grey, hairline; a blue link row ("Add Saved Place") with a 12 grey explanation and chevron.
- Ride sheet over the map: title 17/700 centred, rows with vehicle image 64, name 15/600 + ▲ count, price 15/600 right, "Pickup at" 13, tagline 13 grey; section labels 17/700 ("Popular", "Economy"); the selected ride gets a 2pt black border card; "Add Payment Method" row; black pill 56 with two lines (label 17/600 + 12 sub).
- Map header chip: white pill with a people icon + address + chevron; back button as a white disc 48.
- Forms on black: label 12 grey, value 15, × clear, black toast pill.
- *From the full library (sheets 01–10):*
  - Bottom-panel dialogs replace alerts: the screen dims, a white panel rises with title 17/600 centred over a hairline, body 15 left, black button 57 tall and a grey "Cancel" 57 (or text) under it ("No payment set", "Incorrect card number", "Are you sure?") (02·2, 02·4, 07·2).
  - Payment options: two segment pills 48 tall × 126 with 8 gap (icon + 15/600), selected black with white text, the other grey; section titles 17/700; "+ Add payment method" rows 15/500; "See details" grey chip ≈30 right of a section title (05·5, 07·3).
  - Fare breakdown: × then large title 28/700, a 13-pt paragraph, label/value rows at 64 pitch (label 15/500 left, value 15 right, hairline), 13-pt footnote (06·4).
  - Confirm pickup: map takes ≈75 %, the pin carries a blue label pill 13/600 ("Pickup on Melrose Ave"); sheet title 17/600 centred + hairline, one row address 15/600 + 13 grey with a grey "Search" chip 32, black CTA 57 in 15-pt gutters (05·4, 10·2, 08·3).
  - Loading uses skeletons shaped like the coming sheet (grey bars and a card on white) (04·5); "Confirming Pickup Location…" 28/500 grey with a grey disc placeholder (04·1); error panel "Something went wrong" 22/400 + 15 grey + black "Done" (04·4).
  - Card form: label 15/500 over grey fields ≈44 with 8 radius; focused field gets a 2-pt black border; Exp · CVV two-up with a ? glyph; error 13 red under the field; "Save" becomes a black bar docked on the keyboard (02·3, 09·6, 10·1).
  - Empty vouchers: large title 28/700, grey illustration disc ≈80, title 17/700 + 13 grey line, one grey chip "ⓘ Learn more about vouchers" 32 (04·6).
  - Multi-stop editor: stacked grey fields 32 with ≡ handles, numbered square markers 16 on a vertical line, × to remove a stop; the map fills the rest (03·4, 05·6).

## Apple TV (130) · dark cinematic
- Hero poster 2:3 edge-to-edge under a translucent header; section titles 20/700 with › and 12pt to the rail.
- Episode cards 16:9 with 12pt radius, overlay text block bottom-left (EPISODE 1 eyebrow 11, title 15/600, description 12 grey 3 lines, ▶ 56m 12), ⋯ trailing.
- Rails: 3.5 posters visible, title 13 + type 12 grey under.
- Tab bar: glass capsule (blur) with 4 items + a separate search disc; active item as a filled tint pill.
- Settings panel (subtitles): dark card with segmented labels rotated for landscape, radio rows; permission screen: icon grid, title 20/700, body 17 grey, blue pill + outlined "Not Now".
- *From the full library (sheets 01–10):*
  - Movie detail: artwork fills the top ≈648 of 812 pt and its colour continues as a flat band behind the logo title, genre line 13, a white "▶ Play" pill 151×45 + a 45 grey check disc, a 2-line synopsis with a "MORE" chip and a 12 meta line with badges (06·1, 02·4).
  - Purchase state keeps the geometry: two equal pills "Buy 6,99 € · Rent 0,99 €" + a "+" disc; a pending purchase puts a spinner inside the pill (02·5, 09·4).
  - Tab bar measured: glass capsule 269×59 with 4 items + a separate 59 search disc, 8 gap, 20 from the edges; the active item is a tinted pill inside (06·1).
  - Player: black, × disc + a grouped PiP/AirPlay capsule top-left, mute disc right; centre transport = pause disc 88 flanked by skip-10 discs 62; "Info · Continue Watching" chips ≈30; mini-rows 65 pitch with 16:9 thumbnail 82 + 13/600 title + 12 grey status + ⋯, hairlines (02·1, 05·1, 08·1).
  - Game detail: stadium photo hero, crests 44 with 13/600 codes flanking a white time chip, 12 grey venue line with a tv badge, one white "+ Add" pill ≈44×120 that becomes "✓ Added" (07·1, 08·2, 10·6).
  - Club page: crest 64 on a team-colour gradient, name ≈34/800 condensed, 13 grey record line, white "★ Following" pill 44 (04·1, 09·3).
  - Episode card long-press: dark translucent card of 5 rows (icon 20 + label 15, ≈40 pitch) anchored over the card, rest of the page unchanged (05·6).
  - Rental confirm: dark glass alert, title 15/600 2 lines, 12 grey sub, two equal grey pills Cancel · Play (10·2); downloads error uses stacked pills with the blue primary on top (07·6).

## Rewind (137) · light, purple accent
- Settings: grouped white cards 12pt radius on grey, toggle rows 48 with a 13 grey explanation under the card, link rows in purple with ↗, version line 12 grey centred.
- Segmented "Search / Ask Rewind" as a grey pill with white selected segment; chat bubbles in purple gradient; composer grey field with a purple send disc.
- Timeline scrubber at the bottom with app-colour bands.
- *From the full library (sheets 01–10):*
  - Search results are a 2-column grid of screenshot thumbnails 161 wide with 12-pt gaps and 19 gutters, 12 corners; under each a source icon 16 + "Today 10:33 AM" 13/500; the search field is docked at the bottom, 44 tall (02·1, 04·4, 04·6).
  - Timeline home: the captured page floats as a card with a "⊘ Open in Safari" pill 40 (white on light, dark on dark) at its bottom edge; below, a control row search glyph · relative time 15/600 centred ("49 seconds ago") · ⋯, then a scrubber band coloured per app with 28-pt icon discs and a fixed white playhead (01·4, 07·2, 03·1).
  - Live transcript: lines ≈22/400 stacked 69 pt apart, past lines grey, the current line 22/700 in ink; a floating white "Summarize" pill 44 with icon sits above the bottom row; mic glyph turns red while recording (05·3, 05·6, 07·1).
  - Menu from ⋯ opens as a card ≈200 wide anchored bottom-right: 4 rows ≈36 with label 15 left and share / jump icon right (Share Summary…, Share Audio…, Share Text…, Jump to Now) (05·3, 02·3).
  - Ask chat inside the sheet: intro block "Ask Rewind" 17/700 + 15 grey + a 12 grey disclaimer with a blue "Learn more"; user bubble a purple gradient pill right-aligned 15 white; answer a grey bubble 16 with inline citation links "[1 ↗]"; a rail of source screenshot cards follows the answer (03·6, 03·2).
  - Dark onboarding: back + "Rewind" 17/600, app icon 64, title 17/600, 15 grey body, numbered steps (purple disc 20 + 15 text with the key word bold) interleaved with framed mocks of the iOS Settings screen in a purple 16-pt frame, grey pill CTA ≈50 "Go to Settings ↗" (02·2, 04·3, 08·6).
  - Privacy sheet over the splash: shield glyph 32, "Your data privacy" 17/600, 4 lines 15 grey centred, grey pill "Got It" ≈50, link "Read our Privacy Policy ↗" 15 grey (06·4).
  - Every screen ships in light and dark with identical geometry; in dark the segmented control inverts (black selected segment on a grey track) (01·6, 04·4 vs 04·6).

## Adobe Photoshop (172) · tool app in light mode
- Canvas grey #E5E5E5; image with a thin selection frame and 6pt handles; a floating cluster of 3 white discs (44) bottom-right for contextual tools; the mode bar below: selected tool as a black pill (icon + label 13/600), others as icon + label; then the action row: × left, mode name centred 15, green/black check disc right.
- Layers sheet: white card rising to half height, title 17/700 + × disc, rows thumbnail 40 + name 13 + lock/eye icons; selected row lifted as a white card with a shadow. Three labelled icon actions 11 at the foot.
- Contextual menu: vertical stack of white pills 40 with icon + label 15 attached to a ⋮ disc; destructive item in red; disabled items in grey.
- Text options: a row of value tiles (label 11 grey under a 13 value: "Myriad Pro / Regular / 176 pt / colour swatch"), then the name and the check.
- Forms: label 11 grey uppercase-ish over value 15, hairline under each, blue "Add" text top-right.
- Empty comments: grey outline glyph 64 + "Be the first…" 13 grey.
- Toast: black pill with check "Layer clipped" 14/600 anchored to the affected object.
- *From the full library (sheets 01–10):*
  - Transform mode: header keeps only undo · redo · light bulb; three white 36 discs sit on the canvas under the image (scale from centre, flip vertical, flip horizontal) + ⋯; long-press on them reveals labelled pills ("Flip horizontal", "Flip vertical", "Scale from center"); mode chips band (selected black pill ≈36, icon + 13 label) and the × · "Transform" 15 · grey ✓ disc ≈44 row (01·1, 04·1, 10·2).
  - Canvas action fan: the ⋮ disc at the object's corner opens a column of right-aligned white pills ≈40 on a ≈52 pitch (label 13/600 + icon 20), disabled items faded (Move up, Clip), Delete at the top; the + disc turns into × and fans out "Empty · Fill · Type · Adjustment · Image layer" the same way (02·4, 06·1, 06·2, 09·4).
  - Root tool bar: scrolling band of tools (icon 24 + 10 grey label: Layer properties, Select area, Retouch, Paint, Size) with hairline dividers between groups; with a layer selected it becomes Blend and opacity · Create mask · Transform + a "Layer properties ⌄" row (05·4, 06·1, 07·3).
  - Long-press on a layer opens an iOS-style floating menu ≈200 wide: rows ≈36 with label 15 + trailing icon 18, groups split by 8-pt bands, "Delete" in red; the sheet behind stays visible (01·6, 05·3).
  - Add image sheet: 6 sources as separate white cards ≈86 tall on a light grey sheet, 16 gutters, icon 16 + title 15 + 11 grey sub; sheet title 17/700 + × disc 28 (04·5, 05·2).
  - Select multiple: sheet with back + title + ×, checkbox leading, thumb 32, footer of three icon actions (Group · Delete · More) with 10 labels (02·6, 07·2).
  - Feature requests (feedback portal): header × · title 17/600 · +, tabs All / Mine 12 blue underline + "Top ▾"; rows 80 with an outlined vote box ≈52 (arrow + count 15 + "Votes" 9), title 15, red "Posted" tag 9, comment count and date 11 grey (10·5, 10·6).
  - Rename dialog: white card inset 8 at the top above the keyboard, title 15/600, field ≈38 with a blue outline and ⊗, outlined "Cancel" + blue "Rename" pills ≈38; Rename greys out while the field is unchanged (05·5, 09·2).

## BeReal (174) · black social
- Black canvas; header wordmark 20/700 centred with a → on the right; search field as a dark pill 44.
- Contact rows: avatar 48 (rounded square), name 15/600, handle as a small white chip 11, × trailing grey; "INVITE" as an outlined pill 11/700. Section eyebrows 11/700 grey.
- Empty friends: dark card with title 15/600 + 13 grey.
- Post: header (avatar 32, name 15/600, place · time 12 grey, ⋯), dual camera with a picture-in-picture 96×128 at the top-right with a white border, reaction avatars overlapping bottom-left, comment field.
- Profile: avatar 96, name 30/700 centred, bio 13, link row, section titles 20/700 ("Latest BeReal"), 2-up cards 4:5.
- Segmented "Suggestions · Connections · Requests" as a black pill bar with grey selected segment.
- *From the full library (sheets 01–10):*
  - Feed header: friends icon left, wordmark 20/800 centred, calendar + 32 avatar right; "My Friends · Friends of Friends" text tabs 15/600 white/grey; your own post as a small ≈96×128 thumbnail centred with "Add a caption…" and two 36 grey icon discs (03·1, 07·1).
  - Empty feed: two centred 13 grey lines and a white pill "Add Friends" 124×38 (08·6).
  - Capture: rounded 16 preview with a 96×128 picture-in-picture, a 0.5× chip, record ring 78 with a 64 red core, "VIDEO · PHOTO" 13/600 caps with the active one yellow (10·5); the send screen has two dark chips (audience, location) and "SEND ▸" ≈28/900 as the button (03·2, 04·4).
  - Audience and location sheets float 5 pt in from the screen edges; title 15/600 centred + 20 × disc; options as 52 cards (icon 20 + 15/600 + 12 grey), selected white with ink text, the rest dark grey, 8-pt gaps (04·3, 10·2).
  - Report flow: 13 grey "Your report is confidential", reasons as dark rounded rows 52 with chevrons, 8-pt gaps, 17 gutter (09·4); text step with a white full-width Send 44, grey until 10 characters (01·1, 02·1).
  - Brand grid: 2 columns of cards 167 wide, ≈188 tall, 8 gap, 16 gutter, each tinted by the logo colour, logo 48 rounded, name 13/600, handle as a white chip 11, full-width "Add" 32 black or "Added" grey (05·4, 06·2).
  - Friends segmented control is a floating pill 300×48 at the bottom (Suggestions · Connections · Requests); toasts sit above it as dark pills with a green check ("Invitation Sent") (01·3, 09·3, 09·5).
  - Gated profile content is blurred with an eye-slash icon and "Become a RealFan to see all content" 11/600; the membership sheet lists benefit cards (emoji 24 + 15/600 + 13 grey) (04·5, 05·1, 09·6).

## Riverside (187) · dark recording studio
- Header: red "Record" pill 32 left, studio name 15/600 centred, grey "Leave" pill right; recording state turns the pill into a stop square with a red dot timer "00:13".
- Stage: video tile 4:5 with a 2pt violet border when active, name label 12 bottom-left; teleprompter text 20/600 white over the video with a fade.
- Bottom tool row: 5 discs 44 (camera, mic, script, chat, ⋯), the off state tinted red.
- Settings sheet: title 20/700, rows icon + label 15 + slider (violet) or toggle; a violet tooltip bubble with a pointer.
- Invite sheet: 3 role cards (title 15/600 + 13 grey, share and link icons right), selected card tinted violet.
- Alerts: iOS-style centred dark card with red destructive rows.
- Empty studio: one violet pill "+ Create" centred low on the screen.
- Feedback: chip cloud of reactions with emoji, text area, disabled grey pill.
- *From the full library (sheets 01–10):*
  - Recording detail: blurred video still as header, title 24/700 with a violet play disc 40 at its right, 12 grey meta "1 hour ago • 8m 37s", 3-line transcript excerpt 13 with a bold "View transcript", icons share · link · ⋯ 20; tiles 56 (New edit, Captions) with 11 labels; "Edits" 15/700; empty "No edits yet" 15/600 + 13 grey (06·4, 07·6).
  - Clip editor: the transcript is the timeline — speaker 13 in colour (violet, green) + timecode, body 15 with the played part white and the rest grey; 2-pt progress with 11 grey times; tool band of dark tiles 72×64 (icon 22 + 11 label), 8 gap, 4.5 visible, scrolls; header × + violet share disc 32 (04·2, 06·3, 09·2).
  - Word editor: every word is a dark chip ≈32 tall with 17/600 text, selected words tinted violet, pauses as "•" chips; foot tiles Delete · Restore 56; header Cancel · undo/redo · Save pills (03·1, 05·5).
  - Export: preview card with 16 radius, segmented Video/Audio 144×31, rows pitch 52 (label 13/600 + value ⌄ or toggle), full-width violet CTA 344×48 at 16 gutters; format picker drops as a dark floating menu with a check (04·1, 05·2, 10·3).
  - Countdown before recording: a white numeral ≈64/800 ("5", "3", "1") centred over the teleprompter (01·5, 03·2, 10·2).
  - Header tools measured: Record pill 77×33 left, name 13/600 centred, Leave grey pill right; bottom tool tiles 48×48 with 12 gaps (02·2).
  - Banners under the header: grey bar 36 "Your recording is ready! · View & edit" (violet link), "Uploading recordings… 2" with a violet progress line (01·3, 10·5).
  - Lobby: dark tile 16 radius with an initial avatar 72 rounded square, two 40 discs (camera off tinted red, mic) + ⋯, full-width violet "Join" 44, 12 grey status "Danny's in the studio" (04·3, 08·1).

## Denim (193) · the compact editor reference
- Cover editor: square canvas 340pt with 24pt corners centred on a dark tint of the artwork; header = undo/redo left, "Customize" 15/600 centred, eye + text tools right; tool panel rises as a dark sheet: title 15/600 + × disc, a 4×2 grid of type samples (selected gets a 2pt blue border), a slider, a row of "Uppercase ⌃" + colour discs, a "Font Size − +" stepper row.
- Colour picks: 5 discs 40 with a 2pt ring on the selected one; a hue slider variant with a white knob.
- Discard: grey iOS action sheet with red "Discard Changes" and a white "Cancel".
- Library: "My Covers" 28/700 top-left with a gear disc, blue + disc and ⋯; item = square art 96 with 16pt radius, name 15/600 + "1 Cover" 12 grey. Two-item tab bar.
- Playlist picker: floating white card with rows thumbnail 28 + name 15 and a search disc.
- "Create New Cover" sheet: title 15/600 centred + × disc; discs 72 (Photos blue, Unsplash black) with 13 labels; sections 20/700; rails of 160pt tiles, 20pt corners, 12 label under, lock glyph for Pro.
- *From the full library (sheets 01–10):*
  - Editor commit state: once there is a change, small pills appear in the top corners, grey "Cancel" and yellow "Done" (~24 tall, 12/600); preview mode swaps the eye glyph for a yellow crossed eye and the title for "Preview" (01·3, 04·1, 06·4).
  - My Covers grid: 2 columns of 120 covers with 16-pt corners, playlist glyph + name 15/600 + "1 Cover" 12 grey; the ⋯ disc opens a floating card (Edit · ✓ Group by Playlist · Recently Updated) (05·5, 05·6).
  - Confirm screen: "New Cover" 17/700 + playlist name 12 grey top-left, yellow "Customize" pill 24 + × disc top-right, eyebrow "CENTERED" 11 caps grey over a centred cover ~240, one white pill 306×51 "Add Cover to Playlist" with a leading glyph at the bottom (06·2, 09·4).
  - Success: green check disc 48, "Wohoo!" 22/700, 15 grey line, two grey pills 164×49 side by side (Share Playlist · View in Spotify) with a 15-pt gap, footer help line 11 grey (07·3).
  - Style variant sheet: white sheet with the style name 20/700 + ⌃⌄ switcher and a black × disc 24, stacked-card preview ~250 with page dots; the switcher opens a floating menu (Solid Gold · Chromatic · ✓ Film) (03·3, 09·6).
  - Text colour sheet: eyedropper top-left, × disc, segmented Grid / Spectrum / Sliders 30 tall, a 12×10 swatch grid edge to edge with the pick outlined in white (04·2).
  - Artist image sheet: 3-column grid of 84 discs with 13 labels, selected with a blue check badge; "Using artist image of:" bar with an avatar chip at the bottom of the editor (04·6, 04·1).
  - "Style Copied / Apply it to other lines" toast: white pill 189×44 with a blue glyph disc, dropped over the header at the top (07·6).

## Linear (204) · precise light tool
- Workspace header: 12 grey breadcrumb, title 22/700 with a grey "Projects ⌃" switcher; project rows icon 20 + name 15 + health pill right; bottom bar = back arrow, search pill, compose.
- Issue composer: "Cancel" / team chip / "Create" header, title 20/700, body 15 grey, property chips row (status, priority, project, assignee) as grey pills 32 with icons, a formatting toolbar above the keyboard.
- Pickers: floating white card 16pt radius, title 15/600 + ×, search field, rows icon/avatar + name 15, check trailing, "+ Create new label" row.
- Lists: section eyebrow 13 grey + "+" right, rows 40 with status ring icon 16 + title 15 + avatar 24 right; tabs as outlined pills 32.
- *From the full library (sheets 01–10):*
  - Issue detail: "REF-18" 12 grey + ⋯; title 22/700; properties in one grey 12-radius block holding two rows of ≈24 chips (status, priority, assignee, labels, project, date) with a "+" disc 20 at the right; description 15; attachment as a grey 52 card (file icon, name 14 + size 12 grey, chevron); "+ Add sub-issue" 13 grey (02·2, 02·4, 06·5).
  - Activity is a timeline of 6-pt hollow dots with 13 text (names and values bold) and 11 grey times; comments sit in grey 12-radius cards with a reaction chip; a grey comment pill 36 docks above a 5-icon bottom bar with the search pill centred (02·4, 03·3).
  - Toasts are dark rounded bars ≈34 tall (icon 16 + 13/600 white) floating just above the bottom bar: "Copied issue URL", "Reminder set", and "Issue created" with a green check and a "View issue" text action (02·4, 02·5, 03·4).
  - Display options sheet: rows ≈42 (label 15 + value 15 grey with ⌃⌄), "Row properties" with a grey "Reset", then property toggle chips 40 tall with 6-pt gaps, grey fill when on and outlined when off; the value opens a floating menu with a leading check (03·5, 07·3, 07·5).
  - Action sheet: no title, no Cancel, rows 48 (icon 16 + label 15), destructive "Delete issue" in red last, after a hairline (02·6).
  - Inbox: rows ≈68 with an avatar 34 carrying a 14 status badge, title 15 (grey when read, ink + 6-pt blue dot when unread), 13 grey 2-line sub with "· 4h ago", trailing "⏰ 39m" 13; swipe reveals a blue "Read" tile ≈88 wide (03·2, 08·6).
  - Empty states are a grey line-art illustration ≈80 with one 13 grey line and nothing else: "No notifications", "Nothing to triage"; in pickers "No results for "Diet"" 13 grey centred (08·4, 09·1, 04·5).
  - Grouped issue rows measure 48 pt (status ring 18 at a 21 gutter, title 15, avatar 24 right); the board-level text tabs are outlined pills ≈34 (01·4, 05·6).

## Moises (209) · dark audio tool with one cyan accent
- Sheets: "Song Sections" list 15 rows 40, selected in cyan with a check; "Export" with format picker (selected as a grey pill) and a cyan full-width button 52.
- Player: chord strip at the top (cells 44, current cell white), two track sliders (mic, music) with cyan tracks and ⋯, chord grid 4 columns, section chips outlined cyan 36, thin progress with times 12, transport row (metronome value 11, prev, play disc 56 white, next, key), bottom row of 3 outline tools.
- Camera: full-bleed with a red stop disc 64 and a grey reset disc.
- *From the full library (sheets 01–10):*
  - Song settings sheet: 10 rows on a 52-pt pitch, outline icon 22 + label 15, value 13 grey ("2 Tracks", "OFF", "10 clicks") + chevron; unavailable rows (Trim, Edit Lyrics) at ≈40 %; a cyan dot marks a changed setting (Chords); fits without scrolling (02·3, 10·3).
  - Value dial sheets (Song Key, Count in, Sync, tempo): value in a 52 disc (white at default, green/cyan once changed) over a tick ruler ≈48 tall with − and + at the sides; "Reset to original" 13/600 turns accent only when something changed (03·2, 05·1, 08·2, 09·4).
  - Metronome sheet: header toggle row, Volume and L&R sliders, "Subdivision" 13/600 + three outlined buttons 40 tall ≈98 wide at ≈16 gaps, selected filled white; tempo word "Allegro" / "Vivace" 13 grey above the BPM disc (03·2, 08·5).
  - Mix sheet over the camera preview is frosted and translucent: toggle "Enhanced Audio", sliders with "-1.0 dB" 13 right-aligned values, "Auto Mix" text action (04·2, 08·1).
  - Rename sections: full screen, × left and check right in the header, each item = time range 12 grey over name 20/600 with a hairline, ≈75 pitch (03·1, 09·2).
  - File info: segmented General / Details 32 tall, artwork placeholder ≈142 square, filled dark fields 40 tall with 11 grey labels above on an 88 pitch; Details tab is label 15 left / value 15 grey right rows (06·2, 06·4).
  - Export progress: centred dark card, "Exporting" 15/600 + percent right, thin cyan bar, red "Cancel" pill 40 full card width (02·5, 09·5).
  - The centre tool of the bottom band expands in place into a grey pill holding three view icons (list, lanes, grid) (05·2, 07·3); hints are white speech bubbles ("Tap to loop", "For a better experience, use headphones") (07·4, 10·4).

## (Not Boring) Camera (222) · physical-object UI on dark
- Every group is a dark card 20pt radius with 1pt inner highlight; rows title 15/600 + 13 grey explanation + amber toggle; section eyebrows 11/700 grey spaced.
- Style page: photo card 16:9 with page dots, hexagon style icon, title 28/700, author link, description 13 grey, an "Intensity 59" card with an amber slider.
- Colour picker: 5×3 grid of 36pt discs, selected with a white ring; three round action buttons (×, "Done +" pill with a violet disc, share).
- Stats card: label 15 left, value 15 right, hairlines; support card rows with grey icons.
- Header: back as a grey glass pill "‹ Settings", title 17/700 centred.
- *From the full library (sheets 01–10):*
  - Settings root: stacked navigation cards 351 wide, ~90–107 tall, 8-pt gaps: 3D icon ~44 + title 17/700 + 13 grey sub; then a mono eyebrow "MEMBERS ONLY" with a violet + badge and a list card of rows ~43 (glyph 20 + 13 label + grey value right) (05·1).
  - Every sub-page opens with a centred 3D glyph ~80, one 13 line and a grey "Learn more ↗", then the cards (06·1, 01·5, 03·2).
  - Toggle rows are 76-pt tall: title 15 + 13 grey explanation + amber toggle 58×28; a value pill ("2 sec", "Off" ~36×24) opens a small dark dropdown with a check instead of a new page (01·5, 01·6, 02·1).
  - Single-choice group in one card: rows ~50 with a 24 disc, the chosen one amber with a check, title 15/700 + 13 grey (06·1, 06·4).
  - Styles list: rows at ~89 pt with 55 hexagon 3D icons, name 15/700, trailing eye toggle + chevron + reorder handle; locked items show a violet + disc instead; hidden styles dim to ~40 % (03·2, 03·3, 06·2).
  - Customiser: 3D camera model over a dark gear backdrop, part names as a word carousel 22/800 (active white, neighbours faded), a 6×3 palette of ~42 discs, bottom row × disc 48 · "Done +" pill 160×48 · share disc 48 (03·1, 04·2).
  - Viewfinder drawn as a device: 3:4 preview ~316 wide with a grid, a ~140 round dial as the shutter, knob-like side controls (02·4).
  - Alert: glass card, title 15/700 left + 13 body, three stacked full-width pills 36 (Browse Support · Copy Diagnostics · Cancel) (02·6).

## Sora (226) · black video social
- Search: dark pill 44 with a leading glyph and a trailing people disc; empty state "No results" 17/600 + 13 grey centred in the free space; two grey pills below (Share, Copy link).
- Replies sheet: grabber, "55 replies" 20/700, rows avatar 32 + handle 13/600 + time 11 grey, text 14, "Reply" 12 grey, heart 20 right with count 11; nested replies indented 40; composer dark pill 48.
- Profile: avatar 96 centred, name 20/700, bio 13, three stats (17/700 over 11), outlined "Following" pill 44, two text tabs with icons, 3-column grid with 2pt gaps.
- Context menu: dark card 16pt radius with 3 rows (icon + label 15), destructive in red.
- Confirm: centred dark card, title 15/600, body 13, two pills side by side (grey Cancel, red Block).
- Send sheet: avatar grid 64 with names 11, selected with a check badge; "Send to Group" white pill 48.
- Tab bar 5 icons, the centre one a white pill "+".
- *From the full library (sheets 01–10):*
  - DM thread: all bubbles dark grey (≈18 radius, 15 text, 12 padding), incoming left with avatar 28 and sender name 10 grey above, outgoing right in the same grey (no accent for self); system lines "Connie Perry created the chat." 11 grey centred; composer pill 40 with mic 20 and a grey send disc 24 (01·2, 04·1).
  - Reply in chat: the composer grows into a card with a blue "↪ quoted text ×" chip above the field; in the thread the quote shows as a 12 grey "↪" line above the outgoing bubble (06·2, 06·6, 05·3).
  - Voice note replaces the composer: stop disc, waveform, "0:06" 12 timer and a send disc 24 in the same 40 pill (05·3, 07·3).
  - Long-press on a message: thread dims, a glass card rises with 6 emoji 28 + a "+" disc, then rows (icon 22 + 15) "Copy", "Reply"; own messages get "Copy" + red "Delete" (09·1, 09·3).
  - Feed post: video letterboxed at its own ratio on black, right rail of outline icons 24 with 11 counts (heart turns red when liked), avatar 32 with a + badge, handle 15/600 + one-line caption 13, page dots for remixes; the "For You ⌄" title 15/600 opens a dark menu card with check, icons and a "Pick a mood ›" row (04·6, 08·2, 06·4).
  - Top toasts are glass capsules 49 tall at 12 gutters over the header: a leading × disc 16 + 12/600 text ("Copied post link", "Message copied"); errors add a warning glyph (06·3, 07·1, 08·3, 03·4).
  - Cameo permissions: grouped dark cards 12 radius at 23 gutters, rows 53 with icon 20 + 15 label (+ 13 grey sub-line with ›) + radio 22 trailing, group labels 13 grey; footer strict pair "Retake" grey + "Done" white 44 (08·5, 10·1).
  - Followers list: two stat tabs "889 Followers / 19 Following" (20/700 over 11) as the header toggle, rows 65 with avatar 40, name 15/600 + 13 grey; state by fill: white "Follow" pill 97×40 vs outlined "Following" (04·2, 04·3).

## Netflix (264) · dark, red only for brand
- Screens are #141414 with one white title 17/600 centred and a back disc; helper text 13 grey.
- Search in forms: grey field 44; results as plain 15 rows 44 with hairlines; blocked list rows with an × block on the right.
- Radio/check lists: 24 circles, checked as blue discs; sort sheet: title 20/700 + × disc, rows 15/600 with a check leading.
- Avatar picker: section titles 17/700, 4-up rail of 80pt squares with 4pt corners.
- Home: chips row (Shows, Movies, Categories ⌄) as outlined pills 32; hero poster 2:3 with 8pt corners, genre line 12 with dots, two buttons (white "▶ Play", grey "✓ My List") 44; "Your Next Watch" 15/600 rail; tab bar 3 items with labels.
- Code entry: 4 boxes 56 with 1pt border, red error 12 under, "Resend code" underlined.
- Toasts: dark pill with a check icon at the bottom centre.
- *From the full library (sheets 01–10):*
  - Edit Profile: avatar 72 with an edit badge, name field 44 outlined, then stacked dark cards 61 tall with 8-pt gaps (icon 24 outline + 15/600 title + 11 grey value + chevron, or a blue switch), 11 grey footnote centred (03·4, 07·1).
  - Game detail: key art fading to black, title 24/700 centred, genre 11 + "18+" grey tag, white "Get Game" 46 full width at a 10 gutter, then a row of 38 grey buttons ("+ My List" 138, "Rate" 138, share 62) with 8 gaps (05·5).
  - My List: back + title 17/600 centred + Edit; text tabs "TV Shows & Movies · Games" 17/700 with a 3-pt red underline under the header; outlined chips 30 (active ones white-filled with a leading × disc to clear); "Sort By" 11 grey over 15/700 value ▾; rows at 84 pitch with a 126×62 thumb, title 13/600 and a 32 play ring (red trash in Edit mode) (04·4, 02·4, 10·6).
  - Empty states: filtered list "Nothing here... yet" 24/700 + 15 grey + white pill 35 "Clear All" (04·5); profile lock as a 148 grey disc with a 40 lock, 20/700 title, 13 grey line, white 35 button (04·2).
  - Profile picker over key art: "Choose Your Profile" 13 grey, avatar squares 56 with 8 corners and 13/600 names, Add/Edit as 56 translucent squares with 32 glyphs (06·2, 08·1, 05·6).
  - How-it-works carousel: illustration, 11 caps grey eyebrow "HOW PROFILES WORK", 20/700 title in 2–3 centred lines, dots, white full-width 44 "Next"/"Got It" (02·6, 07·2, 10·3).
  - Delete dialog: dark translucent card, 17/600 title, 13 grey body, two pills 40 side by side (grey Cancel, dark-red Delete with red text) (06·1); feature modal: white card with a red "NEW" tab, 28/400 title, 160 grey disc icon, text actions separated by hairlines (09·3).
  - Game handle form: field with an 11 grey label, counter "3/16" right, red or green 11 validation line, disabled grey "Let's Play" until valid (03·1, 08·6).

## WhatsApp (292) · iOS grouped, green accent
- Onboarding cards: gradient pastel background, illustration, title 20/700, body 15, page dots, blue full-width pill 48.
- Contact lists: index letters on the right edge, grouped white cards per letter, rows avatar 40 + name 15 (surname bold) + radio circle; "Invite" as green text right.
- Empty: grey pill card "No contacts" 15 centred.
- Info sheets: white card with a big icon, title 20/700, 3 benefit rows (icon + 15/600 + 13 grey), legal 12 grey with links, blue pill "OK".
- *From the full library (sheets 01–10):*
  - Profile: avatar 142 centred, "Edit" 15/600 green, one white card at 16 gutters with ≈18 radius and 4 rows pitch ≈50 (label 17 + grey value + chevron), link value in green (02·1, 08·3).
  - Tab bar is a floating white capsule ≈335×58 with 5 icon + 10 label items; the active "You" item is a grey pill holding the avatar (02·1, 05·6).
  - Header controls are white 42 discs with a soft shadow (back, ×, +); the confirm action is a disc/pill that turns from grey to green when valid (03·3, 06·6, 05·6).
  - Contacts: white cards per letter at 16 gutters, rows 48 (avatar 32 + name 15/600), letter headers 13 grey with 52 between cards, "Invite" 15/600 green + × per row, "View all" and "Sort" as small grey pills (05·6, 09·5).
  - Subscription management: benefits card of 6 rows (icon 20 + 15 + chevron, ≈40 pitch), status 12 red "Canceled • Active until …", "Renew now" blue pill inside a card, "Cancel subscription" as a plain row card last (03·1, 06·5, 09·3).
  - Cancel survey: title 22/700, 13 grey privacy line with a blue link, radio card of 5 rows ≈44, text field, pinned blue full-width 44; result is a centred white card with a green full-width OK (05·4, 05·3, 10·5).
  - AI restyle: dark stage, image 16 radius, text tabs Featured · Styles · Moods · Lighting · Colors with a grey pill on the selected, style tiles 58 with 11 labels (selected outlined white), a dark warning pill "Try a different prompt" over the tiles (01·3, 04·4, 06·3).
  - Search: pill field + separate × disc 36; "No results" 17/600 alone centred; skeleton loading as grey bars and cards on white (04·6, 04·2, 09·6).

## TIDAL (298) · dark, glass tab bar
- Album header: art 176 centred over a blurred tint, title 17/700, "by you ›" 13, meta 11 caps grey, two grey pills "▶ Play" / "⤨ Shuffle" 44 side by side, then a row of 3 icon actions with 11 labels.
- Onboarding pick: title 22/700, search pill, section 17/700, 3-column grid of circular artists 96 with 13 labels, grey "More Hip Hop" pill.
- Track list: number 13 grey, title 15 (playing in yellow), artist 13 grey, ⋯; mini player floats above a glass tab bar capsule with 5 icons.
- Share sheet: small info card with title 15/600 + 13, rows icon disc 32 + label 15, "Cancel" text.
- Profile: full-bleed portrait, name 34/700 white over the photo, handle 13, bio 15, link 13, two icon actions with labels.
- *From the full library (sheets 01–10):*
  - Now Playing on a stage tinted from the art (plum): art 335 square on a 20-pt gutter; title 17/700 + artists 15 grey + a trailing + 24; thin progress with times 11 and "24-BIT 48KHZ FLAC" 11 centred; transport as bare glyphs, the pause ~27 wide with no disc, shuffle/repeat dimmed; footer: queue disc 36 + "Playing from" 11 grey over 13, and a share · ⋯ capsule 36 (07·3, 08·2).
  - Lyrics mode: art shrinks to ~88 top-left, a white "Lyrics" pill marks the mode, lines 22/700 with the current one white and the rest ~40 % white (06·4).
  - Queue sheet: dark card over the player, × disc 32, "Now Playing" 13/600 label, rows art 40 + title 15/600 + artist 13 grey + × to remove; a bottom capsule switch "Play queue | Similar tracks" 36 (02·2, 02·3).
  - Action lists fill the screen on black with no cards: item art ~107 + title, then rows icon 20 + label 15/600 at a ~55-pt pitch, destructive in red, "Cancel" 15/600 centred (04·4, 06·1, 08·6).
  - Dark alerts ~285 wide: a title block (15/600 + 13 grey) and separate stacked action slabs 36 each (red "Delete" / "Cancel", or "Confirm" / "Cancel") (09·5, 09·6, 04·5).
  - Toasts are full-width grey bars 353×50 inset 11 pt, sitting just above the glass tab bar, 13/600 left text; errors reuse the bar in red with a "Retry" chip right (08·4, 06·6, 10·5).
  - Paywall: plan card 335 wide on a warm gradient, wordmark 20/800, bullets 15/600 with amber dots, segmented Individual / Family 28, price 13, white "Continue" 288 wide inside the card, "Restore Purchase" 13/600 and 11 grey legal below (07·6, 09·1).
  - Credits: sheet with role eyebrows 10 caps grey spaced, name rows 15/600 at ~31 pt with chevrons and no dividers; album page has a Credits | Info capsule switch 32 (03·3, 07·4).

## Meta AI (300) · light, blue accent
- Drawer: search pill, 6 rows icon + label 15/600, "Chats" 13 grey label, chat rows 15 with pin/⚙ icons, selected row tinted grey; bottom row avatar + two discs.
- Share sheet (dark): preview card 240 with 16pt corners, app discs 48 with 10 labels, legal 11 grey.
- Media picker: dark sheet "Library · See all", thumbnails 88 with check badges, "Recently uploaded" white pill, blue "Add 2 photos" pill.
- Empty search: outline icon 48 + "No results found" 15/600 + 13 grey.
- Product page: light grey card with the object, title 22/700 centred, body 13 grey, blue pill.
- *From the full library (sheets 01–10):*
  - Composer is a floating white card ≈72 tall with ≈24 radius and a soft shadow, placeholder 15 grey ("Reply…", "Ask Meta AI…"), a mode chip "Instant"/"Thinking" 13/500 outlined pill ≈28 and a send disc 28 grey → blue; while generating the send turns into a blue stop square (04·2, 07·4, 09·3).
  - Answer tail: row of 4 feedback glyphs 20 grey (👍 👎 copy share), then follow-up suggestions at ≈70 pitch = ↳ glyph + 13 grey two-line text with hairlines (03·6, 04·6).
  - Agent progress: "Running 5 subagents" 13/600 with a spinning purple glyph, a vertical rule with child rows name 12/600 + status 11 grey; when finished it collapses to "Answered with 5 subagents ›" + a ✓ list (10·2, 09·2); "Show thinking ›" 13 grey above answers opens a "Steps" sheet with bullets and grey cards (04·2, 02·4).
  - Markup tool: black stage, picture at its ratio, bottom dark panel radius ≈24 with 7 colour discs ≈20 at 8 gaps, then undo · (pen | text) grey segmented pill · redo; brush size is a vertical slider over the picture's left edge; white "Next" pill 36 top right, grey while nothing is drawn (02·1, 03·1, 05·1).
  - Edit image: header × disc 36 + "Edit image" 15/600 + ⋯ disc + white "Share" pill 36; foot = "Ideas" chip + dark prompt pill 36 "Describe your changes…"; Ideas opens a dark sheet of 44 pills (+ or image glyph + 15 label) at ≈17 gaps (06·3, 10·5).
  - Intro and consent sheets float 8 from the screen edges with ≈32 radius: icon 48, title 20/700 centred, 13 grey line, 3 rows (icon 20 + 13/600 + 13 grey), blue 46 pill over a grey 48 "Learn more"/"Disconnect", 14 gap (05·2, 05·3, 06·6).
  - Delete alert: centred white card 269 wide, title 15/600, 12 grey three lines, red pill ≈38 over grey Cancel ≈36 (08·6); drawer long-press menu: frosted card with a date eyebrow 11 grey, rows icon 20 + 15, red Delete last (04·3).
  - Media: segmented "Presets · Created · Imported" grey pill 32, "All ⌄" text filter opening a frosted menu (All · Favorites · Images · Videos), 3-column grid with 1-pt gaps under a floating composer (04·1, 08·5); empty tab = glyph 24 + "No videos yet" 15 grey + 13 grey (04·4).

## Playground (243) · light editor
- Canvas grey #F1F0EC; artwork 3:2 centred with a 2pt blue selection frame; floating black tool strip 44 above the selection (colour, outline, corner, align, opacity, download, trash) with the active tool highlighted.
- Bottom: a white composer card 20pt radius ("Describe your edit", + disc, model chip "Nano Banana ⌄", send disc), then a grey pill with 3 icons, then a scrolling icon rail of 12 tools.
- Tool panel: white card rising with title 15/600 + "Close" text, one explanatory line 13, slider, undo/trash discs left, black pill "Erase" right.
- Colour picker: floating white card with a 2-row palette of 36pt discs + "Custom" tile; full picker with a gradient square, hue slider, hex field, blue "Done".
- Selection mode: "0 designs selected" 22/700 + Cancel; a promo card with gradient tint and a black "Upgrade now" pill.
- *From the full library (sheets 01–10):*
  - Paywall sheet: × left + "Restore" 13 right, title 28/800 on two lines with "with Pro" in a gradient + small 3D logo, 4 benefit rows (grey icon disc 24 + 15/600 + 13 grey), two plan cards 165×80 with an 8 gap, the selected one outlined 2.5 pt dark with a filled check, "-28%" blue chip, blue "Purchase" pill 58 tall full width, 12 grey legal. (07·5, 10·1)
  - Share Design sheet: grabber, title 17/700 + "Done", preview at its ratio with an 11 size tag "1024×1536" on a grey pill, "More actions: PRO" 13 grey + a scrolling row of outlined 36 chips (Upscale by 4x, Remove Background), then two black pills Save / Share 166×38 with a 10 gap. (03·6, 10·3)
  - "My Designs" root: title 22/700 + Edit, a Pro promo card on a pastel gradient (title 15/600, 3 emoji bullets 13, black "Upgrade now" pill ≈28), a 2-column masonry of designs, and a floating 3-slot capsule at the bottom (explore · + disc · avatar). Long-press opens a floating frosted card (Download, Duplicate, Delete red) over the blurred grid. (08·3, 10·4)
  - Resize: rows with an outline rectangle at the true proportion (≈48 tall) + ratio 15/600 + pixel size 13 grey; the full ratio picker is a floating 2-column grid of 10 cards (9:16 … 16:9). (05·3, 07·3)
  - Style and face pickers are frosted half-panels "Title · Close" with a search field (outlined 2 pt dark while focused, suggestion rows under it) and a 4-column grid of slightly tilted sticker thumbnails ≈72, "Upload" tile first. (09·1, 09·5, 10·6)
  - Text properties: letter spacing and line height as sliders with 32-pt value fields in a frosted popover above the text toolbar (Aa ⌄ · size ⌄ · align · spacing · colour wheel · download · trash). (03·3)
  - Generating: the canvas is replaced by a blurred warm-gradient card with a 12 spinner in its corner and the composer greys out — no progress text. (04·1, 06·2)
  - Settings sheet: 11 caps grey group labels (ACCOUNT, BILLING, ASSISTANCE), ≈40 rows with icon 18 + 15 label + chevron, "Free plan" row with purple "Upgrade" 13 trailing, version 13 grey centred at the end. (08·2)

## Flighty (049) · dense data, iOS grouped
- Sheets over a map: title 24/700 + × disc; search as three grey pill fields in one row; result rows: flag 20 + name 15/600 with the matched letters bold + codes 12 grey.
- Flight card: eyebrow 12 grey (flight · date), title 22/700, a grey info banner 13, 2-up info tiles (icon + value 17/600 + label 12, "COPY" chip), "Good to Know" card with icon rows.
- Form: label 13/600, grey field 44, chips row (Aisle/Middle/Window) outlined pills 36, radio list 44; segmented "Flight / Airport / Airline / Other" as 2×2 blue-filled/outlined buttons.
- Timeline: airport code 34/700 with the time 22/600 green right, status "On Time" 13 green, meta 12 grey; "Gate Departure in 8h 24m" 15/600 green.
- *From the full library (sheets 01–10):*
  - Flight sheet header (every detail state): airline logo 24 left, eyebrow 12 grey ("JQ 420 · WED, 6 SEP"), title 17/600 on two lines, × grey disc 24 top-right; under it a horizontally scrolling row of ≈32-pt pills (Live Share blue filled, "My Flight ⌄", "Alerts Off" outlined) that runs off the right edge. (05·6)
  - Live timeline: airport code ≈35/700 (cap height 25 pt), time ≈28/500 in state green, the scheduled time struck through in 12 grey + delta "9m early" 12/600 green, terminal/gate 12 grey; "Total 1h 19m · 421 mi" 12 grey centred on a hairline between the two airports; status band "Lands in 30m" 15/600 green on a pale-green strip. (05·6)
  - Search results rows are 120 pt tall (measured pitch 119.1): a 60-pt status column (grey check disc 24 + "ARRIVED" 9/600 caps, or countdown "0 MINUTES" ≈24/700), then code 11 grey + status 11 green/red right, route 15/600 truncated, two time pills 13/600 with a coloured dot; list header "SHOW CODESHARES" 11/600 blue caps left, "23 RESULTS" 11 grey right. (10·1)
  - Bottom of the flight sheet: one white card of 48-pt action rows (hairline pitch 48.4) — blue 15 labels with trailing 20 blue icons, a toggle row, purple "View Pro Benefits" + PRO tag, red "Delete" + trash last — then "Report Data Issue" as a centred grey text link with icon. (06·6)
  - Loading and empty in the search sheet: 3 skeleton rows (circle 32 + two grey bars) in the final layout; "No Flights Found" 15 grey under a 32 outline icon, then 3 help rows (24 icon + 14 text) with inline blue links "Edit Search" / "New Search", and "Tell us what's wrong" grey at the foot. (06·2, 06·3)
  - Report-issue form: nav "Close · Report Data Issue · Submit" with Submit grey until one box is ticked; grouped white cards each holding a 13/500 caps grey group label and ≈42-pt rows with a trailing 18 check disc (grey → blue). Thank-you is a centred grey HUD square ≈200 with a check glyph and two 17/600 lines. (03·5, 04·6, 07·6)
  - Pro upsell lives inside the detail flow as cards: device mock image, title 17/700 centred, 12 grey line, 4-dash page indicator, in-card purple pill ≈40; "Enable popular features" card with × corner, illustration and a purple caps ENABLE pill. (02·6, 04·2)

## Luma (063) · events, black & white
- Ticket: white sheet with a dashed rounded frame around the QR, black pill "Add to Apple Wallet".
- Event page (dark tint from the poster): poster 4:3 16pt corners, chip "Featured in …", title 22/700, rows icon-tile 40 + 15/600 + 13 grey (date, place), "Registration" card.
- Calendar list: date column (NOV / 14 / TUE stacked 11-22-11) left, event title 17/600, meta rows with icons 13 grey, cover images 16:9 with 12pt corners, "External" chip.
- Payment: total 15 grey + 22/700 right, card row dark pill, black pill CTA.
- *From the full library (sheets 01–10):*
  - Registration CTA is a white pill 50 tall, full width at 20-pt gutters, pinned over the poster-tinted page ("Apply to Join", "Register", "Register in One Click" with a leading thumb glyph); the event page gutter is 20, not 16 (05·3, 10·5, 06·5).
  - Event page: under the title, two translucent pills ≈25 tall with icons ("Share", "Open on Web"); a details card holds date 17/600 + time 13 grey + a weather glyph and "63°" right, then the place line and a map snapshot with 12 corners; "Hosts" is a label 13 grey inside a card (05·3, 09·1).
  - Ticket selection: radio cards 113 tall with 9-pt gaps (335 wide): name 15 + price ≈20/700 + an availability dot line 11 (green "Available", grey "Sold Out"); sold-out cards are dimmed, not removed; "Total" 15 grey left + ≈24/700 right; the pay row is a strict pair, grey "Credit Card" pill + white Apple Pay pill (05·6, 06·3, 08·4).
  - Home "Your Events": date column ~55 wide with an "IN 14H" grey chip; covers 267×134 (2:1) with a green outlined "Going" chip top-right; only the next event gets actions: black "Join Zoom" pill 35 hugging its label + grey "Share" pill (05·1).
  - Status after registering is a floating dark capsule at the bottom ("Pending Approval" or "You're Going · View Ticket ›") with a leading icon and ⋯; long-press raises "Change to Not Going" in red above it (02·2, 09·6, 07·1).
  - Host tap raises a white sheet: avatar ≈56, name 20/700, local time 13 grey, bio 13, four grey social glyphs, optional black "Chat" pill top-right (04·1, 09·4).
  - Registration questions on dark: question 15 white above grouped 12-radius cards of 36-pt radio/checkbox rows and textarea cards; the Register pill turns into a spinner-in-pill while submitting (02·1, 04·4, 09·3).
  - Toast: green pill ≈46 tall at 16 gutters with a check glyph and 15 white text ("Your message is on its way to the host!") above the web chrome (10·3).

## Fable (096) · warm literary
- Serif display for names/titles (28/500), sans everything else; quote card as a coloured 16pt block with a big quotation mark and 22 serif text.
- Profile: avatar 64 with a badge, chips "23% Match" / "Moderator" 11, outlined "Following" pill + icon disc, a goal card with a thin progress bar, text tabs with underline, list rows with 3D book stacks.
- Filter sheet: label 13 grey + "Clear all" blue, checkbox rows 40 with counts 12 grey, grey disabled "Apply" 52 + "Cancel" text.
- Empty search: small illustration, "No results" 15/600 + 13 grey.
- Thread: message bubbles left with an image 16:9 and reaction chips 24, a "NEW" pill divider, composer with 2 icons and a grey send disc.
- *From the full library (sheets 01–10):*
  - Club detail: artwork blurred and faded into the ground behind the header (share · gift · settings as 32 dark discs, or a pink "Join" pill 32); club name serif 28/400 on two lines with emoji; body 15 three lines; moderator row avatar 32 + "Moderated by" 11 grey + 13/600, stacked member avatars + "23 Members" 11 right (03·4, 03·5).
  - "Currently reading" 17/600 + history disc; book cover ≈82×120 + title 13/600 + author 12 grey + black "Sample interactive ebook" pill 32; then text tabs Discussion · Schedule with a 2-pt pink underline (03·4).
  - Club list: "Book Clubs" serif 28/400 + search glyph; text tabs Find Clubs · Your Clubs; outlined dropdown chips 28 (Genres ⌄, Sort ⌄); cards on a tinted cover block 84 wide with the cover inside, "Michael Kist moderates" 11 grey, name 15/700, counts 11 grey, "Last activity 4h ago" right; card pitch ≈132; a blue + FAB 44 bottom-right (09·2, 09·3, 05·5).
  - Member list: club name 15/600 + "22 Members" 12 grey centred, "Invite" 15/600 blue right; search pill 36; rows avatar 33 + name 15/600 + pronouns 12 grey, trailing black "Follow" 71×33 or outlined "Following"; row pitch 60 (10·2, 10·6).
  - Feature tour: a carousel of white cards over the dimmed club page, each a colour block with an in-app mock on top and serif title 24/400 + 13 grey two lines + beige "Next" pill 36 below; page dots under the card (08·1, 08·4, 10·4).
  - Chat: long-press shows a floating white reaction bar of 6 emoji 28 above the message (06·2); options sheets are plain: 11 grey label, icon 20 + 15 rows, "Cancel" 17 centred (07·3, 09·6, 05·4).
  - Invite: sheet with "Invite a booklover to Fable" 17/600 + ×; illustration, serif "Give $5, get $5" 20, 13 grey paragraph, dashed link field, black "Copy" pill 36 + grey "Share" pill 36; credits card "$0.00" 22/700 green; a black toast "Invite link copied to clipboard" + "Okay" at the top (04·1, 06·4).
  - Destructive confirm is a centred card with a pink illustration header, 13 grey question, green "Remove" filled + outlined "Cancel" pills 36 side by side (09·1).

## Atoms (099) · editorial habit app
- Cream canvas, serif for the sentence ("I will read 20 pages"), sans for UI; stat tiles 2-up: label 13 + value 40/700; a heat-map calendar of 12pt squares.
- Sheets: icon disc 44 at the top, title 22/700 centred, body 15 centred, field with a 13 label, black pill 52 + outlined "Cancel"; radio list of yellow-filled selected rows.
- Context menu: white card 12pt radius with 4 rows (label 15 + icon right), hairlines.
- Header actions: "Share ⬆" grey pill, ⋯ disc, × disc, avatar 32 left.
- Home: one big yellow disc (habit) with a tiny label, "PRESS AND HOLD" 11 caps grey under. Tab bar 3 items + badge.
- *From the full library (sheets 01–10):*
  - Home disc measures ≈220 pt with a white halo; a logged habit fills with the yellow→orange gradient and shows a black 44 glyph disc with the count; a second habit stacks as an overlapping white 220 disc, a snoozed one shows a grey glyph and "Snoozed until Apr 17, 2024" 11 grey (04·5, 08·1, 10·5).
  - Completion celebration on a dark dotted stage: "Habit completed!" 15/600, hexagon badge in a ≈190 ring, serif headline ≈28/400 "1st Step to Greatness!", 15 body with "1 Rep Milestone" in orange, a week row of 7 circles 32 (today white-filled, next day greyed), then white 46 "View habit details" + dark grey 46 "Back to Home" 10 apart (05·3, 06·6).
  - Milestones: 3-column grid of hexagons ≈80 with serif italic numerals, 11 grey labels under ("7 Day Streak", "25 Repetitions"); only earned ones fill orange (09·3, 05·2).
  - Snooze sheet: options as white 46-pt rows 9 apart, the selected one fills yellow with a black check disc; black 46 "Confirm" + white 42 "Cancel"; 23-pt gutter; a yellow banner card at the top warns when the choice is invalid ("Can not snooze until tomorrow…") (01·5, 10·1).
  - Upgrade sheet (dark): Free/Pro table, rows icon 20 + title 15/600 + 11 grey sub with two check columns; plan cards outlined with "Save 41%" in orange; three stacked 46 pills 9–10 apart (white Subscribe, grey Not right now, grey Restore purchase) and 13/600 legal links (04·1, 05·6).
  - Onboarding forms: serif question ≈22/400 left, 13 body, a thin progress bar top centre; 12 grey labels over 44-pt outlined fields (1-pt grey, 10 radius); the focused field gets a yellow→pink gradient border; a small black "Next" pill right-aligned above the keyboard, and "Skip" text + black 44 "Create Account" at the foot (04·2, 07·4, 05·4).
  - Errors and confirmations: 12 red line under the field (07·5, 10·6); success as a yellow top banner card ≈56 with icon + 15/600 "New verification code sent!" (09·1).
  - Habit detail when snoozed: a dark 50-pt card "Snoozed until Apr 17, 2024" with a "Turn off" 13/600 text action replaces nothing else on the page (09·2).

## Superlist (108) · light productivity
- Titles 34/700 top-left; segmented filter chips (search disc + pills 36, selected grey); task rows checkbox 20 + title 15 + list name 12 grey with an icon, avatar 20 right; subtasks indented.
- Empty inbox: hand-drawn doodle placeholder rows; a coral floating "+" disc 48 bottom-right.
- Drawer: avatar, 4 nav rows icon + 15, "Recent ⌄" 13 grey, "Lists · Browse all + " groups with disclosure rows.
- Doc: cover image 4:3, share chip with stacked avatars, title 28/700, body 16 with 24 line height, formatting bar above the keyboard.
- *From the full library (sheets 01–10):*
  - Due-date sheet floats as an inset card (16 from the sides, ≈30 above the bottom, ≈20 corners): header "Edit due date" 13 grey left + Clear and Done as ≈30 grey pills; quick rows ≈40 (Today, Tomorrow, Next week) with 16 icons; month grid rows ≈38 with today outlined and the pick as a coral disc; then Time / Remind / Repeat rows ≈57 with a trailing × to clear (02·6, 06·6, 09·5).
  - Every picker uses the same inset sheet header (13 grey title · Clear · Done): group-by as plain 15 rows ≈40 with the selected row on a grey band and a coral dot, labels with a search row and coral checks, assignees with invitees greyed and a "Pending" 13 grey trailing, time as a wheel inside the sheet (02·2, 04·4, 08·2, 08·3).
  - Insert menu is a two-column sheet: block types left (Task, Paragraph, lists, Image, Attachment), "Make with AI" + H1–H3 + Divider right, rows ≈40 with a 16 icon + 15 label, a hairline between columns (03·6, 06·2).
  - Task detail: tinted header band holding back disc · "Complete" pill with check · assignee avatar · ⋯; title 28/700; meta line 12 grey with label and list icons; ghost row "Then tap here to add a task"; "Created by Rose · 7 min ago" 11 grey centred above a docked "Leave a message…" pill + coral + disc (06·1, 08·1, 08·6).
  - Messages: sent bubbles blue with white 15 text, max ≈290 wide, 16 right gutter, 4–5 pt between consecutive bubbles, time 11 inside; received grey with a 12 avatar + name; voice notes as waveform bubbles; recording replaces the composer with × · waveform · timer · stop (04·2, 06·5, 07·5).
  - Feature tips are lavender cards (≈136 tall, 24 gutter) with a 24 icon, 13 accent text and two equal grey pills ≈32 "Learn more" · "Dismiss", placed above the list they explain (09·2, 09·4).
  - Filter chips measured 29 tall; task rows with a sub-line repeat every ≈54 pt; the tab bar is 5 icons without labels plus a short coral underline under the active one (01·2, 05·5).
  - Long-press on a sidebar list blurs the whole screen, lifts the row as a white card and shows a 3-row menu (Rename, Remove from sidebar, Delete list in red with trash icon) (05·4).

## Rise (138) · calm task manager, violet accent
- Title 17/600 left with a gear right; search "Filter tasks" grey field 40 + sort disc; section labels 13 grey on a tinted band; rows radio 18 + 15 text, "Due today" chip yellow 11 right; done rows with a violet check.
- Task sheet: Cancel / Task / Save header, title 20/600, property rows icon + grey placeholder 15, segmented "Description / Activity" pill; picker as a rising list with a check.
- Calendar day view: hour labels 11 grey left, coloured blocks with a 2pt left stripe, a red "now" line, violet "+" disc.
- *From the full library (sheets 01–10):*
  - Settings sheet: rows at a 44 pitch, colour icon tiles 28 with ≈6 radius, label 15/500, grey value right ("System", "Google Maps"), violet toggle; groups separated by ≈12 extra air instead of cards; "Current build" 12 grey footer (03·3, 10·6).
  - Display sheet: group-by / order-by options as outlined boxes 45 tall, 1-pt border, ≈8 radius, 10 gap; selected box gets a violet border and an 18 check disc; toggles sit inside the same boxes; group labels 11 grey (02·3, 10·2).
  - Danger zone: pink card at the end of the profile with red 13/600 title, 11 red line and a red 30-pt "Delete account" pill with trash glyph; confirm sheet = title 15/600 + 13 line + red pill 29 over an outlined Cancel 29, 16 gutter (07·3, 03·6).
  - Recurring-event dialog: floating dark card with × top right, title 15/600 centred on 3 lines, radio rows 36 (This event · This and following · All events), then 30-pt stacked buttons red Discard · outlined Continue editing · violet Send update, an "or", violet Save without sending (07·2, 09·3).
  - Empty states: skeleton of two task rows ≈180 wide as the illustration, "Looking a bit empty!" 15/600, 13 grey two lines, outlined violet "+ Add new" pill 28 (07·1, 09·5); search miss = tinted circle icon 40 + "No tasks found!" 15/600 + 13 grey (03·4).
  - Toasts: light grey pill ≈49 tall at the bottom, overlapping the tab bar, 12/600 grey text ("Something went wrong when saving. Reverted.", "Scheduling link copied to clipboard") (08·4, 10·4).
  - Date and time pickers as sheets: month 15/600 + ›, violet chevrons, day cells ≈37, selected violet disc, Confirm violet 38 over outlined Clear 38, ≈6 gap (02·5, 09·2); time as a two-column wheel with a grey selection band and one violet Confirm (07·4).
  - Event RSVP: bottom band of three 32 pills — Maybe (violet fill when chosen), Decline (red ✕), Accept (green ✓), each icon + 13 label (04·5).

## ten ten (148) · black, giant type
- Profile: avatar 96, name 30/700, "PIN: …" mono chip, a big "+ add friends" dark pill 64 with memoji art; friend rows avatar 44 + name 15 + ⋯.
- Segmented "friend requests / sent requests" white-on-dark pill; rows with grey "re-send" pill and ×.
- Walkie-talkie: full-bleed portrait, "👋 Danny ⌄" 26/700, "hold to talk" white pill, a big avatar disc 96 with a green dot, "+" disc left, dashed "+ add friend" disc right.
- *From the full library (sheets 01–10):*
  - Confirm dialogs: dark grey card 295 wide (40-pt margins) radius ≈20 over a dimmed screen, title 17/700 lowercase, body 12 grey on two lines, red pill 41 tall inset 24, "cancel" 15/600 white text under; block/remove stacks two red pills (02·1, 02·2, 06·3, 06·4).
  - Bottom text menus: dark sheet with grabber, lowercase items 17/500 centred on a 66-pt pitch, no icons, no dividers; destructive "delete friend" / "delete account" red, "close" grey last (05·3, 05·5, 07·2, 08·6); "mute for:" picker uses the same sheet with 1 hour / 4 hours / 8 hours / forever (02·4).
  - Mute sheet: flag icon top-left and block icon top-right as 24 glyphs, purple disc 40 icon, title 17/600, 12 grey two-line explanation, purple pill 40 "mute Danny", text "mute everyone" (05·1, 09·3).
  - Sign-in on full brand red: three white provider pills 54 tall with 14-pt gaps at a 24 gutter (logo + 15/600 label), fourth option "use phone or email" as a translucent red pill; back 24 and "?" 24 in the corners (03·6).
  - Code entry on red: "enter the code i sent you by email" 24/700 white centred, six tinted boxes 45×55 at 7-pt gaps, the active one outlined; "code sent to …" 11 + "change" link; "can't find the mail?" translucent pill 44; the red keypad keeps the brand ground (04·4, 10·2).
  - Walkie states are a white pointer bubble 15/700 under the name ("hold to talk", "muted", "do not disturb", "is here!", "ghosted!") plus a badge on the 96 avatar disc (green dot, zZ, sparkle) (02·6, 03·1, 03·2, 04·5).
  - Achievements: 4×6 grid of padlock emoji ≈40 over a blurred photo, unlocked ones shown as their emoji; tap raises a dark card 17/600 ("ghosted a friend"); × disc 44 at the bottom (03·3, 04·3, 09·1).
  - Voice call: photo in a rounded card inset 16, name 26/700 with sound bars, glass pill 56 tall holding 4 icon toggles (active one white disc), red end disc 44 under (04·1, 05·6).

## Raycast (257) · light AI notes
- Header capsule: back disc, title 15/600 + "Ray-1" 11 grey, "+" disc; body 15 with 22 line height, headings 15/700; user prompts as grey 16pt-radius cards; action row of 5 tiny icons 16 grey.
- Composer: grey pill "Ask Raycast AI…" + a separate grey disc for voice; formatting bar above the keyboard with ✦ as the first tool.
- Empty: small grey icon + 13 grey line centred; toast "Text copied" as a white pill with a green check at the top.
- *From the full library (sheets 01–10):*
  - Notes list: header back disc 40 · app icon 20 + "Notes" 15/600 · ⋯ disc 40; purple-tint banner 13 with ⊗, corner 16; group labels 12/500 grey (Pinned, Today); rows ≈54 with no dividers, title 15/500 + 11 grey "Edited 2 minutes ago · 3,394 Characters"; floating search pill ≈44 + "+" disc ≈44 at the bottom (02·1, 06·5).
  - Swipe to delete slides the row and reveals a red pill ≈36 with a white trash icon; the confirming popover is anchored to the row: "Delete Note?" 15/600, 13 grey recovery sentence ("within 60 days"), red "Delete" in a grey pill (07·5, 09·3, 04·3).
  - Note editor: back disc · undo/redo capsule · ⋯ disc; body 14 with ≈20 line height, headings 15/700; floating bottom row of ✦ disc 40 · grey count pill ("2,365 characters" 12) · voice disc 40; with the keyboard up a formatting bar (✦ H list B I U S code …) sits above it and "Proofread · Rewrite" replace the suggestion row (03·4, 01·3, 02·6).
  - Menus are frosted popovers ≈235 wide from ⋯ or long-press: rows ≈40 (icon 16 + label 15), "Export As" opens inline with a chevron, "Delete Note" red last; long-press shows the row's title 11 grey on top (03·5, 04·6, 08·3).
  - AI result "Make Longer": floating card inset 8 with ≈32 corners, header app icon 20 + 15/500 + ×, result body 14, footer regenerate icon left, outlined "Copy" ≈34 + black "Apply" ≈34 right (06·1, 07·3).
  - Launcher: settings disc · "Search Raycast" pill · avatar 32; 4 app icons ≈44 on an 88-pt pitch with 11 labels; "Favorites" 12 grey + rows ≈50 (icon 24 + 15); a Raycast AI composer card docked at the bottom with a "Ray-1 ⇅" model switch (09·1, 02·5).
  - Model picker card: provider logo 20 + model 15, check disc on the selected row, red outlined "Deprecated" tag 10 (02·5). Find & replace: card above the keyboard with field ≈32, "Done" 13/600, "1 / 6" grey counter and prev/next discs 20 (03·2, 05·4).
  - Voice note: bottom bar trash · tick waveform · "00:05" 12 · red stop disc 40, orange dot in the Dynamic Island; then "Transcribing…" 12 grey beside a black stop disc (06·4, 10·4).

# More apps (v2 · 34 apps added from Refero, every sheet read)

## Asos (006) · light fashion commerce, caps chrome
- All chrome is uppercase: nav titles 13/700 tracked centred ("SAVED ITEMS", "CHECKOUT"), buttons 12/700 tracked, field labels 10/700 tracked; body and product names stay sentence case 12–13. (02·6, 05·2, 07·5)
- Home: grey search pill 36 with a camera icon right, underline tabs HOME / TOPMAN / SPORTSWEAR 12/700 caps with a 2-pt blue underline, then full-bleed promo blocks in loud flat colours (neon yellow, orange) with italic 800 caps copy. (01·4, 02·3)
- Product grid: 2 columns 164 wide, 15 gap, 16 gutters, image 4:5 (208 tall), price 14/700 + heart 20 right, name 12 grey on two lines; header "SORT ⌄ | FILTER" split bar ≈44 and "2,642 items found" 11 grey centred. (02·5)
- Filter value lists: caps title + grey "CLEAR" chip right, rows ≈52 (swatch disc 24 + label 13 + count grey in brackets) with a blue ✓ trailing, sticky black "VIEW ITEMS" bar ≈44 with square corners. (02·6, 03·1)
- Product page: edge-to-edge photo carousel with dots and a "121 ♥" count pill, SAVE / VIDEO icon + 10 caps label pair, price 15/700 (sale in red with struck RRP and "(-44%)"), colour thumbnails 48 with the selected outlined, "LOW IN STOCK" row with a clock icon. (03·3, 04·2)
- Fit assistant: height and weight fields each with a CM|FT (KG|LB) segmented toggle, blue selected; fit preference sliders with the value word above the knob; "SHOW MY SIZE" black bar. (03·5, 03·6)
- Brand picker step: 4-pt blue progress bar at the top, title 22/700 centred + 13 grey, wrapping outlined caps chips 10/700 ≈28 tall, selected filled black, A–Z index rail on the right, black "DONE" bar pinned. (04·4, 04·5)
- Bag: header "BAG" + green "CHECKOUT" rectangle ≈28 top-right, total line 12; rows thumb ≈90×110 + price 13/700 + name 12 grey + "LOW IN STOCK" 10 caps + two dropdown selects (colour, size) + QTY. (05·1)
- Saved items: rows thumb ≈90 + ⋯ + outlined green "MOVE TO BAG" button ≈24 (10/700 caps); a full-width mint banner ≈40 "Item added to Board" under the tabs confirms. (06·1, 06·2)
- Checkout: white sections separated by 12-pt grey bands, caps section titles 15/700, full-width outlined option buttons ≈48 with a leading icon split by "OR" (ADD POSTAL ADDRESS / CLICK & COLLECT), Premier promo as a black block, pale-mint disabled "PLACE ORDER" bar. (07·5, 07·6, 08·1)
- Errors are inline: red 11/700 sentence "Oops! This e-gift card code is not valid." under a red underline; the page-level info line sits in a grey band with an ⓘ 20. (07·2, 08·4)
- Empty states: outline icon ≈40 + caps title 13/700 + 13 grey line + one black caps button (a second green button on gift cards). (05·5, 09·2)

## Calm (017) · blue gradient wellness audio
- Ground is a full-bleed nature photo or a vertical blue → indigo gradient (#1a598f at the top to #1d2353 at the bottom); surfaces are translucent darker-blue cards; white appears only on sheets and pills (01·5, 02·4).
- Home: wordmark centred with two 36 glass discs (scene, gift), greeting 17/400 white about 330 pt down under the photo, a mood row as an outlined 44 pill (emoji 24 + 15 + ›), "Start with one of these" 17/500 (01·5, 02·1).
- Content cards: 335 wide at 20 gutter, ≈112 tall, 12 gap, ≈10 radius, square art 88 left with a ▶ badge, eyebrow 11/600 ("Meditation • 10 min"), title 15/600, sub 13 blue-grey (02·4, 02·5).
- Browse: chip tabs as outlined 28 pills (selected filled white, blue label), section 17/500 + "See All" 12, rail tiles 160 square 12 radius with a "▶ 35 min" chip bottom-left, title 13/600 + 12 grey (03·1, 03·3).
- Detail: title 28/400, narrator row avatar 36 + 15/600 + 12 grey role, 15 description, then duration variants as 52 rows (13/600 label + heart 20) with hairlines (03·4, 03·6); album detail puts a strict pair under the title — white "▶ Play" and outlined "Shuffle", 157 wide each, 52 tall, 12 gap (04·1).
- Player: dark photo, title 28/400 centred, 15 description, "ARTIST" 10 tracked caps eyebrow, three 36 discs (heart, share, timer), transport ≪ ❚❚ ≫ ≈36 white with shuffle / loop 20 at the edges, 2-pt progress with 11 times (04·2).
- Mini player 50 above the tab bar: art 50 flush left, pause 24, title 13 + sub 11, × disc 20 right, 2-pt progress line under (03·1, 03·4).
- Category filter sheet: white, × + "Category" 17/500 centred + "Clear", 2-column grid of outlined tiles 160 × ≈52, 12 column gap, 8 row gap, 20 gutter; selected tiles get a 2-pt navy border (04·6, 05·1).
- Paywall: photo top 40 %, title 22/400 two lines, 3 checked benefits (✓ 17 + 15/600 + 15 grey), white 52 pill "Try Free & Subscribe" inside a darker card with 11 legal (01·4); splash = photo, 26/300 three-word promise, white 52 pill at 16 gutter (01·1).
- Profile and notifications: chip tabs, rows icon 24 + 17/400 + › at ≈52 pitch; toggles white thumb on navy; reminder times as grey values right; groups split by hairlines (05·2, 05·3).
- Tab bar 3–4 items, icon 24 + 10 label, active white, inactive ≈50 % (01·5, 04·5).

## Kitchen Stories (022) · light recipe feed, orange and green
- Recipe grid: header 15/600 centred + filter glyph right; one text tab "Kitchen Stories" 13/500 orange with a 2-pt orange underline; 2 columns 165 wide at 15-pt gutters with 15-pt gaps; image 3:4 (165×221) with 12 corners; overlay chips top-left ("40 min." cream, "Vegan" green, 11 on ≈20 pills) and a white like pill bottom-right "♡ 2,214" 11; title 13 on 2–3 lines; author avatar 24 + name 12 orange (01·5, 02·2).
- Search: outlined field ≈40 with ⊗ and a filter glyph right; three text tabs (Kitchen Stories · Community · From the web) with the orange underline; "From the web" renders the site inside with a floating green "Download" pill 36 bottom-right; no results is an illustration + "We're sorry!" 13/600 + 15 two lines (02·3, 02·4, 07·6).
- Cooking mode: photo ~170 at the top with a × disc; ingredient and utensil lines 13 with basket / pot icons; step text ≈22/400 with a 31-pt line height at 16 gutters; times in orange inline with a timer glyph; a 64-tall step bar of numbered blocks (≈60 wide, 3-pt gaps) filled orange up to the current step, grey after, a flag block last (04·1, 04·3).
- Ingredients: "INGREDIENTS" 13/700 tracked caps; "4 servings" 13 + a −/+ grey stepper ≈32; two-column table amount 15 / ingredient 15 on a 19-pt pitch; a green "Add to shopping list" pill 44 hugging its label; a floating green "Start cooking!" pill with a shadow at the bottom centre (03·5, 06·4).
- Story cards: full-bleed photo with an overlapping card at the bottom (dark or cream, small radius): eyebrow "TODAY'S STORY" 11 tracked caps, serif headline ≈24/400 on three lines, author 12 orange + heart count right (02·5, 02·6, 08·1).
- Toasts: grey banner with small radius inset 8 at the top, text 15 dark, no icon, auto-dismissed ("The ingredients have been added to your shopping list.", "Successfully saved to 'Longshanks'.") (06·4, 07·2, 08·1); a green pill tooltip "Find your likes here" points at the Profile tab (01·5).
- Add-ingredient form: "Cancel · Add ingredient · Save" header with Save in orange; labels 11 tracked caps + red asterisk; value 17 on an underline; counter "5/55" 13 grey right; "MORE DETAILS ⌄" orange caps disclosure; the unit picker is an inline wheel under a cream "Done" bar (03·2, 03·6, 04·2).
- Sign-up: blurred food photo ground, serif "Sign up" ≈34, stacked pills ≈32 (Apple white, Facebook blue, Email green); errors 11 red under each field in the app's voice ("Knock, knock! Who's there?") (08·5, 08·6, 09·1).
- Tab bar: five items, icon 24 outline + label 10, active item a filled orange icon + orange label; "Create" in the centre is a plain item, not raised (01·4, 02·2).
- Comments: rows avatar 24 + name 13 + "10 months ago" 11 grey + ⋯; a 4:3 photo inside the comment; like count + "Reply" 12 grey; replies indented ~40; composer with a camera glyph, outlined field "Write a comment" and a grey "SEND" text (07·4).

## Cron (033) · light calendar, orange accent
- Root: hamburger left, month title ≈28/700 with a chevron (grey pill when the grid is open), a grey 28 date chip right that turns orange; weekday labels 11 grey; month grid rows 44 pitch, day numbers 15, outside days grey; today an orange 32 rounded square with white text; the visible range tinted grey (01·1, 02·1).
- Day grid below the month: "GMT+5" 11 grey column, day headers "Wed [24]" 13/600 with the orange date chip, hour labels 9–10 grey; now line 1 pt black with a "6:24PM" 11/600 label (01·1, 01·6).
- Events: muted colour blocks with a 3-pt left stripe in the calendar colour and an 11/600 label; dark mode keeps the layout on #1C1C1E with the same orange (01·2, 01·4).
- Bottom tray: grabber, "No upcoming meeting" / "Upcoming in 15 mins" 15 grey, ⋯, and a grey + disc 36 — the add button is not orange; notices arrive as a white card 15/600 + 13 grey with × over the tray (01·1, 01·3).
- Event sheet: "Event" 13 grey + ⋯ + "Done" grey pill 28; title 22/600; rows ≈40 with 16 grey outline icons: "9PM → 10:30PM 1h 30mins" (duration grey), date, all-day toggle, time zone, "Every week on Fri" with the qualifier grey; RSVP segmented Yes · No · Maybe 28; orange split button "Send invite ⌄" 40 bottom-right (01·5, 02·5, 02·6).
- Date picker: sheet with "May 2023 ›" 17/600 + orange chevrons, day grid, selected as an orange disc 36, full-width orange "Confirm" pale until changed (02·3).
- Repeat: "Every 2 weeks" with the editable value orange, weekday discs ≈28 outlined, selected filled orange; Ends as radio rows 32; unit picker as a list in a grey sheet (03·1, 03·2).
- Settings: grouped white rows ≈44 on #F5, group labels 13 grey, orange toggles, 12 grey help under groups, "Log out" red last, "Close" text top-right; list pickers rise under the row with the chosen value orange and a grey selected row with a leading check (04·6, 06·3, 06·4).
- Drawer: account row avatar 28 + 13/600 + 12 grey email + gear; 1/2/3-day view rows 40 with icons, selected as a grey pill; calendars with colour square + eye toggle; "+ Add calendar account" grey (02·2, 04·1).

## Todoist (034) · light task list, red header
- The brand red fills the header under the status bar: back chevron + title 20/700 white left + white icons 22 (warning, search, ⋯) right; content below sits on white. (01·1, 01·4)
- Task rows: check circle 20 at x 22 outlined in the priority colour (orange P2, grey none), title 15/400 up to 2 lines, 13 grey note on 1 line, meta 12 with the date in purple or orange + calendar glyph + link and comment glyphs; hairline inset at 48; 3-line rows measure 84 pt. (01·4)
- Sections: header 15/700 + count 13 grey + chevron + ⋯ right, 44 pt; "+ Add Task" row with a red plus; reorder sections lifts the dragged row with a shadow on a grey sheet. (01·5, 05·1)
- Browse root: grey ground, white 12-corner cards with 48-pt rows (coloured icon 22 + 15 label + count 13 grey right), an Upgrade card 83 tall with a star, "Projects" 15/700 with a caps grey "USED: 3/5" tag, project rows with a grey 8 dot + emoji; cards 18 apart; red FAB ≈56. (01·2)
- Task detail half sheet: breadcrumb "Education / Routines ›" 13 grey + ⋯ and × grey discs 28; check 22 + title 20/500; property rows 44 with icon 20 (date, coloured priority flag, grey label chip); outlined chips 32 (Reminder, Move to…); "+ Add Sub-task"; Comments with count, first comment, "Show All" red, composer pill. (02·2, 06·2)
- Settings: iOS grouped cards with 13 caps grey labels, 48-pt rows (measured 47.6), green toggles, 13 grey footnotes under groups with a red "Learn more"; a dark twin uses the same layout. (03·2, 03·3)
- Sign-in and questionnaire: illustration + 22/700 centred title, black "Continue with Apple" and outlined "Continue with Google" ≈36, "More sign-in options" 11 underlined; question screens use 22/700 left + 13 grey, choice cards 82 tall with an 18 gap (illustration 72 + 15/600 + red radio 20), a pink hint card, and Skip grey + Continue red side by side at 35 pt (Continue 50 % tint until chosen). (06·6, 07·1, 07·2)
- Multi-select: header becomes "Inbox · 3 selected" with Cancel / Select All; a 5-icon grey toolbar at the bottom (date, move, priority, assign, ⋯); ⋯ opens the iOS action sheet: Select Labels, Complete 3 Tasks, Duplicate 3 Tasks, Delete 3 Tasks in red, Cancel. (05·2, 06·4)
- Project editor: Color row with a 20 swatch, Parent project, Favorite toggle, then the view choice as two illustrated tiles (List / Board, ≈116 tall) with a red radio under each; "Archive Project" and red "Delete Project" each in its own card. (05·4, 05·6)
- Activity log: avatar 36 with a small badge, 15 sentence with bold "You" and italic task names, 13 grey quote, time 11 grey, project tag 11 right; filter sheet "Cancel · Activity: Inbox · Apply" with a red ✓. (03·4, 04·4, 05·3)
- Daily goal sheet: pale-green header "Daily Goal · 25 May 2023" 12 grey, "7 tasks completed" 22/700, "↑ 7 more than yesterday" 15 grey, the completed tasks with grey filled checks, grey full-width "Share" ≈40. (04·1)
- Notification opt-in happens on an explainer ("Support healthy habits" 22/700 + 15 grey + illustration) with three toggle rows behind the system alert. (03·1)

## The Athletic (038) · light editorial sports news
- Home/Discover: serif wordmark ≈20/800 centred with a 28 grey search disc right; hero image full-bleed 16:9 (375×212), headline serif ≈17/400 on two lines at 16 gutter, byline 11 grey + comment glyph and count. Story rows: headline serif ≈15/400 up to 3 lines left, 4:3 thumb 109×82 right, 40 pt between thumbs (row pitch ≈121), hairlines inset to the gutter (01·2).
- Section blocks: league logo 20 + title ≈17/700 slab, then a lead image 16:9 and a rail of 3:2 tiles 160×107 with 15 gaps, 2.2 visible; tile title serif 13 two lines + meta 11 (01·3, 01·4).
- "Most Popular": numbered list with large light grey numerals ≈24/300 as the leading element, headline serif 15, thumb 4:3 right (02·1).
- Game detail: back · "OAK @ TOR" 15/700 · share; logo 32 + abbr 13/600 + record 11 grey per side, score ≈34/400, "Sun, Jun 25 / FINAL" 11 centred; underline tabs Game · Stats · Plays; key-value rows (label 13 grey left, value 13/600 right) (02·3, 10·3).
- Standings and box scores are dense tables: 11 caps grey column headers, rows 49 pt, team logo 16 + abbr 13/600, streak W/L in green/red; a black-selected segmented control (Division · Wild Card · League) above; columns run off the right edge (04·1, 05·5, 06·1).
- Team pages repaint the whole header in the team colour (Senators red) with white tabs Home · Schedule · Standings · Stats · Roster; league pages keep a dark grey header (04·5, 06·3, 10·6).
- Account: first name as a serif display ≈30/800 + "Subscribed Member" 11; Following rail of 42 logo discs with 18 gaps (60 pitch) and 10 caps labels, "Edit" 13 grey; plain rows ≈78 pt tall, 15/600 label + chevron (05·1, 05·2).
- Following editor rises as a sheet over the home: "Done" red text · "Following" 17/700 · black + disc 28; rows red minus disc 22 + logo 24 + 15/600 + drag handle, swipe reveals a red "Delete" block (04·6, 07·2).
- Podcasts: text tabs Following · Discover with 2-pt underline; episode rows art ≈82 square, date 11 grey, title 14/600 two lines, play disc 24 + duration 12 grey + download glyph + ⋯ (07·6, 08·1).
- Player is a sheet: × · show name 15/700 · ⋯; art 344 square at 16 gutter; episode title 15/700 centred up to 3 lines; thin progress with 11 times; row speed "1.5x" · back 30 · ring ≈58 pause · forward 30 · AirPlay; sleep timer and queue glyphs below. Dark and light variants share geometry (08·4, 08·6).
- Article reader: header back · AA · comment count · bookmark · share; body serif ≈19/400 with ≈26 line pitch at 24 gutter; charts sit on full-bleed black blocks with the wordmark bottom-left (02·6, 03·1, 09·6).
- Intro and permissions: poster type ≈44/800 black on light grey, a black full-width 52 "Start Reading →" and "Already a subscriber? Log In" 13; the notification prompt appears over it, and a second custom alert asks again after "Don't Allow" (06·5, 06·6).

## Wise (039) · light money transfer app
- Home: avatar 32 with red dot left, "Earn $115" green pill 32 + chart icon right; "Account" ≈28/700; balance cards ≈208×206 radius 20 on light grey, flag 48 top-left, amount 20/600 + currency 13 grey bottom-left, 12-pt gap with the next card peeking; sections "Transactions" ≈22/700 + "See all" 15/600 underlined dark green (01·1).
- Rows: 48 flag or icon disc + title 15/600 + one to three 13 grey sub-lines, amount 15/600 or chevron right; pitch 80–92 depending on sub-lines (01·1, 01·6).
- Tab bar: 5 labelled items (11), centre "Send" a 42 green disc with an up arrow, active label bold dark green (01·1).
- Send calculator: × disc 32; underline tabs International / Same currency; two outlined amount fields 76 tall radius ≈10 (amount 22/500 left, flag 20 + code 20/600 + chevron right); fee lines on a dotted timeline with dashed-underlined green links; "Should arrive in 2 hours" 15 with the time bold; bottom bar under a hairline: outlined calendar disc 44 + green Continue 49 (03·2, 03·3).
- While computing, fee lines are grey skeleton bars and Continue is a grey disabled pill (03·1, 03·4); a blocked route turns the field outline red with a 13 red message under it (03·5).
- Recipient: logo 56 with a badge, name 22/600 centred, label 13 grey over value 15 pairs, outlined red "Delete recipient" pill 44, green "Send money" pinned; delete confirms in a system alert (04·3, 04·4).
- Confirm your order: order lines (icon disc 32 + 15/600 + 13 grey, amount right), quick-amount chips 31 tall outlined with the chosen filled green, "Payment method" 13 grey + underlined "Change", "Total" 17 row, pinned CTA (04·6).
- Currency picker: search pill 40 grey, group labels 13 grey over a hairline ("Recent currencies", "All currencies"), rows flag 40 + code 15/600 + name 13 grey (05·5, 05·6, 06·2).
- Onboarding carousel: 3D illustration, heavy condensed uppercase title ≈28, body 15 grey centred, dots, green pill 54 (07·1, 07·2, 07·3).
- Goal choice: two grey cards 155–178 tall at 17-pt gap, icon disc 40, title 20/600 centred, 13 grey sub; "Take a look around first" underlined text link (06·5).
- 2-step verification: rows icon disc 40 + title 15/600 + 13 grey body + a strength word 13/600 green ("Very secure", "Secure"); "Change default" underlined link beside the group label (08·6).
- Transaction status: grey top block with a yellow "!" disc 56, status 13 grey, amount 28/700, tag chip "Bills"; label/value rows 15 under "Transaction details" 20/700; outlined "View order" pill 44 (10·3).

## Bear (043) · light writing app, red accent
- Note list: 28-pt gutter (wider than the usual 16), title 15/600, 2-line preview 14 grey, a row of attachment thumbs ≈73 tall × ≈110 wide with 7-pt gaps, timestamp 11 grey, hairline under each note; header is hamburger · "Notes ⌄" 17/600 centred · search, no large title (02·4, 09·4).
- Create is a 57-pt red pencil disc 21 pt from the right edge, the only coloured object on the list; in Trash it becomes a trash disc, in the web help a chat disc (02·4, 07·3, 10·2).
- Editor: title ≈28/700, body 15 with ≈22 line height; a toolbar above the keyboard (undo · redo · # · keyboard switch · … · BIU) swaps the keyboard for a formatting keyboard: 4 × 6 grey keys at ≈54-pt pitch with H1, B, I, U, S, list, checkbox, code, link, table, camera (02·5, 03·6, 04·2).
- Long-press menu: note preview card on top, white menu ≈250 wide under it, rows ≈44 with trailing 20 icon, groups split by a thicker gap, "Delete note" red placed third, Export… and Copy as… expand in place (07·2, 08·1).
- Multi-select: header becomes "N selected" (red when > 0), radio circles 20 on the left of each note, a floating white bar at the bottom holds Cancel (red text on pale-red pill) · trash · share · ⋯ (07·6, 08·1).
- Swipe on a note reveals two square tiles with ≈8 corners: pin on pale red, delete on solid red (08·2).
- Settings open as a sheet with a 34/700 large title and × disc; a mascot "Bear PRO" card, then grouped white cards on grey, rows ≈43 with a coloured 20 line icon + 15 label + grey value + chevron, group labels 12 uppercase grey (05·5, 06·1).
- Typography sheet: font-size slider with value right ("16 pt"), stepper rows (label · value · − | + segmented), 12 grey footnote, "Restore Defaults" as red text on a ≈42 pale-red bar, and a live preview card of the result under it (03·5, 06·6).
- Theme swaps the accent, not only the ground: toggles are red on the light theme and blue on the dark one (04·3, 04·4).

## Google Maps (053) · light map utility, blue accent
- Explore root: map full-bleed; white search pill ≈48 inset 8 pt (x 8–367) with logo, "Search here" 17, mic and avatar 32; category chip row under it (white chips ≈32, icon 16 + 13/500, 8 gaps, scrolls off the edge); layers disc ≈40 top-right; locate disc 56 white and Directions disc 56 blue stacked bottom-right (measured 307–363 × 482–536); tab bar of 5 labelled items, active icon in a light-blue pill (01·1, 01·3).
- Map type sheet rises over the lower half: title 15/500 + ×; 3 image tiles 56 with 12 corners, selected with a 2-pt blue outline and a blue 11 label; "Map details" as a 4-column grid of the same tiles, two with red "New" badges (01·4–01·6).
- Place as a peeking sheet: grabber, title 20/400, rating 13 with stars and count, grey meta line, 3-photo rail, then a horizontal row of pills: filled blue Directions, the rest outlined ≈32 (Start, Call, Save, Share) scrolling off the edge (03·5, 03·2).
- Place detail: header back · truncated title 17/500 · share · ⋯; underline tabs 13/500 (Overview, Menu, Reviews, Photos, Updates) in blue; a sticky bottom bar of a 40 blue disc + outlined 32 pills (04·5, 04·6, 05·1).
- Saved: outlined "+ New list" pill 40 full width; list rows 70 pt (hairlines at 227 · 297 · 369 · 440 · 511 · 581 pt) with a coloured icon 24, title 15, 12 grey "Private · 5 places" and ⋯; a "Less" disclosure ends the group (06·1).
- Route planner: two stacked fields ≈36 joined by a dot-to-pin connector with a swap icon; mode chips with times ("10 min" in a tinted pill); route sheet "10 min (3 stops)" 17 green + grey, 13 grey reason line, filled blue "Start" 40 × 87 and outlined "Steps" 40 (08·3, 07·5, 07·6).
- Turn-by-turn: green instruction banner ≈88 tall inset 8 with arrow 32, street 24/500 and "toward …" 17; right column of 40 discs (search, mute, compass); bottom sheet with "12 min" 22/700 + 15 grey arrival time, reroute disc and red "Exit" pill ≈56, then menu rows ≈64 (icon 20 + label 17) (09·6, 10·1, 10·3).
- Account menu from the avatar: × + wordmark header, account row avatar 40 + name 15 + 12 grey email, outlined "Manage your Google Account" pill ≈32, icon rows ≈39 pt (icon 20 + 13), footer links 11 grey; identical in dark (10·5, 10·6).
- Toasts are dark bars at the bottom over the sheet ("Can't show your trip details"), a dark account snackbar with a blue "Switch account" link, and a white tooltip card with × and "Learn more" for zoom hints (01·2, 01·3, 08·2).
- Dark mode swaps map and chrome together; Directions disc becomes pale blue on dark (02·2, 04·3).

## CARROT Weather (056) · playful weather, blue cards
- Home: a blue hero card 344 wide at 16 gutter, ≈244 tall, 24 corners, with share and ⋯ icons at its top corners, city 17/500, temperature ≈90/200 white and a snarky two-line quip 17/400 centred (01·1).
- Daily rows at a 49-pt pitch: day name 16 grey-ink left, precipitation 13 blue with a drop icon, high 16/700 + low 16 grey right, over a 4.6-pt coloured bar spanning the high/low pair; the hourly strip above is 6 columns (time 12 with small caps AM/PM, icon 28, temperature 17/600) (01·1, 02·3).
- Tab bar: 5 labelled tabs; the first shows live data ("78↑ 61↓") instead of a label, the CARROT tab carries a red dot (01·1).
- Metric detail (temperature, wind, dew point, precipitation, humidity): back text + title 17/600 + share · a 6-segment day control ≈32 tall with a calendar icon at the end · "RANGE" 11 caps grey · value 22/700 · chart ≈150 tall with right-side axis and condition icons above · two metric cards 167×62, the selected one filled in the metric's colour (red, green, blue) · "About X" 17/700 + body 16 in a white card (02·5, 03·1, 03·5).
- Every screen has a pixel-identical dark twin (#000 ground, #1C1C1E cards) (02·6, 03·2, 05·5).
- Radar: header title is a dropdown ("Next-Hour Radar ⇕") opening a floating menu with a lock on premium rows; a 4-pt rainbow legend strip under the header; three floating 36 icon discs on the right; bottom timeline card ≈56 with play and a ticked scrubber (04·1, 04·2, 05·1).
- Locations: iOS grouped on grey; search field 36; the current location as a 205-pt card with a 7-column hourly mini chart; other places as 48 rows with an ⓘ; "Recents" group label 13 grey (05·4).
- Settings: iOS inset grouped rows 44, caps group labels 12 grey, blue "Add Location…" rows with a trailing +, 12 grey footnotes under groups (07·4); units as value-grey + chevron rows (08·6).
- Onboarding: 96 logo disc, two short lines 17 (brand name bold), 11 grey disclaimer, blue Continue 55 tall, full width at a 20 gutter (09·5); personality set with a 5-stop slider and a tooltip card naming the stop (10·3, 10·4).
- Empty alerts: a 96 grey warning glyph, "No Active Alerts" 20/600 grey and a one-word joke line 12 grey, centred (08·1).
- Achievements: rows with a 40-pt progress-ring icon (empty, filled, 50 %), title 15/500 + two 13 grey lines (09·3).

## Nike Training Club (057) · black-and-white editorial fitness
- Welcome: full-bleed video, swoosh top-left, "Nike Training Club" 22/500 white + tagline 22/500 grey, then two hugging pills side by side, white filled "Join Us" and outlined "Sign In", 112×≈48 (01·2).
- Questionnaire: step "1/2" 15/600 centred in the header; question 22/600 two lines left at 27 gutter; 13 grey explanation; full-width answer pills 1-pt grey outline, fully rounded, ≈48 for one line and ≈80 with a grey sub-line; the selected answer fills black with white text; no Next button (01·6, 02·1, 02·2).
- Permission primers: Apple Health on a full-bleed photo with a heart ring 56, title 22/600 white, 13 centred body, white "Allow Access" 48 full width; notifications on grey with an outlined icon disc 56, black "Allow Notifications" 48 over an outlined "Not Now" 48 (02·3, 02·4).
- Home: avatar 28 top-left, "Home" 28/500; "What's New" 17/500 + "View All" 13 grey + a 17 grey sub-line; a full-bleed poster card ≈380 tall with an eyebrow 13 and condensed caps title ≈30/800 white, white "Explore" pill 36 (03·1).
- Community section is typographic: "CONNECT WITH FRIENDS ON NTC" condensed ≈24/800 among floating avatars 32–56, black "Add" pill 36; the feed ends with "Looking for more? Let's do a workout!" 22/500 + black pill 48 (03·2, 03·3).
- Browse By: scrolling text tabs with a 2-pt underline, "40 workouts" 13 grey; rows thumb 101 square at 24 gutter, title 13/600, three 12 grey meta lines, outline bookmark 20 top-right; row pitch 124; a pinned bar "⇆ Filter | ⇅ Sort" with the count in "Filter (4)" (03·5, 03·6, 04·1).
- Program detail (dark): hero with title 28/500 white two lines + outlined "▶ Watch Trailer" pill 32; a 2×2 facts grid (icon 16 + 13); stages as "Stage 1" 13 + "Active" 13 accent + title 17/600 + 13 grey body + 3-segment progress; white "Start Program" 48 floats over a bottom fade (04·5, 04·6, 05·1).
- Live workout: black top bar with elapsed "1:41" condensed ≈48/800 white left and an outlined pause ring ≈44 right; white cards per circuit "Warm-Up" 17/500 + "⟲ 2x"; rows index 13 + title 13/600 + 12 grey instructions + thumb 60; the current exercise expands inline into a video with a scrubber and "Step 5 of 6" (06·2, 06·3, 06·5).
- Completion: header ✓ · date 15/600 · bookmark · share; photo with workout name 22/500 white centred; "2:46" 15 + "Duration" 11 grey; location glyph 44 + "Home" 15/600 (05·6, 06·1).
- Sharing: "SHARE" 13/500 caps header with × and "Post"; post preview; a ring with a spinner then a check and "POSTING/POSTED" 11 caps over the dimmed preview; share-to rows 48 with brand icon 24 + caps 11/700 label + chevron (07·4, 07·5, 08·1).
- Activity: History · Achievements tabs; a dark tooltip pill "You have new achievements!"; total workouts as a single numeral ≈72/800 with 13 grey label (08·4).
- Settings: flat rows ≈49 with 13 label + chevron and hairlines, groups separated by grey bands ≈32 with no labels; Partners uses caps 11 grey band labels and rows 56 with app icons 40 (09·4, 10·1).

## Gmail (069) · light utility inbox
- Inbox: a floating search pill ≈48 tall at a 15 gutter with a soft shadow (menu 24 · "Search in mail" 16 grey · avatar 32); "PRIMARY" 11/600 caps grey; rows at an 85-pt pitch with a 40 letter avatar, sender 15/600 (bold when unread) + time 12 grey right, subject 13, snippet 13 grey, star outline trailing, optional 28 attachment chip under the snippet (01·2).
- Compose is an extended white pill ≈47×135 with a red pencil + "Compose" 14/500 red, shadow, bottom-right; the tab bar has two icons only (mail red, video) (01·1).
- Snackbar: dark bar 48 tall, inset 8, "Moved to Trash." 14 white left, "Undo" 14/600 blue right, sitting above the tab bar (01·3, 08·5).
- Selection mode: avatars turn into blue check discs, rows tint blue, header shows the count + archive · delete · mark · ⋯; the action sheet is plain 44 text rows with Cancel last (01·5).
- Drawer at ≈80 % width: logo row, items ≈38 (icon 20 + 14 label), the selected item a pink-tinted pill capped on the right with red text and icon, counts 12 grey right, hairlines between groups (01·6, 03·2, 04·1).
- Thread: subject 22/400 in two lines + an 11 outlined "Inbox" tag + star; collapsed messages as one grey snippet line; a numbered circle for hidden messages; expanded header with avatar 40, name 14/600, time 12 grey, "to me ⌄", reply and ⋯ (02·2).
- Reply footer: three smart-reply chips 49 tall outlined with blue text, then Reply and Forward outlined 35, half width each (08·4).
- Search: back + query 17 + ×; dropdown filter chips ≈30 scrolling (Label, From, To, Attachment, Date), active ones blue-tinted; "Top results" / "All results in mail" 15/600; matched words highlighted yellow; empty as a 160 illustration + 13 grey "No matches" (05·3, 05·5, 06·1, 05·4).
- Recent searches: rows 42 with a 32 grey history disc; swipe reveals a red delete square 60 (06·5, 06·6).
- Settings: modal sheet, "Done" 17/600 blue top-right, large title 34/400, caps group labels 12 grey, white grouped cards on grey with 44.6 rows (28 coloured icon square + 17 label + chevron), 54 between groups (04·4, 07·6).
- Compose: × · attach · send header, To / From / Subject stacked 38 lines with hairlines, "Compose email" placeholder; a contacts-permission banner docks above the keyboard (02·6, 04·2).
- Coach mark: blue bubble with a pointer at the header icon, 15/600 title, 13 line, "Got it" 13/600 (04·2).

## Coinbase (093) · light and dark crypto wallet
- Home header: grid icon 24 · grey search pill 40 tall · bell 24; promo card (15 text + 3D coin art ≈56) and a strict pair of buttons 43 tall, 161 wide, 6 gap: "Buy & Sell" filled blue, "Transfer" pale-blue tint; gutter 24 (01·1, 01·4).
- Prices list: "Prices" 20/700 with a grey dropdown chip 36 tall ("Top assets ⌄") right; rows on an 80-pt pitch: coin icon 32 · name 15/600 + ticker 13 grey · sparkline ≈40 wide in orange/blue · price 15 right + change 12 in a tinted pill with ↘/↗ (red or green) (01·1, 01·4, 02·1).
- Skeleton keeps the list geometry: grey circle ≈24 + bar left, two short bars right, same row pitch (01·2).
- Top movers rail: grey cards ≈120×120 radius 16, icon 28, ticker 11 grey caps, price 15/700, change 12 coloured with arrow; next card peeks (01·3, 01·5).
- Asset detail: header back · name 15/600 centred · star · share; label 13 grey, price ≈28/700, change 13 coloured; full-width line chart with high/low labels 11 grey; range chips 1H…ALL 13, selected as a pale-blue pill; 5 action discs 42 blue with 12 labels, unavailable ones in pale blue (03·1, 03·2, 03·3).
- Action sheet (Buy / Sell / Convert): no title, rows ≈80 with icon 20 + title 15/600 + sub 13 grey + chevron; identical in light and dark (02·2, 02·3); list chooser sheet "Choose a list to display" 20/700, selected row as a filled dark card with a blue check (02·4).
- Welcome carousel: logo ≈130, "Welcome to Coinbase" ≈34/400 left, 6 dots, CTA 56 tall full width at a 24 gutter + "Browse assets" 15/600 blue text under (06·1, 06·2, 06·3).
- KYC flow: 4-segment progress bar top + "Explore" text right, illustration, title 17/700 left, body 15, bullet list, Continue 56 pinned; review screen lists steps with numbered blue discs 20 + label 15/600 + "Completed" / "In review" right (07·4, 08·1, 08·3, 08·4).
- Settings: flat rows ≈52 on white, section titles 20/700 ("Display", "Security"), toggles, dependent row greyed until the toggle is on, "Sign out" 15/600 red, app version + user ID 12 grey at the end (09·2, 09·3).
- Hide balances confirmation: bottom sheet with title 20/700 + body 15 grey + grey "Dismiss" pill 44 full width (09·4).
- Virtual assistant: bot bubbles blue radius 16 with white 15 text and a logo disc 24 at the left, user bubbles grey right; topic chips outlined blue 13/600 ≈32 tall wrapping right-aligned; composer pill 44 outlined (10·2, 10·3, 10·4).

## Copilot (100) · blue-branded personal finance tracker
- Root header: brand-blue band with "Copilot" 28/700 centred, gear 24 left, chat glyph right, then a scrolling row of text tabs 15/600 with the active tab in a white 30-pt pill; the band runs to ≈160 pt and the first white card overlaps it (03·5, 04·4).
- Dashboard: summary card at 16 gutters, "$10,700 left" 17/700 with a superscript $, 13 grey sub-line, burn-up line with a green "$4,637 under" tag; "TO REVIEW" 11/600 uppercase grey label with "view all ›" 13 blue; 4-up budget discs ≈56 with emoji, amount 13/700 and "left" 11 grey (03·5, 04·1).
- Categories: donut 72 between two figures (spent 17/700, budget 17/700 with 11 grey labels), then dense rows 32 pt: colour dot 6 + emoji 16 + 13 label, spent 13 tabular, a 60-wide bar coloured green (under), orange (near) or red (over), budget 13 right; column heads "SPENT · BUDGET" 11 uppercase grey (04·4, 04·5, 05·1).
- Recurrings: list rows 40 in white 8-radius cards with 8 gaps (date 11 grey · icon · name 13 · amount 13 coloured by status · tick), or a 3-up tile grid 90 × 90 with a corner flag for paid; a ≡/⊞ switch sits right of the "THIS MONTH" label; an empty month is one dashed "+" tile (05·4, 05·5, 05·3).
- Onboarding "Link bank accounts": sections titled 11 uppercase grey between two hairlines, account cards 2-up ≈106×62 in the account's own colour, dashed "Link new account" slots, two grey 36 buttons, and a full-bleed 90-pt blue "Continue" bar at the bottom (01·4, 01·6, 02·1).
- Sheets are minimal: a centred 11 uppercase grey caption ("ADD AN ACCOUNT"), then centred 15 text options ≈32 apart with no dividers or icons (02·2, 02·3, 06·4).
- Institution picker: 2 × 4 logo tiles ≈124 × 68 on grey 8 radius, "Link other institutions through Plaid" grey button 44, 13 grey fallback link (02·5).
- Investments: holdings rows 56 in one white card (ticker chip 11 grey · name 13 · sparkline 40 green · value 13 tabular); stock sheet with name 20/700, change 13 green ↗, price 22/700, a line chart with a scrub marker and date label, range segments 1D…1Y with the active one in a grey pill (08·3, 09·2).
- Coach marks: white popover with a pointer, 15/700 title, 13 body, blue full-width 32 "GOT IT" 11/700 (03·3, 03·4).

## X (114) · light social feed and composer
- Composer: "Cancel" 16 left, blue "Post" pill ≈32×60 right at 40 % opacity until text; avatar 32 + outlined blue audience chip "Everyone ⌄" ≈22 + placeholder 18 grey; an 8-icon blue toolbar (20-pt icons, no labels) docks on the keyboard, "Everyone can reply" 13 blue line above it. (01·2, 01·6)
- Audience and reply-control sheets: title 17/700 centred or 22/800 left + 13 grey explanation; option rows ≈68 pitch with a 40 blue disc and white glyph + 15 label; the selected option gets a green check badge on its disc, no trailing radio. (01·3, 01·4)
- Poll composer: outlined choice fields ≈44 with an in-field character counter 13 grey ("25"), + to add a choice, "Poll length 1 day ⌄" row that expands to a 3-column wheel (days · hours · min). (01·6, 02·1)
- Post detail: stats line "2 Reposts 1 Quote 33 Likes 4 Bookmarks" 13 with bold numbers between hairlines; 5 action icons 20 evenly spread; long-press menu is a floating white card of ≈36 rows with trailing 20 icons, "Delete post" first in red; delete confirm is the iOS alert. (03·3, 03·4)
- Share sheet: title "Share post" 15/700 centred, two text rows (icon 20 + 14 label), then 4 app discs 56 (pitch 87, 28-pt gaps) with 11 labels, then an outlined full-width "Cancel" pill ≈44. (03·6)
- Profile: gradient banner ≈120, avatar 64 overlapping with a white ring, outlined "Edit profile" pill ≈32 right, name 22/800, handle 15 grey, meta 13 grey with icons, "36 Following 1 Follower" 13 with bold numbers; scrolling tabs 15/600 with a 4-pt blue underline under the active one. (04·2, 04·4)
- Members list: grey search pill 36, "All / Moderators" underline tabs, rows at 72 pitch: avatar 48 + name 15/700 + grey role tag 10 + handle 13 grey, trailing black "Follow" pill 33 tall × 114 wide. (08·4)
- Subscribe: tiers as a carousel of dark cards 53 tall; features in grey grouped cards of ≈22-pt rows (13 label + ⓘ + green check or grey value right); pinned black pill 37 "Starting at $22"; plan sheet with two cards (selected outlined blue 2 pt, green "SAVE 13%" chip), black "Subscribe & Pay", legal in an outlined box 11 grey. (08·6, 09·1, 09·2)
- Sign-up entry: X logo 28 centred, headline 28/800 left mid-screen, two outlined social buttons ≈30 + "or" hairline + black "Create account" 33, all 310 wide on 32-pt gutters; legal 12 grey with blue links, "Log in" link at the bottom. (10·1)
- Account form: underline fields with 13 grey label over a 17 blue value, green check disc 20 trailing when valid, red "!" disc and a full-width red bar with 12 white error text under the field; black "Next" pill ≈32 bottom-right, grey when disabled. (10·2, 10·4)
- Interests step: 2-column outlined tiles 167×72, gap 8, 16 gutters, label 13/700 bottom-left; footer "0 of 3 selected" 12 grey left + disabled "Next" pill right. (10·6)
- Live audio room (Spaces) is a sheet: "REC" chip, title 17/800, host avatar 56 + role 11; bottom bar = mic disc 44 with "Mic is off" 10 label + 5 unlabelled 20 icons; overflow is a floating card of 36 rows with trailing icons; reactions as a 2×5 emoji tray. (04·5, 05·1, 05·4)

## Acorns (122) · light investing, green money screens
- Root header: "Home" 15/600 centred, profile glyph left, and two chips right, a grey count pill "◐ 2" and a violet filled "Get $888" pill ≈28; sub-screens centre a 13/600 title over a 11 grey state line ("$0", "Market is closed") (01·1, 01·3, 01·5).
- Fund detail: text tabs "Performance / About" 15 with a 2-pt underline; price ≈28/700; change line 15/600 with a green up or red down arrow; one green line chart ~250 tall edge to edge with no axes or grid; range control 1D·3M·1Y·3Y·5Y as a grey pill ≈42 tall at 20 gutters, selected white; 11 grey disclaimer under (04·3, 04·4, 05·3).
- Stats: "Your position" / "Stats" 20/700 with "As of 14 hr. ago" 11 grey right; rows label 13 grey + ⓘ + value 13/600 right on a ~34-pt pitch, no hairlines (04·4, 04·6).
- Holdings: 48 black discs with the ticker in white 13/700, symbol 13/600 + company 11 grey, weight % right; "Top holdings" with "10 of 508" and a dark tooltip bubble for the ⓘ (05·2).
- Settings: white sections separated by 8-pt grey bands; section title ≈20/700; rows on a 60-pt pitch with a 20 outline icon, label 13 and a chevron, the trailing slot carries the state (green "Premium", red ! badge, toggle, violet "New" chip) (09·2, 09·3).
- Primary action: green pill 45 tall, full width at 20 gutters (10·6); black pill for neutral steps ("Next", 06·3, 07·1); disabled grey (03·6).
- Money input: "Monthly recurring amount" 13 + "$249" ≈28/700 + a tick-ruler slider; Round-Ups slider with $ tick labels 11 and a dark value bubble over the thumb, example sentence with the value in green (04·1, 03·4).
- Confirmations are centred white cards: title 15/600, body 13 grey centred, a hairline, then "Cancel" grey text and the action in green text split in two halves (04·1, 04·2).
- Cancel flow: retention screen "Switch to Acorns Assist?" with five icon rows and a green "Downgrade instead" pill + "No thanks, cancel my subscription" text; final step "Close and cancel subscription" as a red outlined pill; success as a 64 green check disc + ≈20/600 line + green Done (10·2, 10·4, 10·5).
- Tab bar: five icons 24 + labels 10, active label black 600, violet dots under items that need attention (01·1, 06·1).
- Message Center: 44 black icon discs with a violet badge dot, title 13/700 + 13 grey body, rows separated by inset hairlines (09·6).

## Uber Eats (131) · light food marketplace, black actions
- Home header: 12 grey delivery-time eyebrow over "1248 E 23rd St ⌄" 15/600, bell and cart 24 with a green count badge; a grey search pill ≈44; a category rail of 3D food icons ≈44 with 11 labels (≈5.5 visible); a row of grey filter chips ≈32 with ⌄ (01·2, 01·3).
- Sections: title 20/700 + a 32 grey → disc; rail tiles ≈230 wide with ≈104-tall image, 12 corners, ≈6 gaps, a green "Top Offer" badge 11 top-left, name 15/600 + heart right, fee 12 with a gold member glyph, rating 12 grey (01·2, 02·1); "Stores near you" uses 56 circle logos with 11 labels (02·2).
- Loading: skeleton of four grey 64 circles, two 120-tall rounded blocks and grey text bars in the same layout as the loaded feed (01·6, 03·1).
- Map search: floating white search pill with back disc, a chip row over the map (selected black), rating pins as small white pills, a white "List" toggle pill and a bottom carousel card (03·4, 03·5).
- Sort and Dietary sheets: title 17/700 centred, rows ≈52 with black radio or checkbox, full-width black Apply ≈44 and a text Reset under it (04·2, 04·3).
- Cart: rows with 73 square thumbs (12 corners), name 15/600 + price 13 grey, a trash · n · + stepper; "+ Add items" grey pill; full-bleed gold Uber One savings bar 50; black "Go to checkout" 57 tall × 344 (05·3, 05·4).
- Checkout: Standard / Schedule option cards with the chosen one outlined 2 pt black, a map with an "Edit pin" pill, rows icon 24 + 15/600 + 12 grey + chevron, fee lines with the old value struck through, black "Place order" 57 (06·2, 06·3).
- Account: name ≈30/700 left + avatar 48 right, three grey tiles ≈82 (icon 32 + 13/600), then rows at a 64-pt pitch (icon 16 + 15/500 + 12 grey sub-line), no chevrons, no hairlines (07·5, 07·6).
- Empty orders: illustration ≈70, "No orders yet" 17/700, two 15 grey lines centred, a black "Start an order" pill 37 tall hugging its label (07·1).

## Apple News (136) · editorial news reader
- Today feed (dark): date eyebrow "News+ / August 19" 13/700 top-left instead of a big title; 2-up story cards 167 wide with an 8-pt gap on a 16-pt gutter, 12-pt corners, dark grey card on black; image on top, publisher logo 11, headline 15/700, footer "35m ago" 11 grey + ⋯; then full-width cards with the image at the right (01·1).
- Channel pages replace the title with the publisher's own wordmark (serif, centred between a 28 back disc and a 28 ⋯ disc) and set headlines in the publisher's face; list rows = headline 15 serif + 96 square thumbnail right + red "News+" tag 10 and ⋯ in a footer line (01·2, 01·3).
- Article reader: body 17–19 serif on a 20-pt gutter, line height ~1.45; header discs back · reactions · share · ⋯; "Included in News+" 11 centred under the header; photo caption 11 grey; byline with a 64 portrait (02·1, 02·2, 03·1).
- Following tab: large title with a 36 grey search field; utility rows red glyph 20 + label 15 at a ~45-pt pitch with no dividers; then section rows 17/700 with red chevrons that expand in place; "Edit" red top-right (04·3, 04·4).
- Topic search results: grouped cards with rows 46 = rounded-square monogram 28 + name 15/600 + a 20 red-tinted + disc; following flips it to a filled red check and a banner card drops in on top (red check disc 32, title 15/600, 13 grey, ×) (03·3, 03·4, 03·6).
- Paywall sheet: News+ wordmark top-left + × disc, headline 28/800 centred on 3 lines, 15 grey body, collage of three phone mockups, red CTA 325×51 on a 25-pt inset, 11 grey renewal line under (04·5).
- Welcome: red logo 44, title 36/800 on two lines with the second line in red, 15 body, privacy glyph + 10 grey paragraph, red CTA 289×51 at the bottom on a 44-pt inset (08·6, 09·1).
- News+ tab: three 36 pill chips at the top (Downloaded / Newspapers / Catalog, selected inverted); magazine catalogue as a 2-column grid of 3:4 covers with a stacked-issue shadow, title 13/600 + "✓ FOLLOWING" 10 caps grey or an outlined red "FOLLOW" chip 20 (10·1, 10·2).
- Crossword archive: dark card list, rows at a 131-pt pitch = 96 thumbnail showing the grid's progress + red eyebrow 11 + date 15/700 + title 15 + difficulty 12 grey + author 11 (07·5).
- Audio tab: title with a red "Play" pill 36 top-right that turns into a grey "Playing" pill; Editors' Picks rail of ~290-wide cards (16:9 image, eyebrow, headline 15/600, "See Details" red 11 + progress); mini player as a dark card above the tab bar with 15-s skip, play and × (05·4, 06·1).
- Empty Saved Stories: "No Saved Stories" 22 grey centred and nothing else; "Clear" greyed in the header (08·4).

## Target (144) · red-accent retail, light and dark
- Tab bar: 5 labelled items (Discover, Essentials, Wallet, Cart, My Target) icon 24 + 10 label, active in red, cart count as a red 16 badge; every screen, light and dark, keeps it (01·1, 04·3).
- Cart: title ≈32/800 left with a 13 grey "$110.99 subtotal • 2 items" line and a ⋯ disc 36 at right, over a faint doodle pattern in the header only; item rows carry a ≈100-pt photo, price 17/700, name 13, a red "Add to cart" pill 36 and a heart (03·6, 04·1).
- Order summary: rows on a 64-pt pitch with full-width hairlines (leading icon 24 or green check, title 17/700 + 13 grey, trailing ⓘ 24 or blue "Add"), sections split by an 18-pt grey band; footer red "Check out" 44 + outlined Apple Pay 44 side by side at the 16 gutter (04·6).
- Shop All Categories: nav 44 (red ← · title 17/700 centred · red search), rows 64 with full-width hairlines, icon disc 40 at a 12-pt edge, label 17/700, grey chevron (09·6).
- Payment sheet: title 15/700 + × disc, radio rows on a 64 pitch with a green selected radio and inline card-brand logos; unavailable methods are greyed with ⊘ and a 13 grey reason; red "Continue" 43 full width (10·3).
- Empty states: illustration disc ≈160 (grey or full colour), title 17/700, one 13 grey line, no button: "Try a different search term", "No previous orders", "You have no gift cards added." (03·3, 08·1, 10·6).
- Store hours: title 34/700, three action tiles ≈109×52 (icon 20 + 11 label in blue), then day rows (day 17/700 + date 13 grey, open/close 13 right), today in green (09·4, 09·1).
- Coachmark: dark card with title 13/700 + 13 body and a blue "Got it" split off by a vertical hairline, pointing at the control it explains (08·4).

## Tripsy (149) · light travel planner, orange accent
- Onboarding: pale peach gradient top, one glossy 3D icon ≈120, title 28/700 centred, 15 grey three lines centred, 7 page dots in orange, full-width orange gradient pill ≈48 at 20 gutter (01·2, 01·3, 01·4).
- My Trips: title 17/600 centred with three orange-tinted 28 discs (settings left, stats and + right); search pill 36 grey; years as headers ≈22/600 (current year orange with ⌄, past years grey); rows cover 97×97 with ≈20 continuous corners, "3 years ago" 13 grey, title 20/600, "Nov 11 → Nov 18" 15 grey; 15 pt between covers (row pitch 112) (02·4, 09·6).
- Empty trips: card with a tilted photo collage, "Welcome Traveler!" 22/700, 15 grey two lines, black pill 40 "Create a Trip" (02·1).
- Places sheet: "Places ⌄" 13 grey eyebrow over "Quest Voyage" 24/700; orange-tinted chips 28 (Categories ☰, Cities ◉); "Sort by Distance ⇅" 13 orange + "Current Location" 13 orange; city header 15/600 grey with a flag right; rows tinted category disc 32 + 15/600 + orange distance 13 + grey address; bottom bar filter glyph · "All / 5 activities" · + (02·6).
- Multi-select: radio circles 22 lead each row, selected rows get a grey band and an orange check; a floating dark capsule toolbar (Date · Move · Remove · More, icon 22 + label 11) sits 16 from the edges; More opens a dark 3-row menu with trailing glyphs (03·1, 03·2, 03·3).
- New Activity: Cancel 15 orange above a large title 28/700; search 36; four pastel discs 56 with 11 grey labels (Flights · Lodgings · Routes · Car Rental); category rows 44 with a tinted 20 icon + 15/600 + trailing ↗, grouped under 13 grey labels (04·2).
- Place detail sheet: title 22/700 + 13 grey type line, share and × discs 28; three action tiles 107×81 with 8 gaps (icon 24 orange + 13 grey label); grouped cards with a 13 grey label over an orange 15 value (phone, website), address in ink; separate 52-pt cards for Total Cost, Write a note, Add File, 15 pt apart (06·3, 04·5).
- Date/time inside rows: grey pills 28 "Date" and "Time" trail the row; the time picker rises as a half sheet with Cancel · name + date 11 · orange "Save" pill, wheels, then tinted "Timezone" and red "Clear Time" pills (06·4, 06·5).
- Trip header: full-bleed photo with overlapping flag discs 32, title 28/700 white, "Starts in 35 days, 7 days trip" 13; three frosted discs 56 with 11 labels; a white flight card ARN ✈ DXB with codes 24/700 (05·6).
- Stats: "0 Visited" 40/700 orange next to "247 World total" 40/700 grey and a 0 % ring 72; continent rows 40 with a globe icon and "0x" grey; a PRO card behind blur with a lock and an orange "Unlock" pill 28 (08·4, 09·3).
- Plans: dark screen, "Tripsy PRO" 28/700 + "All Plans"; four outlined row cards ≈60 (name 17/600 left, price 17/600 right, "81% OFF" 13 orange), selected outlined orange; orange "Continue" 48 pinned; "What's Included" as a Free/PRO table with orange check discs 22 and empty circles (08·5, 08·6).
- Settings: grouped white cards on grey, caps group labels 13 grey, rows 52 with orange-tinted glyph 22 + 15 + chevron, trailing grey value ("English"); "Close" orange text top right; Delete Account red in its own card (09·4, 10·4, 10·6).

## Google Gemini (153) · white AI assistant chat
- Welcome: 4-point blue star 24, title ≈34/400 left over 3 lines with ≈45 line height, "Gemini" in a blue→pink gradient, 15 body; the bottom band (hairline above) holds the Google wordmark, account row avatar 32 + name 13 + email 11 grey + chevron, and one full-width blue 4-radius button ≈30 tall "Continue as John" (01·1).
- Empty home: only "Hello, Connie" ≈26/500 in the gradient, centred; composer docked (01·3, 02·3).
- Composer: white pill 44 with 1-pt border, "Ask Gemini" 15 grey, an inner grey capsule holding mic + camera glyphs, a separate 44 disc for Live on the right; 11 grey disclaimer with an underlined link under it (02·2). While answering, the Live disc becomes a black stop disc (06·6, 07·2).
- Chat: user prompt as a grey-blue bubble ≈44 tall, 18 radius, 15, right-aligned; the answer has no bubble: star glyph 18 left + speaker 20 right, body 15/400 with ≈23 line height, 16 gutter; under it 6 grey 20-pt icons 36 apart (up, down, G, share, copy, ⋮) (02·2, 03·1).
- Snackbar: dark grey rectangle ≈52 tall, 4 radius, 8-pt side margins, 14/400 white left ("Thank you for your feedback", "Chat renamed", "Image downloaded"), optional trailing "Open" (03·2, 08·2, 08·6, 10·2).
- ⋮ menu: floating white card ≈200 wide, rows ≈36 (label 15 left + icon 20 right), groups split by an 8-pt grey band; "Modify response" expands in place into Shorter / Longer / Simpler / More casual / More professional (05·1, 05·5).
- Rating feedback sheet: "Why did you choose this rating? (optional)" 15, outlined 36 chips that tint blue with a check when picked, multi-line field, 11 grey legal, "Submit" blue text right (02·4).
- Public link: preview in an outlined card, "Headline" as two selectable cards (selected tinted blue with a pencil), 11 info line, "Cancel · Create public link" as text buttons; then "Public link created" ≈22/400 with the URL in a blue-tinted pill + copy and share glyphs (05·2, 05·3).
- Live: black stage, a blue-violet glow band at ≈60 % height, "Live" 13 with a waveform glyph at the top, two 64 discs with 11 labels: grey pause "Hold" + red × "End" (04·1, 04·2).
- Voice picker: full-screen pager on black, name ≈44/400 white centred, "Bright · Higher voice" 13 grey, dots + ‹ › chevrons, one dark "Start" pill ≈64; header × + title 15 (04·4, 04·5, 04·6).
- Chat history: 11 grey section labels ("Pinned", "Today"), rows ≈42 pitch: 20 glyph in a 24 grey square + title 13 + pin 16 right; long-press lifts the row as a white card over a blur with Pin · Rename · Delete (red) (07·5, 07·6, 08·1).
- Loading answer: three shimmering blue gradient bars 12 tall (last one ≈60 % width) under the star glyph (06·6).

## Structured (154) · pastel day-timeline planner
- Timeline header: "December" ≈26/700 ink + "2024" in the blue accent, four accent glyphs 22 right (✦ AI, calendar, inbox, gear); week strip: day 11 grey over date ≈16/500, today a 28 accent disc, a row of tiny colour dots per day for its tasks (01·2).
- Timeline body on a white rounded sheet: time labels 9 grey in a ≈50-pt left column; each task a vertical capsule 56 wide whose height follows the duration, tinted in the task colour with a 24 icon, joined by a line; time 11 grey + title 15/600; a 22 completion circle right that fills with a check in the task colour and strikes the title (01·2, 01·3).
- Free time between tasks is a line of 11 grey text ("1h 1m to pursue passion.") + two tinted chips ≈24 "Add Task · Copy Day"; FAB 56 accent "+" bottom-right, turning into a red trash disc while dragging a task (01·2, 01·5).
- Task quick sheet: header card (icon 24, date 11 grey, title 17/600, × disc), three equal tiles ≈60 (Delete, Duplicate, Complete: icon + 11 label in the accent), then a tinted full-width "Edit Task" 44 (01·6).
- Task editor sheet: title "Edit" 22/700 ink + "Task" in the task colour; sections as questions 15 grey ("When?", "How long?", "What color?", "How often?", "Needs alerts?") with "More…" right in the task colour; wheel with the selected slot as a filled pill; durations as a segmented row (1 · 15 · 30m · 45 · 1h · 1.5h); colour discs 38, 16 apart, selected ringed; "Every 7 days − +" stepper; alert rows 44 grey with bell + ×; CTA ≈56 filled in the task colour; the whole sheet re-tints when the colour changes (02·2, 02·3).
- AI planner sheet: "Structured AI ✦" 22/700 grey, "Hi there!" 22/700 accent + question 22/700 ink; a rail of suggestion cards (icon + 13/600 + 11 grey); composer = outlined 44 pill with a 2-pt accent border, mic + scan glyphs; typed text expands into a card with a mono 11 counter "123/500" and a "✦ Generate" accent pill 28 (03·3, 03·5, 04·2).
- AI result: collapsible "Your plans" card with "✓ Accept All" accent + thumbs up/down; grey caution card with ⓘ 11; proposals as grey cards (icon 24 + date 11 + title 15/600); tapping one reveals Add · Edit · Discard accent chips 28 (04·3, 04·5).
- Scan: camera with a 64 white ring shutter, "Cancel · ⚡ · Auto" header; review with Done / Retake text and a bottom row of 4 tool glyphs (crop, filter, rotate, trash) (05·2, 05·3).
- Onboarding: full-bleed salmon illustration pages, title ≈32/400 + one bold word, dots top-left, "Skip" 15 right, 36 arrow disc bottom-right; question pages add a thin progress bar + back, a title 24/700 with one word in salmon, a wheel with the selected time as a salmon pill 44, full-width salmon "Continue" 44 (07·2, 07·3, 07·4, 07·5).
- Plan picker sheet: "Choose a plan" 17/700 + × disc; three cards ≈80 tall, 12 radius, 12 apart (name 17/700 left, price 17/700 + "/ month" 13 right, 13 grey sub), the selected with a 1-pt accent border and a "FREE TRIAL" 10/700 chip; "Request Scholarship" and "Redeem" as 15 accent links under 13 grey questions; no separate CTA (07·6).
- Settings: iOS grouped rows 36–44 (icon 20 + 15 label + toggle or ↗), 11 grey caps group labels and 11 grey footers; each page opens with a pastel illustration card; "DANGER ZONE" group last with a red "Delete Account" (08·5, 09·5, 10·1).
- Energy limit: a "− [4/20] +" stepper whose pill fills green in proportion to the value, mono ≈20 figures (03·1).

## Tinder (157) · light swipe-card dating app
- Discovery: header 44 with the wordmark 22 left and bell · filters · boost disc right; the card fills the width (≈565 tall), photo progress as 2-pt segments at its top, name and meta over a bottom gradient with a green "Nearby" chip and an ↑ info disc 24 (01·3, 02·5, 02·6).
- Action row overlaps the card bottom: 5 white discs 43 / 62 / 43 / 62 / 43 with 17-pt gaps (rewind yellow, nope pink, super-like blue, like green, send blue); tab bar of 5 unlabelled icons with a brand-gradient active flame (02·5, 01·3).
- Welcome: full-screen brand gradient, wordmark centred, white pills 50 tall at 31 gutters with 16 between, 12 white legal lines with underlined links above, "Trouble signing in?" 15/600 white text under (01·1, 01·4).
- Code entry: back chevron, title 28/700 left, number 15 under, 6 underline slots, grey disabled "Next" pill 50 above the numeric keypad (01·6).
- Interests: title 28/700 with "0 of 10" 15 grey right, grey search field 36, outlined chips 26 tall with 13 labels, 8 horizontal and 10 vertical gaps; while searching, the chosen ones rise to a top rail as dark filled chips with × (04·1, 04·2).
- Coach marks: a black card over the deck, glyph 32, 15/700 uppercase heading with a 2-pt colour underline (red for pass, teal for like), 15 white body centred, and the one disc the gesture maps to shown under it (02·4, 03·3, 03·4).
- Edit Info: "Edit / Preview" text tabs 17 with the active in brand red, grey group bands ≈55 with 13/700 uppercase labels, white 44 rows with chevrons or toggles, a "Tinder Plus" pill badge on a paid group (06·2, 06·4).
- Photo slots: 3 × 3 grid of 2:3 tiles, dashed borders on empty slots, a brand "+" disc 20 on each corner, × disc on filled ones; "+35%" nudge in brand red next to the label (05·1).
- Centred modals: white card 16 radius, blue check badge 32, title 17/700, 13 body, gradient pill 44 + outlined "Maybe later" 44, page dots when there are several (07·6, 08·4, 08·5).
- Paywall: title 22/700 two lines, horizontally peeking plan cards 263 wide with the selected one in a 2-pt black outline and a check, a dark 44 pill "Continue - $21.99 total"; scrolling collapses it to a bottom bar "1 Week / $21.99 total" + dark 36 "Continue" (10·3, 10·4).
- Out of people: pulsing radar around the user's avatar, 13/600 message, distance slider with "20 mi" value, gradient "Done" pill 44 and "Go to my settings" 15/600 text (04·5).

## Apple Invites (163) · dark event invitations, photo-led
- Root "Upcoming ⌄" ≈28/700 with a + disc and a 28 avatar; one event per screen as a card 337 wide (19 gutter) × ≈575 tall with ≈28 corners, background art full bleed, a "Hosting" chip with crown top-left, the title in a wide display face ≈34/800 white and date/place 14 under it; a dark "1 Access Request ›" pill below the card when guests are waiting (04·1, 09·1).
- Intro: carousel of tilted portrait event cards, title ≈30/700 centred on 2 lines, 13 grey sentence, a white "Create an Event" pill 49 × ≈180 that hugs its label rather than spanning the width (01·5, 01·6, 02·1).
- Create screen is the invitation itself: gradient ground, "Add Background" pill, then stacked translucent cards (title placeholder ≈30/700 grey, Date and Time, Location as centred icon + 15 label cells ≈62, host card); × top-left and a "Preview" pill top-right (02·2, 04·2).
- Background picker: Photos and Camera as white 52 discs with 12 labels, sections Emoji / Photographic / Colors 20/700, portrait tiles ≈88 × 120 with ≈10 corners, 3 visible + a peek, the page scrolling vertically between rails (02·3, 02·4, 04·3).
- Event page: every section is a translucent card tinted from the background (16 gutter, ≈8 gaps), centred: small icon + 13/600 label in the event's accent (Weather, Directions, Shared Album) + 15 body; optional features are cards with a × corner and a tinted ≈36 pill ("Create Album", "Add Playlist") (05·3, 07·1, 07·5).
- RSVP: a 3-segment capsule ≈72 tall (Going · Not Going · Maybe, icon 16 + 13/600), the chosen segment turns white; the reply sheet has "✓ Going" 22/700 + ×, a name row with Edit, a message field and a full-width white "Send Reply" 51, with a 12 grey privacy note (06·2, 06·3, 06·6).
- Invite sheet: "Invite with Public Link" card with four share discs ≈45 (Messages, Mail, Share Link, Copy Link) + Approve Guests toggle + 12 grey footnote; "Invite Individuals" card with a Choose a Guest field; guest list grouped by 11 uppercase status labels (HOST, GOING (1), REQUESTING TO JOIN) with green ✓ / red × discs (08·3, 09·2).
- Confirmations are dark centred HUDs: "Copied to Clipboard" with a green icon over the sheet, "Invitation Sent" with a green check near the bottom (03·4, 08·3).

## Substack (169) · light reading and notes feed
- Home header has no title: orange bookmark logo 24 left, grey search pill 36 centred, avatar 28 right; then a rail of post cards 190×240 (8 gap, 12 corners) with image on top, 10 grey caps publication eyebrow, 13/700 title, "New · 1m read" 11 + ⋯, and a × to dismiss on each card. (01·1)
- Note rows: avatar 28 + name 15/600 + time 13 grey, sub-line publication 13 grey + "Subscribe" 13 orange, body 15, embedded post card indented to x 56 (16 right gutter), action row heart · comment · restack · share 20 grey with 13 counts. (01·1, 02·3)
- Orange FAB 44, rounded square (≈12 corners) with a white +, bottom-right above a 5-icon unlabelled tab bar that marks new activity with a 4-pt orange dot under the icon. (01·1)
- Toasts are dark grey pills ≈40 at the bottom centre above the tab bar: glyph 20 + 14/500 white ("Note posted", "Post saved", "Copied link", "Blocked", "Post archived"); no action. (01·5, 02·2, 03·2, 08·2)
- Hiding a note collapses it in place to a panel: "Note hidden" 15/600 + 13 grey reason + outlined "Undo" pill right, then 4 rows (icon 20 + 15/500): show fewer, snooze 30 days, unfollow, more options. (02·6)
- Comments: name 15/600, time 11 mono grey, "AUTHOR" 11 mono purple tag, grey "Liked by …" tag, body 15, actions "LIKE · REPLY" 11 caps grey + ⋯; docked "Leave a comment" field with avatar 24 right; options sheet: 13 grey quote of the comment, 3 rows, "Report comment" red. (03·6, 04·2)
- Settings sheet: × 24 left, title 34/800 left, profile row card with avatar 40, grouped white cards on grey with 54-pt rows (measured pitch 54.6): dark 24 icon tile + 15/600 label + chevron; Support uses ↗; "Sign out" alone in a card with a red icon tile. (04·6, 05·4)
- Create profile: logo 28, title 28/800 left, 15 grey serif line, avatar placeholder 80 with orange camera badge, 11 caps grey label "FULL NAME", outlined field ≈44 with 8 corners, full-width orange "Continue" ≈38. (05·2)
- Inbox: title 22/800 + avatar; rows: publication eyebrow 11 caps grey + date + orange bookmark right, title 17/800 two lines, 13 grey sub, thumbnail 84 square on a 20 gutter, outlined status chips 11 caps (READ, PREVIEW); a floating segmented pill "All · Paid · Saved · Media" sits above the tab bar. (08·2)
- Post editor: formatting bar above the keyboard (Aa, link, B, I, S, code) swaps to a block bar (+, link, list, quote, undo, hide keyboard) when the cursor is on an empty line; heading applied inline at ≈28. (06·4, 06·6)
- New note composer: × left, "New note" 15/600 centred, orange "Post" pill ≈32 at 40 % until text; media icons row; a type switcher "Note · Post · Video · Live" on black with the selected in a grey pill. (07·6)
- Chat: blue right bubbles and grey left bubbles with avatar 24, 16 corners; long-press sheet with quoted message, 5 reaction discs 36 (selected outlined blue), Copy text, Reply, Report red. Empty chat: info glyph 20, "No messages yet" 15/600, 13 grey, black "New message" pill ≈28. (08·4, 09·2, 09·5)

## Luminar (176) · dark photo editor, amber accent
- Editor bands on black: picture edge to edge at the top; a value capsule ≈28 tall over the picture's bottom edge ("CONTRAST −40", 11/700 tracked caps); a header row of five amber outline icons 24 (back, history, random, ⋯, share); a tool strip; a dark panel ~140 tall with 12 corners; a bottom module bar of five white glyphs 24 without labels (04·3, 03·1).
- Tool strip: an amber film-canister preset disc 40 at the left, then 6–7 grey tool glyphs 20 on a ~40 pitch; the selected tool sits on a 44 dark rounded square; tools carrying a value get a 4-pt amber dot under them; AI tools carry a tiny "AI" superscript (03·3, 04·3, 05·3).
- Every tool has its own control instead of a slider: a sun-ray dial (Enhance), H/W/S/B discs around a tall exposure capsule outlined in amber, a sine-wave scrubber (contrast), two gradient bars with ring thumbs (colour), a dot-grid pad (saturation), an arc ruler (structure), nested rounded rects (vignette), S/M/L knobs with a bar meter (details) (03·1, 03·3, 04·3, 04·5, 05·1, 05·3, 06·1, 06·5).
- Presets: category names as 11 tracked caps text tabs ("CREATIVE", "PORTRAIT", "FAVORITES"), a rail of 3D film canisters, and an arc scale 0–100 above for intensity with the value in amber (02·3, 02·4, 09·1).
- Crop mode drops the tool bands: picture with white corner brackets, a "W 1543 · H 1029" chip 11 on a dark capsule, a rotation arc ruler below, a row of undo/redo + ⋯ disc + aspect pill, then × (grey) and ✓ (amber) pills at the bottom corners; ⋯ opens a floating dark menu of five rows, label left + icon right (07·5, 07·6, 08·2, 08·3).
- Feedback reuses the value capsule: "RANDOM PRESET APPLIED", "SAVED TO PRESETS"; an in-panel empty state reads "NO SKY FOUND. TRY ANOTHER PHOTO" in 11 tracked caps under a small glyph (03·6, 09·1, 09·3).
- Library root: segmented "Photos / Collections" pill ≈28 centred, dark search field ≈36 with a mic, 3-column grid with 1-pt gaps, a floating dark capsule with folder-plus and camera icons, sort icon amber bottom-left (02·1).
- Sign-in: 48 logo tile, title ≈28/700 centred on three lines, four white pills 44 tall with 16-pt gaps (Email, Apple, Google, Microsoft), opt-in radio with 11 grey text, terms 11 grey links (01·2).
- Paywall: photo top, title ≈26/700 white, three check lines 13, three plan cards side by side (Lifetime / 12 Months / 1 Month) with a "20% OFF" chip and a struck-through price, selected with a 2-pt blue outline; white Continue pill 57 tall; 9-pt caps legal; three text links (01·3, 10·5).

## Apple Podcasts (186) · light media library, purple accent
- Library root: title ≈34/700 with a grey ⋯ disc 28 and avatar 32 right; menu rows 48 pt (purple outline icon 24 + label 17/400 + grey chevron), hairlines inset from the label; ≈46 pt of air, then "Recently Updated" 20/700, 12 to a 2-column grid of 161-pt squares with 12 gaps in 20 gutters, title 13 + 12 grey under (08·2).
- Mini player is a floating white card 56 tall inset 12 with ≈14 radius, art 40, title 15/500 + date 13 grey, play 24 and a "30" skip glyph; it sits 7 pt above the 4-item tab bar (icon + 10 label, purple active) (06·1, 08·2).
- Episode rows (Up Next, Saved): art 90 square 8 radius, eyebrow 11/600 caps grey ("6D AGO · E"), title 15/600 two lines, a purple-tinted pill 24 "▶ 19m" with an inline progress bar, trailing download/⋯ 20 grey; 104-pt pitch (06·1, 02·2).
- Context menu over a blurred screen: card ≈210 wide, 12 rows ≈36 (label 15 left, icon 20 right), groups split by 8-pt grey gaps, "Remove Download" red when present (03·2, 06·3, 03·4).
- Now Playing: the whole ground is a colour sampled from the art; art ≈338 wide while playing and ≈240 when paused; row art 40 + date 11 caps + title 17/600 + show 15 dim + ⋯ disc; progress 4 with 11 times; control row speed "1×" · ⟲15 · play 44 · ⟳30 · sleep; volume slider; bottom row transcript · AirPlay · queue with an 11 route label (04·6, 05·1, 05·3).
- First-run coach marks: white tooltip 14 radius with title 15/600 + 13 grey, arrow pointing at the unlabeled control it explains (04·3, 04·4).
- Player menus: speed and sleep timer as dark translucent lists, rows 36, check on the current value, anchored to the button (04·6, 05·2).
- Transcript: serif ≈17 white on the art colour, current passage bright and the rest 60 %; in-transcript search shows the query, match count and ⌃⌄ in a bottom bar (05·4, 05·5).
- Show page: art full bleed with a tint, "+ Follow" pill and ⋯ disc over it; one white pill ≈48×263 "▶ Latest Episode"; description 15 with a trailing "MORE"; meta 13 grey; then a white section "Episodes ›" 20/700 (07·4, 02·5).
- Ratings: score 5.0 ≈48/700 + "out of 5" 13 grey beside a 5-bar histogram, "Tap to Rate" 13 grey over 5 outline stars 28 purple, review cards grey 12 radius (07·5, 08·1).
- Search: grey field + Cancel, a scope segment "Apple Podcasts · Library" under it; results art 56 + caps eyebrow 11 + 15/500 two lines + purple play disc 28; browse is a 2-column grid of colour tiles 163×≈89 with 11 gaps, label 15/700 white bottom-left; "No Results" 20/700 + "Try a new search." 15 grey centred (02·3, 10·5, 10·6).
- Swipe on a row reveals two full-height blocks ≈60 wide, orange "Unsave" and red "Remove Download", icon + 13 label (10·3).

## Dropset (203) · black monochrome gym tracker
- Every screen is a stacked sheet on #030305 with a 36×4 grabber and a peek of the sheet behind; header row = ↓ (dismiss) or ← (back) 24 left, then dark 40 discs #2a2a2e and one pill action right (white "Start"/"Log"/"Get routine" or outlined "Finish") (03·5, 06·5, 08·6).
- Titles 28/700 left with a 12 grey line under at 16 gutter; body copy 12–13 (01·2, 06·2).
- Add sheet: 4 rows at an 82 pitch — disc 46 #2e2d32 + 17/600 title + 12 grey sub — each with a trailing grey 36 pill verb ("Create", "Get", "Add") 13/600 (01·2).
- Session list: running time as the title 28/700 ("18:36"), rows at an 82 pitch = status disc 40 (white with ✓ when done) + 17/600 + 12 grey "All sets completed" + ⋯ + ›; supersets are linked by a chain glyph between discs; "+ Add exercises" row; a "Type anything…" notes field (06·5, 09·5).
- Set logging: each set = square checkbox 36 + outlined pills "6 lbs" · "8 reps" 36 + ⋯; the set type replaces the checkbox with a white tile glyph (⚡ warmup, ↘ dropset) (05·1, 05·5); ⋯ opens a floating dark menu with groups split by thick gaps (05·3).
- Onboarding questions: 24/700 question, answers as dark 44 chips right-aligned like chat replies, a "0 of 4" outlined counter pill, and a white "→ Continue" pill 46 hugging its label bottom-left (02·1, 02·3, 01·4).
- Numeric input is a wheel of huge numerals ≈64/700 with the neighbours faded, between two hairlines (01·5, 02·2, 08·6); weight entry uses a − 6 + stepper over a keypad sheet (05·2).
- Interval timer flips the whole screen white for Work and black for Rest: label 28/700 + exercise 17, countdown ≈100/700 (cap 71), "Round 1 of 4" 20/600; bottom bar = 40 pause disc with a progress ring + total 28/700 + grey "Stop" pill 36 (04·4–04·6).
- Destructive: dark sheet floating 8 from the edges, title 22/700, 13 grey line, red pill 48 inset 23 ("Delete", "Remove 'Burn focus'"); a reset warning pairs grey Cancel over red (03·3, 06·4, 09·6).
- Library: A–Z index rail 9 grey on the right, section letter 20/700 right-aligned, rows square 36 + 15/600 + ›, bottom bar "No active filter" + grey "Select ⌄" pill; filter sheet is a chip cloud with a Body parts / Equipment segmented pill at its foot (07·1–07·3).
- Dashboard: widgets instead of lists — folder tiles 2-up with 16 radius, a full-width metric card with "0 lbs" ≈64/700, a "Next up is Full body" 12 hint above a 4-icon tab bar without labels (01·1, 03·2).
- Chart: line chart in a #1c1c1e card, 24 radius, two dropdown pills 36 above ("Weight ⌄", "All time ⌄"), y labels 9 right, three x labels (10·2).

## Train Fitness (211) · light workout logger, grey cards
- Ground is light grey with white 16-corner cards; black is the primary action colour, purple marks AI actions (Generate, Suggest, Personalize), tan marks Pro and create (Create Account, Earn Train Pro) (01·3, 03·3, 01·5).
- Account: large title 28/700 + gear; profile card avatar 64 + name 17/700 + handle 13 grey; three stats (label 11 grey, value 15/600); grey "View Profile" pill 32 + two square icon buttons 32; tan "Earn Train Pro for free" row; "Getting Started 0/6" checklist cards 2-up with × (01·1, 08·2).
- Workout hub: pink gradient top, a recovery gauge arc with "Quads" 20/600, "5%" 34/700 and "8 days to recovery" 13 red; black "Empty Workout" and purple "Generate" side by side, 168 wide each, 8 gap, ≈48 tall; "My Week" card of day discs 30 (done days filled black with an icon); streak and minutes ring row (01·3, 07·1).
- Feed card: avatar 28 + name 13/600 + activity glyph + time 11 grey; title 17/700; three stats split by hairlines (label 11 grey, value 15/600); muscle map in a grey 12-corner panel with muscle chips 24; heart + comment glyphs 22 (01·4, 05·6).
- Workout detail: "Add Caption" and "Add Photo" grey pills 32 with icons; stat line; "Workout Log" 20/700 + "Edit" 13 grey; each exercise a white card ≈64 (thumb 48 + 15/600 two lines + "4 Sets" 12 grey + chevron), 8 apart; supersets share one card under "⇄ Superset" 13/600 (06·1, 06·3).
- Live logger: header ⌄ · elapsed 17/600 · ⋯; rest timer 15/600 red + a 6-pt red bar full width; per exercise a set grid with columns Set · Rest/Effort ⌄ · Reps · Lb · ✓, grey 8-corner cells ≈38 tall, row pitch 52, done rows get a green-tinted check cell, the next set is a pale blue band; "+ Add Set" grey pill 36 + stats disc 36; a floating purple "Suggest" pill 44 + black + disc 44 (03·5, 03·6, 04·1).
- Exercise library sheet: Clear · title · Create; search + Cancel; filter chips 28 white; rows thumb 44 + 15/600 + 12 grey muscles, trailing radio 22 that fills black; selected rows turn grey; pinned pair tan "Add Superset (4)" + black "Add Exercises (4)" (04·3, 04·4).
- Search: underline tabs Exercises · People · Templates · Workouts; section letters A/B 13/600; rows thumb 44 + name + muscles grey, a trailing blue waveform disc 28 marks auto-detected exercises (06·5, 06·6).
- Toasts: white pill ≈32 at the top with a green check 16 + 13/600 ("Username Updated", "Link Copied", "Added to Favourites", "Feedback Submitted"), a red trash for "Workout Deleted" (08·3, 08·4, 08·6, 09·3).
- Settings: grouped white cards, caps group labels 11 grey, rows 44 with a 16 glyph + 15 label + chevron; inline Kg/Lb and Km/Mi segments 28; photo promo cards (Tips & Tricks, "Invite a friend" with a black Invite pill) sit between groups (07·2, 07·3, 07·4).
- Post-workout form: caps labels 11 grey, title field 17/600, caption and private note cards; "How was your workout today?" 15 + thumbs up/down discs 56; black "Done" 48 pinned (05·2, 05·4).

## SSENSE (212) · monochrome editorial fashion store
- Type-only chrome: header "BACK" / "SEARCH" left and "BAG 00" right as ≈9/400 uppercase, no icons; tab bar of four uppercase text labels ≈9 (HOME · SHOP · WISHLIST · PROFILE) with a 3-pt dot under the active one (01·2, 01·3).
- Gutter is 10–11 pt throughout: left edges 11 pt ×31 on the product page, fields at 10 pt ×76 on the address form (02·5, 05·6).
- Buttons are square-cornered black rectangles 45–46 tall with ≈11 uppercase white labels; the pair "ADD TO BAG" (black, ≈175 wide) + "ADD TO WISHLIST" (plain text) sits side by side; full-width only at onboarding, login, save address and place order (02·5, 03·6, 06·4).
- Onboarding: "01 / 03" 9 counter, title ≈22/400 uppercase on two lines, 13 body, two stacked full-width black buttons 46 with an 8-pt gap pinned at the bottom (01·1).
- Home: black hero block with "SHOP NEW ARRIVALS" ≈20/400; grey shipping band 12 + "DISMISS"; numbered sections ("007 NEW FROM" 11 uppercase + chevron) listing designers as ≈22/400 uppercase lines (01·2, 09·2).
- Product grid: three columns of cutouts on white, no tiles or borders, brand 8 + price 8 under; department tabs WOMENSWEAR / MENSWEAR (underlined) / EVERYTHING ELSE 9; a floating black split bar "SORT BY | FILTERS" ≈32 × 244 above the tab bar (01·3, 01·4).
- Filters: full screen in two columns, facets left in 9 uppercase with two-digit counts ("02 DESIGNERS", active underlined), values right in 13 on a ≈28 pitch, applied filters on top as "4SDESIGNS ×", an A–Z index rail 8, "VIEW RESULTS" black 147 × 46 centred at the bottom (01·5, 01·6, 02·1).
- Confirmations and errors are one full-width bar ≈40 under the header: black with 12 text and a trailing uppercase action ("Size M has been added to Bag. CHECKOUT", "Filters saved. DISMISS"), red for errors (02·6, 02·4, 06·3, 08·1).
- Bag and checkout: column labels ITEMS / DESCRIPTION / PRICE 9; rows with a cutout ≈60 × 100, brand + name + size 12, price right, "MOVE TO WISHLIST" / "REMOVE" 8; pinned "TOTAL ESTIMATE" 8 + "$270.00 USD" ≈17 left with a black "GO TO CHECKOUT" 178 × 45 right; checkout rows are a 9 label column (SHIPPING, DELIVERY, PAYMENT) + 13 values + chevron (05·3, 06·4, 07·1).
- Forms: 9 uppercase label above a ≈38 outlined box (1-pt line), field pitch ≈87, "Optional" 8 grey under; address autocomplete lists matches with the typed part in bold (05·6, 05·5).
- Settings / profile: section labels 13/500 uppercase, rows 51 pt with full-width hairlines, › for drill-in and ↗ for external links (03·2, 07·4).
- Loading is one word: "LOADING" / "SENDING" 8 uppercase with a 12-pt rule under it, centred; empty search is one uppercase line "NO PRODUCTS FOUND. TRY ADJUSTING YOUR SEARCH." (06·2, 08·2, 04·3).

## PayPal (213) · light fintech, black buttons
- Home: pale lavender-grey ground, white cards 16 radius, 16 gutter; header = menu, bell, person as 28 white discs with blue glyphs; balance card ≈80 tall: logo disc 28 + "0,00 US$" ≈24/800 + "Balance" 11 grey (01·2).
- "Send again" 15/700 + a rail of avatars 55 with 11 names, ending in a black 55 search disc; activity in one white card, rows ≈118 pitch: avatar 40 + name 13/700 + date 11 grey, then a status line 11 grey ("Request sent · Pending") with the amount 13/700 right (green for incoming); "See more" 13/700 blue centred (01·2, 01·3).
- Tab bar 3 items with 10 labels; on Home the middle Send/Request tab becomes a ≈44 filled blue disc with ⇅ (01·2); a later build shows 4 tabs with plain icons (03·2).
- Amount: recipient avatar ≈62 + name 15; "You send" 11 grey over "£200" ≈40/600 with "GBP" 13 right; hairline; "They get" $257.03 same size with an outlined blue currency pill 28 "USD ⌄"; rate 11 grey; message field pill 40 grey; Request · Send as two black pills 170×47, 12 apart, 12 gutter (05·2).
- Review sheet: back + "Review" 13/600 + ×; label/value rows 13, "Total 0.50 USD" 13/700, chevron rows for shipping and conversion, 11 grey notes; the black CTA shows a spinner while sending (05·5); a loading sheet is pale lavender skeleton bars (05·3).
- Success: plain white, headline ≈22/800 centred on two lines, 15 body centred, black full-width 44 "Done" + "New Request" 13/700 blue text under (06·1, 06·2).
- Sign-in: outline logo 40, title ≈26/800 centred, outlined 52 field, "Use phone number instead" 13/700 blue, black 44 "Next" + outlined 44 "Sign Up"; failure as a pink banner card with ⚠ + × at the top (03·3, 03·5).
- OTP: a sheet rises over the flow; 6 grey boxes ≈40×48, the active one outlined blue, system number pad (02·6).
- International: "Where are you sending?" 22/800 left, search field, 2×2 grid of country tiles (flag 20 + 13 name), then a flat country list; receiving options as radio cards 12 radius, the selected with a 2-pt black border and a blue "Best Xoom Rate" chip 9; fee note 11 grey; black 44 "Next" + "Show fees…" blue text (06·5, 06·6).
- Fundraiser page: cover image, avatar 48 overlapping, white card with organiser 11 grey, title 20/800, purple category chip 11, yellow "Ends in 3 days" chip 11, donor avatar stack + "17 people have donated" 11, green 4-pt progress, "£86 of £250" 13; segmented About/Updates with a black selected pill; bottom pair outlined "Share" + black "Donate" (07·2, 07·6).
- Activity no-results: illustration ≈100, ≈20/800 centred 3 lines, one blue 13/700 text action "Choose another filter"; active filters above as white removable chips 28 (label + ×) under a search pill 36 + filter glyph (10·1).
- Toasts: black 12-radius cards at the top with a check-circle 16 + 13 white, overlapping the header (02·3, 04·4, 09·2).

## komoot (234) · warm outdoor maps, olive accent
- Sign-in: logo + title ≈30/700 centred on 3 lines, 12 grey legal with orange links, four stacked full-width ≈44 provider buttons (Google outlined white, Apple black, Facebook blue, email olive) with an "or" divider (01·1); login fields are white ≈44 pills with 13/600 labels over them, the focused one outlined dark (01·2).
- Route planner: 32-tall grey search field with sport glyph left and × right, an olive hint bar ≈36 "Tap the map to add a point" 13 white, then the map with 40 white discs (locate, layers) and one floating olive "Plan new route" pill 175 × 45 centred above the tab bar (01·4, 01·5).
- Planned route: 4 stats in a row (label 11 grey + value 15/600 with small unit) and a strict pair Save (olive filled) · Navigate (beige tonal) each ≈173 wide with a 10 gap (02·2, 02·3).
- Route detail sheet over the map: difficulty chip 11 on dark olive, ★ 5.0 and participants, title ≈22/700 on up to 3 lines, Loop · Hiking meta, 2 × 2 stats (label 12 + value 17/600), underline tabs (Map · Tips & Info · Waypoints · Elevation), pinned Save 250 × 42 + two 42 square tonal buttons (02·4, 03·4).
- Saved routes: back disc 31 · title 17 centred · search + "Import" olive text; filter row "All sports" olive + "3 routes" grey; rows ≈160 tall: 65 square map thumb with a sport badge disc, title 15/600 on 2 lines, stats line with 13 icons, difficulty chip, date/place 11 grey, privacy icons trailing (04·1, 04·6).
- Map sheet "Select a map" 22/700 + × disc: base maps in a dark card (thumb 28 + label + radio dot), layers in a white card, help rows grey below; the satellite choice asks consent in a small card with a preview and Cancel · Agree (02·6, 03·1, 03·2).
- Privacy selector: three radio cards (title 15/600 + 13 grey), the chosen card with a 2-pt olive outline and a light tint (05·3).
- Navigation: dark olive top band with a turn arrow and "Follow the map" ≈22/700 white, a stats band (traveled · next waypoint 20/700), floating olive "Share Live Tracking link" pill and a "Controls" pill; Controls opens a sheet of rows (icon 20 + 13 label + chevron, toggle or value) with a full-width olive Pause ≈40 (07·3, 07·6).

## ElevenLabs (265) · light AI voice studio, black pills
- Home: title ≈28/700 left + avatar disc 32 right; full-width black "+ Create new" pill 47 at 18-pt gutters; a scrolling row of grey source chips ≈40 (icon + 13/500: Image, Video, Text to speech); promo banner ~114 tall with gradient and dots; "Recent projects" 13 grey; 2-up project tiles ≈161×163 with play glyph, ⋯, title 13/600 white and an 11 date line over blurred colour; a floating glass tab capsule ≈52 (Home · Creator) with a separate "+" disc 48 at the right (06·1).
- Text-to-speech editor: × disc + title 15/600 centred (later the script's first words, truncated) + "+" and ⋯; each paragraph starts with a speaker chip (gradient orb 16 + name 13 grey pill) and an emotion tag in pink 15 inline ("thoughtful", "annoyed"); bottom bar: "Using 46 credits" 11 grey, grey "⊕ Add a speaker" pill 47, settings disc ≈40, black "Generate" pill 47 (01·2, 01·4, 10·4).
- Result: a black card with 16 corners and a grabber docks above the action bar: 11 timecodes, white scrubber, title 13/600 + speaker, grey share disc 36 and white play/pause disc 40; it collapses to a black capsule with expand and pause (01·4, 07·1, 09·3); "Regenerate" replaces "Generate" with "5 free regenerations" 11 grey above.
- Voice picker: sort disc + filter pills ≈36 (Language, Category, Gender), selected black with a flag; rows on a 61-pt pitch: gradient orb 40, name 15/500 truncated + 12 grey meta (count · language +N · use), trailing ⊕ 20 black; the playing row's orb becomes a pause disc; a black "Select voice" pill 47 and a search field + × disc dock above the keyboard (01·6, 02·5, 07·3).
- Settings sheet: 24-radius sheet, × disc 36 top-left, title ≈22/700 left; model as two selectable cards ≈130×145 (version chip, name 15/600, 13 grey line, "High quality" chip), selected with a 2-pt black outline + check disc; sliders as full-width 36 bars with black fill and end labels 11 inside ("Slow" / "Fast"); ⓘ opens a nested sheet (title 20/700 + bullets); "Reset values" grey + "Save" black pills paired at the bottom (01·1, 03·4, 09·1).
- Image settings: segmented Image / Video; rows label 13 + value 13 + ⌃⌄ glyph on a ~43 pitch; each picker is a floating white card of plain options (1:1 … 21:9) rather than a wheel; a black ✓ disc top-right confirms (03·1, 05·4, 05·5).
- Model list: filter chips (Realistic, Cheap, Editing, Fast) with multi-select in black; rows with a 36 logo tile, name 15/500, 2-line 12 grey description, credit cost "◎ 2010" 11 grey right; selected row outlined 2 pt black with 12 corners; floating search capsule at the bottom (08·6, 09·5).
- Share card: black stage, 4:5 quote card with "AI voice / Rob" eyebrow 11, quote ≈22/700 whose spoken words are white and the rest dimmed, wordmark at the foot; three swatch discs 28 with the selected one labelled under; a white "Share" / "Generate video" pill 36 hugging its label (02·2, 05·3, 07·5).
- Empty create page: two grey placeholder tiles, "Nothing here yet" 13 grey, "Start creating now" ≈20/600, 15 body centred, then the composer card docked (reference chips "@Image 1 ×", prompt, a tool row of glyphs with chevrons, black ↑ send disc 32) (06·3, 09·4); generation progress shows the same tiles with "Almost done…" or "38%" 13 grey (03·6, 08·5).

## Apple Books (280) · light editorial reader, serif titles
- Tab bar is a floating glass capsule ≈58 tall with 4 labelled items (icon 24 + label ≈10) and a grey pill behind the active one; search is a separate ≈58 disc to its right; a glass mini-player capsule ≈46 floats above it (01·3, 03·4, 04·4).
- Titles are in a serif (New York): screen titles ≈28/700 ("Home", "My Samples", "Top Charts"), section titles ≈20/700 serif with ›, book titles 15/700 serif; meta and UI stay in the sans at 12–13 grey (01·3, 05·1, 03·4).
- Home sections: serif title + one 13 grey subtitle ("It costs nothing to bag your next great read."), then covers at their own ratio ≈150 tall with shadows, 2 + peek; sections sit on alternating white and light-grey bands instead of dividers (01·3).
- Book detail: a full-screen card coloured from the cover, × disc 32 left, ✓ + ⋯ in one pill right; cover ≈196 wide centred; title 20/700 serif, author 15 ›, meta 12; a tinted "Book ⓘ" card with Sample (tinted) · Get (white) pills ≈40, then "View the Audiobook ›" card with a price pill (01·4, 02·1).
- Confirmation HUD: frosted square card ≈180 centred, glyph ≈44, "Added" 20/700 serif, 13 line, auto-dismissing ("GOT IT" text in the first-run variant) (01·5, 04·3, 06·3).
- Library: 2-column covers ≈158 wide with 10 gaps in 24 gutters, bottom-aligned at their natural ratio; under each a status chip 10/700 (NEW blue, SAMPLE red) or remaining time 12 grey + ⋯; the list mode uses cover 40 + 13/600 + 12 grey; Grid/List and Sort sit in one floating glass menu (04·4, 04·5, 04·6).
- Reader: 38-pt side margins, serif ≈13 justified and hyphenated; header "26 pages left in chapter" 12 grey + × disc 32; footer "2 of 87" 12 grey + a menu disc 36 bottom-right that opens into a stack of glass pills 40 (Contents · 1 % with a progress fill, Search Book, Themes & Settings) over a row of 4 icon discs (07·1, 07·4, 09·1).
- Themes & Settings sheet: title 20/700 + × disc, a text-size segment (A · A) + two icon toggles, a brightness slider, 3×2 theme tiles ≈98×93 with 10 gaps ("Aa" 22 + 12 name, selected with a 2-pt ink border), "Customize" grey pill full width (09·2, 09·4).
- Selecting text pops a capsule of 5 colour dots 16 + underline; long-press on a highlight gives a glass menu (Highlight, Edit Note, Remove…, Search, Writing Tools) (08·2, 08·5).
- Audiobook player: brown ground sampled from the cover, art ≈265, title 17/600 + author 15 dim + price pill + ⋯, progress with a "Sample" label, 3 controls ⟲15 · pause 44 · ⟳15, bottom row speed "1×" · sleep · AirPlay · list (10·4, 10·6).
- Review composer: header × disc + cover 40 + "Write a review…" 15/600 + a dark ✓ disc; 5 stars 32 black; a grey card with title 15/600 and body 15; "Remove Rating" as a red row with a trash icon (06·5, 06·6).
- Goal reached: blue check disc ≈124, "Daily Goal Achieved" 17/700 serif + "47 minutes" 17 blue serif, 13 body, black pill 44 "SHARE" 13/700 caps + "ADJUST GOAL" text (03·1).

## Wispr Flow (304) · light voice keyboard, serif display
- Intro carousel: full-bleed cinematic photo, wordmark 17/700 white, serif title ≈30/400 centred on two lines, serif caption 22 with one italic word, 3 dots, cream pill ≈49 tall with 15/600 ink label, ≈35 gutter (01·1–3).
- Sign-in: wordmark, serif headline ≈24 with an orange italic phrase ("4x faster"), stacked auth buttons 52 tall and 13 apart at an 18 gutter (1-pt ink outline; Apple filled dark), legal 11 grey centred (01·4, 10·3).
- Onboarding steps: back chevron + 3–5 segment progress dashes + "Skip" 13 grey; serif title ≈26 centred with an italic accent word; a grey mock card (Gmail, Notes) for the demo; dark full-width button ≈50 "Next" (02·3, 04·5, 05·2).
- Custom keyboard: top strip with ☰, undo, a white style chip "very casual" 32 and an ink mic disc 36; listening replaces the keys with × disc, "Listening · iPhone Microphone" 13 grey, a dotted waveform and an ink ✓ disc (02·2, 03·2, 04·6).
- Tab bar is a floating white capsule ≈58 tall, 336 wide, inset 19, with 5 items (icon 18 + label 11); the selected item sits in a grey inner capsule with a violet icon; an ink FAB ≈60 floats above it at the right (08·3, 06·3).
- Feature header card: cream card 16 radius with × top-right, serif title ≈24 on two lines, 13 grey body with bold keywords, dark full-width button ≈49; below, "Your words (3)" 13 grey and a white card of 52-pt rows ("btw → by the way" 15) with hairlines (06·5, 07·1).
- Toasts: dark pill ≈38 tall centred at the top of the list, green check disc 16 + 13/500 white ("Replacement added to dictionary", "Note deleted"), or a red minus for "Flow is off" (06·6, 08·6, 09·4).
- Scratchpad: note cards white, ≈18 radius, 17 apart at a 16 gutter on a #F2F1F5 ground (name 17/500, body 15 in 3 lines, 12 grey time, "✦ AI" lavender chip 24); swipe left reveals three 44 discs (red delete, violet share, green copy) (08·3, 08·5).
- Account: stacked white cards ≈18 apart; profile card with outline avatar glyph 48, name 15/600, 12 grey email · plan, stat line 12 ("255 words · 115 WPM"), lavender pill 36 "Manage plan"; group cards with a 13/600 icon header and full-width grey buttons 42 tall, 15 apart (10·4).
