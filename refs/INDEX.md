# Reference library index

The 78 iOS apps studied (4,536 screens, 760 contact sheets), with screen and sheet counts. Study notes per app are in `refs/notes.md`; patterns across apps in `refs/patterns.md`; measured recipes by screen type in `refs/recipes.md`. Contact sheets of six screens live in `refs/sheets/<appId>-<App>-<nn>.jpg`; read a sheet to study six screens at once. `refs/screens-index.csv` maps every screen (sheet, position) to its file in `refs/screens/<appId>/`, and `python3 scripts/refs.py --screen "App NN·k"` prints it for measuring.

v1 (44 apps) was read closely on sheets 01–03 and sampled beyond; v2 read every sheet of all 78 apps and added 34 apps (fintech, commerce, maps, calendar, fitness, reading, AI, weather).

| id | app | tagline | screens | sheets | what to look at |
|---|---|---|---|---|---|
| 1 | Spotify | Discover the latest songs | 60 | 10 | dark · media player · rails · context sheets |
| 2 | Airbnb | Homes, experiences, services | 60 | 10 | light marketplace · cards · filters sheet · calendar · map |
| 4 | Headspace | Relaxation for Sleep & Stress | 60 | 10 | illustrated · timeline cards · paywall |
| 5 | Duolingo | Learn Spanish, French, German | 60 | 10 | playful · lesson flow · chunky buttons |
| 6 | Asos | Discover fashion online | 54 | 9 | light fashion commerce · product grid · SORT|FILTER bar · checkout on grey bands |
| 8 | Pinterest | Home, fashion, lifestyle ideas | 60 | 10 | masonry grid · toasts · long-press radial menu |
| 17 | Calm | Sleep, Meditation, Relaxation | 30 | 5 | gradient wellness · scene-photo home · category filter tiles · album detail |
| 22 | Kitchen Stories | Anyone can cook | 49 | 9 | recipe grid 3:4 · ingredients with servings stepper · hands-free cooking steps |
| 26 | Apple Music | Over 100 million songs | 60 | 10 | iOS native · numbered lists · mini player |
| 27 | Halide Mark II | RAW, Manual and Macro Capture | 60 | 10 | pro camera · dark tool bands · readouts |
| 29 | ChatGPT | The official app by OpenAI | 60 | 10 | quiet assistant · composer · drawer |
| 33 | Cron | Next generation calendar for professionals and teams | 35 | 6 | month grid over day timeline · event sheet · widgets |
| 34 | Todoist | To do, task reminders & habit | 52 | 9 | task rows with priority checks · task detail sheet · onboarding choice cards |
| 35 | YouTube | Videos, Music and Live Streams | 60 | 10 | dense feed · shorts rail · accordion settings |
| 38 | The Athletic | Stories, scores, stats & more | 60 | 10 | editorial news home · serif headlines · game detail · podcast player |
| 39 | Wise | Money without borders | 59 | 10 | money home with balance cards · send calculator · transaction status |
| 41 | Instagram | Bringing you closer to the people and things you | 60 | 10 | feed · stories · comments sheet · follow lists |
| 42 | Threads | Share ideas & trends with text | 60 | 10 | text feed · action row · share sheet |
| 43 | Bear | Write naturally | 60 | 10 | note list · formatting keyboard · typography sheet |
| 49 | Flighty | World's Fastest Delay Alerts | 60 | 10 | dense data · grouped forms · timeline |
| 53 | Google Maps | Places, Navigation & Traffic | 60 | 10 | map root · place sheet · route sheet · turn-by-turn |
| 56 | CARROT Weather | Local Forecasts & Live Maps | 60 | 10 | weather hero card · hourly/daily rows · metric charts |
| 57 | Nike Training Club | Holistic Fitness & Workouts | 59 | 10 | questionnaire steps · browse lists · live workout |
| 63 | Luma | Host Events, Send SMS Invites | 60 | 10 | events · tickets · date column lists |
| 64 | Notion | The all-in-one workspace | 60 | 10 | iOS grouped forms · share · paywall |
| 69 | Gmail | Secure, fast & organized email | 51 | 9 | inbox rows · search chips · settings modal · undo snackbar |
| 71 | Craft | Journal ideas, meeting notes | 60 | 10 | document editor · space home · promo dialog |
| 72 | Figma | Design, collaborate, & mirror | 60 | 10 | minimal tool · empty states |
| 74 | Revolut | Travel, transfer, and exchange | 60 | 10 | fintech · pill forms · plan picker · ID capture |
| 76 | Opal | Focus, block apps & Save Time | 60 | 10 | dark utility · gradient CTA · schedule cards |
| 93 | Coinbase | Most trusted crypto exchange | 60 | 10 | prices list with sparklines · asset detail chart · KYC flow |
| 96 | Fable | Find, read, & chat about books | 60 | 10 | literary · serif · quote cards · filters |
| 99 | Atoms. | The official Atomic Habits app | 60 | 10 | editorial habits · serif · stat tiles · sheets |
| 100 | Copilot | Spending, investing, net worth | 58 | 10 | finance dashboard · budget table · category tags |
| 107 | VSCO | Filters, Effects & Collages | 60 | 10 | photographic · type on white · black rectangles · discussion |
| 108 | Superlist | Home to all your lists | 60 | 10 | productivity · drawer · doc editor |
| 114 | X | Formerly Twitter | 60 | 10 | composer · sign-up entry · subscription table |
| 116 | TikTok | Videos, Music & Live Streams | 60 | 10 | video feed · profile · share sheet |
| 119 | Claude | The AI assistant by Anthropic | 60 | 10 | warm editorial · serif display · form validation |
| 122 | Acorns | Investing. Banking. Growing | 60 | 10 | asset detail chart · settings bands · cancel/retention flow |
| 124 | Uber | Rideshare, taxi cabs and more | 60 | 10 | utility · map sheet · ride rows · two-line CTA |
| 130 | Apple TV | Originals, Sports & More | 60 | 10 | cinematic dark · posters · glass tab bar |
| 131 | Uber Eats | Fresh grocery shopping & more | 56 | 10 | marketplace home · cart with stepper · filter sheets · skeletons |
| 136 | Apple News | News + magazines, in one app | 60 | 10 | editorial feed cards · channel list · paywall sheet |
| 137 | Rewind | Find anything you've seen | 48 | 8 | light · grouped toggles · segmented chat |
| 138 | Rise | Projects, tasks and scheduling in your pocket | 60 | 10 | calm tasks · violet · day calendar |
| 144 | Target | Shop and save from anywhere | 60 | 10 | retail cart/checkout · category index · store hours |
| 148 | ten ten | walkie talkie | 60 | 10 | black · giant type · walkie-talkie |
| 149 | Tripsy | Trip Itinerary Plan Organizer | 60 | 10 | trip list covers · place sheet over map · date ranges |
| 153 | Google Gemini | Your AI assistant from Google | 60 | 10 | assistant chat · live voice · composer |
| 154 | Structured | Visual Calendar & To-Do List | 59 | 10 | day timeline capsules · task editor sheet · AI planner |
| 157 | Tinder | Meet New People & Date Singles | 60 | 10 | swipe deck · action discs · paywall plan cards |
| 163 | Apple Invites | Invite, Plan & Celebrate | 60 | 10 | event page cards · RSVP capsule · intro carousel |
| 169 | Substack | Videos, writing & podcasts | 60 | 10 | notes feed · reader inbox · settings sheet |
| 172 | Adobe Photoshop | Powerful AI Image Editor | 60 | 10 | editor · layers sheet · contextual pills · transform bar |
| 174 | BeReal. | Real photo, no filter | 60 | 10 | black social · dual camera · contact rows |
| 176 | Luminar | Easy picture editing with AI | 60 | 10 | photo editor bands · crop · value capsule |
| 186 | Apple Podcasts | Audio that informs & inspires | 60 | 10 | library root · episode rows · Now Playing (spoken) |
| 187 | Riverside | Video Editor & Recorder | 60 | 10 | recording studio · teleprompter · role cards |
| 193 | Denim | Playlist art, made easy & fun! | 60 | 10 | cover editor · type panel · discs · artwork rails |
| 203 | Dropset | Track your gym workouts | 60 | 10 | live workout list · interval timer · add sheet |
| 204 | Linear | Plan and build your product | 60 | 10 | precise tool · pickers · property chips |
| 209 | Moises | Remove vocals or instruments | 60 | 10 | dark audio · one cyan accent · chord grid |
| 211 | Train Fitness | Auto-tracking for Apple Watch | 60 | 10 | live set logger · workout detail · social feed |
| 212 | SSENSE | Luxury and streetwear brands | 52 | 9 | editorial product page · bag · caps filter screen |
| 213 | PayPal | Savings, cash back, pay later | 60 | 10 | money home · send amount · activity rows |
| 222 | (Not Boring) Camera | Pro Camera with Natural Photos | 34 | 6 | physical-object dark UI · toggle cards · colour grid |
| 226 | Sora | A new video app by OpenAI | 60 | 10 | black video social · replies sheet · profile grid |
| 234 | komoot | Your all-in-one route planner | 60 | 10 | route detail over map · planner · saved list |
| 243 | Playground | Logos, T-Shirts, Posters, etc | 60 | 10 | light editor · floating tool strip · colour picker |
| 257 | Raycast | Productivity on the go | 60 | 10 | light AI notes · capsule header |
| 264 | Netflix | Start Watching | 60 | 10 | dark · red only for brand · radio lists · code entry |
| 265 | ElevenLabs | Text to voice for creators | 60 | 10 | AI voice studio · create hub · script-to-audio editor · picker lists |
| 280 | Apple Books | Read, listen, discover | 60 | 10 | reader page · themes sheet · book detail |
| 292 | WhatsApp | Simple. Reliable. Private. | 60 | 10 | iOS grouped · green · indexed contacts |
| 298 | TIDAL | Music is better on TIDAL | 60 | 10 | dark · glass tab bar · album header |
| 300 | Meta AI | Your personal AI assistant | 60 | 10 | light · drawer · media picker · share sheet |
| 304 | Wispr Flow | Voice dictation & quick notes | 60 | 10 | sign-in · note cards · account cards · serif display |
