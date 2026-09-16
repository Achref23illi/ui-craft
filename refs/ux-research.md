# UX research — fewer taps, labelled icons, the right typeface

Compiled September 2026 from primary sources and practitioner threads. Each finding
carries its source so it can be checked. By Achref Arabi.

## 1 · How many choices a screen may offer

- **Five or fewer main choices per screen.** W3C's cognitive accessibility pattern
  "Avoid too much content": "Provide users with five or less main choices on each
  screen and remove unnecessary content"; extras go behind a clearly named "more".
  https://www.w3.org/WAI/WCAG2/supplemental/patterns/o5p03-manageable-quantity/
- **One primary action per screen state.** Design systems converge on it (eBay
  Playbook, EU component library): "There should only be a single primary action
  per screen." https://playbook.ebay.com/design-system/components/cta-button
- **Progressive disclosure, two levels maximum.** Nielsen Norman Group: show the
  few most important options first; "designs that go beyond 2 disclosure levels
  typically have low usability because users often get lost when moving between
  the levels." Choose the split from frequency of use, not from what is possible.
  https://www.nngroup.com/articles/progressive-disclosure/
- **Similar buttons side by side spike cognitive load.** UX Movement: when two
  choices look alike users "debate in their head which button they should click"
  and hesitate. Make the primary visually dominant, demote the rest to text.
  https://uxmovement.substack.com/p/how-to-make-similar-button-choices
- **Hick's law in practice**: group, prioritise the frequent option, break a task
  into steps (IKEA and Apple checkouts), reveal the rest on request.
  https://blog.logrocket.com/ux-design/using-hicks-law-help-users-make-decisions/
- **Fewer decisions beat fewer taps.** A six-screen flow with zero ambiguous
  choices outperforms a two-screen flow with three unclear decisions
  (onboarding practitioners, 2026). Activation, not tap count, predicts retention.
  https://www.aaronmallen.com/2026/07/22/how-to-design-a-mobile-app-onboarding-flow-that-reduces-drop-off/
- **Options live next to the feature they affect**, not in one giant options
  screen (UX StackExchange, 19-vote answer): "put the options with the feature it
  affects." And the 127-vote answer warns not to slim down so far that power users
  cannot find a setting: keep a searchable full list behind the simple one.
  https://ux.stackexchange.com/questions/115414/is-it-possible-to-make-a-good-options-dialog
- Yale usability: 5–7 top-level navigation items, hide extras under "more".
  https://usability.yale.edu/ux/best-practices/less-is-more

## 2 · Icons need labels

- **Only three icons are near-universal**: home, print, search magnifier. "A user's
  understanding of an icon is based on previous experience" and "a text label must
  be present alongside an icon." Do not rely on hover or long-press to reveal it.
  Nielsen Norman Group. https://www.nngroup.com/articles/icon-usability/
- **Eleven studies, five companies, 19 years, same result**: users fail to match
  icons to commands; experienced users rely on position, not recognition, and are
  lost when icons move. "Icons without labels simply don't work." Trevor Calabro.
  https://trevorcalabro.substack.com/p/every-icon-needs-a-label
- **Icon + label has the highest recall and lowest error rate**; text is processed
  holistically, icons are an app-specific language users must learn. Christopher
  Butler, "In Defense of Text Labels", and the Hacker News thread on it (the most
  upvoted line: "Icons are optional. Text is required.").
  https://www.chrbutler.com/in-defense-of-text-labels ·
  https://news.ycombinator.com/item?id=43142989
- Hacker News, "The best icon is a text label" and "The Dilemma of Icons": even the
  print and trash icons had to be learned; pencil means create, edit, write or
  draw; when in doubt skip the icon. https://news.ycombinator.com/item?id=10757842 ·
  https://news.ycombinator.com/item?id=37245530
- **The filter funnel is "on the verge" of universal, still label it** (UX
  StackExchange, 33-vote answer). "Letters are still the symbols with the least
  ambiguity." https://ux.stackexchange.com/questions/134929/
- **Where icons may stand alone**: the universal three, the back chevron, the ×
  close, and a repeated per-row action once the first instance was labelled; and
  tab bars must carry labels (Apple HIG, Material 3, NN/g).
- Counter-view worth knowing: UX Movement argues frequently used icons can lose
  their label once learned. Apply only to power-user tool rows, never to
  navigation. https://uxmovement.substack.com/p/why-you-shouldnt-always-label-your

## 3 · Tap targets

- Steven Hoober's measurements, via Smashing Magazine: precision is worst at the
  top and bottom edges; 44×44 pt minimum everywhere, 48×48 for sticky and edge
  controls, and padding between neighbours so a miss lands on nothing. "Rage taps"
  come from undersized, edge-placed or hover-dependent controls.
  https://www.smashingmagazine.com/2023/04/accessible-tap-target-sizes-rage-taps-clicks/

## 4 · Typeface for a mobile UI

- The traits that matter at small sizes: high x-height, open apertures, clear
  letterforms, tabular figures, at least five weights, ideally a variable font.
  Body 16 with 1.5 line height; display 1.0–1.25; limit to one family, two at most.
  Untitled UI, "31 best free fonts for UI" (2026).
  https://www.untitledui.com/blog/best-free-fonts
- Inter is the default tell of generated and template UI; alternatives designers
  now reach for: Satoshi (editorial, premium), Geist (technical), Switzer
  (neutral), Mona Sans (industrial), Public Sans (civic, invisible), Figtree
  (warm consumer), Plus Jakarta Sans (approachable, bright), Onest (closest free
  substitute for SF Pro), General Sans (compact, for dense mobile UI).
  https://superfiles.in/7-clean-alternatives-to-inter-font.php
- Platform reality: the apps in the ui-craft library overwhelmingly use the system
  face (SF Pro / Roboto) or a bespoke brand face (Spotify Circular, Airbnb Cereal,
  Netflix Sans). A free Google face with Expo packages is the honest middle: it
  reads as designed without the licence.
- Packages that exist for Expo (`@expo-google-fonts/*`): plus-jakarta-sans,
  figtree, dm-sans, onest, manrope, geist, public-sans, work-sans, hind, lexend.
  Satoshi, Switzer and General Sans are Fontshare files loaded with expo-font.

## 5 · Icon systems for React Native

- `@expo/vector-icons` is being deprecated by Expo; the guide points to
  `@react-native-vector-icons` or SVG sets. https://docs.expo.dev/guides/icons/
- SVG sets with React Native packages and one consistent grid: Lucide
  (`lucide-react-native`, 1,500 icons, single 2-px stroke, tree-shakable), Phosphor
  (`phosphor-react-native`, six weights: thin, light, regular, bold, fill, duotone,
  which gives outline-inactive / fill-active tab bars for free), Tabler
  (`@tabler/icons-react-native`), Hugeicons (`@hugeicons/react-native`, paid tiers).
- Rule from the platform guides: tab bar 3–5 destinations, icon + label, the
  active item filled or tinted, never actions in the tab bar (Apple HIG tab bars;
  Material 3 navigation bar; Nick Babich on bottom navigation).
  https://uxplanet.org/perfect-bottom-navigation-for-mobile-app-effabbb98c0f

## What this changes in the skill

- Rule 11, the tap budget: at most five tappable choices in the first viewport
  besides the tab bar and back; one primary; everything else behind one clearly
  named "more" at most two levels deep.
- Rule 12, labels: every icon that triggers an action carries a visible label,
  except back, close, search and home; tab bars always labelled.
- Font and icon recommendations in the measurements table.
