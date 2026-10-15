# Polymarket Data: Forecast Accuracy, Calibration, Market Efficiency, and Elections (2020 – Oct 2026)

Scope note: research conducted 2026-10-15. Most rigorous Polymarket-specific work is very recent: 2025–2026 working papers and preprints on arXiv, SSRN, SocArXiv and NBER. Almost none of it is peer-reviewed yet. Dates below are arXiv/SSRN posting or revision dates. SSRN abstract pages returned HTTP 403 to my fetcher, so SSRN-only findings come from secondary summaries (search snippets, seminar pages, press) and are marked **[secondary]**. Adjacent topics (microstructure, wash trading, insider trading, datasets, AI forecasting) have separate notes files in this folder. They appear here only where they bear on accuracy or efficiency.

### Master index (quick reference)

| # | Authors | Title (short) | Venue / date | Data | Headline |
|---|---|---|---|---|---|
| 1 | Reichenbach & Walther | When Can Prediction Market Prices Be Trusted? | SSRN 7552098, ~Oct 2026 | 1.5B trades, 779k markets | Prices informative, improve with maturity; no general longshot bias; matches bookmakers in sports [secondary] |
| 2 | Reichenbach & Walther | Exploring Decentralized Prediction Markets: Accuracy, Skill, and Bias on Polymarket | SSRN 5910522, Dec 2025 | Polymarket | Prices track realized probabilities; slightly beat bookmaker odds [secondary] |
| 3 | Cardozo & Rivero-Wildemauwe | The Favorite-Longshot Bias in Prediction Markets: Evidence from Polymarket | arXiv 2609.12878, 11 Sep 2026 | 588M trades, 2.48M accounts | <10¢ buys lose 19.3¢/$; ≥90¢ earn 0.83¢/$; sign depends on grouping |
| 4 | Nam Anh Le | Decomposing Crowd Wisdom | arXiv 2602.19520, Feb 2026 (v2 Aug 2026) | 353M trades, 429k contracts (Kalshi + Polymarket) | Political markets underconfident (compressed toward 50%), replicated on Polymarket |
| 5 | Qin & Yang | Polymarket-v1 Database | arXiv 2606.04217, Jun 2026 | 1.20B trades, 1.30M markets, Nov 2022–Apr 2026 | "Favorite-longshot reversal"; VPIN/spread predict Brier |
| 6 | Clinton & Huang | Prediction Markets? The Accuracy and Efficiency of $2.4 Billion in the 2024 Presidential Election | SocArXiv d5yx2, 1 Dec 2025 | >2,500 markets, IEM/Kalshi/PredictIt/Polymarket, final 5 weeks of 2024 | Better than coin flip: PredictIt 93%, Kalshi 78%, Polymarket 67%; arbitrage on 62 of 65 days |
| 7 | Ng, Peng, Tao & Zhou | Price Discovery and Trading in Modern Prediction Markets | SSRN 5331995, Jul 2025 (rev. Apr 2026) | Polymarket, Kalshi, PredictIt, Robinhood | Liquid markets beat polls; Polymarket leads Kalshi; large-trade imbalance predicts returns [secondary] |
| 8 | Aktuğ & Torul | Price Discovery Across Political Prediction Markets | Working paper, Jun 2026 | 9 venues, 5-min data, Jan–Nov 2024 | Polymarket + Betfair ≈85% of information share; led S&P futures on election night |
| 9 | Tsang & Yang | The Anatomy of a Blockchain Prediction Market | arXiv 2603.03136, Mar 2026 (v3 Sep 2026) | Full on-chain ledger, 249 markets | Naive volume overstated ~2.5×; whale = 15.1% of Oct net inflow; heterogeneous beliefs, not one-sided manipulation |
| 10 | Tsang & Yang | Political Shocks and Price Discovery | arXiv 2603.03152, Mar 2026 (v4 Jul 2026) | On-chain, 3 shocks of 2024 | Debate repricing reversed; assassination-attempt repricing persisted |
| 11 | Saiegh | Forecasting the 2024 U.S. Presidential Election | UCSD working paper (undated, 2025) | Daily, 4 Oct–5 Nov 2024 | Polymarket overestimated Trump and was most volatile; S&P options most accurate |
| 12 | Cutting et al. | Are Betting Markets Better than Polling? | arXiv 2507.08921, Jul 2025 | Polymarket vs polls, 2024 | Polymarket better than polls, esp. swing states (no numbers in abstract) |
| 13 | Sethi et al. | Political Prediction and the Wisdom of Crowds | ACM CI '25, Aug 2025 | 41 Nov 2024 outcomes, 3 models vs 1 market | Models failed to beat the market on the presidency; beat it on down-ballot races |
| 14 | Gómez-Cram, Guo, Kung & Jensen | Prediction Market Accuracy: Crowd Wisdom or Informed Minority? | SSRN, Apr 2026 | 1.72M accounts, 210k markets, $13.76B, 2023–2025 | 3.14% of accounts are skilled and drive accuracy [secondary] |
| 15 | Mitts & Ofir | From Iran to Taylor Swift: Informed Trading in Prediction Markets | SSRN 6426778, 2026 | ~93k markets, ~50k wallets, Feb 2024–Feb 2026 | 210,718 flagged wallet-market pairs; 69.9% win rate; ~$143M anomalous profit |
| 16 | Deleep et al. | How Wise is the Crowd? Bias and Edge in Prediction Markets | SSRN 6322678, 2026 | Polymarket + Kalshi, "Mention Markets" | Longshot bias is an artifact; real effect is a "Yes bias"; whales lose to small traders [secondary] |
| 17 | Fabi, Marfè, Ruffo & Schönleber | Are Decentralized Prediction Markets Efficient? Evidence from Bitcoin Options | FC'26 DeFi workshop talk, 2026 | 255 BTC bets, Mar 2024–May 2025 | Tracks options benchmarks (ρ 0.73–0.97); tail events overpriced |
| 18 | Saguillo, Ghafouri, Kiffer & Suarez-Tangil | Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets | AFT 2025 / arXiv 2508.03474 | Markets resolved Apr 2024–Apr 2025 | ~$40M realized arbitrage profit |
| 19 | Gebele, Mutzel & Matthes | Executable Arbitrage and Market Efficiency in Prediction Markets | arXiv 2608.00666, Aug 2026 | NegRisk markets | ~$1.12M arbitrage profit; YES-side violations persist |
| 20 | Cheng, Yang & Zou | Arbitrage Analysis in Polymarket NBA Markets | arXiv 2605.00864, Apr 2026 | 75M LOB snapshots, 173 NBA games | Single-market arbitrage very rare (7 episodes, median 3.6 s) |
| 21 | Ibrahim & Zaki | Price Dislocations, News Citations, and Epistemic Leverage on Polymarket | arXiv 2609.06005, Sep 2026 | 173.7M trades; 6,990 news articles | ~$0.7–1.0M needed to move a market 5 pp and get the move cited |
| 22 | Zitzewitz | Are Prediction Markets Politically Biased? | NBER w35846, Oct 2026 | 1880–2025, **Polymarket not yet included** | No partisan bias; favorite-longshot bias common |
| 23 | Polymarket (company) | Accuracy page | polymarket.com/accuracy, accessed Oct 2026 | Resolved markets | 90.4% at 1 month to 98.7% at 4 h; Brier 0.059 |
| 24 | JohnLeslie_PM | Empirical calibration of Polymarket (7,661 markets) | LessWrong, 28 Apr 2026 | 7,661 binary markets | Brier 0.042 (30d) → 0.032 (7d) → 0.025 (24h) |
| 25 | wasabipesto | Brier.fyi / Calibration City | Web dashboard, ongoing | Kalshi/Manifold/Metaculus/Polymarket | No platform wins on all topics [secondary] |
| 26 | Sirolly, Ma, Kanoria & Sethi | Network-Based Detection of Wash Trading | SSRN 5714122, Nov 2025 | 1.26M wallets | ~25% of volume is wash trading; ~17% in election markets |

---

## Q1. What studies measure Polymarket calibration, Brier scores, and accuracy (by time to resolution, category, liquidity), and what did they find?

### Takeaway
Large-sample studies agree that Polymarket prices are informative and broadly well calibrated in aggregate. Polymarket's own figures put the Brier score at about 0.06, with accuracy rising from about 90% one month out to about 99% four hours out. Calibration depends on the setting, though. It improves as a market matures and nears resolution, it varies by category (weather best; mentions and geopolitics worst), and political markets are persistently underconfident, with prices compressed toward 50%. Whether thin markets are worse depends on how liquidity is measured.

### Cited Findings
**Large-sample academic studies**
- **Reichenbach & Walther (2026), "When Can Prediction Market Prices Be Trusted? Price Informativeness, Calibration, and Bias on Polymarket," SSRN 7552098 (posted ~early Oct 2026, preprint)** [secondary: abstract seen via search, full text not accessed]:
  - Data: 1.5 billion trades across 779,000 Polymarket markets.
  - Prices are highly informative, and informativeness improves with market maturity.
  - Accuracy is category-dependent: weather markets are most precise, mentions and geopolitics markets least precise.
  - There is no general longshot bias (see Q4).
  - In sports, Polymarket matches professional bookmakers' accuracy, but live trading shows temporary distortions when news arrives fast.
  - [SSRN listing](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7552098)
- **Reichenbach & Walther (Dec 2025), "Exploring Decentralized Prediction Markets: Accuracy, Skill, and Bias on Polymarket," SSRN 5910522** [secondary]: the earlier version reported that market prices closely track realized probabilities and slightly outperform bookmaker odds — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5910522)
- **Nam Anh Le, "Decomposing Crowd Wisdom: Domain-Specific Calibration Dynamics in Prediction Markets," arXiv 2602.19520 (v1 23 Feb 2026; v2 4 Aug 2026)** — [arXiv](https://arxiv.org/abs/2602.19520):
  - Data: 353 million trades on 429,000 binary contracts across Kalshi and Polymarket.
  - Method: decomposes cell-level logistic recalibration slopes; Bayesian measurement-error model; market- and event-clustered bootstraps.
  - The decomposition explains 87.3% of in-sample variance on Kalshi and 71.5% out of sample.
  - The most robust result is persistent **underconfidence in political markets**, with prices compressed toward 50%. This replicates on Polymarket.
  - Large political trades on Kalshi go with further compression (a calibration-slope gap of about one half), but this is not robust on Polymarket.
  - Roughly half of raw slope variation is estimation noise.
  - Conclusion: "calibration is conditional" on what, when and how much is traded.
- **Qin & Yang, "Polymarket-v1 Database," arXiv 2606.04217 (2 Jun 2026; v2 8 Jun 2026)** — [arXiv](https://arxiv.org/abs/2606.04217):
  - Data: complete on-chain archive of the first-generation CTF Exchange, 21 Nov 2022 to 28 Apr 2026. 1.20 billion trades, 1.30 million markets, $61B nominal volume, with ground-truth aggressor side.
  - Forecast-quality results: true VPIN positively predicts Brier scores (more toxic flow, worse forecasts). Gibbs spread *negatively* predicts Brier scores; the authors attribute this to high-spread niche markets attracting informed specialists.
  - Using classified proxies instead of ground truth weakens both relationships.
  - Tick-rule accuracy is 49.83% and BVC 50.51%, close to random.
- **Gómez-Cram, Guo, Kung (LBS) & Jensen (Yale), "Prediction Market Accuracy: Crowd Wisdom or Informed Minority?" SSRN (posted 20 Apr 2026, revised 25 Apr 2026)** [secondary, via press] — [The Block](https://www.theblock.co/post/398902/skilled-polymarket-traders-are-a-3-minority-and-everyone-else-funds-their-gains-study):
  - Data: every Polymarket trade 2023–2025. 1.72M accounts, 210,322 markets, ~$13.76B volume.
  - Method: sign-randomization test (10,000 random flips per trader), validated on held-out events.
  - 3.14% of accounts are "skilled winners."
  - Skilled winners plus market makers (<3.5% of accounts) capture more than 30% of gains.
  - About 67% of accounts (unlucky or unskilled losers) absorb the entire loss pool.
  - 44% of skilled accounts stay skilled out of sample, versus ~10% for active mutual funds.
  - Accuracy reflects "the wisdom of an informed minority, not the wisdom of the crowd."
  - 1,950 single-event "insider-like" accounts move prices 7–12× more per dollar than skilled traders, but are too isolated to drive aggregate accuracy.
- **Clinton & Huang (2025), log-skill and Brier accuracy, 2024 election markets** (details in Q2) — [SocArXiv/IDEAS](https://ideas.repec.org/p/osf/socarx/d5yx2_v1.html):
  - On accuracy correlates, the (logged) number of trades is unrelated to accuracy once exchange and contract type are controlled for.
  - "Political Speech" (mention) markets were least accurate: 62% better than a coin flip.
  - Descriptively, less accurate markets were thinner. About $198M traded on markets worse than a coin flip, versus more than $2.2B on more accurate ones.
  - [Full text PDF](https://osf.io/download/692db7dd37baa6ac72b550fb/)

**Platform and industry dashboards**
- **Polymarket official accuracy page (accessed Oct 2026)** — [polymarket.com/accuracy](https://polymarket.com/accuracy):
  - Accuracy (leading outcome matched the result): 98.7% at 4h, 97.3% at 12h, 96.6% at 1d, 94.2% at 1 week, 90.4% at 1 month before resolution.
  - Overall Brier 0.059; the horizon is not stated.
  - A Brier-vs-volume chart spans <$1K to $1M+, but per-bin values are not shown.
  - Resolution mix: 21.9% Yes, 78.1% No. Market count and date range are not disclosed.
  - An unofficial mirror snapshot showed 90.1% at 1 month and Brier 0.0627 ([mirror](https://polymarket.206.189.21.72.sslip.io/accuracy)), so the figures update over time.
- **Alex McCullough Dune dashboard (cited by Polymarket's accuracy page)** [secondary] — [pm.wiki entry](https://pm.wiki/zh/projects/alexmccullough), [The Defiant](https://thedefiant.io/news/research-and-opinion/polymarket-is-up-to-94-accurate-in-predicting-outcomes-analysis):
  - About 90% accurate one month out and about 94% at 4 hours.
  - "Persistent Yes-outcome bias on longshots" (2025).
  - Per search summaries, the headline figures exclude markets priced >90% or <10%, and accuracy is lower in sports markets because head-to-head sports lack longshots. I could not open the Blockworks article to verify this.
  - The Blockworks write-up says the Brier score uses prices one day before resolution ([Blockworks](https://blockworks.co/news/predicting-trading-insights), 403, unverified).
- **"Empirical calibration of Polymarket: analysis of 7,661 markets," LessWrong user JohnLeslie_PM, 28 Apr 2026** — [LessWrong](https://www.lesswrong.com/posts/Hruc6Gwo3vBZFGb6v/empirical-calibration-of-polymarket-analysis-of-7-661):
  - Data: 7,661 resolved binary markets from the Gamma API with CLOB price history; ~2,000 had enough price history for horizon analysis.
  - Calibration at the extremes:
    - 0–5% bucket (n=5,693) resolved YES 0.1% (expected ~2.5%).
    - 95–100% bucket (n=1,209) resolved 100%.
  - Brier by horizon: 0.042 at 30d, 0.032 at 7d, 0.025 at 24h.
  - Mid-range buckets have small n (e.g., 65–75% bucket n=29 resolved 96.5%).
  - A commenter notes the "expected" column assumes uniform spread within buckets.
  - Informal, not peer-reviewed.
- **Brier.fyi / Calibration City (wasabipesto)** [secondary; site returned HTTP 530] — [Manifund project page](https://manifund.org/projects/calibration-city):
  - Cross-platform calibration across Kalshi, Manifold, Metaculus and Polymarket.
  - One month before close, 62% of markets were within 30 pp of the correct resolution (Brier ≈ 0.09).
  - No platform wins on every topic. Kalshi narrowly leads overall; Kalshi and Polymarket do well on sports, Metaculus on science.
- **"Polymarket Calibration Analysis Across 4 Domains,"** Laidlaw Scholars post (student work; not opened) — [link](https://laidlawscholars.network/posts/polymarket-calibration-analysis-across-4-domains)

### Inferences
- Headline accuracy and Brier numbers are flattered by the base rate. 78% of Polymarket markets resolve No, and the 0–5% bucket alone holds ~74% of markets in the LessWrong sample. "Leading outcome correct" rates of 90–99% largely reflect many near-certain markets. Informative comparisons condition on category, price bucket and horizon, as Le (2026) and Reichenbach & Walther (2026) do.
- The liquidity–accuracy link is not monotonic. Clinton & Huang find trade count is unrelated to accuracy once controls are added. Qin & Yang find wide-spread niche markets can be *more* accurate. Polymarket's own chart only shows Brier by volume bin.
- The informed-minority result (Gómez-Cram et al.) and the insider-trading screens (Mitts & Ofir) suggest that part of Polymarket's accuracy comes from concentrated, sometimes privileged information rather than diffuse crowd wisdom.

### Gaps
- The full texts of Reichenbach & Walther (both SSRN papers) were inaccessible (SSRN 403). Their exact Brier values, category tables and sports-bookmaker comparison are unverified.
- No peer-reviewed journal article on Polymarket calibration was found as of Oct 2026.
- Polymarket's accuracy page does not disclose N, date range, or the horizon behind its Brier score.
- Brier.fyi's current platform-level numbers could not be retrieved (site down).

---

## Q2. Which studies compare Polymarket with polls, PredictIt, Kalshi, Betfair, Metaculus, Manifold, or expert forecasts (2020, 2022, 2024 and later)?

### Takeaway
The evidence is mixed and depends on the event. On the 2024 headline presidential contract, Polymarket beat polls and poll-based models, and it led price discovery with Betfair, ahead of Kalshi and sportsbooks. Across the full cross-section of 2024 political contracts, however, Polymarket was the *least* accurate of PredictIt, Kalshi and Polymarket (unadjusted). Prices diverged persistently across venues, and statistical models beat markets on down-ballot races. In the 2022 midterms, one log-score comparison ranked Polymarket below FiveThirtyEight and Metaculus.

### Cited Findings
**2024 cross-venue and poll comparisons**
- **Clinton (Vanderbilt) & Huang, "Prediction Markets? The Accuracy and Efficiency of $2.4 Billion in the 2024 Presidential Election," SocArXiv d5yx2_v1, dated 1 Dec 2025** — [IDEAS](https://ideas.repec.org/p/osf/socarx/d5yx2_v1.html); [PDF](https://osf.io/download/692db7dd37baa6ac72b550fb/):
  - Data: more than 2,500 political markets on IEM, Kalshi, PredictIt and Polymarket, final five weeks of the 2024 campaign. About $2.4B was wagered 1 Sep to Election Day. The accuracy analysis uses the 1,237 markets active on 4 Nov 2024; IEM is excluded because it had only 4 contracts.
  - Method: log-skill score (Brier in the appendix) relative to a coin flip; OLS of accuracy on exchange, log volume, days to election, and hand-coded contract type.
  - Share of markets better than a coin flip: **PredictIt 93%, Kalshi 78%, Polymarket 67%**.
  - The text cautions that exchange differences may reflect contract mix.
  - Accuracy by contract type: national presidential contracts 82% of 72 better than a coin flip; state presidential 72%; state non-presidential 71%; political speech 62%.
  - The Figure 1 panel labels show 27.9%/22%/6.9% of markets with log-skill < 0. These do not map exactly onto the abstract's 67/78/93%, so I could not reconcile the panel order or sample.
- **Ng, Peng, Tao & Zhou, "Price Discovery and Trading in Modern Prediction Markets," SSRN 5331995 (posted Jul 2025; revised Apr 2026)** [secondary, via search snippets, seminar abstracts and a citing paper] — [SSRN](https://papers.ssrn.com/abstract=5331995); [RUC seminar abstract](https://en.rmbs.ruc.edu.cn/Media/Seminars/cf4d5bbb42da4fac808ba83cbe692759.htm):
  - Data: common contracts on Polymarket, Kalshi, PredictIt and Robinhood.
  - More liquid markets "substantially outperform polls" in predicting 2024 results, but large price disparities persist across platforms.
  - Polymarket leads Kalshi in price discovery, especially when liquidity and activity are high.
  - Large-trade net order imbalance predicts returns.
  - In matched 2023–2026 markets, Kalshi leads in sports and Polymarket in politics and entertainment, including when insider-trading risk is high.
  - Method per Aktuğ & Torul: a 30-minute return VAR.
- **Aktuğ (Sabancı) & Torul (Boğaziçi), "Price Discovery Across Political Prediction Markets: Evidence from the 2024 U.S. Presidential Election," working paper, June 2026** — [PDF](https://web.bogazici.edu.tr/torul/pridis.pdf):
  - Data: 5-minute implied probabilities for "Trump wins" on 9 venues (Polymarket, Betfair, Kalshi, 6 dealer sportsbooks), Jan–Nov 2024.
  - Method: Hasbrouck information share, Gonzalo–Granger component share, Putniņš information leadership share (VECM).
  - Polymarket and Betfair jointly hold ~85% of information share (Polymarket IS midpoint 47.5%). No sportsbook exceeds 11%.
  - Leadership between the exchanges depends on horizon (Polymarket leads at the 5-minute horizon).
  - Kalshi reached nontrivial share within 32 days of listing.
  - Average cross-venue spread was 6.2 pp.
  - Polymarket's $3.6B in election volume is noted.
  - The prediction-market consensus led S&P 500 futures through election night and Trump Media equity across the overnight gap, and it priced the two weekend shocks.
  - The authors caution their design cannot fully separate venue organization from attention and liquidity.
- **Saiegh (UC San Diego), "Forecasting the 2024 U.S. Presidential Election: Financial Markets Trump Opinion Polls and Prediction Markets," working paper (undated; cites 2025 work)** — [PDF](https://pages.ucsd.edu/~ssaiegh/forecast_2024.pdf):
  - Daily Trump-win probability, 4 Oct to 5 Nov 2024 (23 trading days). Compares RCP, the Economist, FiveThirtyEight, Silver Bulletin, IEM, PredictIt, Polymarket, Kalshi, Virtual Tout, and an S&P 500 options-implied estimate.

    | Forecast | Final | Mean | SD | Min |
    |---|---|---|---|---|
    | Polymarket | 62.65 | 59.97 | 5.21 | 49.65 |
    | Kalshi | 58.57 | 56.35 | 4.63 | — |
    | PredictIt | 54.0 | 55.2 | — | — |
    | Options-based | 57.7 | — | 2.30 | — |
    | Economist (final) | 43.0 | — | — | — |
    | FiveThirtyEight (final) | 49.45 | — | — | — |
    | Silver Bulletin (final) | 49.65 | — | — | — |

  - Conclusion: polls and models underestimated Trump, while prediction markets "were prone to overestimation and excessive volatility."
  - The author attributes the market error to traders' concentrated stake in the outcome, not illiquidity or partisan bias.
- **Cutting, Hughes-Berheim, Johnson, Baroud & Goldstein, "Are Betting Markets Better than Polling in Predicting Political Elections?" arXiv 2507.08921 (11 Jul 2025)** — [arXiv](https://arxiv.org/abs/2507.08921): descriptive and predictive analytics conclude Polymarket was "superior to polling" for 2024, particularly in swing states. The abstract gives no quantitative metrics.
- **Sethi, Seager, Morstatter, Benjamin, Hammell, Liu, Patel & Subramanian, "Political Prediction and the Wisdom of Crowds," Proc. ACM Collective Intelligence (CI '25), pp. 214–225, 3 Aug 2025, DOI 10.1145/3715928.3737483** — [MIT DSpace](https://dspace.mit.edu/handle/1721.1/162638):
  - Data: 3 statistical models vs 1 prediction market on 41 Nov 2024 outcomes: presidency, popular vote, 15 states, 11 Senate races, 13 House races.
  - Method: a profitability test (a virtual trader bets on each model's forecast) instead of average daily Brier score, which "can reward modeling flaws."
  - All models failed to beat the market on the headline presidential contract. Some beat it "convincingly" on less visible races.
  - The DSpace abstract does not name the market (PredictIt or Polymarket); unverified.
  - Sethi's Substack summary: models generally outperformed the market on competitive states and congressional races. The FiveThirtyEight popular-vote model profited betting on Trump. — [Sethi, "Markets, Models, and Mamdani," 28 Jun 2025](https://rajivsethi.substack.com/p/markets-models-and-mamdani)

**Earlier cycles (2020, 2022)**
- **Sethi et al., "Models, Markets, and the Forecasting of Elections," arXiv 2102.04936 (2021)** — [arXiv](https://arxiv.org/abs/2102.04936): the 2020 benchmark uses **PredictIt, not Polymarket**, against the Economist model. The market was better months out, the model better near the election, and an average beat both. Relevant as methodological precedent only.
- **2022 midterms:** in a First Sigma log-odds analysis cited by Jeremiah Johnson, FiveThirtyEight beat Manifold, Polymarket, Election Betting Odds and PredictIt, and only Metaculus scored higher than FiveThirtyEight. Numeric scores are in a chart not reproduced in the text, and the First Sigma original was not located. — [Asterisk, Feb 2024](https://asteriskmag.com/issues/05/prediction-markets-have-an-elections-problem-jeremiah-johnson)

**Macro and other benchmarks**
- **Fed decisions:**
  - A Gothenburg master's thesis (26 FOMC meetings, Feb 2023–Mar 2026) found Polymarket and Fed funds futures accuracy "statistically indistinguishable"; they are comparable signals but not perfect real-time substitutes. [secondary; page blocked by bot protection] — [GUPEA](https://gupea.ub.gu.se/items/996923e1-337f-4bd2-ba95-3a3144f3ce9c)
  - Good Judgment Inc. (an interested party) claims the prediction market "simply tracked CME pricing" in 2025 and that its superforecasters were nearly 2× more accurate (Brier) than futures. [secondary; 403] — [Good Judgment](https://goodjudgment.com/superforecasters-beat-futures-markets-third-year/)
  - Dune blog (2026 meetings): Kalshi and Polymarket priced "no change" higher than FedWatch from ~3 months out; no accuracy scoring. — [Dune](https://dune.com/blog/pricing-the-fed-kalshi-polymarket-cme-fedwatch)
  - The Fed staff paper by Diercks, Katz & Wright ("Kalshi and the Rise of Macro Markets," FEDS 2026-010, 12 Feb 2026) evaluates **Kalshi only**. It cites Eichengreen, Viswanath-Natraj, Wang & Wang (2025), which "use Polymarket data to explore questions surrounding Fed independence" ("Under Pressure? Central Bank Independence Meets Blockchain Prediction Markets," SSRN, 30 Jul 2025; findings not retrieved). — [FEDS PDF](https://www.federalreserve.gov/econres/feds/files/2026010pap.pdf); [Eichengreen research page](https://eml.berkeley.edu/~eichengr/research.shtml)
- **Crypto (vs options):** Fabi, Marfè, Ruffo & Schönleber, "Are Decentralized Prediction Markets Efficient? Evidence from Bitcoin Options," talk paper at FC'26 DeFi workshop — [PDF](https://fc26.ifca.ai/defi/papers/market-efficiency-prediction-markets.pdf):
  - Data: 255 Polymarket BTC bets, Mar 2024–May 2025, compared with Deribit option-implied risk-neutral densities.
  - Mean CLOB–options correlation: "Above" 0.97, "Range" 0.83, "Reach" 0.79, "Dip" 0.73.
  - Mispricing is largest at contract inception and near expiry, and amplified on weekends and in macro uncertainty.
  - Tail events (BTC to $200k, or below $40k) are persistently overpriced.
- **Sports vs bookmakers:** Reichenbach & Walther (2025, 2026) report parity with or a slight edge over bookmakers [secondary; see Q1]. No head-to-head Polymarket-vs-Pinnacle closing-line study was found; OddsPapi only gives a backtest tutorial. — [OddsPapi](https://oddspapi.io/blog/?p=2489)
- **Cross-platform calibration (Brier.fyi):** see Q1. An informal Medium essay using 971 linked Kalshi–Polymarket markets says the two are similar at midpoint, with Polymarket better at close (403, unverified). — [Medium](https://medium.com/@gaetanlion/kalshi-vs-polymarket-5acbbb0dc049)

### Inferences
- Results on the "markets vs polls" question are sensitive to the unit of analysis:
  - A single headline contract (Trump wins) favors Polymarket: Ng et al., Cutting et al., and Sethi et al. on the presidency.
  - Broad contract cross-sections and down-ballot races favor PredictIt or models: Clinton & Huang; Sethi et al. on Senate/House.
  - Volatility- or calibration-based judgments (Saiegh) penalize Polymarket for overshooting.
- Price discovery and accuracy are distinct properties. Polymarket can lead other venues in incorporating news (Aktuğ & Torul; Ng et al.) while its *level* is biased or noisy (Saiegh; Clinton & Huang).
- PredictIt's apparent accuracy edge conflicts with Zitzewitz (NBER w35845, Oct 2026), which documents larger longshot overpricing and persistent >110¢ bid sums on PredictIt because of its $850 cap. — [NBER w35845](https://www.nber.org/papers/w35845). The two findings use different measures and samples.

### Gaps
- No study found that systematically compares Polymarket against Metaculus or Manifold on matched questions with published numbers, beyond Brier.fyi dashboards.
- No rigorous 2020 Polymarket-vs-polls study was found; Polymarket was very small in 2020.
- Ng et al.'s full methods and numbers are unverified (SSRN 403).
- It is unverified whether Sethi et al.'s CI '25 market is Polymarket or PredictIt.
- Saiegh's "true probability" benchmark is Trump's electoral-vote share (57.99%), which is not a probability. His accuracy ranking should be read with caution (my inference).

---

## Q3. 2024 US presidential election: the "French whale" (Théo / Fredi9999), neighbor polling, whether Polymarket "called" the election, and manipulation vs information

### Takeaway
A French trader ("Théo") controlling Fredi9999 and related accounts (four per Polymarket; nine per Chainalysis) bet more than $45M on Trump. Chainalysis estimated his net profit at about $78.7M. Polymarket and the best on-chain academic analysis (Tsang & Yang 2026) found no evidence of one-sided manipulation. Tsang & Yang put his October buying at about 15% of the Trump market's net inflow, with capital entering both sides. Polymarket priced Trump at about 60–65% at the end, above polls and models, which looked right ex post. Academics disagree on whether that was skill: Saiegh calls it overestimation and excess volatility; Clinton & Huang document broad inefficiency; Sethi says one event cannot settle it.

### Cited Findings
**The trader and his claims**
- Polymarket's investigation (Oct 2024) identified the trader behind four large accounts, including "Fredi9999," as a French national with trading experience. It said it "has not identified any information to suggest that this user manipulated" the market. The four accounts spent more than $45M on Trump. — [The Block, 25 Oct 2024](https://www.theblock.co/amp/post/323007/polymarket-manipulation-us-election-liquidity)
- Liquidity debate at the time — [The Block, 25 Oct 2024](https://www.theblock.co/amp/post/323007/polymarket-manipulation-us-election-liquidity):
  - Presto Research: the ~$65M daily turnover made manipulation impractical.
  - Kaiko: ~$267M open interest meant the market was "highly illiquid" with minimal predictive value.
  - Trader "GCorttell93" cleared the book with a $3M order, buying at 99.7% before the price reverted to ~64%.
  - Prices that day: Polymarket 63.9% Trump, Kalshi 61%, PredictIt 59%.
- Chainalysis estimated Théo's net profit on US election bets at $78.7M and linked him to **nine** accounts, based on funding patterns, timing and exchange cash-outs. — [The Block, 7 Nov 2024](https://www.theblock.co/post/324996/french-polymarket-whale-us-election-profit-france-ban)
- Neighbor polling: Théo said he commissioned private surveys asking respondents whom their *neighbors* would vote for, to get around social-desirability bias, and that these showed strong Trump support. He declined to publish them, citing a confidentiality agreement. The WSJ could not verify his account or rule out links to political organizations. — [The Block summarizing WSJ, Nov 2024](https://www.theblock.co/post/324996/french-polymarket-whale-us-election-profit-france-ban); see also [Marginal Revolution, Nov 2024](https://marginalrevolution.com/marginalrevolution/2024/11/prediction-markets-for-the-win.html)

**Academic on-chain analyses**
- **Tsang & Yang, "The Anatomy of a Blockchain Prediction Market: Polymarket in the 2024 U.S. Presidential Election," arXiv 2603.03136 (v1 3 Mar 2026; v3 14 Sep 2026; also SSRN 6336679)** — [arXiv abs](https://arxiv.org/abs/2603.03136); [HTML v3](https://arxiv.org/html/2603.03136v3):
  - Data: complete OrderFilled and OrdersMatched logs from Polygon, Trump market 5 Jan–6 Nov 2024 (2,348,771 matched transactions), plus 249 election markets.
  - Turnover: naive volume overstates exchange-equivalent turnover about 2.5× because shares are minted and burned within trades. October Trump-market turnover was $391M versus $958M naive. The overstatement is largest in thin, young markets.
  - Depth: moving the October forecast 5 pp cost $9.1M, not the naive $15.6M. Corrected October Kyle's λ ≈ 0.02 log-odds per $1M.
  - Whale: bought $26.6M of Trump YES exposure in October, **15.1% of the $176.4M October net inflow**. The $9.1M cost of a 5-pp move is "about a third of the whale's net buying."
  - Concentration: the 20 largest non-market-maker buyers made up ~50.7% of October net inflow.
  - Capital entered both sides; the authors call this "consistent with heterogeneous beliefs rather than one-sided manipulation."
  - An earlier ResearchGate draft reportedly showed λ falling from ~0.518 to 0.01 as volume grew [secondary, unverified]. — [ResearchGate](https://www.researchgate.net/publication/401523188_The_Anatomy_of_Polymarket_Evidence_from_the_2024_Presidential_Election)
- **Tsang & Yang, "Political Shocks and Price Discovery in Prediction Markets: Evidence from the 2024 U.S. Presidential Election," arXiv 2603.03152 (v1 3 Mar 2026; v4 18 Jul 2026)** — [arXiv](https://arxiv.org/abs/2603.03152):
  - Shocks studied: the Biden–Trump debate, the assassination attempt, and Biden's withdrawal.
  - Trading rose after every shock, concentrated among experienced incumbent traders.
  - The debate repricing largely reversed (overreaction), while the assassination-attempt repricing persisted.
  - The withdrawal brought the heaviest trading but little change in the Trump price.
  - "Trading volume measures participation, while belief revision must be read from linked outcome prices."
- **Aktuğ & Torul (2026):** Polymarket was a leading price-discovery venue, and the prediction-market consensus led S&P 500 futures on election night (see Q2). — [PDF](https://web.bogazici.edu.tr/torul/pridis.pdf)

**Did Polymarket "call" the election?**
- *Yes, broadly:* Polymarket outperformed polls, especially in swing states (Cutting et al. 2025, [arXiv](https://arxiv.org/abs/2507.08921)); Ng et al. (2025/26) report the same [secondary]. Saiegh quotes Koleman Strumpf saying "nobody came close to prediction markets" in 2024. — [Saiegh PDF](https://pages.ucsd.edu/~ssaiegh/forecast_2024.pdf)
- *No, or not convincingly:*
  - Saiegh: markets overestimated Trump and were the most volatile; options were better. — [Saiegh PDF](https://pages.ucsd.edu/~ssaiegh/forecast_2024.pdf)
  - Clinton & Huang: Polymarket's 2024 contract cross-section was least accurate among the three exchanges, with arbitrage on 62 of 65 days (see Q5). — [PDF](https://osf.io/download/692db7dd37baa6ac72b550fb/)
  - Sethi: "a single event could not be used to evaluate the relative accuracy" of mechanisms. — [Sethi Substack](https://rajivsethi.substack.com/p/markets-models-and-mamdani)
  - Polymarket's popular-vote market reportedly favored Harris (77% at one point per Cointelegraph; date not verified), and Trump won the popular vote. — [Cointelegraph](https://cointelegraph.com/news/kamala-harris-leading-in-4-6-swing-states-polymarket)

**Wash trading and volume integrity during the 2024 cycle**
- Chaos Labs: roughly one-third of presidential-market volume was likely wash trading. Inca Digital: actual presidential-market volume ~$1.75B versus $2.7B reported. Chaos Labs also said Polymarket counted share counts as dollars. — [Fortune, 30 Oct 2024](https://fortune.com/crypto/2024/10/30/polymarket-trump-election-crypto-wash-trading-researchers/)
- Sirolly, Ma, Kanoria & Sethi (Columbia), "Network-Based Detection of Wash Trading," SSRN 5714122 (Nov 2025) — [Fortune, 7 Nov 2025](https://fortune.com/2025/11/07/polymarket-wash-trading-inflated-prediction-markets-columbia-research):
  - About 25% of Polymarket volume over three years was wash trading; 14% of 1.26M wallets were flagged.
  - Wash share was ~60% in Dec 2024, ~5% in May 2025, and ~20% in early Oct 2025.
  - It was ~45% in sports and ~17% in election markets.

**Partisan bias claims, 2024**
- Bernstein argued Polymarket showed stronger-than-expected Trump support. — [cbonds summary](https://cbonds.com/news/3101119/)
- A Medium analysis found an average pro-Trump spread of 3% on Polymarket versus a 13% pro-Harris spread at 538 (informal). — [Medium](https://medium.com/@gaetanlion/investigating-the-polymarket-pro-trump-market-manipulation-1a68d3d63daf)
- Systematic tests are in Q4.

### Inferences
- The best on-chain evidence (Tsang & Yang) points to a large directional bettor in a shallower-than-advertised market, not price-setting manipulation. Still, at $9.1M per 5 pp, the whale's $26.6M of October buying was big enough to plausibly move the price several points. "Manipulation vs information" is therefore partly a question of semantics: the whale's beliefs were priced in, whether or not they were correct.
- The neighbor-poll story is self-reported and unverified. No academic work tests whether Théo's private polling contained real information.
- Wash trading means reported volume is a poor liquidity proxy for 2024 election markets. Several 2024 "liquidity" arguments (e.g., Presto's $65M/day turnover) likely overstate depth.

### Gaps
- No peer-reviewed paper directly estimates the whale's causal price impact with an identification strategy. Tsang & Yang give only back-of-envelope comparisons.
- No academic study verifies or tests the "neighbor effect" polling the whale described.
- No published study scores Polymarket's state-by-state 2024 calls (all 7 swing states) with Brier or log scores against polls. Only secondary news snapshots exist (e.g., Trump favored in 6 of 7 swing states in Oct 2024 per [Benzinga](https://www.benzinga.com/markets/cryptocurrency/24/10/41342342/donald-trump-extends-betting-odds-lead-to-58-42-heres-how-kamala-harris-plans-to-reverse-l)).

---

## Q4. Favorite-longshot bias, overreaction/underreaction, partisan/wishful-thinking bias, and other behavioral anomalies on Polymarket

### Takeaway
The favorite-longshot bias on Polymarket is contested and depends on how it is measured. Trade-level returns show steep losses on sub-10¢ purchases. Grouping contracts by parent event can flip the sign, and some studies find a "reversal": longshots underpriced early, or a default/"Yes" outcome overpriced. Tail overpricing is clear in crypto price-threshold markets. Short-horizon overreaction appears in specific episodes (2024 debate, papal conclave, large price jumps). No robust partisan bias has been established for Polymarket specifically.

### Cited Findings
**Favorite-longshot bias**
- **Cardozo & Rivero-Wildemauwe, "The Favorite-Longshot Bias in Prediction Markets: Evidence from Polymarket," arXiv 2609.12878 (11 Sep 2026)** — [arXiv](https://arxiv.org/abs/2609.12878):
  - Data: 588M trades by 2.48M accounts. Method: returns by price level from transaction flows.
  - Purchases below 10¢ lose 19.3¢ per $; purchases at ≥90¢ earn +0.83¢ per $.
  - Longshots lose 6.3¢ per $ when each contract is weighted equally, but *gain* 4.1¢ when related contracts are grouped by parent event.
  - The two-sided pattern is robust in Crypto and Politics and **absent in Sports**.
  - The top decile of habitual longshot buyers makes 26.6% of next-month low-price purchases but earns returns similar to others.
  - The top favorite-buying decile makes 15.1% of high-price purchases and earns less.
  - Conclusion: an aggregate FLB exists, but its magnitude depends on grouping.
- **Reichenbach & Walther (2026)** [secondary] — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7552098):
  - No general longshot bias.
  - Low-probability outcomes start out *underpriced*, then reverse late in the market lifecycle.
  - "Default outcomes" stay persistently overpriced.
- **Qin & Yang (2026)** — [arXiv PDF](https://arxiv.org/pdf/2606.04217): low-probability tokens have negative realized returns and high-probability tokens positive returns. The authors call this a "favorite-longshot reversal" relative to the betting-market framing (as described in the search snippet; the full section was not read).
- **Deleep, Lee, Bai, Suresh & Dhawan, "How Wise is the Crowd? Bias and Edge in Prediction Markets," SSRN 6322678 (2026)** [secondary] — [Quantpedia summary, 5 Jun 2026](https://quantpedia.com/how-wise-is-the-crowd-in-prediction-markets/):
  - Data: Polymarket and Kalshi tick data, wallet histories, and commentary, with a focus on "Mention Markets." Method: penalized splines controlling for lifecycle and liquidity.
  - The apparent FLB is an artifact; the real effect is a **"Yes bias"**: traders overpay for Yes relative to No.
  - Whales lose expected value to smaller traders through adverse selection.
  - Sentiment intensity does not correlate with edge.
- **Polymarket accuracy-page dashboard (McCullough):** "persistent Yes-outcome bias on longshots" (2025) [secondary]. — [pm.wiki](https://pm.wiki/zh/projects/alexmccullough)
- **Crypto tail markets:** prices for highly improbable BTC moves persistently exceed near-zero option-implied probabilities (Fabi et al., FC'26). — [PDF](https://fc26.ifca.ai/defi/papers/market-efficiency-prediction-markets.pdf)
- **Context (non-Polymarket):**
  - Kalshi shows a standard FLB, stronger for takers (Bürgi, Deng & Whelan, "Makers and Takers: The Economics of the Kalshi Prediction Market," CESifo WP / CEPR DP20631, 2025–26). — [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
  - PredictIt longshot overpricing exceeds other markets (Zitzewitz, NBER w35845, Oct 2026). — [NBER](https://www.nber.org/papers/w35845)

**Calibration shape and underconfidence**
- Political markets on both Kalshi and Polymarket are **underconfident**: prices are compressed toward 50%, meaning favorites are underpriced (Le 2026). — [arXiv](https://arxiv.org/abs/2602.19520)
- The LessWrong 7,661-market analysis found the 0–5% bucket resolves YES only 0.1% of the time. Taken at face value, cheap contracts are overpriced, consistent with an FLB at the extremes. — [LessWrong](https://www.lesswrong.com/posts/Hruc6Gwo3vBZFGb6v/empirical-calibration-of-polymarket-analysis-of-7-661)

**Overreaction and underreaction**
- 2024 debate shock: the Polymarket price increase "largely reversed," while the assassination-attempt repricing persisted (Tsang & Yang). — [arXiv 2603.03152](https://arxiv.org/abs/2603.03152)
- Clinton & Huang: 58.3% of 182 national-presidential markets had significantly *negative* daily price autocorrelation (only 41.7% were consistent with a random walk). They read this as short-term overreaction or momentum-trader profit-taking. Large swings often occurred on days with no identifiable political event. — [PDF](https://osf.io/download/692db7dd37baa6ac72b550fb/)
- Papal conclave (8 May 2025), from Sethi — [Substack](https://rajivsethi.substack.com/p/prediction-markets-and-the-pope):
  - Pre-smoke Polymarket prices: Parolin ~33%, Tagle ~25%, Prevost ~2% (ninth).
  - After the white smoke, Parolin roughly doubled within minutes and stayed above 60% for about an hour, while Prevost *fell*.
  - Sethi reads this as momentum and herding on uninformative timing signals, not leaked information.
  - More than $40M was wagered on the conclave.
- An informal GitHub event study of 1,744 resolved markets found jumps of 30+ points reversed by ~7.3 points within 24h; a reversal classifier reached test AUC 0.609. It ignores spreads and fees. — [GitHub vivaans07/polymarket-overreaction](https://github.com/vivaans07/polymarket-overreaction)

**Partisan, wishful-thinking and demographic bias**
- **Zitzewitz, "Are Prediction Markets Politically Biased?" NBER w35846 (Oct 2026, preliminary)** — [NBER](https://www.nber.org/papers/w35846); [ppc.land summary](https://ppc.land/prediction-markets-show-no-partisan-bias-in-data-since-1880-nber-paper-finds/):
  - Data: political market returns 1880–2025.
  - No systematic overpricing of left- or right-leaning candidates. The all-markets coefficient is +0.03 pp (SE 2.66) per secondary coverage.
  - No bias by candidate gender, race or age.
  - Most political markets show an FLB, plus a tiny left-leaning overpricing in polling-average markets.
  - **Caveat: Polymarket is not yet in the sample.** The NBER page says the post-2026-midterm revision will add Polymarket data.
- **Saiegh:** neither illiquidity nor traders' unrepresentativeness or partisan bias explains the 2024 market errors; he points to traders' concentrated stake. — [PDF](https://pages.ucsd.edu/~ssaiegh/forecast_2024.pdf)
- **Johnson (Asterisk, Feb 2024):** argues identity-driven betting distorts national markets, with candidates who have energetic online fan bases (Trump, Yang, Ramaswamy) overperforming. This is inference, not measurement. — [Asterisk](https://asteriskmag.com/issues/05/prediction-markets-have-an-elections-problem-jeremiah-johnson)

**Whale and large-trader behavior**
- In Mention markets, whales lose to small traders (Deleep et al.) [secondary].
- An agent-based simulation shows biased whales shift prices in proportion to their capital share, for longer when other traders herd (arXiv 2601.20452; simulation, not Polymarket data). — [arXiv](https://www.arxiv.org/pdf/2601.20452)

### Inferences
- The FLB results on Polymarket can be reconciled as follows:
  - Trade-weighted returns on cheap contracts are very negative, driven by the many 1–5¢ "No-favorite" markets and crypto tails.
  - Event-grouped or lifecycle-controlled analyses remove much of the bias or reverse it.
  - Sports markets, which have few longshots and professional market makers, show little bias.
  - Any downstream study should state its weighting scheme explicitly.
- "Yes bias" (Deleep; McCullough) and "default outcome overpricing" (Reichenbach & Walther) may be the same phenomenon: affirmative or narrative outcomes are overbought, especially in mention, crypto and novelty markets.
- Political underconfidence (Le) and an FLB (Zitzewitz on other markets) look contradictory but can coexist: compression toward 50% across the mid-range, with overpricing only at the far tails.

### Gaps
- No Polymarket-specific test of partisan or wishful-thinking bias with trader-level political identity or market-level partisanship coding was found. Zitzewitz's Polymarket extension is forthcoming.
- No systematic study of overreaction or underreaction to scheduled news (polls, debates, CPI) across many Polymarket markets was found. Evidence comes from single episodes and informal repositories.
- Full texts of Deleep et al. and Reichenbach & Walther were not accessible, so effect sizes are missing.

---

## Q5. Weak/semi-strong form efficiency tests, return predictability, and mispricing persistence

### Takeaway
Polymarket is efficient at the cross-venue price-discovery margin and fast in liquid sports and headline markets. Its efficiency is weak in several documented ways:
- persistent cross-venue price gaps (6 pp on average in 2024);
- negative daily autocorrelation in most 2024 presidential contracts;
- order-flow-based return predictability (large-trade imbalance, informed-minority flow);
- tens of millions of dollars in realized within-platform arbitrage;
- protocol-level frictions that keep some payoff-equivalent mispricings from being arbitraged away.

### Cited Findings
**Cross-venue inefficiency**
- **Clinton & Huang (2025)** — [PDF](https://osf.io/download/692db7dd37baa6ac72b550fb/):
  - Buying the cheapest Harris and Trump contracts across Kalshi, PredictIt and Polymarket cost less than $1 on **62 of 65 days**, and the gap *grew* in the final two weeks before converging on Election Day.
  - Price levels correlated ~0.9 across exchanges, but daily price *changes* were nearly uncorrelated.
  - Mutually exclusive margin contracts (e.g., "Dem by 6–7%" and "GOP by 6–7%") moved together, violating basic coherence.
  - Arbitrage existed on nearly one in ten days in the final 90 days.
- **Aktuğ & Torul (2026):** the average cross-venue spread for "Trump wins" was 6.2 pp across 9 venues. Limits to arbitrage come from jurisdictional barriers and locked capital. — [PDF](https://web.bogazici.edu.tr/torul/pridis.pdf)
- **Ng et al. (2025/26):** significant price disparities persist and imply economically meaningful arbitrage; Polymarket leads Kalshi. [secondary] — [SSRN](https://papers.ssrn.com/abstract=5331995)
- PredictIt and Polymarket diverged in 2024 with limited arbitrage between them, due to segmentation (PredictIt: verified US residents funding in cash; Polymarket: crypto). Per search summary of Gelman's blog; the page itself returned 403. — [Statistical Modeling blog, Sep 2024](https://statmodeling.stat.columbia.edu/2024/09/13/movements-in-the-prediction-markets-and-going-beyond-a-black-box-view-of-markets-and-prediction-models/)

**Within-Polymarket arbitrage**
- **Saguillo, Ghafouri, Kiffer & Suarez-Tangil, "Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets," AFT 2025 (LIPIcs vol. 354) / arXiv 2508.03474** — [arXiv](https://arxiv.org/pdf/2508.03474); [Dagstuhl](https://drops.dagstuhl.de/storage/00lipics/lipics-vol354-aft2025/LIPIcs.AFT.2025.27/LIPIcs.AFT.2025.27.pdf):
  - Data: on-chain order books for markets resolved Apr 2024–Apr 2025.
  - Single-market (YES+NO ≠ 1) and combinatorial cross-market arbitrage yielded about **$40M in realized arbitrage profit**.
- **Gebele, Mutzel & Matthes, "Executable Arbitrage and Market Efficiency in Prediction Markets," arXiv 2608.00666 (1 Aug 2026)** — [arXiv](https://arxiv.org/abs/2608.00666):
  - Covers NegRisk (mutually exclusive outcome) markets.
  - Realized arbitrage of ~$1.12M ($1.086M converter-enabled; $32k settlement baskets).
  - Positive payoff-bound violations concentrate on the YES side, which the protocol cannot execute. Executable NO-side violations are rarer and shorter-lived.
  - Conclusion: efficiency depends on whether protocols expose payoff equivalences as executable primitives.
- **Cheng, Yang & Zou, "Arbitrage Analysis in Polymarket NBA Markets," arXiv 2605.00864 (22 Apr 2026)** — [arXiv](https://arxiv.org/abs/2605.00864):
  - Data: 75M LOB snapshots across 173 NBA games.
  - Only 7 executable single-market arbitrage episodes, with a median life of 3.6 s.
  - 290 combinatorial episodes (mostly in the final minutes of play), median return 101 bp.
  - 76.9% of opportunities averaged only 14.8 shares of executable size.
  - "Structurally efficient yet not frictionless"; arbitrage is limited to retail scale.

**Return predictability and informed flow**
- **Gómez-Cram et al. (2026):** order flow of a persistent 3.14% skilled minority predicts both short-term price moves and final outcomes. Skill persists out of sample for 44% of accounts. [secondary] — [The Block](https://www.theblock.co/post/398902/skilled-polymarket-traders-are-a-3-minority-and-everyone-else-funds-their-gains-study)
- **Ng et al.:** large-trade net order imbalance predicts subsequent returns. [secondary] — [SSRN](https://papers.ssrn.com/abstract=5331995)
- **Mitts (Columbia) & Ofir (Haifa), "From Iran to Taylor Swift: Informed Trading in Prediction Markets," SSRN 6426778 (2026)** — [Harvard Law School Forum, 25 Mar 2026](https://corpgov.law.harvard.edu/2026/03/25/from-iran-to-taylor-swift-informed-trading-in-prediction-markets/); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6426778):
  - Data: ~93,000 Polymarket markets and ~50,000 wallets, Feb 2024–Feb 2026.
  - Method: a five-signal screen (bet size cross-sectionally and within trader, profitability, pre-event timing, directional concentration), buy-side only, positions ≥$500.
  - 210,718 flagged wallet-market pairs with a 69.9% win rate, more than 60 SD above a permutation null.
  - About $143M in anomalous profit, described as a lower bound.
  - Semi-strong efficiency is violated in the sense that private information earns returns, though this also improves price accuracy.
- **Nechepurenko, "Information Leakage at Population Scale … 2020–2026," arXiv 2605.00459 (1 May 2026)** — [arXiv](https://arxiv.org/abs/2605.00459):
  - Data: 12,708 markets, Oct 2020–Apr 2026.
  - Only 88 (0.7%) yielded computable deadline-resolved leakage scores, and 12 of 88 passed anchor-sensitivity checks.
  - Conclusion: "resolution semantics," not computation, is the binding obstacle to measuring pre-event leakage at scale.
- **Tsang & Yang (2603.03152):** the 2024 debate repricing reversed, i.e., predictable mean reversion. — [arXiv](https://arxiv.org/abs/2603.03152)
- **Fabi et al.:** crypto mispricing relative to options declines monotonically from inception to expiry for simple bets, and is amplified on weekends and during macro shocks. — [PDF](https://fc26.ifca.ai/defi/papers/market-efficiency-prediction-markets.pdf)

**Microstructure and measurement issues that affect efficiency tests**
- Heuristic trade-sign classifiers are close to random on Polymarket (tick rule 49.83%), which biases VPIN/OFI-based efficiency and informed-trading tests (Qin & Yang). — [arXiv](https://arxiv.org/abs/2606.04217)
- Dubach (arXiv 2610.06412, Oct 2026) validates public trade prints against on-chain settlement and finds that trade-sign errors can distort measured trading costs even when classification accuracy is high. Abstract only, from a search snippet. — [arXiv](https://arxiv.org/abs/2610.06412)
- Naive volume double-counts mint/burn activity by ~2.5× (Tsang & Yang). Wash trading is ~25% of volume (Sirolly et al.). — [arXiv](https://arxiv.org/abs/2603.03136); [Fortune](https://fortune.com/2025/11/07/polymarket-wash-trading-inflated-prediction-markets-columbia-research)

### Inferences
- Efficiency is best described as category- and liquidity-dependent:
  - Liquid sports and headline political markets show fast correction and rare single-market arbitrage.
  - Multi-outcome (NegRisk), cross-venue, and thin long-dated markets show persistent mispricing.
  - Protocol design (which conversions are executable) is a first-order determinant of observed inefficiency.
- Large documented informed-trading profits ($143M; 3% skilled minority) show Polymarket is *not* semi-strong efficient with respect to private information. The same flows are what make its prices accurate.

### Gaps
- No formal variance-ratio or random-walk test across the full Polymarket universe was found. Clinton & Huang only test 2024 political markets.
- There is no published long-horizon test of whether simple public-information strategies (e.g., fading longshots net of fees and spreads) are profitable after costs across categories. Cardozo et al. report gross returns.
- The Saguillo et al. full breakdown of the $40M by arbitrage type was not retrieved.

---

## Q6. 2025–2026 work evaluating Polymarket accuracy (2025 elections worldwide, NYC mayoral race, papal conclave, Fed decisions, others)

### Takeaway
Systematic 2025–2026 *event-level* evaluations are scarce. Most evidence is single-event commentary, along with the large cross-sectional preprints in Q1, Q4 and Q5. Polymarket's 2025 record includes several high-profile misses on favorites:
- the NYC Democratic primary (Cuomo ~93% in late May 2025);
- the Romanian presidential runoff (Simion ~75%);
- the papal conclave (Prevost ~2%).

It also includes hits, such as Mamdani in the Nov 2025 general election. On Fed decisions, Polymarket appears statistically indistinguishable from fed funds futures.

### Cited Findings
- **NYC mayoral race 2025:**
  - Democratic primary: markets gave Mamdani ~5% to lead the first round for most of the final week, rising to ~1-in-5 on election night after an Emerson poll showed Cuomo +3. Mamdani won by 7. Only 1 of 32 NYT-tracked polls had predicted his first-round win. Sethi judged markets "did poorly but were not clearly worse on average than polls." — [Sethi, 28 Jun 2025](https://rajivsethi.substack.com/p/markets-models-and-mamdani)
  - Polymarket had Cuomo around 93% at the end of May 2025 [secondary]. — [Next Event Horizon Substack](https://nexteventhorizon.substack.com/p/nyc-mayor-kalshi-polymarket)
  - General election (4 Nov 2025): Polymarket correctly favored Mamdani, in line with polls. A contrarian trader lost nearly $1M betting against him. — [CoinDesk, 5 Nov 2025](https://www.coindesk.com/markets/2025/11/05/biggest-loser-of-nyc-election-polymarket-contract-is-down-almost-usd1m-betting-against-mamdani); [Cryptonews](https://cryptonews.com/news/zohran-mamdani-wins-nyc-mayoral-race-as-polymarket-traders-nail-another-prediction/)
- **Papal conclave (May 2025):**
  - Prevost was priced at ~1–2% on Polymarket and Kalshi. — [Decrypt](https://decrypt.co/318672/american-cardinal-prevost-elected-pope-betting-markets-upset); [CNN](https://edition-prod-cf.sitemirror.cnn.com/2025/05/09/business/online-betting-markets-failed-pope)
  - Nate Silver (a Polymarket adviser) argued that 1–2% outcomes happen in fields of dozens of plausible candidates. — [Silver Bulletin](https://www.natesilver.net/p/why-didnt-anyone-predict-the-american)
  - Sethi documented post-smoke herding (Q4).
  - No systematic calibration study of papal markets exists.
- **Romanian presidential election (May 2025):** before the runoff, ~75% of Polymarket money backed George Simion; Nicușor Dan won. In April 2025 Simion was at 28%. Resolution data comes from a third-party archive. — [Puterea.ro](https://www.puterea.ro/?p=485469); [Romania Insider, Apr 2025](https://www.romania-insider.com/polymarket-presidential-elections-romania-april-2025); [polyguana resolved market](https://polyguana.com/resolved/541107)
  - Sethi lists the conclave and the Romanian election as 2025 "embarrassments for markets." — [Sethi](https://rajivsethi.substack.com/p/markets-models-and-mamdani)
- **Fed/FOMC (2023–2026):** Polymarket accuracy is statistically indistinguishable from fed funds futures over 26 meetings (Gothenburg thesis) [secondary]. Good Judgment says Polymarket tracks CME. Dune finds both prediction markets priced "no change" above FedWatch at long horizons. — [GUPEA](https://gupea.ub.gu.se/items/996923e1-337f-4bd2-ba95-3a3144f3ce9c); [Good Judgment](https://goodjudgment.com/superforecasters-beat-futures-markets-third-year/); [Dune](https://dune.com/blog/pricing-the-fed-kalshi-polymarket-cme-fedwatch)
- **Large 2026 cross-sectional preprints** (all detailed above):
  - Reichenbach & Walther (Oct 2026);
  - Cardozo & Rivero-Wildemauwe (Sep 2026);
  - Le (Feb/Aug 2026);
  - Qin & Yang (Jun 2026);
  - Gómez-Cram et al. (Apr 2026);
  - Mitts & Ofir (2026);
  - Ibrahim & Zaki (Sep 2026);
  - Tsang & Yang (Mar–Sep 2026);
  - Aktuğ & Torul (Jun 2026).
- **Media influence (Sep 2026):** Ibrahim & Zaki, "Price Dislocations, News Citations, and Epistemic Leverage on Polymarket," arXiv 2609.06005 — [arXiv](https://arxiv.org/abs/2609.06005):
  - Data: 173.7M signed trades; 6,990 news articles from 2024–2025; 44,976 detected ≥5-pp dislocations.
  - Citation rates rise about 33% after a dislocation (τ = 0.283, p = 0.001).
  - Market prominence predicts citation far more than move size (β 0.610 vs 0.159).
  - It costs roughly $0.7–1.0M to move a market 5 pp *and* get the move cited, so manipulation of a few prominent markets is "within reach" of interested actors.
- **Insider-trading era (2026):**
  - Bloomberg (Jul 2026, using Polysights data): ~$200M in H1 2026 trades flagged as possible insider activity. — [Bloomberg](https://www.bloomberg.com/graphics/2026-polymarket-traders-who-knew-the-future/)
  - The first US federal indictment for prediction-market insider trading (23 Apr 2026, Venezuela/Maduro operation) is noted in arXiv companion papers. — [arXiv 2605.02287](https://arxiv.org/pdf/2605.02287)
  - These matter for accuracy: insider flow improves pre-event prices but undermines the "crowd wisdom" interpretation.
- **Qualitative critique:** Rohanifar, Ahmed & Sultana, "Prediction Laundering: The Illusion of Neutrality, Transparency, and Governance in Polymarket," arXiv 2602.05181 (5 Feb 2026) — [arXiv](https://arxiv.org/abs/2602.05181):
  - Method: interviews and ethnography (N=27).
  - Argues that aggregation strips whale and hedge noise and presents a capital-weighted signal as "objective" probability.

### Inferences
- The 2025 misses (primary, Romania, conclave) were all on favorites priced at 75–98% or longshots at 2–25%. Individually they are consistent with calibrated pricing. They still highlight that Polymarket's accuracy reputation rests heavily on the 2024 presidential call. No 2025-cycle aggregate scoring exists to judge whether these were bad luck or bias.
- With the Zitzewitz paper promising a Polymarket extension after the Nov 2026 US midterms, the midterms are the likely next large benchmark. No results existed as of Oct 2026.

### Gaps
- No systematic studies were found on Polymarket accuracy in other 2025 national elections (Germany Feb 2025, Canada Apr 2025, Australia May 2025, Poland May–Jun 2025, Japan, Chile, etc.). Only press snapshots exist.
- No academic paper evaluates Polymarket's NYC mayoral pricing beyond blog commentary.
- No 2026 US midterm accuracy results exist yet; the elections are 3 Nov 2026, after the research date.
- Polymarket's in-house blog ("The Oracle") was not retrieved. I found no evidence of a formal Polymarket-published accuracy white paper beyond the /accuracy page.
- Kalshi-published research comparing itself with Polymarket was not found. The Fed FEDS paper covers Kalshi only.
