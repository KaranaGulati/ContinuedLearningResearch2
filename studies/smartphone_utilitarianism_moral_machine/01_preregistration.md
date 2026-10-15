# Pre-registration: Do smartphone users make more utilitarian choices in the Moral Machine?

Written and committed on 15 Oct 2026, before any moral-choice outcome was compared across devices. Earlier work on this dataset (the reading-direction study in this repository) looked at left/right clicks by device and at the overall stay rate on desktop only. No device comparison of who was spared has been run.

## Background
Barque-Duran, Pothos, Hampton and Yearsley (2017, *Computers in Human Behavior*, 75, 184 to 193) found that people answering trolley-type dilemmas on a smartphone gave more utilitarian answers than people on a PC: in their first experiment 33.5% vs 22.3% chose to sacrifice one man to save five in a high-conflict dilemma. The effect did not appear in every experiment they ran. Proposed reasons are greater psychological distance and more time pressure on phones. The Moral Machine (Awad et al., 2018) recorded the device for millions of decisions. The original paper checked only that the direction and order of the moral preferences were the same on every device.

## Data
- `SharedResponsesFullFirstSessions.csv` (each user's first completed session), OSF project 3hvt2.
- `SharedResponsesSurvey.csv` for demographics (age, gender, education, income, political and religious sliders), used only in H3.
- Devices compared: `Template` = Desktop vs Mobile. Rows with a missing template are excluded.
- Scenarios 2 to 13 only, for consistency with the reading-direction study (scenario 1 has a fixed layout). All 13 scenarios are a sensitivity check.

## Measure
Utilitarian scenarios are those with `ScenarioType == "Utilitarian"` and `ScenarioTypeStrict == "Utilitarian"`, following the README. In these scenarios one group is the other group plus one to four extra characters. The outcome `SavedMore` is 1 if the user spared the larger group. That is the `Saved` value of the row with `AttributeLevel == "More"`.

`MoreNeedsSwerve` = 1 if sparing the larger group requires the car to swerve. That is the case when the "More" row has `Intervention == 0`, meaning those characters die if the car stays on course.

## Hypotheses
- **H1 (primary):** within the same country, mobile users spare the larger group more often than desktop users.
- **H2:** the mobile advantage is larger when sparing the larger group requires swerving (an action) than when it requires staying on course (inaction). This follows from the trolley framing in Barque-Duran et al., where the utilitarian answer is the one that takes an action.
- **H3:** the mobile advantage in H1 remains after adjusting for age, gender, education, income, political and religious views (survey subset).

## Tests
1. **H1 primary test.** For every country with at least 100 users on each device, compute d_c = P(SavedMore | Mobile) − P(SavedMore | Desktop). Run a one-sample t-test of d_c against 0 across countries (equal weights, two-sided, α = .05).
   - Supporting estimate: a decision-level linear probability model SavedMore ~ Mobile + country fixed effects, with standard errors clustered by user.
   - H1 counts as supported if the primary test is significant with d > 0 and the fixed-effects estimate has the same sign.
2. **H2.** For each country, compute (d_c among MoreNeedsSwerve = 1) − (d_c among MoreNeedsSwerve = 0). Test the mean against 0 across countries with a one-sample t-test. Supporting estimate: the Mobile × MoreNeedsSwerve interaction in the fixed-effects model.
3. **H3.** In the survey subset, a linear probability model SavedMore ~ Mobile + age + gender + education + income + political + religious + country fixed effects, with standard errors clustered by user. Users who left a question at its default are coded as missing for that question and dropped from H3. The default is "default" for categorical questions and exactly 0.5 for the sliders. The test is the Mobile coefficient (two-sided α = .05).
4. **Equivalence.** If H1 is not supported, run a two one-sided tests (TOST) procedure on the fixed-effects Mobile estimate with a smallest effect of interest of ±2 percentage points. A 2-point effect is about one fifth of the effect reported by Barque-Duran et al.
5. **Descriptive.** Raw Mobile vs Desktop rates, a user-level Welch t-test without country adjustment, and the same analysis on all 13 scenarios.

## Exploratory (labelled as such)
- Device differences for the other Moral Machine preferences: age, gender, fitness, social status, species, pedestrians vs passengers, and law-abiding vs not.
- Whether opening the text description changes the device gap.
- Which countries show the largest gaps.

## Known limitations, stated in advance
- Device is self-selected and not randomised. Country fixed effects and the H3 demographics adjust for some differences between phone and desktop users, but not all of them.
- The mobile interface differs from the desktop one. It shows one outcome at a time in a carousel with "stay" and "swerve" buttons, while desktop shows two pictures side by side. Any device difference is the combined effect of device and interface, and this study cannot separate them.
- These are Moral Machine dilemmas, which are impersonal (the car does the harm). Barque-Duran's effect was strongest in personal, high-conflict dilemmas like the footbridge case, so a smaller effect is expected here.
