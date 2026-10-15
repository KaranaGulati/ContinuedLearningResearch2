# Applied uses of Polymarket data across domains, and open research gaps (2020 – Oct 2026)

Scope note: this file catalogs studies that use Polymarket prices as an input or measurement instrument, plus domain studies of Polymarket sports and crypto markets, and the gaps authors have flagged. Notes were compiled 2026-10-15. "Verified" means I read the abstract or full text myself. "Snippet-only" means the claim comes from a search summary or secondary coverage and should be checked before citing. Many 2026 items are arXiv/SSRN preprints with no peer review.

## Q1. Finance/macro: Polymarket probabilities as shocks for asset-price identification (elections, tariffs, Fed, recession, crypto)

### Takeaway
The strongest finance use of Polymarket so far is high-frequency identification of 2024 US election effects on equities. Aktuğ & Torul (Mar 2026) use 5-minute Polymarket probabilities and validate them against Betfair and sportsbooks. For Fed, inflation and recession, the rigorous academic work uses Kalshi rather than Polymarket. I found no published study that uses Polymarket tariff or recession probabilities to identify asset-price responses. That is a clear gap.

### Cited Findings
**Election → equities (Polymarket as the shock series)**
- **Aktuğ, E. (Sabancı) & Torul, O. (Boğaziçi), "Political Capital: Real-Time Electoral Probabilities and the Value of Corporate Political Alignment," working paper, March 2026.** Verified (abstract and introduction read). The paper combines 5-minute Polymarket Trump-win probabilities (it notes $3.6B in 2024 volume) with OpenSecrets contribution records for 71 firms, using local projections at 5-minute, hourly and daily frequencies. A 1-pp rise in Trump's win probability opens a 0.25% return gap between Republican- and Democrat-affiliated firms. The gap is significant within the first hour, peaks around day 20 and persists for about 60 trading days. A dose-response pattern replicates across six probability sources (prediction markets, a betting exchange and sportsbooks). In the Butler assassination-attempt event study (13 Jul 2024), Polymarket rose 7.5 pp and produced a 1.2% partisan differential on the first trading day. The paper reports a three-tier lead-lag hierarchy: Polymarket and Betfair lead together, sharp books (Bovada, BetOnline) follow within hours, and Unibet lags by at least 12 hours. Its structural estimate is about $125M per 1-pp shift for a fully aligned $50B firm. — [PDF](https://web.bogazici.edu.tr/torul/polcap.pdf)
- The same paper's literature review cites **Flynn & Tarkom (2025)** on "information processing frictions between betting and equity markets during the 2024 election." — [Aktuğ & Torul PDF](https://web.bogazici.edu.tr/torul/polcap.pdf)
- **"How do financial markets price political uncertainty? Evidence from the 2024 United States presidential election," *Finance Research Letters* (Elsevier), 2025, article S1544612325001448.** Snippet-only, because the page returned 403. The paper studies Trump Media (DJT) returns against Polymarket odds and reports that DJT takes 3–5 days to fully reflect shocks to election odds. It uses Trump's April Fools' withdrawal joke as an instrumental-variable natural experiment. The authors are unverified; this may be the Flynn & Tarkom (2025) paper cited above, which is my inference. — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1544612325001448)
- **"Global Stock Market Reactions to 2024 US Presidential Election Probabilities," SSRN 5238389, c. April 2025.** Snippet-only, because the page returned 403. This event study covers 40 national stock indexes and splits days into high and low Trump-probability regimes. Mexico and some emerging markets react strongly, while the US index shows no significant bias. I could not confirm whether the probability source is Polymarket. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5238389)
- **Chernov, M., Elenev, V. & Song, D., "The Comovement of Voter Preferences: Insights from U.S. Presidential Election Prediction Markets Beyond Polls," NBER WP 33339, January 2025.** This paper combines polls, fundamentals and political prediction-market prices to forecast state-level 2024 outcomes. Ignoring cross-state correlations can bias win probabilities by more than 10 pp. It is a forecasting paper, not an asset-pricing paper, and I did not verify which platforms it uses. — [NBER](https://www.nber.org/papers/w33339)
- The historical precedent for this design is Snowberg, Wolfers & Zitzewitz, which used IEM and Intrade odds; their NBER WP 18222 reports that Republican wins raise broad equity indexes by about 2.5%. — [NBER w18222](https://www.nber.org/system/files/working_papers/w18222/w18222.pdf)

**Fed, inflation and recession markets**
- **Diercks, A. M. (Fed Board), Katz, J. D. (Northwestern) & Wright, J. H. (JHU/NBER), "Kalshi and the Rise of Macro Markets," FEDS 2026-010, 12 Feb 2026.** This is Kalshi-only (CPI, payrolls, unemployment, GDP, FOMC). It finds Kalshi a high-frequency benchmark with rich distributional information that performs about as well as surveys and derivatives. It argues Kalshi is better than SOFR-based measures for meeting-specific FOMC risk-neutral distributions. This is a template study that has not been replicated on Polymarket. — [Fed PDF](https://www.federalreserve.gov/econres/feds/files/2026010pap.pdf); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6333085); [Forbes coverage, Feb 2026](https://www.forbes.com/sites/jasonbrett/2026/02/23/kalshi-polymarket-offer-evolution-of-predictions-for-fed-wall-street/)
- **Angelini, G., "The Shape of Macroeconomic Beliefs," arXiv:2606.30040, 29 Jun 2026.** This is Kalshi-only. The author builds CPI and core-CPI implied distributions from 30 days down to 1 hour before each release. A 0.1-pp lagged positive Reuters surprise raises P(monthly CPI > 0.3%) by about 4.7 pp. Upper-tail probabilities predict high-inflation outcomes even when the mean equals consensus. The paper does not mention Polymarket. — [arXiv](https://arxiv.org/abs/2606.30040)
- **"Cross-Market Event Pricing: Evidence from Polymarket and Fed Funds Futures,"** an unattributed document on bscapitalmarkets.com. It asks whether Polymarket FOMC probabilities differ systematically from CME FedWatch. I could not verify its authors or results. — [link](https://www.bscapitalmarkets.com/cross-market-event-pricing-evidence-from-polymarket-and-fed-funds-futures.html)
- Non-academic evidence shows large Polymarket–futures divergences. For the September 2026 FOMC, one outlet reported Polymarket at 53% for a hike against about 32% in futures; another reported CME 64%, Kalshi 58% and Polymarket 56%. The two outlets conflict, likely because they used different snapshot times and SOFR versus FF futures. — [KuCoin news](https://www.kucoin.com/news/flash/polymarket-prices-53-odds-of-fed-rate-hike-in-september-2026-vs-32-in-futures); [PredictionMarketsPicks](https://predictionmarketspicks.com/articles/fed-rate-hike-odds-september-2026-kalshi-polymarket-futures)
- Recession odds as of March 2026: Kalshi's 2026-recession contract rose above 34% after oil passed $100, while Polymarket stood at about 31%, per CNBC. No academic paper uses these as an uncertainty measure. — [CNBC, 9 Mar 2026](https://www.cnbc.com/2026/03/09/recession-odds-kalshi-oil.html)
- **Gómez-Cram, Guo, Kung (LBS) & Jensen (Yale), "Prediction Market Accuracy: Crowd Wisdom or Informed Minority?"** SSRN 6617059, covered June 2026. The sample is 1.72M Polymarket accounts, 210,322 markets and $13.76B in volume. About 3% of accounts are skilled, with 44% persistence across split samples. Skilled traders move prices toward outcomes and react faster to FOMC announcements and earnings reports. This is relevant to using Polymarket around macro releases. — [Yale Insights](https://insights.som.yale.edu/insights/wisdom-of-the-few-prediction-markets-are-driven-by-small-number-of-skilled-traders); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6617059)
- **Tariffs:** Polymarket has listed many tariff markets, for example SCOTUS upholding the tariffs (about 25% for approval per Benzinga/Yahoo), the weighted average tariff reaching 5% or more (resolved Yes), and tariff revenue above $250B in 2025. I found no academic study that uses them as shocks. — [Yahoo/Benzinga](https://finance.yahoo.com/news/trump-tariffs-allowed-stand-now-223245417.html); [Polymarket Oracle newsletter](https://news.polymarket.com/p/reverse-tariff-taco)

### Inferences
- Election-probability identification is the most mature approach, and Polymarket's 5-minute granularity is its main advantage over IEM/Intrade-era work. Cross-venue validation (Aktuğ & Torul) suggests Polymarket is a leading, not lagging, election signal.
- Macro-release work has gravitated to Kalshi because it is CFTC-regulated, has bracketed strike ladders for CPI and payrolls, and has a Fed-staff endorsement. A Polymarket version of Diercks-Katz-Wright or Angelini, with horse-races against FedWatch or SOFR and checks on whether offshore and crypto-collateralized pricing differs, is an obvious replication gap.

### Gaps
- No verified paper uses Polymarket tariff-event probabilities (for example the April 2025 "Liberation Day" episodes or the SCOTUS IEEPA case) to identify equity, FX or Treasury responses.
- No verified paper uses Polymarket recession, government-shutdown or debt-ceiling odds as a policy-uncertainty index, or compares them to the Baker-Bloom-Davis EPU index.
- No peer-reviewed comparison of Polymarket FOMC markets with fed funds futures or SOFR exists. The only document found is unattributed.
- Crypto-ETF approval markets (SEC spot BTC/ETH ETF decisions in 2024) as event-study shocks: I found nothing in this search.

## Q2. Political science: forecasting, uncertainty, partisan perception, media integration and influence

### Takeaway
Several 2025–26 papers compare Polymarket with polls and generally favor Polymarket for 2024. Accuracy evidence across contract types is mixed: one Vanderbilt study finds lower accuracy for Polymarket than for PredictIt and Kalshi. Media integration of Polymarket odds is now real, through X/xAI (2025) and Dow Jones (WSJ, Barron's, MarketWatch) from Jan 2026. The first quantitative study of how media cite Polymarket odds appeared in Sept 2026. No experiment yet tests whether displaying Polymarket odds changes voter attitudes or turnout; this is explicitly flagged as open.

### Cited Findings
- **Cutting, L. E., Hughes-Berheim, S. S., Johnson, P. M., Baroud, H. & Goldstein, B., "Are Betting Markets Better than Polling in Predicting Political Elections?" arXiv:2507.08921, 11 Jul 2025.** Using Polymarket data, the authors find it "superior to polling" for 2024, particularly in swing states. They interpret this through wisdom-of-crowds and note that markets ask "who will win" while polls ask "who will you vote for." Their stated future work is to test the explanation and check whether it generalizes to other events. — [arXiv](https://arxiv.org/abs/2507.08921)
- **"Beyond the Polls: Quantifying Early Signals in Decentralized Prediction Markets with Cross-Correlation and Dynamic Time Warping,"** *Future Internet* (MDPI) 17(11):487, 2025. Snippet-only. The paper reports that Polymarket prices led shifts in voter sentiment ahead of polls in an Arizona case. — [MDPI](https://www.mdpi.com/1999-5903/17/11/487)
- **Tsang & Yang, "The Anatomy of a Blockchain Prediction Market: Polymarket in the 2024 U.S. Presidential Election," arXiv:2603.03136, March 2026.** This is a transaction-level study. The market was shallower than volume implied: moving the October forecast by 5 points cost about $9.1M, not the $15.6M a naive estimate gives. Price-parity deviations from $1 narrowed as depth grew. Snippet-only for the numbers. — [arXiv](https://arxiv.org/abs/2603.03136)
- **Clinton, J. & Huang, T. (Vanderbilt), 2025–26.** As reported by the press, Polymarket matched outcomes in 67% of political markets, against 78% for Kalshi and 93% for PredictIt. Clinton says the paper is mainly about prices responding to each other rather than to political news. Secondary only; I did not see the primary text. — [DL News](https://www.dlnews.com/articles/markets/polymarket-kalshi-prediction-markets-not-so-reliable-says-study)
- **Nechepurenko, M., "Price as Focal Point: Prediction Markets, Conditional Reflexivity, and the Politics of Common Knowledge," arXiv:2604.24147, 27 Apr 2026.** The paper treats markets as coordination devices that can be self-fulfilling. It proposes a Signal Credibility Index (variance ratio VR(6), a two-sidedness diagnostic and a trader-concentration adjustment). It argues "the most visible market was the least accurate" across three 2024 shocks. Channels: bandwagon and viability inference for voters, and narrative shorthand for media. These are theoretical and descriptive claims, and the paper itself says the evidence is uneven across channels. — [arXiv](https://arxiv.org/abs/2604.24147)
- **Ibrahim, H. & Zaki, Y., "Price Dislocations, News Citations, and Epistemic Leverage on Polymarket," arXiv:2609.06005, 5 Sep 2026.** Data: 173.7M Polymarket trades from 2024–25, 6,990 news articles mentioning prediction markets, 1,582 odds-quoting sentences (918 attributed to a specific market) and 44,976 dislocations (moves of at least 5 pp). After a dislocation, a market's citation rate is about 33% above baseline (τ = 0.283, permutation p = 0.001). Prominence predicts citation more than move size does (β 0.610 vs 0.159). The authors define "epistemic leverage," the dollar flow needed to move a market 5 pp and get it cited, at about $0.7–1.0M. — [arXiv](https://arxiv.org/abs/2609.06005)
- **"Prediction Laundering: The Illusion of Neutrality, Transparency, and Governance in Polymarket,"** arXiv:2602.05181, Feb 2026. This is a critical sociotechnical audit. It calls for future work combining sociotechnical analysis with on-chain forensics to show how "hedge wagers become authoritative signals." Snippet-only. — [arXiv](https://arxiv.org/html/2602.05181v1)
- **Media integration facts:**
  - Polymarket became X/xAI's "Official Prediction Market Partner" (2025; exact date not confirmed in the source found). — [Closing Line Substack](https://closingline.substack.com/p/polymarket-signs-deal-with-x)
  - Dow Jones signed a data deal in January 2026 to put Polymarket probabilities in WSJ, Barron's, MarketWatch and IBD, including an earnings calendar based on bets. One outlet noted the data was not yet visible at announcement. — [The Block](https://www.theblock.co/amp/post/384646/polymarket-to-provide-prediction-data-to-wall-street-journal-barrons-in-dow-jones-deal); [DeFi Rate](https://defirate.com/news/polymarket-deal-with-dow-jones-brings-data-to-wsj-marketwatch-barrons/)
  - CNN's partner is Kalshi, not Polymarket, and CNBC also has a Kalshi deal. — [Crowdfund Insider, Jan 2026](https://www.crowdfundinsider.com/2026/01/257185-prediction-markets-platform-polymarket-secures-data-partnership-with-dow-jones/)
- **Influence on voters is untested:** "There is as yet no empirical basis for establishing how, or to what extent, the publication of data from prediction markets … affects voters' attitudes or behavior." The Brennan Center warned in June 2026 that treating Kalshi/Polymarket odds as reliable election information could confuse voters. — [Israel Democracy Institute](https://en.idi.org.il/articles/66410); [The Conversation](https://theconversation.com/prediction-markets-are-going-mainstream-what-does-that-mean-for-public-health-and-democracy-291948)
- The closest experimental precedent is Westwood, Messing & Lelkes on probabilistic forecasts (538-style) confusing and demobilizing voters. It predates Polymarket. — [UPenn PDF](https://www.asc.upenn.edu/sites/default/files/2021-03/Projecting%20Confidence-%20How%20the%20Probabilistic%20Horse%20Race%20Confuses%20and%20Demobilizes%20the%20Public.pdf)

### Inferences
- The 2024 "Polymarket beat the polls" result rests on essentially one election cycle, and most papers do not adjust for the correlated-states issue Chernov et al. flag. Generalization to the 2026 midterms is an obvious next test.
- Media-citation research (Ibrahim & Zaki) plus the Dow Jones and X integrations together create a natural experiment. Outlets that started displaying odds in Jan 2026 could be compared with those that did not, with on-chain flows used to check for manipulation targeting cited markets.

### Gaps
- No randomized survey experiment shows Polymarket odds (vs. polls or 538-style model probabilities) to respondents to measure turnout intention, perceived inevitability or donations. This is explicitly flagged as an open question.
- I found no published use of Polymarket to measure partisan perceptions, for example partisan wallet flows or partisan disagreement in probabilities. Wallet partisanship is not observable directly.
- I found no 2026 midterm study using Polymarket yet, which is unsurprising since the midterms are Nov 2026.
- The Clinton & Huang accuracy figures need primary-source verification.

## Q3. Sports markets on Polymarket: efficiency, growth, in-play

### Takeaway
Sports is Polymarket's largest category, at about 39–44% of volume in 2025–26, but rigorous academic evidence on its efficiency is thin. One arXiv NBA microstructure paper (May 2026) finds near-zero exploitable arbitrage because of thin depth. A Sept 2026 paper finds the favorite-longshot bias is absent in Polymarket sports while present in politics and crypto. Comparisons against Pinnacle and Betfair are mostly vendor blogs with conflicting, unverified numbers. I found no peer-reviewed in-play study.

### Cited Findings
- **Volume share:** Pew Research Center (27 May 2026) puts sports at 39% of Polymarket volume since July 2024, against 80% on Kalshi. — [Pew](https://www.pewresearch.org/short-reads/2026/05/27/trading-volume-on-prediction-markets-has-soared-in-recent-months/)
  - Statista: about $4B of about $9B on Polymarket international in April 2026 was sports, roughly 44%. — [Statista](https://www.statista.com/chart/36341/global-trading-volume-on-prediction-platforms/)
  - Sacra: sports about 39–40%, politics 32%, crypto 20%. — [Sacra](https://sacra.com/c/polymarket/)
  - Gambling Insider: Polymarket 2025 volume was $21.5B. — [Gambling Insider](https://www.gamblinginsider.com/in-depth/110180/prediction-market-statistics)
  - The Polymarket US exchange had about 10% of US prediction-market notional volume in June–July 2026 (World Cup). — [Sportico](https://www.sportico.com/business/sports-betting/2026/prediction-market-data-volume-polymarket-kalshi-world-cup-1234939529/)
- **"Arbitrage Analysis in Polymarket NBA Markets," arXiv:2605.00864, May 2026** (authors not captured). The authors use order-book snapshots from 173 games. Arbitrage is rare and short-lived, indicating strong microstructural efficiency. Execution is depth-constrained: 76.9% of combinatorial opportunities are capped at an average executable size of 14.8 shares. — [arXiv](https://arxiv.org/abs/2605.00864)
- **Cardozo, M. & Rivero-Wildemauwe, J. I., "The Favorite-Longshot Bias in Prediction Markets: Evidence from Polymarket," arXiv:2609.12878, 11 Sep 2026.** The data cover 588M trades by 2.48M accounts. Contracts below 10¢ lose 19.3¢ per $, while contracts at or above 90¢ earn 0.83¢ per $. The bias's sign flips depending on grouping (−6.3¢ equal-weighted vs +4.1¢ grouped by parent event). The two-sided FLB is robust in crypto and politics but **absent in sports**. — [arXiv](https://arxiv.org/abs/2609.12878)
- **Reichenbach, F. & Walther, M. (International Univ. of Berlin), "Exploring Decentralized Prediction Markets: Accuracy, Skill, and Bias on Polymarket," SSRN WP 5910522, 2025.** The sample is 124M+ trades and $48B in volume. Prices are "accurate most of the time" and reportedly slightly outperform bookmaker odds, with biases toward overtrading the default and "Yes" options. The paper lists future research directions across disciplines. Snippet-only: abstract not read, details from press and a ResearchGate snippet. — [ResearchGate](https://www.researchgate.net/publication/398660802_Exploring_Decentralized_Prediction_Markets_Accuracy_Skill_and_Bias_on_Polymarket); [Investment Officer](https://www.investmentofficer.lu/en/news/prediction-markets-prove-accurate-enough-help-investors-german-study-finds)
- **Vendor and non-peer-reviewed comparisons (all unverified):**
  - NBA 2024–25: Polymarket 67% vs 66% for the average of 9 sportsbooks. — [Polymarket Analytics](https://polymarketanalytics.com/research/nba-sportsbooks-vs-prediction-markets)
  - Calibration error of 2.1 pp across 28,407 resolved markets vs 4.4 pp for sportsbooks, with books unnamed. — [PolySyncer](https://www.polysyncer.com/blog/polymarket-prediction-accuracy)
  - OddsPapi expects Pinnacle to be better calibrated on sports and notes thinner Polymarket books. — [OddsPapi](https://oddspapi.io/blog/prediction-market-accuracy-backtest-polymarket-sportsbooks/)
  - A median arbitrage edge of 0.44% on $4,023 of depth between Polymarket and local bookmakers. — [OddsPapi arbitrage](https://oddspapi.io/blog/polymarket-arbitrage-local-bookmakers/)
- Election-context evidence: Polymarket and Betfair moved simultaneously and led sportsbooks by hours (Aktuğ & Torul). This suggests Polymarket sits in the "exchange" tier of price discovery. — [PDF](https://web.bogazici.edu.tr/torul/polcap.pdf)

### Inferences
- The absence of an FLB in sports (Cardozo & Rivero-Wildemauwe), alongside near-zero NBA arbitrage, suggests Polymarket sports prices may be anchored to sharp-book lines by arbitrageurs and market makers. That is a hypothesis to test directly against Pinnacle closing lines.

### Gaps
- I found no peer-reviewed study benchmarking Polymarket sports prices against Pinnacle or Betfair closing lines (CLV-style), and none on the 2026 World Cup or NFL.
- I found no academic study of in-play (live) Polymarket sports trading, such as latency, reaction to goals, or suspension and halting rules.
- I found no study of how sports-category growth affects platform-wide liquidity or accuracy in non-sports markets (cross-subsidy and attention effects).
- The authors of the NBA arbitrage paper were not captured.

## Q4. Crypto price markets: vs. options-implied distributions; short-horizon up/down markets and bots

### Takeaway
One arXiv paper (Portnaya, Jun 2026) finds a persistent 5–11 pp gap between Polymarket BTC threshold prices and option-implied binary values from Binance and Deribit. The gap is mean-reverting with a roughly 4-hour half-life and is largest in the tails and at long maturities. Short-horizon (5- and 15-minute) up/down markets are dominated by bots, according to trade press. I found no peer-reviewed study of them, though a 2026 synchronized Polymarket–Binance dataset (OpenMarket) now enables one.

### Cited Findings
- **Portnaya, V., "Do Prediction Markets Match Option Prices? Bitcoin Threshold Evidence from Binance and Polymarket," arXiv:2606.19517 (q-fin.TR), 17 Jun 2026.** Verified abstract. Hourly Polymarket "Yes" prices are matched to Binance call-implied discounted binary values at the same strike and maturity. Main contract (Sep 2023 BTC, n = 214): mean gap 5.6 pp (t = 6.46). Pooled across 3 BTC markets (n = 287): 6.3 pp. AR(1) half-life is about 4 hours. Gaps are largest at low implied probabilities and long maturities, which the author attributes to speculative demand. A delta-hedged arbitrage proxy stays profitable after costs but with marginal precision. The Deribit extension shows a gap of about 11 pp; ETH evidence is mixed. Samples are small. — [arXiv](https://arxiv.org/abs/2606.19517)
- **Alonso, I. (GitHub project "implied-odds"), Jul–Oct 2026.** This 75-day study backs implied volatility out of Polymarket daily BTC brackets and compares it with Deribit DVOL. At 24h and 12h before the close, Polymarket bracket probabilities have significantly better Brier scores (paired t > 2) than DVOL-based probabilities. DVOL, a 30-day measure, stays near 37% and misses intraday patterns. It is a single-author, non-peer-reviewed project. — [GitHub](https://github.com/ivanalonso-dev/implied-odds)
- **"OpenMarket: A Synchronized Polymarket–Binance Dataset for High-Frequency Prediction-Market Research,"** arXiv:2607.26245, Jul 2026. The authors note that "reproducible public infrastructure for high-frequency cross-venue work remains scarce." Snippet-only. — [arXiv](https://arxiv.org/html/2607.26245v1)
- **Qin, B. & Yang, R., "Polymarket-v1 Database," arXiv:2606.04217, June 2026.** The database documents an FLB in which low-probability tokens have negative realized returns, attributed to retail overestimation of tail events. Snippet-only. — [arXiv](https://arxiv.org/pdf/2606.04217)
- **Short-horizon up/down markets:**
  - Polymarket reportedly switched 5-, 15-minute and 4-hour crypto up/down markets to Chainlink TWAP settlement on 7 Aug 2026, with a 30-second window for 5-minute markets and 60 seconds for 15-minute and 4-hour markets. Sourced from a dev blog and vendor pages, so unverified. — [DEV Community](https://dev.to/benjamin_cup/polymarket-trading-bot-twap-60s-explained-how-crypto-up-or-down-markets-resolve-15nb)
  - Trade press reports a bot exploiting latency arbitrage against Binance and Coinbase on 15-minute BTC/ETH/SOL markets. A leaderboard review reportedly found 14 of the top 20 profitable wallets were bots; the method is unverified. — [Finance Magnates](https://www.financemagnates.com/trending/prediction-markets-are-turning-into-a-bot-playground/)
  - A taxonomy of bot strategies: pure arbitrage, directional arbitrage, repricing, cross-timeframe, order-book imbalance and near-resolution. Informal. — [Medium](https://medium.com/@RetroValix/6-main-types-of-trading-bots-on-up-down-markets-on-polymarket-f0a6fd836491)
- In the Cardozo & Rivero-Wildemauwe sample, the favorite-longshot bias is robust in the crypto category. — [arXiv](https://arxiv.org/abs/2609.12878)

### Inferences
- The two crypto findings, a persistent wedge at weekly/monthly horizons and Polymarket's edge over DVOL at intraday horizons, fit together. Polymarket appears informative at short horizons where 30-day option-implied measures are poorly matched, and biased in the tails at long horizons. A proper comparison would use the full Deribit implied distribution (Breeden–Litzenberger) at matched expiries, not DVOL.
- The TWAP settlement change (Aug 2026) is a natural experiment on manipulation and latency arbitrage around settlement, but this is unverified.

### Gaps
- No peer-reviewed paper analyzes 5- and 15-minute up/down markets: who trades, bot share, latency-arbitrage profits, fee-rebate economics, or the effect of the TWAP switch.
- No study compares the full Polymarket bracket distribution with the Deribit risk-neutral density at matched expiries. Portnaya uses only single strikes.
- I found nothing on whether Polymarket crypto prices lead or lag spot or perp prices (price discovery). OpenMarket was built to enable this.

## Q5. Geopolitics, war and health markets: research and ethics

### Takeaway
Research on Polymarket geopolitical markets is dominated by informed-trading forensics. Mitts & Ofir (Mar 2026) is the main systematic study and covers Iran strikes and the Maduro capture. Oracle and resolution-governance controversies around Ukraine markets are documented only in news and blogs. Health-market research so far uses Kalshi (Nature-family 2026 paper); Polymarket health and pandemic markets (hantavirus 2026) are covered only by the press. Forecast-accuracy studies of war markets, such as ceasefire timing, appear absent.

### Cited Findings
- **Mitts, J. (Columbia) & Ofir, M. (Haifa), "From Iran to Taylor Swift: Informed Trading in Prediction Markets," SSRN 6426778; Harvard Law Forum post 25 Mar 2026.** Verified via the forum post. Data: all Polymarket markets from Feb 2024 to Feb 2026, covering more than 93,000 markets and about 50,000 wallets. The screen combines 5 signals: cross-sectional bet size, within-trader bet size, profitability, pre-event timing and directional concentration. It flags 210,718 wallet-market pairs, which win 69.9% of the time (more than 60 SD above a permutation null), and estimates about $143M in anomalous profit as a lower bound. Cases: Iran strikes (about $1.2M across 6 new wallets) and the Maduro capture (about $485K from a $38.5K stake). Stated limitations: full portfolios are unobservable, the screen is buy-side only, positions under $500 are excluded and size-limited insiders are missed. Policy options discussed: platform surveillance, contract-level rules for high-risk categories, and CFTC misappropriation rulemaking. — [Harvard Law Forum](https://corpgov.law.harvard.edu/2026/03/25/from-iran-to-taylor-swift-informed-trading-in-prediction-markets/); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6426778)
- **Gómez-Cram et al. (2026)** find insider trading "sporadic and small" and say it does not systematically drive price discovery. This partly contrasts with Mitts & Ofir's $143M aggregate. — [Yale Insights](https://insights.som.yale.edu/insights/wisdom-of-the-few-prediction-markets-are-driven-by-small-number-of-skilled-traders)
- **Iran war markets (journalism):**
  - Bloomberg (2026), using the Polysights database, found about $45M in anomalous flagged transactions on US-strike and ceasefire markets, and cautions this "does not constitute definite proof." — [Bloomberg](https://www.bloomberg.com/graphics/2026-polymarket-bets-iran-war-insider-trading/)
  - Bubblemaps found 9 linked accounts that earned more than $2.4M. — [NPR, 10 Apr 2026](https://www.npr.org/2026/04/10/nx-s1-5780569/betting-polymarket-iran-investigation-lawmakers)
  - Sen. Chris Murphy introduced the BETS OFF Act to bar contracts on war, terrorism and assassination. — [Al Jazeera, 4 Mar 2026](https://www.aljazeera.com/economy/2026/3/4/traders-mint-money-on-betting-platforms-on-us-israel-strike-on-iran)
  - Polymarket apologized over a downed F-15 pilot market. — [Fortune, 6 Apr 2026](https://fortune.com/2026/04/06/polymarket-apology-market-downed-f-15-us-pilot-insider-trading-iran-war)
- **Ukraine markets and oracle governance:**
  - The roughly $7M Trump–Ukraine minerals-deal market (March 2025) resolved "Yes" without a confirmed deal; a whale allegedly controlled about 25% of UMA votes. — [CryptoSlate](https://cryptoslate.com/polymarket-faces-backlash-over-resolving-disputed-7-million-trump-ukraine-market/); [Web3 is Going Great](https://web3isgoinggreat.com/single/polymarket-governance-attack)
  - The roughly $237M Zelensky-suit market (July 2025) resolved "No." — [Decrypt](https://decrypt.co/es/329318/polymarket-dictamina-no-en-controvertida-apuesta-de-237-millones-sobre-el-traje-de-zelensky?amp=1)
  - Ceasefire-market resolution records were inconsistent across archives (unverified).
- **Health:**
  - **"Prediction markets as a collective expectation signal for disease surveillance,"** a Nature Portfolio journal (s44482), 2026. It studies 13 Kalshi public-health markets (measles counts, H5N1 human case, outbreak declarations) as surveillance signals and notes sparse H5N1 and mpox panels. Platform details and authors are snippet-only because the page was behind an auth redirect. — [Nature](https://www.nature.com/articles/s44482-026-00042-6)
  - Polymarket's 2026 hantavirus pandemic market drew nearly $3M; it resolves on WHO "pandemic" wording, not on a PHEIC alone. — [Mother Jones, May 2026](https://www.motherjones.com/politics/2026/05/polymarket-prediction-market-hantavirus-pandemic-epidemic-betting/)
  - Public-health and democracy concerns are raised in The Conversation. — [The Conversation](https://theconversation.com/prediction-markets-are-going-mainstream-what-does-that-mean-for-public-health-and-democracy-291948)

### Inferences
- Geopolitical markets are studied mainly as an integrity problem (insiders, oracles), not as a forecasting or measurement tool. A study evaluating Polymarket war and ceasefire probabilities against expert forecasts (e.g., Good Judgment, Metaculus) or using them as geopolitical-risk shocks (cf. the Caldara–Iacoviello GPR index) would be novel.
- The Mitts & Ofir and Gómez-Cram et al. results conflict on how much insider activity matters. They are reconcilable, since an aggregate $143M can still be small relative to total volume, but a joint test is open.

### Gaps
- I found no academic study of the accuracy of Polymarket Ukraine-ceasefire or Israel–Iran markets, or of their use as a geopolitical risk index linked to oil, defense stocks or sovereign CDS.
- I found no peer-reviewed study of Polymarket H5N1, COVID or hantavirus markets. The existing health work is Kalshi-based.
- The ethics literature is mostly journalism, op-eds and law-forum posts. I found no empirical study of harms from war or death markets, such as incentives to cause outcomes.

## Q6. Explicitly stated open questions, limitations, and survey papers

### Takeaway
The main survey is Rahman, Al-Chami & Clark, "SoK: Market Microstructure for Decentralized Prediction Markets" (arXiv:2510.15612, v1 Oct 2025, v4 Jul 2026). It lists 11 numbered research gaps: insider classification, cross-platform accuracy, copy trading, machine-checkable resolution specs, negRisk, combinatorial markets, AMMs, MEV, oracle guarantees, replay and backtest tooling, and adaptive parameter tuning. Individual papers add questions on cross-venue lead-lag, skill persistence across platforms, media effects and voter influence.

### Cited Findings
- **Rahman, N., Al-Chami, J. & Clark, J., "SoK: Market Microstructure for Decentralized Prediction Markets (DePMs)," arXiv:2510.15612 (v1 17 Oct 2025; v4 8 Jul 2026).** Verified from HTML. The paper uses an 8-stage workflow framework. Its research gaps:
  1. Can insider trades be classified from blockchain data with reasonable precision? Are unregulated markets more insider-prone or more accurate?
  2. Can accuracy metrics compare centralized and decentralized platforms (CePM vs DePM), and does accuracy correlate with microstructure choices?
  3. Can copy traders be classified, is copy trading profitable, and does herding harm accuracy?
  4. Can market topics be written as machine-checkable predicate specifications, with model checking to remove resolution ambiguity?
  5. How does the negRisk gadget affect price parity and execution costs?
  6. Combinatorial and conditional markets, and parlays, are unimplemented in DePMs.
  7. AMMs need adapting to the [$0, $1] bounded and jump-to-resolution constraints.
  8. Measuring MEV on on-chain DePMs, and which order-flow privacy mechanisms apply.
  9. Formal incentive and safety guarantees for oracle voting such as UMA.
  10. No tool exists for replaying and backtesting markets with point-in-time data.
  11. No mechanism exists for automated post-resolution tuning of fees, incentives, liquidity or oracle parameters.

  — [arXiv abs](https://arxiv.org/abs/2510.15612); [HTML](https://arxiv.org/html/2510.15612)
- **"The Anatomy of a Decentralized Prediction Market: Microstructure Evidence from the Polymarket Order Book," arXiv:2604.24366, Apr 2026.** It leaves open whether Polymarket prices lead or follow real-world events and suggests comparing with Kalshi, PredictIt and sportsbooks. Snippet-only. — [arXiv](https://arxiv.org/html/2604.24366v1)
- **Gómez-Cram et al. (2026)**, open questions as relayed by Yale Insights:
  - Do the patterns hold on Kalshi?
  - Will the losing majority keep subsidizing accuracy?
  - How much does multi-wallet identity break account-level identification?
  - Does persistence hold across event types (mention markets vs economic events)?

  — [Yale Insights](https://insights.som.yale.edu/insights/wisdom-of-the-few-prediction-markets-are-driven-by-small-number-of-skilled-traders)
- **Mitts & Ofir (2026)** limitations: hedges and portfolios are unobservable, the screen is buy-side only, there is a $500 floor, and size-limited insiders are missed. — [Harvard Law Forum](https://corpgov.law.harvard.edu/2026/03/25/from-iran-to-taylor-swift-informed-trading-in-prediction-markets/)
- **Cutting et al. (2025):** "future investigations are needed" on mechanism and generalization to other events. — [arXiv](https://arxiv.org/abs/2507.08921)
- **Saguillo et al., "Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets," AFT 2025 (arXiv:2508.03474).** This is described as the first large-scale analysis of combinatorial and conditional arbitrage on Polymarket, covering markets resolved Apr 2024 – Apr 2025. — [IMDEA PDF](https://suarez-tangil.networks.imdea.org/papers/2025aft-arbitrage.pdf); [arXiv](https://arxiv.org/pdf/2508.03474)
- **Dataset papers flag infrastructure gaps:**
  - OpenMarket (arXiv:2607.26245) says public cross-venue high-frequency infrastructure is "scarce." — [arXiv](https://arxiv.org/html/2607.26245v1)
  - "Unlocking the Forecasting Economy" (arXiv:2604.20421) offers datasets across the market lifecycle. — [arXiv](https://arxiv.org/html/2604.20421v1)
  - Qin & Yang, Polymarket-v1 database (arXiv:2606.04217). — [arXiv](https://arxiv.org/pdf/2606.04217)
- **Other relevant 2026 arXiv items, titles only and not read:**
  - "When Certainty Is Not Worth It: Capital Lock-Up and Settlement Discounting in Prediction Markets" (2605.31431). Relevant because capital lock-up biases near-certain prices, which matters when prices are used as probabilities. — [arXiv](https://arxiv.org/pdf/2605.31431)
  - "Manipulation in Prediction Markets: An Agent-based Modeling Experiment" (2601.20452). — [arXiv](https://arxiv.org/html/2601.20452v1)
- **Kalshi-side critique:** Karl Whelan (CEPR/VoxEU) argues the accuracy "promise has not been fulfilled" on Kalshi, which is a caution against treating raw prices as probabilities. — [VoxEU](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market)

### Inferences — synthesized underexplored directions (my synthesis, ranked by apparent novelty × feasibility)
1. **Polymarket tariff, shutdown and recession odds as policy-uncertainty shocks.** Use 5-minute Polymarket series with intraday equity, FX and Treasury data, following the Aktuğ–Torul local-projection design. No study was found.
2. **A Polymarket replication of Fed-staff Kalshi work.** Run FOMC and CPI horse-races against FedWatch, SOFR, inflation swaps and surveys, and test whether offshore, crypto-collateralized pricing (USDC collateral, opportunity cost and capital lock-up) produces systematic wedges.
3. **Full risk-neutral density comparison.** Compare Polymarket BTC/ETH bracket ladders with Deribit Breeden–Litzenberger densities at matched expiries, and test lead-lag with OpenMarket-type synchronized data.
4. **Microstructure and welfare of 5- and 15-minute up/down markets.** Measure bot share, latency-arbitrage rents and fee-rebate economics, and evaluate the Aug 2026 TWAP settlement switch as a natural experiment (the switch date itself is unverified).
5. **Sports efficiency against sharp benchmarks.** Compare Polymarket with Pinnacle and Betfair closing lines in the 2026 World Cup, NFL and NBA, including in-play reaction speed. Also explain why the FLB is absent in sports but present elsewhere.
6. **Media-display effects.** Use the staggered Dow Jones/WSJ (Jan 2026) and X integrations as a difference-in-differences design, and run survey experiments showing Polymarket odds vs polls for 2026 midterm turnout and inevitability beliefs. The voter-influence question is explicitly open in the sources.
7. **Geopolitical-risk index from war and ceasefire markets.** Validate against GPR, oil and defense equities, and benchmark accuracy against Metaculus and Good Judgment.
8. **Health-market surveillance on Polymarket.** Extend the Kalshi-based Nature-family study to Polymarket H5N1, hantavirus and measles markets, accounting for thinness and resolution-wording risk.
9. **Joint insider and skill accounting.** Reconcile the Mitts–Ofir $143M with the Gómez-Cram "sporadic and small" finding, and add multi-wallet clustering, which Gómez-Cram et al. and the SoK both flag.
10. **Resolution-risk premia.** Quantify how UMA dispute risk (e.g., the Ukraine minerals and Zelensky-suit cases) and ambiguous wording drive wedges between price and probability. This connects SoK gaps 4 and 9 to applied users who treat prices as probabilities.

### Gaps
- I could not read the full texts of the SSRN papers (403 errors), the ScienceDirect article or the Nature article. The authors of the FRL DJT paper, the SSRN global-equity paper and the NBA arbitrage paper are unconfirmed.
- I did not verify the "future work" sections of Tsang & Yang (2603.03136), the microstructure paper (2604.24366) or Cardozo & Rivero-Wildemauwe (2609.12878); only abstracts were seen.
- Kalshi and Polymarket research blogs were not searched directly. Polymarket's "The Oracle" newsletter appeared only as a tariff-market source.
- Political science journal or OSF/SocArXiv items specific to Polymarket were not surfaced. Their absence may reflect search limits rather than a true gap.
