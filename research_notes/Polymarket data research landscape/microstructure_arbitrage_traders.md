# Polymarket Data Research Landscape: Microstructure, Liquidity, Price Discovery, Arbitrage, and Trader Behavior/Profitability (2020 – Oct 2026)

Notes compiled 2026-10-15. Labels used: **[Primary, read]** means I read the paper's abstract page or full text. **[Primary, abstract only]** means I saw only the abstract or a listing. **[Secondary]** means the findings come from news, a blog summary, or a citing paper, so check the original before citing. **[Unverified]** means a vendor, affiliate, or anecdotal claim with no stated method.

Most of this literature appeared in 2025–2026. I found almost no peer-reviewed Polymarket-specific microstructure work from 2020–2023 (the AMM era); see the Gaps sections.

---

## Q1. Microstructure of the Polymarket CLOB (spreads, depth, market makers, liquidity rewards, AMM vs CLOB, toxicity, fees)

### Takeaway
Rigorous CLOB microstructure work only started in 2026. Two strands stand out:
- **Dubach (arXiv 2604.24366):** tick-level order-book feed joined to on-chain fills.
- **Qin & Yang (arXiv 2606.04217):** the Polymarket-v1 on-chain trade archive.

Their shared finding is about method: you have to take trade direction from on-chain `OrderFilled` events, because feed-based inference and tick-rule/BVC inference are close to random. That error can flip the sign of spread and Kyle's λ estimates. On fees, the only quantitative source I found is a practitioner analysis (Pine Analytics). It covers the January–March 2026 taker-fee rollout and found no measurable volume damage.

### Cited Findings

**Catalog entries**

**1. Dubach, P. D., "The Anatomy of a Decentralized Prediction Market: Microstructure Evidence from the Polymarket Order Book"** [Primary, read]
- Venue: arXiv:2604.24366 (q-fin.TR). v1 27 Apr 2026, v2 14 May 2026. Single author.
- Data: continuous tick-level archive of Polymarket's public WebSocket order-book feed, about 30 billion events over 52 days, joined to the on-chain trade record. Pre-registered stratified panel of 600 markets; two 7-day windows for direction tests.
- Method: eight stylized facts, effective half-spread, Kyle's λ, self-counterparty (wash) share, cross-sectional depth regression.
- Spreads: longshot markets carry a spread premium, and effective spreads differ across categories.
- Depth: the depth profile is closer to uniform across price levels than concentrated at the top of the book. No block-clock alignment effect.
- Makers: maker wallets are broadly diverse, with a concentrated tail.
- Self-counterparty share: median 1%, upper tail 22%.
- Depth drivers: depth is explained by market duration, price level, and volume. After controlling for duration and p(1−p), the time-to-close coefficient is not significant.
- Trade direction: feed-inferred direction matches on-chain direction in about 59% of buckets (panel mean 0.615, 95% CI [0.58, 0.65]), versus about 80% Lee-Ready accuracy on Nasdaq.
- Sign flips: the effective half-spread changes sign in 67% and 50% of markets (two windows), and Kyle's λ in 60% and 43%.
- Feed latency: median ingestion delay is under 50 ms, with a tail of several seconds.
- Replication package on GitHub and Zenodo.
- Source: [arXiv 2604.24366](https://arxiv.org/abs/2604.24366). Companion blog post: [philippdubach.com](https://philippdubach.com/posts/the-anatomy-of-a-decentralized-prediction-market-notes-from-the-polymarket-order-book/).

**2. Qin, B. & Yang, R., "Polymarket-v1 Database"** [Primary, abstract only]
- Venue: arXiv:2606.04217 (cs.CE). v1 2 Jun 2026, v2 8 Jun 2026.
- Data: the complete on-chain trade archive of Polymarket's first-generation CTF Exchange on Polygon, 21 Nov 2022 – 28 Apr 2026. 1.20B trade records, 1.30M markets, about $61B nominal volume. Aggressor direction is 100% ground truth from settlement. Hosted on Hugging Face.
- Classification accuracy: the tick rule reaches 49.83% and bulk volume classification 50.51%, both near random. Errors follow a price-level gradient tied to positive trade-direction autocorrelation and concentrated market-making.
- Order-flow toxicity: inferred VPIN diverges substantially from true VPIN, and OFI estimates are directionally biased.
- Spreads and forecasting: true VPIN positively predicts Brier scores and Gibbs spread negatively predicts them. High-spread niche markets appear to attract informed specialists rather than noise traders.
- Source: [arXiv 2606.04217](https://arxiv.org/abs/2606.04217).

**3. Tsang, K. P. & Yang, Z., "The Anatomy of a Blockchain Prediction Market: Polymarket in the 2024 U.S. Presidential Election"** [Primary, read]
- Venue: arXiv:2603.03136 (econ.GN). v2 7 May 2026.
- Data: Polygon `OrderFilled`/`OrdersMatched` logs for the 17-outcome 2024 Presidential Election Winner market, 5 Jan – 6 Nov 2024. Transaction-level, daily, 5-minute, and hourly views.
- Volume decomposition: separates exchange trades from minting and burning. For October, the Trump market's raw `OrderFilled` sum is $958.48M, against $391.03M exchange-equivalent volume and $567.45M gross activity. From July to November, raw `OrderFilled` exceeds gross activity by about 60–88%.
- Kyle's λ (Trump YES, rolling 30-day, tick-rule direction, log-odds): spiked to about 0.53 in late July, fell to about 0.04 after September and about 0.01 by October. At p = 0.5, a $1M net buy moved implied probability about 13 points at the spike versus about 0.25 points at λ = 0.01.
- Source: [arXiv 2603.03136](https://arxiv.org/html/2603.03136v2).

**4. Slivkoff, S. (Paradigm), "Polymarket Volume Is Being Double-Counted"** [Secondary]
- Date: 8 Dec 2025.
- Claim: summing `OrderFilled` events double-counts both contracts and USD, because maker and taker legs each emit an event. Example: a $4.13 trade is recorded as $8.26.
- Polymarket's data team disputed that its own reporting is affected. Paradigm's CEO amplified the post one week after Paradigm led a Kalshi round, a possible conflict of interest.
- Sources: [Paradigm](https://www.paradigm.xyz/2025/12/polymarket-volume-is-being-double-counted); [Unchained](https://unchainedcrypto.com/paradigm-claims-polymarket-trading-figures-are-double-counted/); [rekt.news](https://rekt.news/the-big-blind).

**5. Rahman, N., Al-Chami, J. & Clark, J., "SoK: Market Microstructure for Decentralized Prediction Markets (DePMs)"** [Primary, abstract only]
- Venue: arXiv:2510.15612 (cs.CE). v1 17 Oct 2025; v4 8 Jul 2026.
- Scope: an eight-stage design workflow (infrastructure through archiving). States that "modern DePMs like Polymarket deviate materially from earlier designs like Truthcoin and Augur v1."
- Tsang & Yang note that it is a broad survey, not a Polymarket-specific empirical study.
- Source: [arXiv 2510.15612](https://arxiv.org/abs/2510.15612).

**6. Pine Analytics, "Polymarket Fee Rollout: Revenue Impact and Market Implications"** [Primary practitioner blog; numbers are the author's estimates from a 7-day Dune query]
- Date: 25 Mar 2026.
- Rollout dates: crypto taker fees began 5 Jan 2026 on 15-minute markets and covered all crypto timeframes by 6 Mar. Sports fees began 18 Feb. Nearly all remaining categories followed 30 Mar 2026. Geopolitics stays fee-free.
- Fee formula: fee = C × p × feeRate × (p(1−p))^exponent.
- Post-rollout peak effective rates: Crypto 1.80%, Economics 1.50%, Culture and Weather 1.25%, Politics, Finance, and Tech 1.00%, Sports 0.75%.
- Maker rebates: 20% of taker fees in Crypto, 25% in most categories, 50% in Finance, paid daily pro rata to filled maker volume. Referral payouts are 30% (direct) and 10% (indirect).
- Volume: crypto settled at $73–100M per day after a spike, which the author calls a modest pullback within normal variance. Sports rose from $100–150M to $150–250M per day after fees. Taker volume is about $160M/day, roughly half of the ~$350M notional Polymarket reports.
- Revenue: about $1.2M/day gross fees and about $573K/day net, roughly $209M annualized (range $209–342M). Blended effective fee about 0.76% of taker volume.
- No spread measurements.
- Source: [Pine Analytics](https://pineanalytics.substack.com/p/polymarket-fee-rollout).
- Corroborating news: [Cryptopolitan](https://www.cryptopolitan.com/polymarket-introduces-taker-fees/) reports that the 15-minute crypto taker fees fund a Maker Rebates Program. [Polymarket US docs](https://docs.polymarket.us/fees) say the US exchange moves maker/taker rebates to volume tiers on 19 Oct 2026.
- Caveat: affiliate and blog sources give conflicting category rates ([Sacra](https://sacra.com/c/polymarket/), [StartPolymarket](https://startpolymarket.com/learn/polymarket-fees/)).

**7. Becker, J., "The Microstructure of Wealth Transfer in Prediction Markets"** [Primary, read; Kalshi data, included as the closest maker/taker comparator]
- Date: 18 Jan 2026 (web); SSRN 7217640, dated 1 Aug 2026.
- Data: Kalshi, Jun 2021 – Nov 2025. 72.1M trades, $18.26B volume.
- Maker vs taker: takers average −1.12% excess return and makers +1.12%. Takers are negative at 80 of 99 price levels.
- Time trend: the maker/taker gap swung 5.3 pp in makers' favor after the 2024 election. Before that, takers averaged +2.0% from launch through 2023.
- Longshots: 5¢ contracts won 4.18% of the time.
- No Polymarket results of its own. Cites Reichenbach & Walther on Polymarket as consistent.
- Source: [jbecker.dev](https://jbecker.dev/research/prediction-market-microstructure).
- Becker's open dataset (the largest public Polymarket and Kalshi trade data, 36 GiB Parquet, gathered via the API and blockchain indexers): [GitHub jon-becker/prediction-market-analysis](https://github.com/jon-becker/prediction-market-analysis).

**8. Bürgi, Deng & Whelan, "Makers and Takers: The Economics of the Kalshi Prediction Market"** [Secondary; Kalshi comparator]
- Venue: CEPR DP20631 / CESifo WP 2025.
- Data: more than 300,000 contracts.
- Findings: makers earn more than takers, and both show a favorite–longshot pattern.
- Source: [CEPR](https://cepr.org/publications/dp20631).

**Other related items, not read in full**
- "OpenMarket: A Synchronized Polymarket-Binance Dataset for High-Frequency Prediction-Market Research" (arXiv 2607.26245, 2026). I saw only its reference list. [arXiv](https://arxiv.org/pdf/2607.26245)
- "Optimal Market Making in Prediction Markets" (arXiv 2607.17991, 2026). Title only seen. [arXiv](https://arxiv.org/pdf/2607.17991)
- "Resolution-Aware Perpetual Futures on Binary Prediction Markets… Using Polymarket Data" (arXiv 2605.10400, 2026). Title only. [arXiv](https://arxiv.org/pdf/2605.10400)

### Inferences
- Any spread, Kyle's λ, VPIN, or OFI result for Polymarket that relies on tick-rule, BVC, or WebSocket-feed direction is suspect. Dubach and Qin & Yang independently show near-random direction accuracy. Tsang & Yang's λ uses the tick rule, so it falls under this critique.
- Raw `OrderFilled` sums overstate volume by roughly 2x (Paradigm), and minting and burning distort things further (Tsang & Yang). Volume-based liquidity and growth metrics across dashboards are not comparable without normalization.
- Pine Analytics finds taker volume is about half of reported notional, which is consistent with the double-counting critique.

### Gaps
- **AMM era (2020 – ~late 2022):** I found no empirical study of Polymarket's FPMM/AMM-era liquidity, or a formal AMM-versus-CLOB comparison. The SoK may cover it qualitatively; I could not confirm. The Polymarket-v1 database starts 21 Nov 2022, which marks roughly when the CTF Exchange went live.
- **Liquidity rewards program:** I found no causal study of the quote-based rewards on spreads or depth.
- **Fee effects:** I found no academic study of the 2026 fees' effect on spreads or depth; Pine Analytics reports no spread data.
- **Numbers:** Dubach's abstract gives no numeric spread or depth levels; the full PDF tables would be needed.

---

## Q2. Price discovery and information aggregation (news events, lead-lag vs Kalshi and other venues)

### Takeaway
The core cross-venue paper is Ng, Peng, Tao & Zhou (SSRN 5331995). Polymarket led Kalshi around the 2024 election, but leadership is two-way across 2023–2026 matched markets: Kalshi leads more in sports, Polymarket in politics and entertainment. Event-level evidence is thin. Tsang & Yang show YES+NO deviations decaying in under a minute by October 2024, and a 2026 paper links large price dislocations to higher press citation.

### Cited Findings

**1. Ng, H., Peng, L., Tao, Y. & Zhou, D., "Price Discovery and Trading in Modern Prediction Markets"** [Primary, abstract via search; the SSRN page returned 403]
- Venue: SSRN 5331995, version dated 27 Apr 2026.
- Data: Polymarket, Kalshi, PredictIt, and Robinhood. Matched markets 2023–2026.
- Findings: around the 2024 election, Polymarket led Kalshi, particularly when liquidity and activity were high. Across matched markets, leadership runs both ways: Kalshi leads more in sports, Polymarket in politics and entertainment.
- Sources: [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5331995); described in [Tsang & Yang](https://arxiv.org/html/2603.03136v2).
- A citing review (seen only through search) reports persistent cross-platform probability gaps. Its October–November 2024 Trump-YES weekly spread chart sits above a ~2% arbitrage break-even [Secondary].

**2. Tsang & Yang (arXiv 2603.03136)** [Primary, read]
- YES+NO deviation half-lives (AR(1), 5-minute bars):
  - Trump: about 2 hours in April 2024, 0.74 minutes in October, 0.67 minutes in November.
  - Harris: over 30 hours in March–April, a few minutes after late July.
  - Biden: about 3 hours at peak, about 8 minutes by July.
- Disagreement: the 90-day correlation between Trump-YES and Democratic-side net inflows rose from about 0.17 to 0.76 in early October 2024, and fell after the 10 Sep debate.
- Inflows: Trump-YES net inflow rose from about $0.1M (end-September) to nearly $5M on 3 Oct.
- The authors read two-sided inflows as heterogeneous beliefs, not one-sided manipulation.
- Source: [arXiv 2603.03136](https://arxiv.org/html/2603.03136v2).

**3. Ibrahim, H. & Zaki, Y., "Price Dislocations, News Citations, and Epistemic Leverage on Polymarket"** [Primary, abstract]
- Venue: arXiv:2609.06005, 5 Sep 2026.
- Data: 173.7M signed trades; 6,990 news articles from 2024–2025; 44,976 dislocations, defined as moves of at least 5 pp backed by concentrated one-sided flow.
- Citations: a market's citation rate is about 33% higher in the days after a dislocation (log ratio 0.283, p = 0.001). Prominence predicts citation more than move size (β 0.610 vs 0.159).
- Epistemic leverage: about $0.7–1.0M of flow is needed to move a market 5 pp and get the move cited.
- Source: [arXiv 2609.06005](https://arxiv.org/abs/2609.06005).

**4. Gómez-Cram, Guo, Kung (LBS) & Jensen (Yale), "Prediction Market Accuracy: Crowd Wisdom or Informed Minority?"** [Secondary, via The Block]
- Venue: SSRN 6617059, revised 25 Apr 2026.
- Data: every Polymarket trade 2023–2025; 1.72M accounts, 210,322 markets, $13.76B.
- Conclusion: accuracy reflects "the wisdom of an informed minority." 3.14% of accounts' order flow predicts short-term price moves and outcomes.
- Source: [The Block](https://www.theblock.co/post/398902/skilled-polymarket-traders-are-a-3-minority-and-everyone-else-funds-their-gains-study).

**5. Clinton, J. & Huang, T. (Vanderbilt)** [Secondary]
- Data: all political markets on Kalshi, PredictIt, and Polymarket in the final five weeks of the 2024 election.
- Reported accuracy: Polymarket about 67%, Kalshi 78%, PredictIt 93%. Inefficiency rose near the end, with significant cross-platform price divergences.
- Kalshi disputes the methodology.
- Source: [DL News](https://www.dlnews.com/articles/markets/polymarket-kalshi-prediction-markets-not-so-reliable-says-study).

**6. Reichenbach, F. & Walther, M., "Exploring Decentralized Prediction Markets: Accuracy, Skill, and Bias on Polymarket"** [Secondary]
- Venue: SSRN 5910522, 2025.
- Data: more than 124M trades, about $48B volume.
- Findings: markets are "accurate most of the time," with biases such as overtrading 'Yes' or default options.
- A follow-up is listed: "When Can Prediction Market Prices Be Trusted?" (SSRN 7552098, 2026).
- Sources: [Investment Officer](https://cms.investmentofficer.com/en/news/prediction-markets-prove-accurate-enough-help-investors-german-study-finds); [Becker repo bibliography](https://github.com/jon-becker/prediction-market-analysis).

**7. Cardozo, M. & Rivero-Wildemauwe, J. I., "The Favorite-Longshot Bias in Prediction Markets: Evidence from Polymarket"** [Primary, abstract]
- Venue: arXiv:2609.12878, 11 Sep 2026.
- Data: 588M trades by 2.48M accounts.
- Returns by price: purchases below 10¢ lose 19.3¢ per $1, and purchases at 90¢ or above earn 0.83¢.
- Grouping sensitivity: longshots lose 6.3¢ with equal weighting but gain 4.1¢ when grouped by parent event.
- Categories: the pattern holds in Crypto and Politics but is absent in Sports.
- Source: [arXiv 2609.12878](https://arxiv.org/abs/2609.12878).

**8. Akey et al., "Trades, Quotes, and Price Discovery in Prediction Markets"** [Title only]
- Venue: SSRN 7547106, 2026. Listed in Becker's bibliography; not read.
- Source: [GitHub](https://github.com/jon-becker/prediction-market-analysis).

### Inferences
- Cross-venue leadership appears to depend on where liquidity and the natural clientele sit: crypto-native or international users in politics, US sports bettors on Kalshi. This is my reading of Ng et al.'s category split, not a claim the authors tested.
- Within-market parity arbitrage tightened from hours to under a minute between spring and October 2024. This is consistent with professional market makers and arbitrage bots entering as election volume grew.

### Gaps
- I found no event-study papers on Polymarket reactions to specific debates, court rulings, Fed (FOMC) announcements, earnings, or live sports scoring, beyond the NBA arbitrage paper in Q3.
- I found no lead-lag studies of Polymarket versus Betfair, options, equities, or crypto spot or perps. The OpenMarket Polymarket–Binance dataset (arXiv 2607.26245) is the likely starting point, but I did not see its findings.
- The Ng et al. full text was not accessible, so I have no magnitudes (information shares, lead times).

---

## Q3. Arbitrage (intra-market YES+NO, NegRisk/combinatorial, cross-venue, logical dependency)

### Takeaway
The anchor paper is Saguillo et al. (AFT 2025). Using on-chain data from Apr 2024 to Apr 2025, it estimates about $39.6M of realized arbitrage profit. Most of it came from NegRisk multi-outcome rebalancing (about $29M) and single-condition YES+NO trades (about $10.6M). Cross-market logical-dependency arbitrage was tiny, about $95K in election pairs. A 2026 NBA study finds that later, live-sports arbitrage is rare, short-lived (seconds), and depth-constrained to retail size. Rigorous cross-venue (Polymarket–Kalshi) arbitrage evidence is essentially absent; the figures are blog or vendor claims.

### Cited Findings

**1. Saguillo, O., Ghafouri, V., Kiffer, L. & Suarez-Tangil, G., "Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets"** [Primary, full text read]
- Venue: arXiv:2508.03474 (cs.CR / q-fin.TR), 5 Aug 2025. Published at AFT 2025 (LIPIcs vol. 354, paper 27). Authors are at IMDEA Networks.
- Data: markets resolving 1 Apr 2024 – 1 Apr 2025, with Polygon transaction traces of the Conditional Token contract from 1 Jan 2024 – 1 Apr 2025.
  - Events used: `OrderFilled`, `PositionSplit`, `PositionsMerge`.
  - About 86M bids, filtered at $2 or more.
  - 8,659 single-condition markets plus 1,578 NegRisk markets (8,559 conditions), 17,218 conditions in total.
- Method: detection thresholds were no token above $0.95 and profit of at least $0.05 per $1. An LLM (DeepSeek-R1-Distill-Qwen-32B) plus heuristics (end date, topic) find dependent market pairs, with manual validation.
- Opportunity counts:
  - 7,051 conditions had at least one single-condition opportunity (2,628 NegRisk, 4,423 single). All were long-side (sum < $1).
  - 662 of 1,578 NegRisk markets had opportunities, averaging about 100 per market.
  - In the Nov-5-2024 politics group (128 NegRisk plus 177 single markets, 46,360 pairs), 13 dependent pairs were confirmed.
- Realized single-condition arbitrage: buying below $1 earned $5,899,287; selling above $1 earned $4,682,075.
  - Notable trade: one account (@Tutaaa91) bought YES and NO each under $0.02 for a single-trade profit of $58,983.
- Realized NegRisk (within-market) arbitrage: buy YES $11,092,286; buy NO $17,307,114; sell YES $612,189; sell NO $4,264.
  - Buying NO dominates. Politics dominates the total: the November election, plus August's Democratic nominee and VP picks.
  - Sports are largely absent from realized NegRisk arbitrage, though Sports has the most detected long opportunities.
- Realized combinatorial (cross-market) arbitrage: value was extracted in 5 of 11 pairs, about $95K total ($60,237, $18,472, $15,819, $629). None in NegRisk–Single pairs.
- Totals and concentration: $39,587,585 across all strategies (assuming ε = $1 profit per trade). The top account earned $2,009,632. Several accounts show bot-like bid counts.
- Sources: [arXiv abs](https://arxiv.org/abs/2508.03474); [AFT 2025 / Dagstuhl](https://drops.dagstuhl.de/storage/00lipics/lipics-vol354-aft2025/html/LIPIcs.AFT.2025.27/LIPIcs.AFT.2025.27.html); full text from [arXiv PDF](https://arxiv.org/pdf/2508.03474).

**2. Cheng, G., Yang, J. & Zou, H., "Arbitrage Analysis in Polymarket NBA Markets"** [Primary, read]
- Venue: arXiv:2605.00864 (q-fin.TR), 22 Apr 2026.
- Data: CLOB `GET /book` polling, 173 NBA games, 4 Feb – 4 Mar 2026. 75,088,497 Level-1 snapshots, with a 3.6–5.5 s sweep latency.
- Single-market (YES+NO) arbitrage: only 7 valid in-game episodes. Of 37 raw candidates, 30 were post-game artifacts after makers withdrew. Median duration about 3.6 s. Capped profit $210 ($4,418 uncapped).
- Combinatorial (moneyline vs spread): 290 valid episodes (279 in-game) out of 8.59M states.
  - Median in-game duration 16 s, median yield about 101 bp. Opportunities cluster late in games.
  - In 76.9% of episodes, $100 could not be fully deployed; average executable size was 14.8 shares.
  - Capped profit $560 ($2,033 uncapped).
- Conclusion: risk-free extraction is limited to retail-scale amounts.
- Source: [arXiv 2605.00864](https://arxiv.org/html/2605.00864v1).

**3. Tsang & Yang:** YES+NO parity deviations in the election market had half-lives under 1 minute by October–November 2024 (see Q2). [arXiv 2603.03136](https://arxiv.org/html/2603.03136v2)

**Cross-venue Polymarket–Kalshi**
- Academic evidence: persistent cross-platform gaps in 2024 (Ng et al. 2026; Clinton & Huang), with no net-of-fee executability study. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5331995)
- Claims of 2–5% spreads on major events are [Unverified]: [Dropstab](https://news.dropstab.com/research/kalshi-vs-polymarket).
- A claim that "an IMDEA study found profitable players were sub-second bots" is [Unverified]; it may refer to Saguillo et al. [newyorkcityservers blog](https://newyorkcityservers.com/blog/prediction-market-arbitrage-guide).
- Frictions cited by practitioners [Unverified]: contracts are not identical (e.g., Fed-decision buckets vs rate ladders), and resolution rules differ (the "same" shutdown event reportedly resolved differently on the two venues).
- Open-source bots: [ImMike/polymarket-arbitrage](https://github.com/ImMike/polymarket-arbitrage). Practitioner explainer: [Trevor Lasn](https://www.trevorlasn.com/blog/how-prediction-market-polymarket-kalshi-arbitrage-works).
- A GitHub PR from a hobbyist reported "no lead-lag between Kalshi and Polymarket" in a first live sample [Unverified, trivial sample]: [GitHub PR](https://github.com/pointlessbassmusic-byte/pointless-repo/pull/33).

### Inferences
- Polymarket arbitrage profit ran heavily through NegRisk "buy all NO / buy all YES" rebalancing in politically salient multi-outcome markets during 2024. By 2026, at least in NBA live markets, residual opportunities were seconds-long and book-depth-limited. This is consistent with professionalized arbitrage, though the two studies differ in method (on-chain realized profit versus polled L1 snapshots).
- The $40M figure is an upper-bound style estimate. It assumes ε = $1 per trade and counts any YES+NO deviation in a user's acquisitions as arbitrage, so it may include directional trades that happened to net out.

### Gaps
- I found no rigorous, fee-adjusted, timestamp-synchronized cross-venue arbitrage study (Polymarket–Kalshi, Polymarket–Betfair, Polymarket–sportsbooks).
- I found no study of arbitrage after the 2026 fee introduction. Fees peak at p = 0.5 and should widen no-arbitrage bands; this is untested.
- Logical-dependency arbitrage beyond election pairs (e.g., nested crypto price ladders, date ladders) remains unquantified.

---

## Q4. Trader profitability distributions (share profitable, whale concentration, bots and makers, copy-trading, smart money, behavior)

### Takeaway
Several independent 2026 academic studies agree on extreme concentration:
- **Akey et al.:** the top 1% of users capture 76.5% of profits.
- **Gómez-Cram et al.:** 3.14% of accounts are statistically "skilled."
- **Della Vedova:** winners are distinguished by execution and timing, not forecasting. Bots earned about $133M at 49.9% accuracy while retail lost about $79M at 51.3%.

Limit-order liquidity provision (making) predicts profit, and market-order or longshot buying predicts losses. Headline "X% of wallets lose" numbers range from about 16% to 72% profitable, depending on wallet filters and whether splits and merges are counted.

### Cited Findings

**1. Akey, P., Grégoire, V., Harvie, N. & Martineau, C., "Who Wins and Who Loses in Prediction Markets? Evidence from Polymarket"** [Primary abstract via HEC seminar page plus secondary]
- Venue: SSRN 6443103 / CEPR DP 21615, 2026.
- Data: 588M trades, about $67B, more than 2.4M users, 2022–2026.
- Concentration: the top 1% of users capture 76.5% of profits.
- Strategy: winners provide liquidity with limit orders, and losers take liquidity with market orders. Market-making strongly predicts positive performance, and longshot betting drives losses.
- Persistence: monthly persistence is weak and may reflect selection. Insider trading is unlikely to explain the largest winners.
- Sources: [HEC Paris](https://www.hec.edu/en/faculty-research/events/who-wins-and-who-loses-prediction-markets-evidence-polymarket); [RePEc CEPR](https://econpapers.repec.org/RePEc:cpr:ceprdp:21615); [FlowingData](https://flowingdata.com/2026/05/14/more-people-losing-money-in-prediction-markets/).
- A related Bloomberg analysis found more than 100,000 accounts lost at least $1,000 since the start of 2025 [Secondary, via FlowingData].

**2. Gómez-Cram, Guo, Kung & Jensen** (SSRN 6617059, Apr 2026) [Secondary, via The Block]
- Data: 1.72M accounts, 2023–2025.
- Method: sign-randomization test (10,000 flips per trader), with out-of-sample validation.
- Skill: 3.14% of accounts are skilled winners. Skilled winners plus market makers are under 3.5% of accounts but capture more than 30% of gains.
- Raw P&L vs skill: only 12% of top earners are in the skilled group. About 60% of "lucky winners" revert to losses.
- Persistence: 44% of skilled accounts stay skilled out of sample, versus about 10% for active mutual funds.
- Losses: the 67% of accounts classified as losers absorb all aggregate losses.
- Insiders: 1,950 accounts flagged, moving prices about 7–12x more per dollar than skilled traders. Case study: three accounts made more than $630K on Maduro's ouster before disclosure.
- Source: [The Block](https://www.theblock.co/post/398902/skilled-polymarket-traders-are-a-3-minority-and-everyone-else-funds-their-gains-study).

**3. Della Vedova, J., "Who Profits from Prediction Markets? Execution, not Information"** [Secondary]
- Venue: SSRN 6191618, Feb 2026.
- Data: 222M resolved Polymarket trades.
- Accuracy vs profit: retail picks the right side 51.3% of the time but loses money (about −$79M). Automated traders at 49.9% accuracy earn about $133M.
- Timing: bots enter more than 8 days before resolution versus about 3 days for casual retail. About 70% of the bot edge comes from timing, the rest from spread capture and execution.
- Skill separation: direction and execution skill are nearly independent (shared variance under 1%; the correlation is reported as about 0.13). Bots pay 2.52¢ less per contract.
- Benchmark: no trader type beats the price-implied accuracy benchmark. The inversion does not replicate in 14.1M CBOE option contracts.
- Sources: [Quantpedia](https://quantpedia.com/who-profits-from-prediction-markets/); [Marginal Revolution](https://marginalrevolution.com/marginalrevolution/2026/03/who-profits-from-prediction-markets.html); [European Business Magazine](https://europeanbusinessmagazine.com/?p=139574).

**4. Cardozo & Rivero-Wildemauwe** (arXiv 2609.12878) [Primary, abstract]
- Account-level behavior: the top decile of past longshot buyers makes 26.6% of next-month low-price purchases, with returns similar to others. The top decile of favorite buyers makes 15.1% of high-price purchases and earns less.
- Source: [arXiv](https://arxiv.org/abs/2609.12878).

**5. Saguillo et al.:** the top arbitrage account earned $2.01M. Bot-like accounts dominate arbitrage profit. [arXiv](https://arxiv.org/abs/2508.03474)

**6. Tsang & Yang (2024 election):**
- Participation: 39.3% of traders were only in the Trump market and 18.4% only in Harris. 19.4% were active in all four Trump/Harris YES/NO books, consistent with market-making or hedging.
- Timing: activity peaks 09:00–20:00 UTC; the top 10% of traders peak 14:00–17:00 UTC.
- Late October: Democratic-side traders outnumbered pro-Trump traders, but pro-Trump traders held more dollar volume.
- Source: [arXiv](https://arxiv.org/html/2603.03136v2).

**7. Chen, H., Duan, X., El Saddik, A. & Cai, W., "Political Leanings in Web3 Betting"** [Primary, abstract]
- Venue: arXiv:2407.14844, Jul 2024; ACM WebSci '25.
- Data: more than 15,000 addresses, 4,500 events, 8,500 markets.
- Method: a Political Betting Leaning Score related to more than 800 behavioral features, with a case study of the 2022 Senate race.
- The abstract gives no headline numbers.
- Source: [arXiv](https://arxiv.org/abs/2407.14844).

**8. Solidus Labs (surveillance vendor)** [Secondary, vendor with commercial interest]
- Data: politics markets, Dec 2025 – Feb 2026.
- Concentration: 0.55% of profitable maker wallets captured 50% of gains, and 0.26% of winning taker wallets captured nearly the same share (about $8M of about $16M each).
- Wash-like activity: about 15% of volume in some markets showed self-trading or neutral patterns. The article's example uses Trump/Harris, which does not fit a Dec 2025 – Feb 2026 window, so treat the details cautiously.
- Source: [CoinDesk](https://www.coindesk.com/markets/2026/04/29/a-tiny-group-is-winning-on-polymarket-as-under-1-of-wallets-take-half-the-profits).

**9. Wallet-level headline stats** [Unverified; independent analysts and aggregators]
- 84.1% of 2.5M wallets unprofitable as of 1 Apr 2026, with 840 addresses (0.033%) above $100K. This updates an earlier December 2025 finding of 70% unprofitable among 1.7M addresses; including splits and merges raised the loss rate. [KuCoin News](https://www.kucoin.com/news/flash/84-of-polymarket-traders-are-losing-money-0-033-capture-majority-profits); [TechFlow](https://www.techflowpost.com/en-US/article/31018)
- Polycopy: about 23% of wallets with 5 or more resolved trades are profitable. [polycopy.app](https://polycopy.app/best-polymarket-traders)
- Vultax: 36 wallets took 44% of gains; winners repeat 41–51% of the time. In July 2026, one-trade wallets were profitable 12.2% of the time versus 63.7% for wallets with 6–20 trades. [Vultax](https://vultax.com/research/best-polymarket-traders-leaderboards)
- Contradiction: one analysis of 242,640 traders reports 72% profitable, which conflicts sharply with the others. [Search summary; source not isolated]

### Inferences
- The convergent finding is that P&L on Polymarket is a transfer from liquidity takers (often longshot and late entrants) to liquidity providers and early, well-timed entrants, many automated. This matches Kalshi evidence (Becker; Bürgi–Deng–Whelan).
- The "% profitable" figure is extremely definition-sensitive: denominator filters, split/merge accounting, realized versus mark-to-market. Academic numbers (Akey, Gómez-Cram) should be preferred over aggregator stats.

### Gaps
- I found no rigorous study of copy-trading effects (follower returns, front-running of copied wallets) or leaderboard-selection bias, beyond the vendor sites above.
- Akey et al. and Della Vedova full texts were not accessed directly. Figures come from abstracts and secondary summaries.

---

## Q5. On-chain analytics using Polygon data (CTF exchange, conditional tokens, USDC flows, growth, retention, geography, network/clustering, wash trading)

### Takeaway
The main on-chain network paper is Sirolly, Ma, Kanoria & Sethi on wash trading (Columbia, SSRN 5714122, Nov 2025). Secondary coverage says about 25% of 2022–2025 volume was likely wash trading, with peaks near 60%. Dubach's direct self-counterparty measure is much lower: median 1%, tail 22%. On-chain mechanics are well documented in Saguillo et al. and Tsang & Yang (`OrderFilled`, `PositionSplit`, `PositionsMerge`, exchange as counterparty for mint and burn). Two large open datasets now exist: Polymarket-v1 (1.2B trades) and Becker's. I found no rigorous geography, VPN, or retention studies.

### Cited Findings

**1. Sirolly, A., Ma, H., Kanoria, Y. & Sethi, R., "Network-Based Detection of Wash Trading"** [Primary blog by co-author plus secondary]
- Venue: SSRN 5714122. Versions Nov 2025 and Jan 2026. Not peer reviewed.
- Method: iterative network scoring. Each wallet gets an initial score from repeated open/close behavior, then is updated by volume-weighted counterparties' scores. The core idea is that wash traders show homophily (closed clusters) while market makers show heterophily.
- Example: a 200-wallet "MAY" cluster traded more than 116M shares and more than $113M with an aggregate P&L of −$57.86.
- Sources: [Sethi Substack, 12 Nov 2025](https://rajivsethi.substack.com/p/the-detection-of-wash-trading); [Columbia Business School press](https://business.columbia.edu/faculty/press/polymarket-volume-inflated-artificial-activity-study-finds).
- Headline estimates [Secondary; sources conflict]:
  - About 25% of trades 2022–2025 likely wash.
  - Cointelegraph: nearly 60% of volume in July 2024 and about 20% in early October 2025. A MEXC summary dates the 60% peak to December 2023.
  - Coverage conflicts on whether Polymarket itself was implicated. The authors call the estimates non-definitive.
  - Sources: [Cointelegraph](https://cointelegraph.com/news/columbia-study-polymarket-wash-trading-research); [Coin360](https://coin360.com/news/columbia-study-polymarket-wash-trading-25-volume).

**2. Dubach (arXiv 2604.24366):** self-counterparty share median 1%, upper tail 22%, measured from on-chain fills over 52 days in 2026. [arXiv](https://arxiv.org/abs/2604.24366)

**3. Saguillo et al.: on-chain mechanics and data sources** [Primary, read]
- A Polymarket match mints YES and NO when two buy orders' prices sum to $1, locking USDC in the Conditional Tokens contract.
- `OrderFilled` captures every token-for-USDC trade, and the exchange appears as counterparty on mints.
- `PositionSplit` and `PositionsMerge` record USDC locking and withdrawal.
- NegRisk markets share a market ID across conditions.
- Data came from transaction traces of the Conditional Token contract, plus the py-clob-client and Gamma API for metadata. The paper cites a Dune UMA-dispute dashboard and Jeremy Whittaker's 2024 Python data guide.
- Source: [arXiv PDF](https://arxiv.org/pdf/2508.03474).

**4. Tsang & Yang:** a transaction-level decomposition separating exchange trades from mint and burn, which yields exchange-equivalent volume, net inflow, and gross activity. October 2024 net inflow was $176.4M (Trump) and $106.2M (Harris). [arXiv](https://arxiv.org/html/2603.03136v2)

**5. Paradigm (Slivkoff, Dec 2025):** `OrderFilled` double-counting; see Q1. [Paradigm](https://www.paradigm.xyz/2025/12/polymarket-volume-is-being-double-counted)

**6. Datasets**
- Polymarket-v1 Database: CTF Exchange on Polygon, Nov 2022 – Apr 2026, 1.20B trades, $61B. [arXiv](https://arxiv.org/abs/2606.04217)
- Becker's Polymarket and Kalshi trade dataset. [GitHub](https://github.com/jon-becker/prediction-market-analysis)
- Cardozo & Rivero-Wildemauwe and Akey et al. both use 588M trades across about 2.4–2.5M accounts. This suggests a common underlying dataset, possibly Becker's (my inference).

**7. Market formation and geography**
- "What Prediction Markets Can See: Market Formation, Settlement Legibility, and the Geography of Tradable Uncertainty in Africa and Latin America" (arXiv 2606.17503, 2026). Title only seen; it concerns which events get markets, not user geography. [arXiv](https://arxiv.org/pdf/2606.17503)

### Inferences
- Wash-trading estimates differ by an order of magnitude (Sirolly et al. about 25% average and 60% peaks versus Dubach's 1% median). Window (2022–2025 versus 2026), definition (network clusters versus same-wallet self-fills), and weighting (volume versus market median) all differ. They are not directly comparable.
- Airdrop or points farming is a plausible driver of wash volume (Solidus and press speculation about a POLY token). No study I read establishes it causally.

### Gaps
- Geography and VPN usage: I found no rigorous on-chain or traffic-based study.
- User growth and retention cohorts: I found no academic study. Dune dashboards exist but I did not verify specific ones.
- USDC flow, bridging, and on/off-ramp analyses: none found.
- Funding-source clustering of whales (e.g., the 2024 "Théo" accounts) appears only in news, not in a paper I could verify.
- Galaxy, Messari, Delphi, a16z, and Flashbots Polymarket reports: not searched within the tool budget, so treat this as a coverage gap rather than evidence of absence.
