# Study notes — one block per app (iOS). By Achref Arabi.

What each app does, measured from its screens: observations, not targets. Where a
number here differs from `SKILL.md` (many apps use 48–56-pt buttons, for example),
the rules and measurements in `SKILL.md` win, and the project's own tokens win over both.

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

## Headspace (004) · warm illustrated wellness
- White canvas, section title 22/700 ("Start your day"), timeline rail on the left (dot + dashed line) linking cards.
- Cards: white with 1pt border and 12pt radius, content left (title 17/700, two meta lines with small icons 12), illustration right in a fixed 120×90 box. Lock glyph inline in the title for gated content.
- Dark theme variant keeps identical geometry; only surfaces change.
- Paywall: big illustration, title 24/700, 4 check lines, two plan cards (selected filled orange with a "Best value" chip), full-width blue pill CTA 56 at the bottom.
- Empty search: small mascot illustration, "No results for 'x'" 15/600, one grey line, nothing else.
- Explore: full-width coloured banner tiles 64pt tall with a title 15/700 and an illustration bleed on the right; 8pt gaps.
- Tab bar 3 items only.

## Duolingo (005) · playful learning
- One lesson screen = progress bar (8pt, rounded, green) + close × on the left + hearts count on the right; then an eyebrow chip ("NEW WORD" 12/700 purple with icon), then the question 20/700, then the exercise. Nothing else.
- Buttons: full-width 48–52pt, 16pt radius, all-caps 15/700 label with letter-spacing, a 3–4pt darker bottom edge for depth; disabled state is grey with grey text. Word tokens are 40pt chips with a 2pt border and the same bottom edge.
- Selection cards (pick an image): 2×2 grid, 16pt radius, 2pt border, illustration on top, label 15 below; selected turns blue.
- Streak/celebration screens: one big illustration centred, headline in colour 22/700, one card of context, CTA at the bottom.
- List (courses): white card with dividers, flag 32 + label 16/700, 56pt rows.
- Home path: nodes 64pt discs on a vertical path, locked nodes grey; top bar shows currency chips.

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

## Apple Music (026) · iOS native reference
- Playlist: numbered rows (number 15 grey, title 15/400 caps for this album, ⋯ trailing), 44pt rows with hairline insets; the playing row is tinted with the accent surface and the number becomes a star. Header: back chevron red, title 17/600 centred, + and ⋯ as small grey discs.
- Browse: section titles 20/700 with a chevron ("Hip-Hop ›") and 12pt to a 2-up rail of 16:9 videos with 8pt corners, title 15 + artist 13 grey under.
- Mini player docked above the 5-item tab bar: artwork 40, title 15/600, one-line eyebrow "2 LISTENING" 11 caps grey, play/forward icons. Tab bar uses red for active.
- Empty search: "No Results" 17 grey centred, nothing else. Error: one grey line and an outlined "Try Again".
- Feature page: hero illustration on a colour, then title 34/700 and running body 17/400 with 24pt line height.

## Halide (027) · pro camera, dark
- Viewfinder fills the screen; overlays are 1pt yellow guides and a small histogram. Controls live in two black bands: a thin band of 3 tiny icons, then the main band (rotate, mode disc, +; exposure ruler with a 0.5 readout 13/700; thumbnail 56, shutter 72 white ring, "2×" lens disc).
- Settings: grouped forms on black; radio cards (checked = green disc), option rows 44pt with a 1pt divider, section labels 13 grey, explanatory 13 grey text between groups. Tech readout: icon 20 + label grey + value right-aligned 15/600.
- Support list: icon 24 + title 17/600, 13 grey description under, 1pt dividers.
- Photo review: black stage, format chips (HEIC · DNG) as 1pt outlined tags 11 mono-ish, meta right (date, place), a row of three readouts (1/833 · ISO 25 · 26mm) with hairline separators, then three icons (heart, share, trash).
- Yellow is the only accent: selected RAW+ chip, exposure marker, subscribe button.

## ChatGPT (029) · quiet assistant
- Canvas white; header is just a menu glyph + title 17/600 + compose glyph. No dividers.
- Messages: user bubble grey #F2F2F2 with 18pt radius right-aligned, assistant text as plain body 16/400 on the canvas with 24pt line height; action icons row (copy, speak, up, down, share) at 20pt grey under each answer. Bold inline for labels ("When:").
- Composer docked at the bottom: "+" disc 40 grey, pill field 44 grey with placeholder, mic icon inside, black disc 36 for voice on the right.
- Voice mode: full white screen, one animated blue sphere, two 56pt discs at the bottom (mute, close).
- Drawer: search field, three entries with icons, then plain 16pt text history rows 40pt tall, account row pinned at the bottom.
- Cards inside answers: 1pt border, 12pt radius, title 15/600 + 13 grey + progress line + outlined "Details" pill.
- Search suggestions: title 16 + one 13 grey line with the match bold.

## YouTube (035) · dense but ordered
- Shorts: full-bleed video, a vertical stack of 5 actions on the right (icon 28 + count 11 white), creator row (avatar 32 + @handle 14/700 + red "Subscribe" 13/700 pill), caption 14, sound line; tab bar with a big outlined "+" as the centre item.
- Account: eyebrow chip ("Premium" 11 with logo), name 24/700, "Member since" 12 grey, accordion rows 48pt (icon 20 + label 15 + value right + chevron), expanded rows show a 13 grey explanation under.
- Comments sheet: header 17/700 with back and close; rows avatar 28, handle 12 grey + time, body 14, like/dislike row 12; composer at the bottom with the user's avatar.
- Permission explainer: dark overlay screen, two "why / control" rows with icons before the system prompt, one white pill "Continue".
- Feature/paywall: logo, one line 17, blue pill CTA, small print 12 grey centred; legal block 12 grey left-aligned.

## Instagram (041)
- Feed: stories rail (avatar 64 with gradient ring, label 11), post header (avatar 32 + name 14/700 + sub 12 grey + ⋯), media edge-to-edge, action row (heart, comment, send left; bookmark right) 24 icons, likes 14/700, caption 14 with the name bold, "View all N comments" 14 grey, composer row.
- Comments sheet: grabber, title 15/700 centred, hairline, rows avatar 32 + handle 13/600 + time grey, body 14, right-aligned heart 16 grey; an emoji quick row above the composer; composer = avatar + pill field + GIF chip.
- Follow list: avatar 44, handle 14/700 + name 13 grey + "Instagram recommended" 12, blue "Follow" 13/700 pill 32pt, × trailing.
- Crop: black stage, 3×3 grid overlay, a single outlined "Rotate" chip bottom-left; Cancel / Done text in the header.
- Meta account centre: icon 24 + label 15/600 rows 48pt, one blue full-width pill at the bottom.
- Success: soft gradient wash background, title 24/700, avatar 128 with a ring, outlined "Edit" chip, a toggle inside a white card with an explanation 13 grey under.

## Threads (042) · text-first feed
- Post: avatar 36 + handle 15/600 + verified, time 13 grey right, ⋯; body 15 with 20pt line height; media as 2-up with 8pt corners; action row of 4 outline icons 22 with 24pt gaps; "16 replies · 730 likes" 13 grey; replies indented under a hairline.
- Composer docked: avatar 24 + pill field "Reply to …" 40pt grey.
- Toast: black bar 48pt with check + "Posted" 14/600 and a trailing "View"; a spinner variant "Posting…".
- Share sheet: white rounded cards grouping rows (label 15 left, icon right), 2 groups separated by 8pt.
- Tab bar: 5 outline icons, no labels, active filled.

## Notion (064) · iOS grouped-form language
- Modal lists: title 17/600 centred, "Done" blue right; rows 44pt with a check trailing, grouped with hairlines.
- Export: settings rows (label + value grey right, toggle) then an action row in blue; the picker rises as a bottom sheet with 44pt rows.
- Page: cover image, emoji 44 + title 28/700, body 15 with 22 line height; a "Subscribed · Undo" black toast; bottom bar with 4 grey icons.
- Empty comments: grey outline icon 40, "No open comments yet" 13/600, one 13 grey line. Segmented "Open / Resolved" pill above.
- Share: tabs with 2pt underline, field, a grey info chip, "People with access" 12 grey label, rows avatar 28 + name 14 + email 12 grey + "Full access ⌄" right, blue full-width button.
- Paywall: logo, title 22/700, 3 benefit rows (icon 24 + title 15/600 + 15 grey), two plan cards with 2pt blue border on the selected one, blue CTA, three grey underlined links.

## Craft (071) · document tool
- Editor: title 22/700 in link colour, body 16 with 24pt line height; a floating toolbar band above the keyboard with 6 glyphs; "Done" as a black pill 36 top-right.
- Space home: title 22/700 with a coloured square avatar 24, text tabs with 2pt underline, a rail of outlined action chips 44pt (icon + label), a grey group card "Recently viewed / Daily notes / Hide" with an empty-state dashed placeholder inside, then 2-up promo cards.
- Sheets: white card with a title 17/700, inputs 44pt grey, explanatory 13 grey, blue full-width button. Role picker sheet: title 15/600 + 13 grey description per option, check trailing, destructive red row last.
- Promo dialog: centred white card 24pt radius over a busy image, title 22/700, body 15 grey, blue button + "Not Now" text.

## Figma (072) · minimal tool
- Empty Activity: title 34/700 top-left, then centred "No activity yet" 15/600 + 13 grey. Nothing else; tab bar 4 items with labels.
- Settings: avatar 40 + name/email, section labels 15/600, rows 44 with chevrons, "Log out" plain, floating red record button stack for bug reporting.
- Search: title 34/700, grey field 40, section "Drafts ›" 17/700, 2-up file thumbnails 8pt radius with name 14 + "Drafts" 12 grey.
- Bug report: grey grouped form (label 13 + value 15), attachments as 56pt thumbnails with × badges, bottom sheet of three icon rows.

## Revolut (074) · fintech, confident white
- Titles 28/700 left with 15 grey one-liner under; forms of grey pill fields 56pt with counter "0/50" 11 grey right and "Optional" 11 grey; sticky blue-violet pill CTA 56 at the bottom; secondary as pale tinted pill.
- Plan picker: tabs as text chips (selected white pill with shadow), hero card 16:9 with 16pt radius (title 28/700 white, price 15, tagline 13), "Top features" list in a white card: icon 24 + title 15/600 + 13 grey, 16pt gaps; black pill CTA with price.
- ID capture: full black, document frame with 12pt corners, state pill "Hold still" with spinner, label 20/600 white; result: photo, one line 15, blue "Submit photo" + outlined "Retake".
- Colour swatches: 40pt discs, the selected with a 2pt ring and a 4pt gap.
- Success: white rounded sheet rising with a big check and "Done!" 22/700.

## Opal (076) · dark utility with a gradient CTA
- Black canvas, cards #1C1C1E 14pt radius; row content: icon 24 + label 15 + value grey right + chevron; small info line 12 in violet with an ⓘ.
- The one CTA is a lavender-to-violet gradient pill 56; secondary rows are #2C2C2E pills.
- Idea rail: 3 equal square tiles 96pt (icon + 12 label) then "Work Time · Weekdays" rows with a violet "+ Add" chip.
- Day-of-week picker: 7 circular 36pt toggles, active white.
- Bottom sheets: title 20/700, radio cards with check discs, a nested "Try Opal Pro" card with a white pill.
- Support chat: black, assistant bubble #2C2C2E left, suggestion chips as dark pills above the composer.

## VSCO (107) · photographic, black on white
- Everything is type on white with photos: no borders, no cards. Section titles 17/600, tabs as text with 2pt underline, follow buttons as black 32pt rectangles (4pt radius) with 13/600 white.
- People suggestions: overlapping 3-photo collage 4:3 + avatar 88 over it, handle 13/600 + name 12 grey, Follow right.
- Profile grids 2 columns with 8pt gaps, images keep their ratio; handle 12 under.
- Report list: 15 rows 52pt with hairlines and chevrons only where there is a sub-menu.
- Confirmation sheets: title 20/700 two lines, 13 grey body, black pill "Dismiss"/"Report", outlined "Cancel".
- Toasts: full-width electric-blue bar 48pt with white 14 text and a check.
- Tab bar 5 icons, no labels.

## TikTok (116)
- Feed: video full-bleed; top text tabs "Following · For You" 15/600 white with the active underlined; right rail avatar 48 with a red + badge, then heart/comment/share 32 with counts 12; bottom-left handle 15/700, caption 14, "Add song" chip; tab bar 5 with a white/coloured "+" pill in the centre.
- Profile: avatar 96 centred, @handle 15/600 + verified, three stats (number 17/700 over label 12 grey), action row of grey pills (Send a 👋 · person icon · ▾), bio 13 centred, tab icons row with underline.
- Share sheet: title 13/600 centred, avatars row (name 11 under), app icons row (48 discs with brand colours, 11 labels), grey utility discs row (Report, Block…).
- QR card: white card 20pt radius on a brand gradient, two grey glass buttons under.
- Empty search: outline icon 64, "No results found" 15/600, 13 grey line.
- Suggestions list: avatar 48, name 15/600, handle 13 grey, meta 12 grey, pink "Follow" 13/600 pill 36×80.

## Claude (119) · warm editorial
- Cream #F0EEE6 canvas, serif display (title 30/400 two lines centred), sans body; dark variant #2B2A27 with the same layout.
- Form: pill field 52 grey with a flag, a toggle row inside a grey card ("I am at least 18") 13/600, terracotta button 52 with 15/600, small print 12 grey centred, underlined link. Validation: 12 red under the field, and the button stays.
- Settings: white grouped rows on cream, a dropdown menu card with 13 grey version line, rows with ↗ external icons, red "Log out" with icon.
- Chat: user prompt as a dark pill bubble, assistant as serif 17 with 26pt line height; images as 2-up 96pt thumbnails with the sender name 13/600 above; composer card with three small icons and placeholder "Reply to Claude 3.5 Sonnet".

## Uber (124) · black-and-white utility
- Rows: leading grey disc 40 with a star, title 15/600 + 13 grey, hairline; a blue link row ("Add Saved Place") with a 12 grey explanation and chevron.
- Ride sheet over the map: title 17/700 centred, rows with vehicle image 64, name 15/600 + ▲ count, price 15/600 right, "Pickup at" 13, tagline 13 grey; section labels 17/700 ("Popular", "Economy"); the selected ride gets a 2pt black border card; "Add Payment Method" row; black pill 56 with two lines (label 17/600 + 12 sub).
- Map header chip: white pill with a people icon + address + chevron; back button as a white disc 48.
- Forms on black: label 12 grey, value 15, × clear, black toast pill.

## Apple TV (130) · dark cinematic
- Hero poster 2:3 edge-to-edge under a translucent header; section titles 20/700 with › and 12pt to the rail.
- Episode cards 16:9 with 12pt radius, overlay text block bottom-left (EPISODE 1 eyebrow 11, title 15/600, description 12 grey 3 lines, ▶ 56m 12), ⋯ trailing.
- Rails: 3.5 posters visible, title 13 + type 12 grey under.
- Tab bar: glass capsule (blur) with 4 items + a separate search disc; active item as a filled tint pill.
- Settings panel (subtitles): dark card with segmented labels rotated for landscape, radio rows; permission screen: icon grid, title 20/700, body 17 grey, blue pill + outlined "Not Now".

## Rewind (137) · light, purple accent
- Settings: grouped white cards 12pt radius on grey, toggle rows 48 with a 13 grey explanation under the card, link rows in purple with ↗, version line 12 grey centred.
- Segmented "Search / Ask Rewind" as a grey pill with white selected segment; chat bubbles in purple gradient; composer grey field with a purple send disc.
- Timeline scrubber at the bottom with app-colour bands.

## Adobe Photoshop (172) · tool app in light mode
- Canvas grey #E5E5E5; image with a thin selection frame and 6pt handles; a floating cluster of 3 white discs (44) bottom-right for contextual tools; the mode bar below: selected tool as a black pill (icon + label 13/600), others as icon + label; then the action row: × left, mode name centred 15, green/black check disc right.
- Layers sheet: white card rising to half height, title 17/700 + × disc, rows thumbnail 40 + name 13 + lock/eye icons; selected row lifted as a white card with a shadow. Three labelled icon actions 11 at the foot.
- Contextual menu: vertical stack of white pills 40 with icon + label 15 attached to a ⋮ disc; destructive item in red; disabled items in grey.
- Text options: a row of value tiles (label 11 grey under a 13 value: "Myriad Pro / Regular / 176 pt / colour swatch"), then the name and the check.
- Forms: label 11 grey uppercase-ish over value 15, hairline under each, blue "Add" text top-right.
- Empty comments: grey outline glyph 64 + "Be the first…" 13 grey.
- Toast: black pill with check "Layer clipped" 14/600 anchored to the affected object.

## BeReal (174) · black social
- Black canvas; header wordmark 20/700 centred with a → on the right; search field as a dark pill 44.
- Contact rows: avatar 48 (rounded square), name 15/600, handle as a small white chip 11, × trailing grey; "INVITE" as an outlined pill 11/700. Section eyebrows 11/700 grey.
- Empty friends: dark card with title 15/600 + 13 grey.
- Post: header (avatar 32, name 15/600, place · time 12 grey, ⋯), dual camera with a picture-in-picture 96×128 at the top-right with a white border, reaction avatars overlapping bottom-left, comment field.
- Profile: avatar 96, name 30/700 centred, bio 13, link row, section titles 20/700 ("Latest BeReal"), 2-up cards 4:5.
- Segmented "Suggestions · Connections · Requests" as a black pill bar with grey selected segment.

## Riverside (187) · dark recording studio
- Header: red "Record" pill 32 left, studio name 15/600 centred, grey "Leave" pill right; recording state turns the pill into a stop square with a red dot timer "00:13".
- Stage: video tile 4:5 with a 2pt violet border when active, name label 12 bottom-left; teleprompter text 20/600 white over the video with a fade.
- Bottom tool row: 5 discs 44 (camera, mic, script, chat, ⋯), the off state tinted red.
- Settings sheet: title 20/700, rows icon + label 15 + slider (violet) or toggle; a violet tooltip bubble with a pointer.
- Invite sheet: 3 role cards (title 15/600 + 13 grey, share and link icons right), selected card tinted violet.
- Alerts: iOS-style centred dark card with red destructive rows.
- Empty studio: one violet pill "+ Create" centred low on the screen.
- Feedback: chip cloud of reactions with emoji, text area, disabled grey pill.

## Denim (193) · the compact editor reference
- Cover editor: square canvas 340pt with 24pt corners centred on a dark tint of the artwork; header = undo/redo left, "Customize" 15/600 centred, eye + text tools right; tool panel rises as a dark sheet: title 15/600 + × disc, a 4×2 grid of type samples (selected gets a 2pt blue border), a slider, a row of "Uppercase ⌃" + colour discs, a "Font Size − +" stepper row.
- Colour picks: 5 discs 40 with a 2pt ring on the selected one; a hue slider variant with a white knob.
- Discard: grey iOS action sheet with red "Discard Changes" and a white "Cancel".
- Library: "My Covers" 28/700 top-left with a gear disc, blue + disc and ⋯; item = square art 96 with 16pt radius, name 15/600 + "1 Cover" 12 grey. Two-item tab bar.
- Playlist picker: floating white card with rows thumbnail 28 + name 15 and a search disc.
- "Create New Cover" sheet: title 15/600 centred + × disc; discs 72 (Photos blue, Unsplash black) with 13 labels; sections 20/700; rails of 160pt tiles, 20pt corners, 12 label under, lock glyph for Pro.

## Linear (204) · precise light tool
- Workspace header: 12 grey breadcrumb, title 22/700 with a grey "Projects ⌃" switcher; project rows icon 20 + name 15 + health pill right; bottom bar = back arrow, search pill, compose.
- Issue composer: "Cancel" / team chip / "Create" header, title 20/700, body 15 grey, property chips row (status, priority, project, assignee) as grey pills 32 with icons, a formatting toolbar above the keyboard.
- Pickers: floating white card 16pt radius, title 15/600 + ×, search field, rows icon/avatar + name 15, check trailing, "+ Create new label" row.
- Lists: section eyebrow 13 grey + "+" right, rows 40 with status ring icon 16 + title 15 + avatar 24 right; tabs as outlined pills 32.

## Moises (209) · dark audio tool with one cyan accent
- Sheets: "Song Sections" list 15 rows 40, selected in cyan with a check; "Export" with format picker (selected as a grey pill) and a cyan full-width button 52.
- Player: chord strip at the top (cells 44, current cell white), two track sliders (mic, music) with cyan tracks and ⋯, chord grid 4 columns, section chips outlined cyan 36, thin progress with times 12, transport row (metronome value 11, prev, play disc 56 white, next, key), bottom row of 3 outline tools.
- Camera: full-bleed with a red stop disc 64 and a grey reset disc.

## (Not Boring) Camera (222) · physical-object UI on dark
- Every group is a dark card 20pt radius with 1pt inner highlight; rows title 15/600 + 13 grey explanation + amber toggle; section eyebrows 11/700 grey spaced.
- Style page: photo card 16:9 with page dots, hexagon style icon, title 28/700, author link, description 13 grey, an "Intensity 59" card with an amber slider.
- Colour picker: 5×3 grid of 36pt discs, selected with a white ring; three round action buttons (×, "Done +" pill with a violet disc, share).
- Stats card: label 15 left, value 15 right, hairlines; support card rows with grey icons.
- Header: back as a grey glass pill "‹ Settings", title 17/700 centred.

## Sora (226) · black video social
- Search: dark pill 44 with a leading glyph and a trailing people disc; empty state "No results" 17/600 + 13 grey centred in the free space; two grey pills below (Share, Copy link).
- Replies sheet: grabber, "55 replies" 20/700, rows avatar 32 + handle 13/600 + time 11 grey, text 14, "Reply" 12 grey, heart 20 right with count 11; nested replies indented 40; composer dark pill 48.
- Profile: avatar 96 centred, name 20/700, bio 13, three stats (17/700 over 11), outlined "Following" pill 44, two text tabs with icons, 3-column grid with 2pt gaps.
- Context menu: dark card 16pt radius with 3 rows (icon + label 15), destructive in red.
- Confirm: centred dark card, title 15/600, body 13, two pills side by side (grey Cancel, red Block).
- Send sheet: avatar grid 64 with names 11, selected with a check badge; "Send to Group" white pill 48.
- Tab bar 5 icons, the centre one a white pill "+".

## Netflix (264) · dark, red only for brand
- Screens are #141414 with one white title 17/600 centred and a back disc; helper text 13 grey.
- Search in forms: grey field 44; results as plain 15 rows 44 with hairlines; blocked list rows with an × block on the right.
- Radio/check lists: 24 circles, checked as blue discs; sort sheet: title 20/700 + × disc, rows 15/600 with a check leading.
- Avatar picker: section titles 17/700, 4-up rail of 80pt squares with 4pt corners.
- Home: chips row (Shows, Movies, Categories ⌄) as outlined pills 32; hero poster 2:3 with 8pt corners, genre line 12 with dots, two buttons (white "▶ Play", grey "✓ My List") 44; "Your Next Watch" 15/600 rail; tab bar 3 items with labels.
- Code entry: 4 boxes 56 with 1pt border, red error 12 under, "Resend code" underlined.
- Toasts: dark pill with a check icon at the bottom centre.

## WhatsApp (292) · iOS grouped, green accent
- Onboarding cards: gradient pastel background, illustration, title 20/700, body 15, page dots, blue full-width pill 48.
- Contact lists: index letters on the right edge, grouped white cards per letter, rows avatar 40 + name 15 (surname bold) + radio circle; "Invite" as green text right.
- Empty: grey pill card "No contacts" 15 centred.
- Info sheets: white card with a big icon, title 20/700, 3 benefit rows (icon + 15/600 + 13 grey), legal 12 grey with links, blue pill "OK".

## TIDAL (298) · dark, glass tab bar
- Album header: art 176 centred over a blurred tint, title 17/700, "by you ›" 13, meta 11 caps grey, two grey pills "▶ Play" / "⤨ Shuffle" 44 side by side, then a row of 3 icon actions with 11 labels.
- Onboarding pick: title 22/700, search pill, section 17/700, 3-column grid of circular artists 96 with 13 labels, grey "More Hip Hop" pill.
- Track list: number 13 grey, title 15 (playing in yellow), artist 13 grey, ⋯; mini player floats above a glass tab bar capsule with 5 icons.
- Share sheet: small info card with title 15/600 + 13, rows icon disc 32 + label 15, "Cancel" text.
- Profile: full-bleed portrait, name 34/700 white over the photo, handle 13, bio 15, link 13, two icon actions with labels.

## Meta AI (300) · light, blue accent
- Drawer: search pill, 6 rows icon + label 15/600, "Chats" 13 grey label, chat rows 15 with pin/⚙ icons, selected row tinted grey; bottom row avatar + two discs.
- Share sheet (dark): preview card 240 with 16pt corners, app discs 48 with 10 labels, legal 11 grey.
- Media picker: dark sheet "Library · See all", thumbnails 88 with check badges, "Recently uploaded" white pill, blue "Add 2 photos" pill.
- Empty search: outline icon 48 + "No results found" 15/600 + 13 grey.
- Product page: light grey card with the object, title 22/700 centred, body 13 grey, blue pill.

## Playground (243) · light editor
- Canvas grey #F1F0EC; artwork 3:2 centred with a 2pt blue selection frame; floating black tool strip 44 above the selection (colour, outline, corner, align, opacity, download, trash) with the active tool highlighted.
- Bottom: a white composer card 20pt radius ("Describe your edit", + disc, model chip "Nano Banana ⌄", send disc), then a grey pill with 3 icons, then a scrolling icon rail of 12 tools.
- Tool panel: white card rising with title 15/600 + "Close" text, one explanatory line 13, slider, undo/trash discs left, black pill "Erase" right.
- Colour picker: floating white card with a 2-row palette of 36pt discs + "Custom" tile; full picker with a gradient square, hue slider, hex field, blue "Done".
- Selection mode: "0 designs selected" 22/700 + Cancel; a promo card with gradient tint and a black "Upgrade now" pill.

## Flighty (049) · dense data, iOS grouped
- Sheets over a map: title 24/700 + × disc; search as three grey pill fields in one row; result rows: flag 20 + name 15/600 with the matched letters bold + codes 12 grey.
- Flight card: eyebrow 12 grey (flight · date), title 22/700, a grey info banner 13, 2-up info tiles (icon + value 17/600 + label 12, "COPY" chip), "Good to Know" card with icon rows.
- Form: label 13/600, grey field 44, chips row (Aisle/Middle/Window) outlined pills 36, radio list 44; segmented "Flight / Airport / Airline / Other" as 2×2 blue-filled/outlined buttons.
- Timeline: airport code 34/700 with the time 22/600 green right, status "On Time" 13 green, meta 12 grey; "Gate Departure in 8h 24m" 15/600 green.

## Luma (063) · events, black & white
- Ticket: white sheet with a dashed rounded frame around the QR, black pill "Add to Apple Wallet".
- Event page (dark tint from the poster): poster 4:3 16pt corners, chip "Featured in …", title 22/700, rows icon-tile 40 + 15/600 + 13 grey (date, place), "Registration" card.
- Calendar list: date column (NOV / 14 / TUE stacked 11-22-11) left, event title 17/600, meta rows with icons 13 grey, cover images 16:9 with 12pt corners, "External" chip.
- Payment: total 15 grey + 22/700 right, card row dark pill, black pill CTA.

## Fable (096) · warm literary
- Serif display for names/titles (28/500), sans everything else; quote card as a coloured 16pt block with a big quotation mark and 22 serif text.
- Profile: avatar 64 with a badge, chips "23% Match" / "Moderator" 11, outlined "Following" pill + icon disc, a goal card with a thin progress bar, text tabs with underline, list rows with 3D book stacks.
- Filter sheet: label 13 grey + "Clear all" blue, checkbox rows 40 with counts 12 grey, grey disabled "Apply" 52 + "Cancel" text.
- Empty search: small illustration, "No results" 15/600 + 13 grey.
- Thread: message bubbles left with an image 16:9 and reaction chips 24, a "NEW" pill divider, composer with 2 icons and a grey send disc.

## Atoms (099) · editorial habit app
- Cream canvas, serif for the sentence ("I will read 20 pages"), sans for UI; stat tiles 2-up: label 13 + value 40/700; a heat-map calendar of 12pt squares.
- Sheets: icon disc 44 at the top, title 22/700 centred, body 15 centred, field with a 13 label, black pill 52 + outlined "Cancel"; radio list of yellow-filled selected rows.
- Context menu: white card 12pt radius with 4 rows (label 15 + icon right), hairlines.
- Header actions: "Share ⬆" grey pill, ⋯ disc, × disc, avatar 32 left.
- Home: one big yellow disc (habit) with a tiny label, "PRESS AND HOLD" 11 caps grey under. Tab bar 3 items + badge.

## Superlist (108) · light productivity
- Titles 34/700 top-left; segmented filter chips (search disc + pills 36, selected grey); task rows checkbox 20 + title 15 + list name 12 grey with an icon, avatar 20 right; subtasks indented.
- Empty inbox: hand-drawn doodle placeholder rows; a coral floating "+" disc 48 bottom-right.
- Drawer: avatar, 4 nav rows icon + 15, "Recent ⌄" 13 grey, "Lists · Browse all + " groups with disclosure rows.
- Doc: cover image 4:3, share chip with stacked avatars, title 28/700, body 16 with 24 line height, formatting bar above the keyboard.

## Rise (138) · calm task manager, violet accent
- Title 17/600 left with a gear right; search "Filter tasks" grey field 40 + sort disc; section labels 13 grey on a tinted band; rows radio 18 + 15 text, "Due today" chip yellow 11 right; done rows with a violet check.
- Task sheet: Cancel / Task / Save header, title 20/600, property rows icon + grey placeholder 15, segmented "Description / Activity" pill; picker as a rising list with a check.
- Calendar day view: hour labels 11 grey left, coloured blocks with a 2pt left stripe, a red "now" line, violet "+" disc.

## ten ten (148) · black, giant type
- Profile: avatar 96, name 30/700, "PIN: …" mono chip, a big "+ add friends" dark pill 64 with memoji art; friend rows avatar 44 + name 15 + ⋯.
- Segmented "friend requests / sent requests" white-on-dark pill; rows with grey "re-send" pill and ×.
- Walkie-talkie: full-bleed portrait, "👋 Danny ⌄" 26/700, "hold to talk" white pill, a big avatar disc 96 with a green dot, "+" disc left, dashed "+ add friend" disc right.

## Raycast (257) · light AI notes
- Header capsule: back disc, title 15/600 + "Ray-1" 11 grey, "+" disc; body 15 with 22 line height, headings 15/700; user prompts as grey 16pt-radius cards; action row of 5 tiny icons 16 grey.
- Composer: grey pill "Ask Raycast AI…" + a separate grey disc for voice; formatting bar above the keyboard with ✦ as the first tool.
- Empty: small grey icon + 13 grey line centred; toast "Text copied" as a white pill with a green check at the top.
