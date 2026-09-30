# Screen recipes library — measured, by screen type

These recipes were measured on real apps (375-pt screens); the short versions are the "Screen recipes" in `SKILL.md`.
Where a recipe here disagrees with `SKILL.md`, the rules there win (for example, the main button is 44 even where an app ships 49–57).
Each recipe cites its sheet as `App NN·k`: open `refs/sheets/<id>-<App>-<NN>.jpg` and look at screen k (1–6, left to right, top to bottom).

## Home and browse roots

What they share: a 28–34/700 title with a 28–32 avatar or disc at the right, at most one search field (36–56) or one create pill under it, then content at once: 2-column tiles 160–165 wide with 8–16 gaps, or rows 48–64 with a 20–24 icon. The good ones put nothing else between the title and the first grid, rail or list; Target and Notion show that a plain list of 51–64-pt rows can be the whole root.

- **Notion — sidebar home**: workspace row (avatar 28 + name 15/600 ⇅ + email 12 grey · ⋯ disc 24) · "Jump back in" 13 grey · rail of 144 square cards, 16 gap · group label 13 grey ⌄ + "+" · tree rows 51 (chevron · icon 20 · 16/500 · ⋯ · +) · gutter 20 · 4-icon tab bar (Notion 06·2)
- **Apple Podcasts — library root**: title ≈34/700 + ⋯ disc 28 + avatar 32 · rows 48 (outline icon 24 accent · 17 label · chevron) · ≈46 air · section 20/700 · 12 · 2-column grid of 161 squares, 12 gap, 20 gutter · title 13 + 12 grey · floating mini player 56 · tab bar 4 (Apple Podcasts 08·2)
- **Apple Music — category search root**: title 34/700 + avatar 32 · field 36 grey · section 20/700 · 2-col tiles 163×113, gap 8, corner 12, label 13/600 on the image (Apple Music 05·4)
- **Headspace — explore root**: outlined search 56 · chip row 40 · 2×2 tiles 164×73, gap 16, label ≈17/700 white · programme card · colour banner tiles (Headspace 09·2)
- **Calm — wellness home**: full-bleed scene photo ≈45 % tall · wordmark centred + two 36 glass discs · greeting 17/400 · mood pill 44 outlined · section 17/500 · content cards ≈112 tall, 12 gap, art 88 · mini player 50 + tab bar (Calm 01·5)
- **ElevenLabs — create hub**: title ≈28/700 + avatar 32 · "+ Create new" black pill 47 full width at 18 · source chips ≈40 · promo banner ~114 · "Recent projects" 13 grey + 2-up tiles ≈161 · floating tab capsule ≈52 + "+" disc 48 (ElevenLabs 06·1)
- **Target — category index**: nav 44 (← · 17/700 centred · search) · rows 64 (icon disc 40 at 12, label 17/700, grey chevron) · full-width hairlines (Target 09·6)

## Money home, send and status

What they share: the balance or amount is the biggest thing on the screen (20–28/600–800 on a home, 22–40 on an entry field, 28/700 on a status), rows carry a 32–48 flag or icon + 15/600 name + 13 grey line, and send lives in one fixed place (a 42–44 centre tab disc, a 47–49 pinned button). What separates the good ones: the amount screen shows the fee, rate and arrival time in 11–15 lines right above the button, before the user commits.

- **Coinbase — money home**: header (grid 24 · search pill 40 · bell 24) · promo card + button pair 43 (filled + tint, 6 gap) · "Prices" 20/700 + dropdown chip 36 · rows 80: icon 32 · name 15/600 + ticker 13 grey · sparkline 40 · price 15 + change pill 12 · tab bar 5 labelled, active blue (Coinbase 01·4)
- **Wise — money home**: avatar 32 + earn pill 32 + chart icon · title 28/700 · balance cards ≈208×206 radius 20 grey, flag 48, amount 20/600 + currency 13 grey, 12 gap + peek · section 22/700 + "See all" 15/600 underlined · rows flag 48 + 15/600 + 13 grey · tab bar with centre send disc 42 (Wise 01·1)
- **PayPal — money home**: tinted ground · header discs 28 · balance card ≈80 (logo 28 + ≈24/800 figure + 11 label) · "Send again" 15/700 + avatar rail 55 with 11 names + black search disc · one activity card (avatar 40 + 13/700 + 11 grey lines + amount 13/700, green for incoming) · "See more" 13/700 accent · 3-tab bar with the centre as a 44 accent disc (PayPal 01·2)
- **Wise — send calculator**: × disc 32 · underline tabs · field 76 outlined (amount 22 + flag + code 20/600 ⌄) · fee lines 13 with dashed links · second field · arrival line 15 with bold time · hairline bar: outlined calendar disc 44 + Continue 49 (Wise 03·2)
- **PayPal — send amount**: header back + title 13/600 centred · recipient avatar ≈62 + name 15 · label 11 grey · amount ≈40/600 + currency 13 right · hairline · second amount same size + outlined currency pill 28 · rate 11 grey · message pill 40 · Request · Send black pills 47 as a strict pair, 12 apart (PayPal 05·2)
- **Wise — transaction status**: grey header block · status disc 56 · status 13 grey · amount 28/700 · tag chip · "Transaction details" 20/700 · label/value rows 15 · outlined "View order" 44 (Wise 10·3)

## Dashboards, charts and stats

What they share: one big figure (22–28/700, or 90 for a weather temperature) over a chart 150–250 tall that runs edge to edge with no gridlines, a range control right under it (segmented 32–42 or 13-pt chips), then a 17–20/700 section with label/value rows. What separates the good ones: colour is kept for meaning only (up/down, the selected metric, a status bar), and every number is tabular.

- **CARROT Weather — weather home**: hero card at 16 gutter, 24 corners, ≈244 tall (city 17/500 · temperature ≈90/200 · quip 17 centred) · summary row "Thursday 78 61" · hourly strip 6 columns (time 12, icon 28, temp 17/600) · daily rows 49 pitch (day 16 · precip 13 blue · high 16/700 + low 16 grey over a 4.6 range bar) · 5 labelled tabs (CARROT Weather 01·1)
- **CARROT Weather — metric detail**: back · title 17/600 · share · 6-segment day control 32 · 11 caps eyebrow + 22/700 range · chart ≈150 with right axis · two metric cards 167×62, selected filled in the metric colour · "About X" 17/700 + 16 body in a card (CARROT Weather 02·5, 03·1)
- **Acorns — asset detail**: header back + title 13/600 + 11 grey sub · tabs 15 with 2-pt underline · price ≈28/700 · change 15/600 with arrow · line chart ~250 edge to edge, no axes · range segmented ≈42 at 20 gutter · 11 grey disclaimer · "Your position" 20/700 + label/value rows (Acorns 04·4)
- **Coinbase — asset detail**: header back · name 15/600 · star · share · price label 13 grey · price ≈28/700 · change 13 coloured · line chart full width · range chips 13, selected pale-blue pill · 5 discs 42 with 12 labels · "About X" 20/700 + "View more" 15/600 blue (Coinbase 03·2)
- **Copilot — finance dashboard**: blue band (wordmark 28/700 · gear · chat · text tabs with white active pill 30) · summary card at 16 gutters (17/700 figure + 13 grey + line chart with status tag) · 11 uppercase label + "view all ›" · 4 budget discs ≈56 with 13/700 amount + 11 grey "left" (Copilot 03·5)
- **Copilot — budget table**: donut 72 between two 17/700 figures · column heads 11 uppercase · rows 32 (dot 6 · emoji 16 · 13 label · 13 tabular spent · 60-wide status bar · 13 budget) (Copilot 04·4)

## Grids, browse lists and libraries

What they share: 2 columns 161–165 wide with 8–15 gaps at 15–20 gutters, the image at its own ratio (4:5 product, 3:4 recipe, square cover), a 13–15 title and a 12 grey meta line under it; list rows lead with a thumb 48–144 wide and a 13–15/600 title with 12 grey lines, on a pitch of 56–124 that follows the thumb. What separates the good ones: one geometry per screen, and sort and filter collapse into one 44 bar or one text control instead of a toolbar.

- **Asos — product grid (listing)**: back · brand 13/700 caps centred · SORT ⌄ | FILTER split bar ≈44 · count 11 grey centred · 2 columns 164 wide, gap 15, image 4:5 · price 14/700 + heart 20 · name 12 grey two lines (Asos 02·5)
- **Kitchen Stories — recipe grid**: header 15/600 + filter glyph · orange text tab with 2-pt underline · 2 columns 165, gap 15, gutter 15 · 3:4 image 12 corners with duration/diet chips 11 + like pill · title 13 on 2–3 lines · author 24 + name 12 orange (Kitchen Stories 01·5)
- **Netflix — filtered list**: back · title 17/600 · Edit · text tabs 17/700 with a red underline · outlined chips 30 · sort 11 grey + 15/700 ▾ · rows 84 pitch (thumb 126×62, title 13/600, play ring 32) (Netflix 04·4)
- **Nike Training Club — browse list**: back · title 17/600 · scrolling text tabs 13 with 2-pt underline · count 13 grey · rows thumb 101 square at 24 + title 13/600 + three 12 grey lines + bookmark 20 · pitch 124 · pinned "Filter | Sort" bar 44 (Nike Training Club 03·5)
- **Apple Music — chart list**: large title 34/700 + accent text filter top-right · rows 56 = thumb 48 + rank 15 + title 15 + artist 12 grey + ⋯ · hairline inset from the title · mini player 56 + tab bar (Apple Music 05·5)
- **komoot — saved list**: header (back disc 31 · title 17 · search · Import text) · filter row with count · rows ≈160: 65 square thumb + sport badge · title 15/600 · stats 13 with icons · difficulty chip · 11 grey date · trailing privacy icon (komoot 04·1)
- **Figma — file list root**: title 34/700 + avatar 28 top-right · rows 81 = thumb 88×64 corner 6 + name 13/500 + location 12 grey · tab bar 4 labelled icons, blue active (Figma 07·2)
- **Denim — cover library**: title 28/700 + gear disc, + disc blue, ⋯ disc · 2-col covers 120, corner 16 · name 15/600 + count 12 grey · two-item tab bar (Denim 05·5)
- **Pinterest — collection page**: back · filter · ⋯ header · title ≈30/700 centred · avatar stack 32 + "+" disc · 13 grey privacy line · 3 action tiles 68×72 (icon 24 + 11 label, 12 gap) · "N Pins" 17/700 · 12 · 2-col grid, 7-pt edge · floating "+" disc 56 (Pinterest 08·5)
- **Tripsy — trip list**: title 17/600 centred + tinted header discs 28 · search pill 36 · year header 22/600 (current in accent with ⌄) · rows cover 97 square, ≈20 continuous corners + "3 years ago" 13 grey + title 20/600 + dates 15 grey with → · 15 between covers (Tripsy 02·4)
- **YouTube — downloads list**: header back + title 17/700 + 3 icons 24 · summary (15/600 title + 12 grey "MB used · updated" + gear) · rows on a 106 pitch: thumb ≈144×81 radius 8 with duration badge · title 15 two lines · channel 12 grey · status 12 blue · ⋮ · undo toast 54 dark inset 8 (YouTube 03·4, 10·6)
- **Apple Podcasts — episode row**: art 90, radius 8 · 11/600 caps grey eyebrow · 15/600 title two lines · tinted pill 24 "▶ 19m" with progress · trailing ⋯ 20 grey · 104 pitch, hairline inset (Apple Podcasts 06·1)

## Product, booking and event pages

What they share: the picture first (edge to edge, or at a 20 gutter with 16 corners), a title from 13 to 34 depending on the brand's voice, one grey meta line, and one pinned primary 45–51 tall. What separates the good ones: the footer puts the price or the date next to the button (Airbnb, SSENSE), so the moment of decision answers "how much, when" without a scroll.

- **SSENSE — product page (editorial)**: text header BACK · BAG 00 (≈9 uppercase) · cutout on white ≈420 tall + colour-thumb strip ≈24 · brand 13 underlined + name 13 + price 13 · black ADD TO BAG ≈175 × 45 (≈11 uppercase) + text ADD TO WISHLIST · uppercase section labels 13 over 12 body (SSENSE 03·6, 02·5)
- **Airbnb — booking detail**: hero photo edge to edge with a 1/24 counter · white sheet over it, title 26/600 centred, meta 15 grey, host row avatar 40 · sticky footer: struck price + 15/700 underlined price + 12 grey dates left, coral Reserve 148×51 right, 24 gutter (Airbnb 09·3)
- **Luma — event page**: poster-tinted dark gradient · poster at 20 gutter, 16 corners · eyebrow link 13 grey · title 22/700 · Share / Open on Web translucent pills ≈25 · details card (date 17/600 + time 13 grey + weather right; place + map 12 corners) · hosts card · pinned white pill 50 (Luma 05·3, 09·1)
- **Apple Invites — event page**: art or gradient ground · × and ⋯ discs 32 · title display ≈34/800 centred · date/place 15 accent · RSVP capsule ≈72 (3 × icon 16 + 13/600) · stacked tinted cards (16 gutter, 8 gap, ≈20 corners) each = icon 20 + 13/600 accent label + 15 body · feature cards with × and a ≈36 tinted pill (Apple Invites 06·2, 07·1)

## Cart and checkout

What they share: item rows with a thumb 60–73, a 12–15 name, the price and a stepper or a remove text link; sections split by 12–18-pt grey bands rather than cards; the total at 15–17 bold; one pinned CTA 44–57 in black or the brand colour. What separates the good ones: the total sits beside or right above the pinned button, and Apple Pay is the only second button allowed next to it.

- **SSENSE — bag**: title ≈20/400 uppercase · column labels 9 · rows: cutout ≈60 × 100 · brand / name / size 12 · price right · MOVE TO WISHLIST / REMOVE 8 · pinned: TOTAL ESTIMATE 8 + total ≈17 left, black GO TO CHECKOUT 178 × 45 right (SSENSE 05·3)
- **Target — cart / checkout summary**: title ≈32/800 + 13 grey "subtotal • items" · ⋯ disc 36 · rows on a 64 pitch with full-width hairlines (icon 24 + 17/700 + 13 grey, ⓘ trailing) · 18 grey band between sections · sticky footer red "Check out" 44 + outlined Apple Pay 44 (Target 04·6)
- **Uber Eats — cart**: × + store name 15/600 + group icon · rows 73 thumb + name 15/600 + price 13 grey + stepper (trash · n · +) · "+ Add items" grey pill · option row with checkbox · Subtotal 17/600 · savings bar 50 full bleed · black CTA 56, 16 gutter (Uber Eats 05·3)
- **Asos — checkout**: sections on 12-pt grey bands · caps titles 15/700 · outlined full-width option buttons ≈48 with icon and "OR" · promo block in black · total row 15/700 · pinned PLACE ORDER bar (Asos 07·5, 08·1)
- **Luma — ticket checkout**: event summary card · "Select a Ticket" 15/600 · radio cards 113, gap 9 · Total 15 grey + ≈24/700 · Credit Card grey + Apple Pay white pair (Luma 05·6, 08·4)

## Search, filters and sort

What they share: filters open as a sheet or a full screen with × and a 17/600–700 title, sections with 13–20 labels, controls 28–52 (chips, 30-pt stepper circles, value rows on a 28–52 pitch), and a sticky footer with a text "Clear" or "Reset" 15/600 and one filled button 44–46; search results keep the query in the header with a × and ≈30 dropdown chips under it. What separates the good ones: the button counts the result ("Show N homes", "VIEW RESULTS"), and the selected state is a 2-pt ink border or a check, not a colour change alone.

- **Airbnb — stepwise search**: category tabs · collapsed step cards 56 (grey label left, value right) · open step card inset 12, title 26/700, segmented 41 · footer: "Reset" underlined 15/600 + ink "Next" 46 or coral "Search" 46 (Airbnb 01·1, 08·2)
- **Gmail — search results**: back + query 17 + × · dropdown chips ≈30 scrolling, active blue-tinted · 15/600 section headers · mail rows with highlighted terms · empty: 160 illustration + 13 grey "No matches" (Gmail 05·5, 06·1)
- **Rewind — visual search results**: sheet with segmented header 36 · 2-column grid of thumbnails 161 wide, 12 gap, 19 gutter, 12 corners · source icon 16 + time 13/500 under · field 44 docked at the bottom (Rewind 04·6)
- **Flighty — search results sheet**: title 28/700 + 13 grey sub · three grey field chips 36 in one row · caps 11 blue toggle left + count 11 grey right · rows 120 (status column 60 · code 11 + status 11 · route 15/600 · two time pills 13/600) (Flighty 10·1)
- **SSENSE — filter screen**: CANCEL / CLEAR 9 left, applied values "NAME ×" 13 · facets 9 uppercase with 2-digit counts, active underlined · values 13 at ≈28 pitch · VIEW RESULTS black 147 × 46 centred at the bottom (SSENSE 01·5)
- **Airbnb — filters sheet**: × + title 17/600 centred (or 28/700 left) · gutter 24 · section 20/600 + 13 grey line · histogram + slider with two 48 price pills · stepper rows 44 with 30 outlined circles · outlined icon chips ≈42–48, 8 gaps, selected with a 2-pt ink border · collapsible sections with chevrons · sticky footer: "Clear all" 15/600 + ink button 46 "Show N homes" (Airbnb 02·6, 07·4, 10·6)
- **Asos — filter value list**: caps title + CLEAR chip · rows ≈52 (swatch 24 + label 13 + grey count) with blue ✓ · sticky black caps bar ≈44 "VIEW ITEMS" (Asos 03·1)
- **Uber Eats — filter sheet**: dimmed map · sheet title 17/700 centred · rows ≈52 (control 20 + 15/600) · full-width black Apply ≈44 · text Reset 15/600 (Uber Eats 04·2)
- **Calm — category filter sheet**: white sheet · × · "Category" 17/500 centred · "Clear" · 2 columns of outlined tiles 160 × ≈52, 12 / 8 gaps, 20 gutter · selected = 2-pt navy border (Calm 05·1)

## Maps, places and routes

What they share: the map full bleed or over the top 40–75 %, 40–56 discs floating at the right edge, and a sheet with a grabber, a 17–22/600–700 title with a 13 grey line and one CTA 40–57; the ETA or time is the largest figure. What separates the good ones: the full-width black 57 button appears only where the screen is one decision (confirm pickup, choose a ride); a route overview keeps hugging 40-pt buttons at the left (Google Maps).

- **Google Maps — map root**: map full-bleed · search pill ≈48 white inset 8 (logo · "Search here" 17 · mic · avatar 32) · chip row ≈32 (icon 16 + 13/500, 8 gaps) · layers disc ≈40 · locate 56 white + directions 56 blue stacked on the right above the tab bar · tab bar 5 labelled, active in a tint pill (Google Maps 01·1, 01·3)
- **Uber — confirm on map**: map ≈75 % with pin + blue label pill 13/600 · white back disc 44 top-left · sheet: title 17/600 centred + hairline · address 15/600 + 13 grey + grey "Search" chip 32 · black CTA 57, 15–16 gutters (Uber 05·4)
- **Tripsy — place detail sheet**: title 22/700 + 13 grey type · share + × discs 28 · three action tiles 107×81, gap 8 (icon 24 accent + 13 grey) · cards of label 13 grey over value 15 (links in accent) · separate 52-pt action cards 15 apart (Tripsy 06·3, 04·5)
- **komoot — route detail over map**: map top ≈40% with back disc and share/⋯ discs · sheet ≈20 corners · chip 11 + rating · title ≈22/700 · meta row · 2 × 2 stats (label 12 grey + value 17/600) · underline tabs 13 · pinned Save filled ≈250 × 42 + two 42 square tonal buttons (komoot 03·4)
- **Target — store hours**: title 34/700 · 3 action tiles ≈109×52 (icon 20 + 11 label accent) · day rows 17/700 + 13 grey date, open/close 13 right, today in green (Target 09·4)
- **Google Maps — route sheet**: grabber · "10 min" 17 green + "(3 stops)" grey · reason 13 grey · filled blue "Start" 40 × 87 (icon + 15/500) + outlined "Steps" 40, both hugging and left-aligned (Google Maps 08·3)
- **Google Maps — turn-by-turn**: green banner ≈88, inset 8, corner 12 (arrow 32 · street 24/500 · "toward …" 17) · 40 discs in a right column · sheet: ETA 22/700 + 15 grey arrival, reroute disc + red "Exit" pill ≈56 · rows ≈64 (icon 20 + 17) (Google Maps 10·3)
- **komoot — route planner**: search 32 + sport glyph + × · hint bar ≈36 accent · map · discs 40 right · floating accent pill 45 centred (komoot 01·4)
- **Uber — choose a ride**: sheet title 17/600 · rows vehicle 64 + name 15/600 + price 15/600 right + 13 grey lines · selected ride as a 2-pt black outlined card ≈127 tall with a large image · payment row · black CTA 57 with two lines 17/600 + 11 (Uber 04·3)
- **Flighty — live status sheet over a map**: map top ~40 % · sheet with logo 24 + eyebrow 12 grey + title 17/600 two lines + × disc 24 · pill row ≈32 scrolling · status strip 15/600 green + 12 grey · per airport: code ≈35/700, time ≈28 green, struck old time 12 grey + delta 12/600, terminal/gate 12 grey · total line 12 grey on a hairline (Flighty 05·6)

## Calendar, timeline and task editors

What they share: a weekday row 11 grey, date rows 38–44 tall with today as a 28–32 accent disc or square, hour labels 9–10 grey and a 1-pt now line; editor sheets use a 20–28/600–700 title, property rows 40–57 with 16–20 icons, 24–32 chips and a 28–30 Done pill. What separates the good ones: one colour per task carried through the title, the capsule and the CTA (Structured), and task height drawn from its duration.

- **Cron — calendar root**: ☰ · month 28/700 + chevron · date chip 28 · weekday row 11 grey · month grid rows 44 (today accent 32 rounded square) · day columns with 13/600 headers + accent date chip · hour labels 10 grey · now line 1 pt + 11/600 time · bottom tray (15 grey status · ⋯ · grey + disc 36) (Cron 01·1)
- **Structured — day timeline**: month title ≈26/700 + year in the accent · 4 accent glyphs 22 · week strip (day 11 grey, date ≈16/500, today 28 accent disc, colour dots) · white rounded sheet · time column 9 grey · capsules 56 wide, height = duration, tinted by task colour, icon 24 · time 11 grey + title 15/600 · completion circle 22 right · gap note 11 grey + 24 chips · FAB 56 accent (Structured 01·2)
- **Superlist — due-date sheet**: inset card 16 from sides · header 13 grey + Clear/Done pills ≈30 · 3 quick rows ≈40 (icon 16 + 15) · month title 13 + arrows · 7-column grid rows ≈38, today outlined, pick in accent disc · Time / Remind / Repeat rows ≈57 with trailing × (Superlist 02·6)
- **Cron — event sheet**: "Event" 13 grey · ⋯ · Done pill 28 · title 22/600 · rows 40 (icon 16 grey · value 15 · grey qualifier) · toggle · participants (avatar 24 + 13 + 11 grey role) · RSVP segmented 28 · accent split button 40 bottom-right (Cron 02·5)
- **Structured — task editor sheet**: title 22/700 (verb in ink, noun in task colour) + × · name 17/600 with icon 24 · question labels 15 grey + "More…" in task colour · wheel with a filled selected pill · segmented values · colour discs 38, 16 apart · alert rows 44 · pinned ≈56 CTA in the task colour (Structured 02·2)
- **Todoist — task detail sheet**: breadcrumb 13 grey + ⋯ and × discs 28 · check 22 + title 20 · property rows 44, icon 20 · outlined chips 32 · + Add Sub-task · Comments with count + composer pill (Todoist 06·2)
- **Superlist — task detail with comments**: tinted header (back disc · status pill · avatar · ⋯) · title 28/700 · 12 grey meta line · ghost "add a task" row · "Created by …" 11 grey · composer pill 44 + accent + disc 44–48 above the tab bar (Superlist 06·1)
- **Linear — issue detail**: id 12 grey + ⋯ · title 22/700 · grey 12-radius property block with 2 rows of 24 chips + "+" disc · description 15 · file card 52 · "+ Add sub-issue" 13 grey · activity timeline (6-pt hollow dots, 13 text, 11 grey time) · comment pill 36 over a 5-icon bar (Linear 02·4)

## Inbox, task and note lists

What they share: rows on a 51–85 pitch with a 15/500–600 title, a 13 grey snippet and an 11–12 grey time, no dividers or hairlines inset from the text, unread marked by weight or a 6-pt dot, and creation as one floating disc 44–60 or a search pill + "+" disc at the bottom. What separates the good ones: undo arrives as a 48–54 dark toast instead of a confirm dialog, and swipe carries the quick action (Linear "Read").

- **Gmail — inbox**: search pill ≈48 at 15 gutter (menu 24 · placeholder 16 · avatar 32) · caps label 11 · rows 85 pitch (avatar 40 · sender 15/600 + time 12 · subject 13 · snippet 13 grey · star) · extended Compose pill ≈47 bottom-right · 2-icon tab bar · snackbar 48 with Undo (Gmail 01·1, 01·3)
- **Linear — inbox**: title 22/700 + filter glyph · rows ≈68 (avatar 34 + 14 badge, title 15 ink/grey, 6-pt blue unread dot, 13 grey sub, trailing "⏰ 39m" 13) · swipe → accent "Read" tile · empty = line-art ≈80 + 13 grey (Linear 03·2, 08·6, 08·4)
- **Substack — inbox**: title 22/800 + avatar · rows: eyebrow 11 caps + date + bookmark, title 17/800 two lines, 13 grey sub, thumb 84 · status chips 11 caps · floating segmented pill above the tab bar (Substack 08·2)
- **Sora — dark DM thread**: back disc 32 + avatar 20 + name 15/600 › centred · date 11 grey · system lines 11 grey · bubbles grey ≈18 radius, 15 text, avatar 28 on incoming · composer pill 40 (field · mic · send disc 24) (Sora 01·2)
- **Raycast — notes list**: header (back disc 40 · icon 20 + title 15/600 · ⋯ disc 40) · optional tint banner 13, corner 16 · group label 12/500 grey · rows ≈54: title 15/500 + 11 grey meta, no dividers · floating search pill ≈44 + "+" disc ≈44 at the bottom (Raycast 02·1)
- **Wispr Flow — notes list**: header ☰ + 17/500 centred title + ↻ · search field 36 frosted · "Today" 13 grey · white note cards ≈18 radius, 17 apart (name 17/500 + body 15 in 3 lines + 12 grey time + "✦ AI" chip 24) · ink FAB ≈60 · floating tab capsule 58 (Wispr Flow 08·3)
- **Bear — note list**: header 44 (menu · list name 17/600 ⌄ · search) · gutter 28 · note = title 15/600 + 2 lines 14 grey + thumbs ≈73 tall (gap 7) + time 11 grey + hairline · 57 accent disc bottom right, 21 from edge (Bear 02·4)
- **Todoist — task list**: red header (back · title 20/700 white · icons 22) · section header 15/700 + grey count + chevron + ⋯ · rows: check 20 in priority colour + title 15 two lines + 13 grey note + 12 coloured date · hairline inset 48 · red FAB ≈56 (Todoist 01·4, 01·5)
- **Adobe Photoshop — voting list**: header × · title 17/600 · + · tabs All / Mine 12 blue underline + "Top ▾" · rows 80: vote box ≈52 (arrow + 15 count + 9 "Votes") · title 15 · tag 9 + comments + date 11 grey (Adobe Photoshop 10·5)

## Sign-in, sign-up and passcode

What they share: a logo or wordmark 20–48, one headline 24–28, stacked provider pills 44–54 tall with 13–16 gaps at 14–32 gutters, and 11–12 grey legal at the foot; a passcode is 6 dots and bare 28/400 digits on a ≈64 pitch. What separates the good ones: every provider button has the same height and style, with at most one set apart (Apple filled dark, or the last option translucent), and there is no email form on the first screen.

- **Luminar — sign-in**: logo 48 · title ≈28/700 centred · 4 white pills 44, gap 16 · opt-in radio 11 · terms 11 grey (Luminar 01·2)
- **Wispr Flow — sign-in**: wordmark 20/700 · serif headline ≈24 centred with an orange italic phrase · stacked auth buttons 52 tall, 13 apart, 18 gutter (outlined 1-pt ink; Apple filled dark) · legal 11 grey centred (Wispr Flow 10·3)
- **ten ten — brand-ground sign-in**: full red ground · back and ? 24 in the corners · empty top half · 3 white provider pills 54 (logo 17 + 15/600) at 14 gaps, 24 gutter · last option as translucent red pill (ten ten 03·6)
- **X — sign-up entry**: logo 28 centred · headline 28/800 left at mid-screen · 2 outlined social buttons ≈30 + "or" hairline + black 33 button, 32 gutters · legal 12 grey · Log in link at the foot (X 10·1)
- **Revolut — passcode**: title 28/700 centred · 13 grey hint · 6 dots ≈16 accent · 3×4 bare digits ≈28/400 at ≈64 pitch · delete glyph left of 0 · accent disc 60 with → in the right cell (Revolut 06·3)

## Onboarding questions

What they share: back + progress (an 8-pt bar or "1/2"), a question 20–28/600–700 left-aligned on up to three lines, a 13–15 grey reason, answers as full-width pills or cards 44–82 tall with 8–18 gaps, selected as an ink or accent fill, and a Continue 44–55 pinned and pale until an answer exists. What separates the good ones: a single-choice answer advances on tap with no Next (Nike Training Club), and "Skip" is 13–15 text, not a second button.

- **CARROT Weather — onboarding step**: 96 logo disc · two 17 lines centred · 11 grey disclaimer · blue Continue 55, full width at 20 gutter (CARROT Weather 09·5, 10·3)
- **Duolingo — onboarding question**: back · progress 8 · question 20/700 · field ≈44 with valid check · CTA 49 12 below the field · legal 13 grey centred when pinned (Duolingo 07·6, 04·3)
- **Revolut — yes/No question**: title 28/700 left (up to 3 lines) · 15 one-liner · illustration centred · strict pair of 56 pills at 16 gutter, ≈6 gap, pale tinted "No" + filled "Yes" (Revolut 03·4)
- **Revolut — interest chips**: title 28/700 + 13 grey reason · group header 17/600 · chips 38 tall, emoji 14 + 13/500, 8–10 gaps, grey → accent fill when selected · floating Continue pill, disabled pale until one is picked (Revolut 07·6, 09·5)
- **Opal — survey question**: title 28/700 two lines left · 10 answer pills 44 tall, 8 apart, #1C fill, 15/500 centred · selected white with ink text · white 48 "Continue" pinned or "Skip" 13 grey text (Opal 05·2, 08·3)
- **Nike Training Club — questionnaire step**: back · "1/2" 15/600 centred · question 22/600 left, two lines · 13 grey sentence · full-width answer pills (1-pt grey outline, fully rounded, ≈48 or ≈80 with a 12 grey sub-line), 12 apart · selected = black fill, white text · the tap advances, no Next (Nike Training Club 02·2)
- **VSCO — interest picker**: back arrow + "Skip" 15/600 header · question 15/600 + 12 grey hint · 7 option rows 48 (1-pt outline, selected grey fill) with 8 gaps at 24 gutters · black pill 42 full width 45 below the list (VSCO 08·6)
- **Todoist — onboarding question**: Back red · title 22/700 left two lines + 13 grey · choice cards 82 tall, gap 18, illustration + 15/600 + radio 20 · hint card · Skip grey + Continue red 35 side by side (Todoist 06·6, 07·2)

## Feature intro and permission sheets

What they share: a sheet or card inset 8–24 with 12–32 corners, one glyph or illustration 48–120, a title 17–28/700 centred, one 13–15 grey line, three benefit rows (icon 20–48 + 13–17/600 + 13 grey) and one pill 44–51. What separates the good ones: exactly three rows and one button, and the permission sheets explain why before the system prompt appears (TikTok, Rewind).

- **TikTok — pre-permission sheet**: white sheet, corner 12 · × 24 top-right · illustration ≈120 · title 20–22/800 centred · 13 grey, 2 lines · optional toggle row 15 · pink pill ≈44, inset 32 (TikTok 06·1)
- **Rewind — permission guide (dark)**: back + title 17/600 · app icon 64 · title 17/600 + 15 grey · numbered steps (disc 20 + 15 with bold key word) · framed Settings mock, 16 radius in the accent · grey pill CTA ≈50 with ↗ (Rewind 04·3)
- **Halide Mark II — camera feature explainer**: blurred live view behind · white card inset 20, radius ≈24 · glyph in an 80 ring · title 17 tracked caps · one 15 grey paragraph · 3 rows (grey tile 48 + 17/600 + 13 grey) · outlined pill ≈44 "Continue" (Halide Mark II 06·3)
- **Meta AI — feature intro sheet**: sheet inset 8, radius ≈32 · icon disc 48 · title 20/700 centred · 13 grey line · 3 rows (icon 20 + 13/600 + 13 grey) · accent pill 46 + grey pill 48, 14 gap (Meta AI 05·2)
- **ChatGPT — feature intro sheet**: gradient header with 2 sample prompt bubbles · title 28/700 centred · 15 grey one-liner · 3 benefit rows (outline icon 28 + 15/600 + 15 grey) · ink pill ≈51 full width at a 24 gutter (ChatGPT 09·3)
- **Fable — feature tour card**: dimmed screen behind · white card 16 corners inset 24 · top half a colour block with a real UI mock · serif title 24/400 centred · 13 grey two lines · beige "Next" pill 36 · × disc 24 on the colour · page dots under the card (Fable 08·4, 10·4)
- **Apple Invites — intro**: example cards tilted in a carousel · title ≈30/700 centred · 13 grey line · white pill 49 hugging the label, centred (Apple Invites 01·6)

## Paywalls, plan pickers and cancel flows

What they share: a title 22–28/700–800, 3–4 benefit rows (icon or check 20–24 + 15/600 + 13 grey), two to four plan cards with the selected one in a 2–2.5-pt accent outline with a check, one CTA 44–58 carrying or sitting under the price, Restore as 13 text and legal 11–12 grey. What separates the good ones: the price is on or right above the button; cancel flows offer a downgrade first and make the final step a plain red outlined pill (Acorns).

- **Claude — paywall**: night violet ground · line illustration ≈120 · serif title ≈28 in the accent · 4 check rows 13 · price line 13 with the amount bold · full-width pill 55 at 10 gutter · 11 legal links (Claude 10·1)
- **Apple News — paywall sheet**: wordmark + × disc · headline 28/800 centred 3 lines · body 15 grey · product mockup collage · brand CTA 325×51 · renewal line 11 grey (Apple News 04·5)
- **TIDAL — plan paywall**: card 335 on gradient · wordmark 20/800 · bullets 15/600 amber dots · segment 28 · price 13 · white Continue 288 inside the card · Restore 13/600 · legal 11 grey (TIDAL 09·1)
- **YouTube — plan picker**: title 17/700 centred · outlined radio cards 75–86 tall, 10 gap, plan 15/600 + price 13 + note 11 grey · hairline bottom bar · "Cancel" 15 text left · "Confirm" pill 38 hugging its label right (YouTube 03·5)
- **Tripsy — plan picker paywall**: dark · name 28/700 + PRO chip · four outlined row cards ≈60 (name 17/600 · price 17/600 right · discount 13 accent) · selected in accent outline · accent Continue 48 pinned · legal 11 grey (Tripsy 08·6)
- **Tinder — paywall**: × + wordmark · title 22/700 · plan cards 263 wide peeking, selected with a 2-pt outline + check · 13 note · benefit list (check 20 + 15/600 + 13 grey) · 11 grey legal · dark 44 pill with the price (Tinder 10·3)
- **X — subscription table**: tier carousel 53 · grey cards of ≈22-pt feature rows, check or value right · pinned black pill 37 · plan sheet: 2 plan cards, selected outlined blue + saving chip, black pay pill, 11 grey legal box (X 08·6, 09·2)
- **Playground — paywall sheet**: × + Restore 13 · title 28/800 two lines (product word in gradient) · 4 rows icon 24 + 15/600 + 13 grey · 2 plan cards 165×80, gap 8, selected 2.5 outline + check, discount chip · Purchase 58 blue full width · legal 12 grey (Playground 10·1)
- **Acorns — cancel subscription**: retention screen with icon rows + green "Downgrade instead" + text decline · final red outlined pill · success disc 64 + line + Done (Acorns 10·2, 10·4, 10·5)
- **WhatsApp — cancel / feedback survey**: × · title 22/700 · 13 grey line with a link · group title 15/700 · radio card rows 44 · field · pinned full-width 44 accent (WhatsApp 10·5)

## Settings and account

What they share: an avatar or profile card 40–72 at the top, then rows 44–62 (icon 20–28, often a colour tile, + 13–17 label + grey value or toggle + chevron) in white 12–20-radius cards on grey or flat on white, group labels 11–15 grey, 8–54 between groups, and the destructive row last in red. What separates the good ones: one row style per screen, and Sign out or Log out in its own card or as plain text at the foot.

- **Netflix — profile settings**: title 17/600 centred + Done · avatar 72 with an edit badge · name field 44 outlined · dark cards 61, 8 gaps (icon 24 + 15/600 + 11 grey value + chevron; switches blue) · 11 grey footnote (Netflix 07·1, 03·4)
- **Gmail — settings modal**: Done 17/600 top-right · large title 34/400 · caps group labels 12 grey · white grouped cards on grey, rows 44.6 (28 coloured icon square + 17 label + chevron) · 54 between groups (Gmail 07·6)
- **Acorns — settings**: 8-pt grey bands · section title ≈20/700 · 60-pt rows icon 20 + label 13 + trailing (chevron, green value, badge, toggle) (Acorns 09·2)
- **Craft — space settings**: logo 28 + title 20/700 · text tabs 15 with 2-pt underline · group title 15/600 · rows ≈62 (15 title + 12 grey sub · 13 grey value + chevron) · hairline · next group (Craft 06·2)
- **WhatsApp — profile / account**: back disc 42 white · title 17/600 centred · avatar 142 · "Edit" 15/600 accent · 24 · white card 18 radius at 16 gutters · rows ≈50 (label 17 · grey value · chevron) · floating tab capsule 58 (WhatsApp 02·1)
- **Figma — flat account settings**: header title 17/600 + Done blue · avatar 40 + name 15/600 + email 13 grey · section label 15/500 black · rows 60 pitch, no hairlines, chevron or blue toggle · Log out plain text (Figma 07·1)
- **(Not Boring) Camera — dark settings root**: nav cards 351, gap 8, corner ~20 (3D icon 44 + title 17/700 + sub 13 grey) · mono eyebrow 11 + badge · list card rows ~43 (glyph 20 + 13 + value grey) ((Not Boring) Camera 05·1)
- **(Not Boring) Camera — toggle settings page**: glass back pill + title 17/700 · hero glyph ~80 + line 13 + Learn more · eyebrow 11 mono · cards of rows 76 (title 15 + explanation 13 grey + toggle 58×28 in accent) ((Not Boring) Camera 01·5)
- **Rise — settings sheet**: title 17/600 + accent Done · rows 44 pitch: colour icon tile 28 + 15/500 + grey value or accent toggle · ≈12 air between groups · 12 grey build line at the foot (Rise 03·3)
- **Wispr Flow — account**: stacked white cards on grey, ≈18 apart · profile card (glyph 48, name 15/600, 12 grey email · plan, stat line 12, lavender pill 36) · group cards with a 13/600 icon header and full-width grey buttons 42, 15 apart (Wispr Flow 10·4)
- **Substack — settings sheet**: × 24 · title 34/800 left · profile card with avatar 40 · white cards of 54-pt rows (icon tile 24 + 15/600 + chevron) · Sign out in its own card, red (Substack 04·6)

## Display and tool settings sheets

What they share: a 15–20/600–700 centred title with Done or an × disc, rows 35–52, steppers, segments and sliders instead of text fields, the selected option as an accent or ink 2-pt border or a filled check, and a Reset that is always visible. What separates the good ones: a changed value shows it (accent disc, dot, accent Reset), and the sheet fits without scrolling (Moises).

- **Apple Books — themes sheet**: title 20/700 + × disc · text-size segment + 2 icon toggles 36 · brightness slider · 3×2 tiles ≈98×93, 10 gap, "Aa" 22 + 12 name, selected 2-pt ink border · Customize pill 40 full width (Apple Books 09·2)
- **Rise — display options sheet**: "Display" 17/600 centred + accent "Done" · group label 11 grey · options as boxes 45 tall, 1-pt border, ≈8 radius, 10 gap · selected = accent border + 18 check disc · toggles inside boxes (Rise 02·3)
- **Linear — display options sheet**: rows ≈42 (label 15 + value 15 grey ⌃⌄) · "Row properties" + grey "Reset" · toggle chips 40 tall, 6 apart, grey fill on / outline off · values open a floating menu with a leading check (Linear 07·3, 07·5)
- **Moises — tool settings menu**: sheet title 15/600 centred · rows 52: icon 22 + label 15 · grey value 13 + chevron · toggles in the accent · unavailable rows at 40 % · dot for "changed" · fits without scrolling (Moises 02·3)
- **Moises — value dial sheet**: dark sheet radius 16 + grabber · back ← + title 15/600 centred · optional caption 11 uppercase tracked grey · value disc 52 (white at default, accent when changed) · tick ruler 48 with − / + 24 at the sides · "Reset to original" 13/600 (accent only when changed) · one 11 grey help line (Moises 08·2, 05·1)
- **Bear — typography sheet**: title 17/600 centred + × disc · slider row with value · stepper rows ≈35 (label · value · − | +) · 12 grey footnote · reset bar ≈42 tinted red text · live preview card (Bear 06·6)
- **Halide Mark II — settings sheet over a tool**: chevron grabber · promo card (illustration 56 + 17/600 + 13 grey) · group label 15/600 grey · rows icon 30 + 15/600 + 13 grey two lines at 77 pitch · info rows ≈48 single line (Halide Mark II 03·6)

## Profiles and people lists

What they share: rows on a 60–82 pitch with an avatar 33–56, a name or handle 13–15/600–700 and 11–13 grey lines (handle, reason), and one trailing Follow pill 30–33 tall and 71–89 wide in the accent or black; a profile is name 28/700 + avatar 64, two 28 pills, text tabs and a 2-column grid. What separates the good ones: Follow turns into a grey "Following" in place, and a × to dismiss sits after it at 16 grey.

- **TikTok — suggested accounts**: grey search field 36 · group label 12 grey · rows 76: avatar 56 · name 15/600 + handle 13 grey + meta 12 grey · pink Follow pill 30 × 89, 13/600 (grey "Following" once tapped) (TikTok 02·4)
- **Fable — member list**: header club name 15/600 + count 12 grey centred, "Invite" 15/600 accent right · search pill 36 grey · rows avatar 33 + name 15/600 + 12 grey sub · trailing black "Follow" 71×33 / outlined "Following" · pitch 60, no dividers (Fable 10·2, 10·6)
- **Instagram — suggestion list**: header title 15/700 centred + "Next" 16/600 accent text right · rows at 82 pitch: avatar 56 · handle 13/700 + badge · name 13 grey · reason 11 grey · Follow pill 89×32 13/600 accent (→ grey "Following") · × 16 grey · 16 gutter (Instagram 01·3)
- **VSCO — profile**: name 28/700 left + avatar 64 right · 2 pills 28 (grey Following, black Message) · text tabs 13 with 2-pt underline · masonry 2 × 164 with 15 gap (VSCO 07·4)
- **Tinder — swipe deck**: header 44 (wordmark · bell · filters · boost) · card full width ≈565 with 2-pt segment bars · name 28/700 + meta 13 over a gradient · action row of 5 discs 43/62/43/62/43 with 17 gaps overlapping the card · unlabelled 5-icon tab bar (Tinder 02·5)

## Media detail

What they share: the art edge to edge (up to ≈80 % of the height on Apple TV) with the ground tinted from it, a title 17–28, an 11–13 grey meta line, one white or light primary 45–48 tall (full width, or a strict pair Play · Shuffle 48–52), then a 13 blurb in 2 lines with MORE. What separates the good ones: the colour comes from the artwork, not the brand, and secondary actions are grey 38 buttons or discs.

- **Netflix — title detail with a get action**: key art to black · title 24/700 centred · genre 11 + rating tag · white full-width button 46 at 10 gutter · row of 38 grey buttons (138 · 138 · 62, 8 gaps) (Netflix 05·5)
- **Apple Books — book detail**: full-screen card tinted from the cover · × disc 32 · ✓ + ⋯ pill · cover ≈196 centred · title 20/700 serif + author 15 › + meta 12 · action card: "Book ⓘ" 15/600 + 12 meta + Sample (tinted) · Get (white) pills ≈40 · audiobook card with price pill (Apple Books 02·1)
- **Apple TV — poster detail (dark)**: art edge to edge to ≈80 % height · colour band from the art · logo title · genre 13 · Play pill 151×45 white + disc 45 · synopsis 13, 2 lines + MORE chip · meta 12 with badges · section "Trailers ›" 20/700 · glass tab capsule 59 (Apple TV 06·1)
- **Apple Music — curated playlist header**: full-bleed art ~390 · glass back / download / ⋯ discs 28 · title 17/600 + curator 17 grey + date 11 caps · Play · Shuffle grey pills 157×48, gap 21, gutter 20 · blurb 13 grey 2 lines + MORE · track rows 56 (Apple Music 05·6)
- **Calm — album detail**: art band on top · title 28/400 + heart · creator row avatar 36 + 15/600 + 12 grey · strict pair "▶ Play" white + "Shuffle" outlined, 52 tall, 12 gap · 15 blurb · track rows with heart (Calm 04·1)
- **Headspace — wellness content detail**: hero illustration inset 8 with rounded corners, back 32 white disc · title ≈28/700 + heart right · meta 12 grey with glyph · body 15 grey, 2–4 lines · "Related" 17/700 + 2-up tiles · pinned full-width pill 50 at 23 gutters (Headspace 09·5, 01·4)

## Players

What they share: a ground sampled from the art, the art 335–344 square at 16–20 gutters, a title 15–17/600–700 + 15 grey, a 2–4-pt progress line with 11 times, one play control 44–88 (disc or ring) flanked by skips of 30 or 62, and a tertiary row of icons with an 11 label. What separates the good ones: transport glyphs stay bare, and the art shrinks (≈338 → ≈240) when paused so the state reads without a label.

- **Spotify — queue**: header × + context 13/700 centred · "Now Playing" 15/700 + current row (art 40, title 15 in brand green) · "Next In Queue" 15/700 + outlined "Clear queue" pill ≈28 · rows 64 (radio 20 · title 15 + 13 grey · drag handle) · transport pinned (Spotify 01·3)
- **Apple Podcasts — Now Playing (spoken)**: ground sampled from the art · grabber · art ≈338 (≈240 paused) · row art 40 + 11 caps date + 17/600 title + 15 dim show + ⋯ disc · progress 4 + 11 times · speed · ⟲15 · play 44 · ⟳30 · sleep · volume · 3 icons + 11 route label (Apple Podcasts 05·1)
- **Apple TV — video player**: black · top: × disc · grouped PiP/AirPlay capsule · mute disc · centre: skip 62 · pause 88 · skip 62 · subtitle mono · chips Info · Continue Watching 30 · rows 65 (thumb 82 16:9 + 13/600 + 12 grey) (Apple TV 02·1)
- **TIDAL — Now Playing (tinted)**: stage colour from art · art 335 square, gutter 20 · title 17/700 + artists 15 grey + add 24 · scrubber with times 11 + format 11 · bare transport glyphs, pause ~27 · footer queue disc 36 + source 11/13, share · ⋯ capsule 36 (TIDAL 07·3)
- **The Athletic — podcast player sheet**: × · show 15/700 · ⋯ · art 344 square at 16 · title 15/700 centred ≤3 lines · 2-pt progress with 11 times · speed · back 30 · ≈58 ring play · forward 30 · AirPlay · sleep timer + queue row (The Athletic 08·4, 08·6)

## Editors and camera

What they share: a black stage, the picture at its own ratio, controls in bands under it, tool glyphs 20–24 with 11 labels, the selected tool on a 44 dark square or a white pill, an accent dot for tools that hold a value, and × / ✓ (or Discard / Done) pills at the bottom. What separates the good ones: readouts sit on the picture's edge as small 11-pt capsules and never cover it, and the exit is a clear pair 44–45 tall.

- **BeReal. — capture**: black ground · preview with 16 corners, picture-in-picture 96×128 top-left with a 2-pt border · 0.5× chip · record ring 78 with 64 red core · "VIDEO · PHOTO" 13/600 caps, active yellow (BeReal. 10·5)
- **Luminar — photo editor (one picture)**: black · picture edge to edge at the top · value capsule 11 tracked caps ≈28 on the picture's bottom edge · header row of 5 accent icons 24 · tool strip: preset disc 40 + 6 glyphs 20, selected on a 44 dark square, dot under tools with a value · panel ~140 dark 12-radius with one bespoke control · module bar 5 glyphs 24 (Luminar 04·3, 03·3)
- **Luminar — crop**: picture with corner brackets · W×H chip 11 on dark capsule · rotation arc ruler · undo · redo · ⋯ disc · aspect pill · × grey and ✓ accent pills at the bottom corners (Luminar 07·6, 08·2)
- **Riverside — clip editor (transcript)**: black · × + share disc 32 accent · 9:16 preview · speaker 13 colour + timecode · body 15 (played white, rest grey) · progress 2 pt + 11 grey times · tool band tiles 72×64 (icon 22 + 11 label, gap 8), scrolling (Riverside 09·2)
- **Halide Mark II — edit exit bar**: #121212 band under the picture · two stacked pills 44.6 tall, 36 side inset, 16 gap · "Done" #e6e6e6 ink label · "Discard Changes" #373737 white label (Halide Mark II 01·3)
- **Meta AI — markup tool**: black stage · × disc · "Markup" 15/600 · white Next pill 36 (grey until used) · picture at ratio · vertical size slider left · dark panel: 7 colour discs ≈20 · undo · pen/text segmented pill · redo (Meta AI 02·1)
- **(Not Boring) Camera — object customiser**: 3D object on a dark backdrop · part carousel 22/800 · palette 6×3 discs ~42 · × disc 48 · Done pill 160×48 · share disc 48 ((Not Boring) Camera 03·1)
- **Adobe Photoshop — canvas action fan**: grey canvas · ⋮ disc 28 dark at the object's corner · column of right-aligned white pills ≈40 on a ≈52 pitch (13/600 label + 20 icon) · disabled pills faded · Delete first (Adobe Photoshop 06·2)
- **Denim — apply confirm**: title 17/700 + source 12 grey left · accent "Customize" pill 24 + × disc right · eyebrow 11 caps grey · result ~240 centred · white pill 306×51 with glyph at the bottom (Denim 06·2)

## Composers and forms

What they share: Cancel as text at the left and the primary as a 32–40 pill at the right, pale until the input is valid; the input itself is large (32/700 for a name, 18 placeholder for a post); a 20–44 toolbar docks on the keyboard. What separates the good ones: one field on screen at a time, and the send action hugs its label instead of spanning the width.

- **Spotify — name it**: dark sheet with × disc · prompt 15/700 centred · input ≈32/700 centred on a hairline · one brand pill ≈40 hugging "Create" · keyboard (Spotify 08·2)
- **X — composer**: Cancel 16 left · Post pill ≈32 blue right (40 % until valid) · avatar 32 + outlined audience chip ≈22 · placeholder 18 grey · reply-scope line 13 blue · icon toolbar 20 docked on the keyboard (X 01·2, 01·6)
- **Bear — formatting keyboard**: toolbar row 44 above the keyboard (undo · redo · # · keyboard · BIU) · tap swaps the keyboard for a 4 × 6 key grid at ≈54 pitch, grey system keys for movement, white keys for styles (Bear 04·2)
- **ElevenLabs — script-to-audio editor**: × disc + title 15/600 · speaker chip (orb 16 + 13) · text 15 with pink emotion tags · bottom: 11 grey credits line, grey "Add a speaker" pill 47, settings disc 40, black "Generate" 47 · result card black 16-radius with scrubber, share disc 36, play disc 40 (ElevenLabs 01·4)
- **Figma — bug report**: × · title · send header on a grey band · label 13 grey over value 15 with hairlines · attachments 64 with gap 16 · source sheet rows 54 (blue icon 20 + 15) (Figma 01·6)

## AI assistant chat and voice

What they share: the answer as plain 15/400 text at ≈23 line height on a 16 gutter with no bubble, the user's message as a grey bubble with 16–18 corners at the right, feedback glyphs 20 grey, and a composer pill 40–88 docked at the bottom with mic and a 28–44 send disc; voice screens are black with one glow and two 64 discs. What separates the good ones: the answer has no bubble, and follow-ups or plans come as rows or cards with small 28 chips (Accept, Edit, Discard).

- **Claude — assistant home**: wordmark 22 serif + 32 avatar · serif greeting ≈32 in two centred lines · plan banner 31 outlined with a violet "Upgrade" · chat cards 64 (serif 15 + 11 grey time), 7 gaps, 13 inset · composer sheet 88 with a 12 grey limit line (Claude 02·4)
- **Meta AI — AI answer screen**: header ≡ disc 36 + title 15/600 truncated + compose and ⋯ discs · user bubble grey ≈16 radius right-aligned · "Show thinking ›" 13 grey · body 15/400 · 4 feedback glyphs 20 grey · follow-up rows ≈70 pitch (↳ + 13 grey, hairlines) · floating composer card ≈72 with mode chip 28 + send disc 28 (Meta AI 03·6)
- **Google Gemini — assistant chat**: header back · title 15/500 centred · avatar 32 right · user bubble grey-blue 18 radius ≈44, 15, right · star glyph 18 + speaker 20 · answer body 15/400, line ≈23, no bubble, 16 gutter · 6 icons 20 grey 36 apart · composer pill 44 (inner mic/camera capsule) + separate 44 disc · 11 grey disclaimer (Google Gemini 02·2)
- **Google Gemini — live voice**: black stage · "Live" 13 + glyph top centre · colour glow band at ≈60 % height · two 64 discs with 11 labels (grey Hold, red End), centred low (Google Gemini 04·2)
- **ChatGPT — voice picker**: Cancel + title 15/600 · orb ≈140 centred · name 17/600 + 13 grey trait · 9 page dots · ink pill ≈53 at a 36 gutter (ChatGPT 08·3)
- **ChatGPT — tools sheet**: grabber · "Photos" 15/600 + "Show All" accent · rail of ≈80 square thumbs, camera tile first · hairline · 6 rows icon 20 + label 15 on a 48 pitch, no chevrons (ChatGPT 05·4)
- **Raycast — AI result card**: floating card inset 8, corner ≈32 · header app icon 20 + action 15/500 + × · body 14 / ≈20 · footer regenerate icon left, outlined "Copy" ≈34 + black "Apply" ≈34 right (Raycast 06·1)
- **Structured — AI planner**: sheet title 22/700 grey + ✦ · greeting 22/700 accent + question 22/700 · suggestion cards rail · outlined 44 composer (2-pt accent) with mic + scan · result: collapsible "Your plans" card with Accept All + thumbs · caution card 11 grey · proposal cards with Add · Edit · Discard chips 28 (Structured 03·3, 04·3)
- **Rewind — live transcript**: gear + mic 24 in the header · lines ≈22 grey stacked 69 apart, current 22/700 ink · floating pill 44 "Summarize" · bottom row search · relative time 15/600 · ⋯ · app-coloured scrubber band (Rewind 06·3)

## Reading, articles and news

What they share: serif headlines 15–17 (up to 28 for a section title), rows of headline + thumb on the right 84–109 wide, a 16:9 hero, 11 grey bylines and times; a reader page uses 38 margins and serif text with 12 grey progress lines. What separates the good ones: the thumbnail is always at the right in the same size so the headlines form one text column.

- **Apple Books — reader page**: white or paper ground · margins 38 · serif ≈13 justified, hyphenated · header 12 grey "N pages left in chapter" + × disc 32 · footer "2 of 87" 12 grey · menu disc 36 bottom-right → stack of glass pills 40 + 4 icon discs 36 (Apple Books 07·4)
- **Apple News — editorial feed**: date eyebrow 13/700 · 2-up cards 167, gap 8, gutter 16, corner 12 (image, logo 11, headline 15/700, time 11 grey + ⋯) · full-width cards with image right · tab bar 5 labelled, red active (Apple News 01·1)
- **Apple News — channel list**: publisher wordmark header between 28 discs · section title 28 serif centred · rows headline 15 serif + thumb 96 right · footer tag 10 red + ⋯ (Apple News 01·3)
- **The Athletic — editorial news home**: serif wordmark ≈20/800 centred + search disc 28 · hero 16:9 full-bleed (375×212) · headline serif 17/400 two lines + byline 11 grey · rows headline serif 15 (≤3 lines) + 4:3 thumb 109×82 right, pitch ≈121, inset hairlines · section = logo 20 + 17/700 + rail of 3:2 tiles 160×107 gap 15 · tab bar 5 icon + 10 label (The Athletic 01·2, 01·3)
- **The Athletic — game detail**: back · "AWY @ HOM" 15/700 · share · logos 32 + abbr 13/600 + record 11 grey · scores ≈34/400 · date 11 + FINAL 11/700 centred · underline tabs 15 · key-value rows (13 grey / 13/600) · related stories as headline + thumb rows (The Athletic 02·3, 10·3)
- **Substack — notes feed**: header (logo 24 · search pill 36 · avatar 28) · topic tabs 13/500, selected in a grey pill · rail of cards 190×240 · note rows (avatar 28, name 15/600 + time 13 grey, body 15, embedded card indented to 56, actions 20 grey + counts 13) · orange FAB 44 · 5-icon tab bar with dots (Substack 01·1, 01·3)

## Live sessions, workouts and timers

What they share: one big tabular readout (28–48/700–800 elapsed, ≈100/700 countdown), pause as a 40–44 disc with a progress ring, rows or cells 38–82 with the current step marked, state colours for rest (red) and done (green or orange), and the next action pinned in a bottom bar. What separates the good ones: the whole ground can carry the state (white for work, black for rest in Dropset), so the phone reads from across a room.

- **Dropset — interval timer**: whole screen white (work) or black (rest) · ← 24 · label 28/700 + exercise 17 · countdown ≈100/700 tabular · round line 20/600 · bottom bar: 40 pause disc with progress ring + total 28/700 + grey Stop pill 36 (Dropset 04·4)
- **Dropset — live workout list**: header ↓ + two 40 discs + outlined "Finish" 36 · running time 28/700 + 12 grey "Legs focus · In progress" · rows 82 pitch: status disc 40 + 17/600 + 12 grey + ⋯ + › · "+ Add exercises" row · notes field "Type anything…" (Dropset 06·5)
- **Dropset — add sheet**: grabber · ↓ 24 · title 28/700 + 12 grey line · rows 82 pitch: disc 46 + 17/600 + 12 grey + trailing grey 36 verb pill 13/600 (Dropset 01·2)
- **Train Fitness — live set logger**: header ⌄ · elapsed 17/600 · ⋯ · rest time 15/600 red + 6-pt red bar · exercise card (thumb 48 + 15/600 + ⋯) · column labels 11 grey · set rows pitch 52 of grey 8-corner cells ≈38 (Set · Rest · Reps · Lb · ✓), done = green-tinted check · "+ Add Set" pill 36 + stats disc 36 · floating accent "Suggest" 44 + black + disc 44 (Train Fitness 03·5, 04·1)
- **Train Fitness — workout detail**: back · "Workout" 17/600 · share · ⋯ · author row avatar 28 · title 20/700 · caption/photo pills 32 · three stats (11 grey / 15/600) · "Workout Log" 20/700 + Edit · exercise cards ≈64 (thumb 48 + 15/600 + 12 grey) 8 apart · like + comment bar (Train Fitness 06·1)
- **Nike Training Club — live workout**: black top bar · elapsed ≈48/800 condensed white + pause ring ≈44 · white 12-corner circuit cards (title 17/500 + "⟲ 2x") · rows index + 13/600 + 12 grey + thumb 60 · current step expands into a video with scrubber and "Step n of m" (Nike Training Club 06·3)
- **Opal — live session sheet**: art on a violet glow · 20/700 title + "Remaining time" 15 with a tabular value · timeline strip with 11 times · 2 info tiles (11 caps label + 13 value) · gradient pill 55 + red 15 "Leave Early" text (Opal 10·6)
- **Kitchen Stories — cooking step**: photo ~170 + × disc · ingredient and utensil lines 13 with icons · step ≈22/400 at 31 line height · orange timer value inline · 64-tall bar of numbered step blocks, done in orange, flag last (Kitchen Stories 04·1)
- **Kitchen Stories — ingredients**: caps label 13/700 · servings 13 + −/+ stepper ≈32 · amount / ingredient columns 15 at 19 pitch · hug pill 44 "Add to shopping list" · floating "Start cooking!" pill (Kitchen Stories 03·5)
- **Duolingo — quiz step**: header (× 24 · progress bar 8 rounded · hearts 15/700) · eyebrow 12/800 caps with icon · question 20/700 · exercise · CTA 49 full width, 16 gutters, grey when disabled · after checking, a ≈160 tinted band with title ≈20/700 + answer 15 and the CTA in the state colour (Duolingo 01·1, 04·5)

## Menus and action sheets

What they share: action rows on a 40–66 pitch with a 16–24 icon + 15 label, grouped in cards or split by grey bands, destructive last in red, and Cancel or Close as centred 15/600 text; full-screen menus open with the item's art + title on top. What separates the good ones: chevrons appear only on rows that open a submenu, and quick actions come first as 2–3 tiles above the rows (Instagram, Spotify).

- **Spotify — context menu (full screen)**: blurred artwork ground · art ≈140 centred + title 17/700 + 13 grey · optional strip of 3 toggles (icon 24 + 11 label) · action rows at 64 pt (icon 24 + label 15, Premium pill trailing) · "Close" 15/600 centred at the foot (Spotify 01·2, 09·5)
- **Raycast — row context menu**: frosted card ≈235 wide · row title 11 grey on top · rows ≈40: icon 16 + 15 · submenu chevron · Delete red last (Raycast 08·3)
- **Notion — action list**: title 17/600 centred + Done 17 blue · rows 46 (icon 20 + 15) · groups split by 26 grey bands · chevron only for submenus · destructive last · 12 grey footer (Notion 09·2)
- **TIDAL — action list**: black full screen · art ~107 + title 13/600 · rows icon 20 + 15/600 at ~55 · destructive red · Cancel 15/600 centred (TIDAL 06·1)
- **ten ten — text menu sheet**: dark sheet radius 20 + grabber · items 17/500 lowercase centred on a 66 pitch · destructive red · "close" grey last (ten ten 07·2)
- **Instagram — overflow sheet**: grabber · 2 tiles 163×74 grey (icon 24 + 12 label), 12 apart · grey 12-radius cards of 53-pt rows (icon 24 + 15 label) · 10 between cards · destructive red inside its group · 18 gutter (Instagram 10·5)
- **Adobe Photoshop — source picker sheet**: grabber · title 17/700 + × disc 28 · sources as white cards ≈86 tall on light grey, 16 gutters, small gaps: icon 16 · title 15 + 11 grey sub (Adobe Photoshop 04·5)

## Choice sheets, dialogs and confirmations

What they share: a 15–20/600–700 centred title, options as rows or cards 44–76 tall with 8–11 gaps, the selected one filled or with a check disc; dialogs are centred cards ≈290–295 wide with a 15–17 title, 12–15 body and stacked buttons 40–57, destructive in red and cancel as text or grey. What separates the good ones: buttons stack instead of sitting side by side, and the destructive one is red and says what it does (Block, Delete) rather than "OK".

- **BeReal. — option sheet**: dark sheet inset 5 · title 15/600 centred + 20 × disc · option cards 52 (icon 20 + 15/600 + 12 grey), selected white with ink text, 8 gaps (BeReal. 04·3, 10·2)
- **BeReal. — reason list**: sheet title 15/600 centred · 13 grey note · dark rounded rows 52 with a 15 label and chevron, 8 gaps, 17 gutter (BeReal. 09·4)
- **Opal — choice sheet**: title 20/700 centred · 3 radio cards ≈76 tall, 11 apart (icon tile 32 + 15 title + 12 grey 2 lines, check disc right) · PRO chip 11 · gradient CTA 55 (Opal 06·6)
- **Atoms. — choice sheet**: grabber · icon disc 40 grey · title 20/700 centred · 15 body centred · options as 46 rows 9 apart (selected fills the accent, black check disc) · black 46 Confirm + white 42 Cancel · 23 gutter (Atoms. 01·5)
- **Sora — permission picker**: × disc + ⋯ header · preview disc · group label 13 grey · dark grouped card of 53-pt rows (icon 20 + 15 + radio 22) · second group with value rows › · Retake / Done pills 44 (Sora 08·5)
- **ElevenLabs — picker list**: sort disc + filter pills 36 · rows 61 pitch: orb 40 + 15/500 + 12 grey + ⊕ · docked "Select voice" 47 + search field + × (ElevenLabs 01·6)
- **Craft — task card (sheet substitute)**: floating white card inset 12, radius ≈16 · title 15/600 left + × disc 20 · hairline · search/field 40 grey · 12 grey helper in a grey inner card with a blue link row · full-width blue 44, pale while disabled (Craft 03·5)
- **Notion — confirm dialog**: dim · centred card ≈290 · title 15/600 · option card with checkbox (13/600 + 11 grey) · stacked 40 buttons: red-tinted destructive, outlined Cancel (Notion 09·3)
- **Uber — bottom dialog**: dim · white panel · title 17/600 centred + hairline · body 15 · black button 57 · grey Cancel 57 or text (Uber 07·2)
- **ten ten — dark confirm dialog**: dim ≈70 % · centred card 295 wide radius 20 dark grey · title 17/700 lowercase · body 12 grey ≤ 2 lines · red pill 41 inset 24 · "cancel" 15/600 white text · a second destructive = a second red pill (ten ten 02·1, 06·4)
- **Threads — block confirmation sheet**: grabber · avatar disc 72 centred · title 24/700 centred · one 13 grey line · 3 rows (outline icon 24 + 13 body, ≈40 each) · black button 44 full width at 16 gutters (Threads 04·6)
- **Threads — report sheet**: grabber · title 17/700 centred · question 15/700 + 13 grey explainer · reason rows 61 with hairlines and chevrons · finish sheet with 48 glyph, 20/700 title, 2 icon rows, one 44 button (Threads 06·3, 09·1)

## Empty, error and success states

What they share: a glyph or illustration 48–260, one line 15–24/600–800, one 13–15 grey line, and one pill 28–49 that hugs its label (outlined or grey); success uses a 48–64 check disc. What separates the good ones: exactly one move, and errors stay inline in a tinted card with Retry instead of taking over the screen.

- **Claude — inline error**: tinted card at 16 gutter · 15/600 red title · 13 body centred · one grey pill 28 "Retry" or "Dismiss" (Claude 05·4, 08·6)
- **Rise — empty list**: skeleton of 2 rows ≈180 wide · title 15/600 · 13 grey two lines · outlined accent pill 28 "+ Add new" (Rise 09·5)
- **Uber Eats — empty state**: illustration ≈70 · 17/700 line · 15 grey line centred · black pill 37 hugging label (Uber Eats 07·1)
- **Denim — success**: check disc 48 green · title 22/700 · line 15 grey · two grey pills 164×49, gap 15 · help line 11 grey (Denim 07·3)
- **Atoms. — completion celebration**: dark dotted stage · "Habit completed!" 15/600 centred · badge ≈190 in a 3-pt accent ring · serif headline ≈28/400 · 15 body with the count in the accent · week row 7 × 32 circles, today filled · white 46 pill + dark grey 46 pill, 10 apart, 16 gutter (Atoms. 05·3)
- **Duolingo — session complete**: illustration ≈260 · headline ≈24/800 in accent · 3 stat tiles 94 wide, 27 gaps, 2-pt outline, 10/800 caps tab, value 15/700 · CTA 49 pinned (Duolingo 06·6)

## Share and export

What they share: a preview at its ratio with a small 11 size tag, option rows 52 or scrolling chips 36, and one action: a full-width accent 48, or a pair of 38 black buttons (Save · Share); send-to lists turn the accent "Send" pill grey "Sent" in place. What separates the good ones: the preview comes first, so the user sees what leaves the app before choosing where.

- **TikTok — QR share card**: brand gradient ground · white card inset 32, corner ≈16, avatar 56 on its top edge · name 15/600 · QR ≈140 · caption 11 grey · two white tiles 150 × ≈70 (icon 24 + 13/500), 10 apart · hint 11 grey at the bottom (TikTok 02·3)
- **Pinterest — send-to sheet**: × + title 15/600 centred · search pill 44 · rows 60 (avatar 44 · name 17 with match bold · "Send" pill 58×45 accent, "Sent" grey) (Pinterest 01·4)
- **Riverside — export**: back + "Export" 15/600 · preview card 16 radius · segmented 144×31 · rows 52 (13/600 label · value ⌄ or toggle) · full-width accent 48 at 16 gutters (Riverside 05·2)
- **Playground — export sheet**: grabber · title 17/700 + Done · preview at ratio + 11 size tag · "More actions" 13 grey + scrolling outlined chips 36 · Save / Share black 38 side by side, gap 10 (Playground 10·3)

## How to use

- Pick the section that matches the screen you are building or reviewing, and read its first paragraph for the shared numbers and the one choice that separates the good ones.
- Open one or two of the cited sheets (`refs/sheets/<id>-<App>-<NN>.jpg`, screen k) and look at the screen before drawing anything.
- Apply the numbers through the rules in `SKILL.md`: the project's tokens first, then the rules and measurements (main button 44, dark 40, others 36, gutter 16), then these recipes.
- Take the structure and the numbers, never the branding: no logos, brand colours, wordmarks, illustrations or copy from the cited apps.
