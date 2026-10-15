# Moral Machine: what has already been done (checked 15 Oct 2026)

## The data
- OSF project: https://osf.io/3hvt2/ (Awad et al. 2018). The files are `SharedResponses.csv` (3.2 GB compressed), `SharedResponsesFullFirstSessions.csv` (1.6 GB), `SharedResponsesSurvey.csv` (0.3 GB) and `CountriesChangePr.csv`.
- The columns, read from `MMdata_ReadMe.txt`:
  - IDs: `ResponseID`, `ExtendedSessionID`, `UserID`.
  - Scenario structure: `ScenarioOrder` (1–13), `Intervention`, `PedPed`, `Barrier`, `CrossingSignal`, `AttributeLevel`, `ScenarioType` / `ScenarioTypeStrict`, `DefaultChoice`, `NonDefaultChoice`, `DefaultChoiceIsOmission`.
  - Characters: `NumberOfCharacters`, `DiffNumberOFCharacters`, and counts for 20 character types.
  - Choice and context: `Saved` (the decision), `Template` (desktop/mobile/tablet), `DescriptionShown`, `LeftHand` (screen side), `UserCountry3`.
  - The survey file adds age, education, gender, income, political and religious ratings.
- **Not in the public data:** timestamps or dates, response times, the order of a user's sessions (other than "first completed session"), and the survey-before-or-after-results flag.

## Already studied (crowded)
| Area | Key work |
|---|---|
| Global preferences, 3 cultural clusters, country correlates (Gini, individualism), demographics | Awad et al. 2018, *Nature* — https://www.nature.com/articles/s41586-018-0637-6 |
| Trolley variants across 42 countries, relational mobility | Awad et al. 2020, *PNAS* — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7007553/ |
| Robustness to scenario order, left/right position, device (direction and order of effects "stable"); effects larger when the description is read | Awad et al. 2018 SI; summarised in https://dspace.mit.edu/bitstream/handle/1721.1/125065/Moral%20Machine%20Paper.pdf |
| Forced-choice critique (adding an "equal" option) and reply | Bigman & Gray 2020, *Nature*; coverage https://techxplore.com/news/2020-03-moral-machine-reexamined-forced-choice-reveal.html |
| Conceptual and probability critiques | Etienne 2021 (*Law, Innovation and Technology*); "The probability problems of the Moral Machine Experiment", *AI & Ethics* 2023 — https://link.springer.com/article/10.1007/s43681-023-00287-4 |
| Computational and cognitive models fitted to MM data | Kim et al. 2018 — https://arxiv.org/pdf/1801.04346; Noothigattu et al. 2018 (voting-based) — https://arxiv.org/pdf/1709.06692; Agrawal, Peterson & Griffiths 2020 *PNAS* — https://arxiv.org/pdf/1910.07581 |
| LLMs vs humans (very crowded 2023–26) | Takemoto 2024 *RSOS* — https://royalsocietypublishing.org/doi/10.1098/rsos.231393; Jin et al. MultiTP, ICLR 2025 — https://arxiv.org/abs/2407.02273v3; persona alignment — https://arxiv.org/pdf/2504.10886; LLM robustness — https://royalsocietypublishing.org/rsos/article/12/4/241229/235626/Robustness-of-large-language-models-in-moral; IRL — https://arxiv.org/pdf/2312.17479 |
| Small replications | US/Denmark (Frank et al. 2019, *Sci Rep*) — https://pmc.ncbi.nlm.nih.gov/articles/PMC6739396/; EEG 2025 — https://www.nature.com/articles/s41598-025-99531-6 |

## Not found (open angles that the public columns support)
1. **Do smartphones make people more utilitarian?** Barque-Duran et al. (2017, *Computers in Human Behavior*) found smartphone users more utilitarian in high-conflict dilemmas (33.5% vs 22.3%), but the effect did not hold up across all of their experiments. Moral Machine records device for millions of decisions. The original paper only checked that the *direction* of effects was stable across devices and never tested a difference in size.
2. **Reading direction and side bias.** Do users in right-to-left script countries (Arabic-speaking countries, Israel, Iran, Pakistan) favour the right-hand outcome more than left-to-right users? This comes from spatial-agency-bias theory, and the original paper treated `LeftHand` only as a robustness check.
3. **Repeat participation.** Within the same users, how do first sessions differ from later ones? Moral Machine shows each user a summary comparing them with others after every session. Effects that grow stronger would suggest learning or reflection; effects that weaken would suggest boredom or random clicking. No study of repeat behaviour in MM was found.
4. **Deliberation within the same person.** For each user, compare scenarios where they opened the text description with scenarios where they didn't. The original reports larger effects among description readers, but only across users.

Caveat: this was a targeted search (about 15 queries plus the OSF data dictionary), not a systematic review. Before writing, search Google Scholar's "cited by" list for the 2018 *Nature* paper (several thousand citations) using each angle's keywords.

## Novelty check for angle 2: reading direction and screen-side choice (15 Oct 2026)

**Verdict:** I found no study that tests whether right-to-left readers choose differently by screen side in the Moral Machine data. I also found none that tests reading direction against moral-dilemma choices at all. This search can't prove that nobody has done it, but nothing turned up across about 10 targeted web searches and a read of the original supplement.

**What exists, and how we differ:**
- **Awad et al. 2018 supplement.** The left/right position of the two outcomes was "switched randomly, so as to avoid any bias from handedness". The only position analysis checks that each preference's effect size is the same whether the outcome was shown on the left or the right. They never report the overall rate of choosing the left option, and never break it down by country or by script. https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-018-0637-6/MediaObjects/41586_2018_637_MOESM1_ESM.pdf
- **Spatial agency bias.** Maass & Russo 2003, plus Italian–Malagasy–Arabic comparisons: people place the agent of an action in their script's reading direction. These are drawing and description tasks, not choices. https://www.researchgate.net/publication/258500500_What_Drives_the_Spatial_Agency_Bias_An_Italian-Malagasy-Arabic_Comparison_Study
- **Review of reading-direction effects** (*Psychonomic Bulletin & Review*, 2023): the effects in right-to-left readers are mixed. Arabic readers are usually reversed; Hebrew readers are weaker or mixed, probably because of exposure to English. https://link.springer.com/article/10.3758/s13423-022-02239-1
- **"Heading Right and Judging Harsher"** (*Social Psychology*, vol. 48, no. 5): rightward spatial orientation makes moral judgments harsher. It uses a lab manipulation and does not compare scripts. https://econtent.hogrefe.com/doi/10.1027/1864-9335/a000316
- **Lateral aesthetic preference by reading direction** (Hebrew/Arabic vs Russian; one Arabic–English study found no difference). https://link.springer.com/article/10.1007/s40167-018-0062-6

**Design checks before running anything:**
1. **Mobile layout.** The supplement says the profiles are "left vs. right in the desktop interface", while on mobile `LeftHand` marks the default position. So the main analysis should use only `Template == "desktop"`.
2. **Mirrored Arabic interface.** An Arabic version existed, and Arabic was one of the 9 added languages. If that version mirrored the layout, `LeftHand` might record the code's ordering rather than the side the user saw. Check the site's Arabic page, or ask the authors, before interpreting results.
3. **Country stands in for script.** The data records country, not the interface language or the user's script. Use countries whose dominant script reads right to left (Arabic-speaking states, Israel, Iran, Pakistan, Afghanistan). Keep Israel/Hebrew separate, since prior work says its effect is weaker.
4. **Final check before writing.** Run Google Scholar's "cited by" search on the 2018 *Nature* paper with "reading direction", "left", "script" and "Arabic", and check recent preprints (PsyArXiv, OSF).
