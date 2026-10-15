# Pre-registration: Reading direction and screen-side choice in the Moral Machine

Written and committed on 15 Oct 2026, before any outcome variable was examined. Up to this point the only data work was listing the OSF files and reading the dataset README.

## Background
In each Moral Machine dilemma, the two outcomes (the car stays on course vs swerves) are shown side by side on desktop. Which outcome appears on the left is **randomised** (column `LeftHand`). Because of that randomisation, the moral content of a scenario cannot explain any systematic preference for one side, so a side preference is a pure position effect. Work on spatial agency bias and on reading and writing direction suggests that left-to-right (LTR) readers lean toward the left. Right-to-left (RTL) readers show weaker or reversed biases, with the effect usually stronger for Arabic than for Hebrew readers.

## Data
- Source: Awad et al. (2018), OSF project 3hvt2, file `SharedResponsesFullFirstSessions.csv`. It holds each user's first completed session of 13 scenarios, with two rows (outcomes) per scenario.
- Unit of analysis: the scenario (one decision). Users are the independent units.
- Inclusion:
  - `Template == "desktop"` for all confirmatory tests.
  - The scenario has exactly two rows sharing a `ResponseID`, with one `LeftHand = 1` and one `LeftHand = 0`, and exactly one `Saved = 1`.
  - `UserCountry3` is non-missing.

## Outcome
`ClickedLeft = 1` if the user selected the outcome shown on the left. The README says users click the outcome they choose, which kills the characters in it, and that `Saved` is reverse-coded from that click. So the clicked outcome is the row with `Saved == 0`, and `ClickedLeft = 1` when the left-hand row has `Saved == 0`.

## Country groups (fixed in advance)
- **ARABIC** (Arabic is the dominant script and the site had an Arabic interface): DZA, BHR, EGY, IRQ, JOR, KWT, LBN, LBY, MRT, MAR, OMN, PSE, QAT, SAU, SDN, SYR, TUN, ARE, YEM.
- **RTL_OTHER** (native RTL script, but no interface in that language, so these users saw an LTR page): ISR (Hebrew), IRN (Persian), AFG (Dari/Pashto), PAK (Urdu).
- **EXCLUDED, ambiguous**: COM, DJI, SOM, ERI, TCD (Arabic is official but not the dominant literacy script); also missing or unknown codes.
- **LTR**: all other countries.

## Hypotheses
- **H1 (baseline):** desktop users in LTR countries click the left outcome more than half the time, so P(ClickedLeft) > .50.
- **H2 (primary):** P(ClickedLeft) is **lower** in ARABIC countries than in LTR countries.
- **H3 (secondary):** P(ClickedLeft) is lower in RTL_OTHER countries than in LTR countries. We expect the ARABIC gap to be larger, because those users are both native RTL readers and could use an RTL interface.

## Tests
1. **H1:** compute each user's proportion of left clicks over their desktop scenarios, then run a one-sample t-test of these user means against .50 (two-sided α = .05). Also report the decision-level proportion with a user-clustered 95% CI.
2. **H2 (primary):** Welch's t-test on user-level left-click proportions, ARABIC vs LTR (two-sided α = .05). Effect size as a difference in percentage points and as Cohen's d.
   - **Robustness 1, country level:** compute each country's mean left-click rate (countries with ≥ 100 desktop users). Run a Welch t-test and a 10,000-draw permutation test, ARABIC countries vs LTR countries.
   - **Robustness 2, decision level:** a linear probability model ClickedLeft ~ group, with standard errors clustered by user.
   - H2 counts as supported if the primary test is significant in the predicted direction **and** the country-level difference has the same sign.
3. **H3:** same as the primary H2 test, RTL_OTHER vs LTR.

## Comparison condition (secondary, interpretive)
On mobile, outcomes appear one at a time in a carousel, and `LeftHand` marks the outcome shown first, not a screen side. The same ARABIC-vs-LTR comparison on mobile users will be reported separately. If the desktop difference is spatial, we expect the mobile difference to be smaller or absent.

## Exploratory (labelled as such in the write-up)
- **E1:** does the left-click rate change with `ScenarioOrder` (1–13) in each group, for example as fatigue makes position bias grow?
- **E2:** is the position effect different when the user opened the text description (`DescriptionShown`)?
- **E3:** a map or ranked plot of country-level left-click rates.
- **E4:** a re-run of the H1/H2 tests on `SharedResponses.csv` (all sessions), if it fits the compute budget.

## Known limitations, stated in advance
- Country comes from IP and stands in for native script; interface language is not recorded. Expats, VPN users, and Arabic-country users on the English interface will all dilute any effect toward zero.
- The layout check (Arabic page is not mirrored) was done on today's site and may not match 2016–2018.
- These are observational group differences in a randomised-position task. The randomisation rules out content confounds, but not differences in how screens were used across countries, such as browsers, screen sizes or input devices.
