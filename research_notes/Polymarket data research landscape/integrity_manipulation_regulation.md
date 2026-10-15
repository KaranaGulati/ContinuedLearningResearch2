# Polymarket Market Integrity: Wash Trading, Insider/Informed Trading, Manipulation, Oracle Integrity, and Regulation (2020 – Oct 2026)

Research date: 2026-10-15. Notes compiled from about 22 search/fetch calls. Primary sources (SSRN, CNN, Bloomberg) were often blocked (403/451), so many figures come from reputable secondary coverage (CoinDesk, The Block, Fortune, Decrypt, law-firm memos). Each item is marked with its source tier. **[UNVERIFIED]** marks claims that rest on one weak source or on prior knowledge not confirmed in this session.

---

## 1. Wash trading studies (methods, share of volume, incentives)

### Takeaway
Two main quantitative estimates exist. The first is a forensic estimate from Chaos Labs and Inca Digital (Oct 2024): about one-third of the 2024 presidential market's volume was wash trading. The second is a Columbia SSRN working paper (Nov 2025, "Network-Based Detection of Wash Trading"): about 25% of all Polymarket volume over roughly three years, peaking near 60% of weekly volume in Dec 2024. Both point to token-airdrop or leaderboard farming as the incentive, helped by zero fees and no KYC.

### Cited Findings

**A. Columbia Business School / Columbia University, "Network-Based Detection of Wash Trading" (SSRN abstract 5714122, posted ~Nov 6, 2025; not peer reviewed)**
- SSRN link: papers.ssrn.com/sol3/papers.cfm?abstract_id=5714122. Released about Nov 6, 2025; coverage dated Nov 7, 2025. — [CoinDesk](https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds)
- Authors: four authors, including Columbia Business School professor Yash Kanoria — [FinanceFeeds / coverage summary](https://financefeeds.com/columbia-study-alleges-25-of-polymarket-volume-was-wash-trading/). The other co-authors are reportedly Allen Sirolly, Hongyao Ma and Rajiv Sethi **[UNVERIFIED: SSRN page returned 403, so this rests on prior knowledge]**.
- Data: more than two years of on-chain Polymarket data (Polygon) — [CoinDesk](https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds)
- Method:
  - A new algorithm flags wallets by how often they open and quickly close positions, especially when they trade mainly with other wallets showing the same pattern.
  - It detects simple back-and-forth trades as well as larger loops and clusters, some with tens of thousands of accounts.
  - Contracts were seen passing through dozens of wallets in quick succession, and USDC moved across multiple wallets to reuse capital.
  - — [CoinDesk](https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds)
- Headline figure: about 25% of historical volume involved likely wash trading — [CoinDesk](https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds); [Fortune](https://fortune.com/2025/11/07/polymarket-wash-trading-inflated-prediction-markets-columbia-research)
- Time series:
  - Flagged volume peaked at nearly 60% of weekly volume in December 2024 — [CoinDesk](https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds)
  - It fell to about 5% in May 2025 and rose to about 20% in early October 2025 — [coverage summary, FinanceFeeds/Cointelegraph](https://cointelegraph.com/news/columbia-study-polymarket-wash-trading-research)
  - One outlet dates the peak to Dec 2023. This conflicts with the other reports, and Dec 2024 is the majority reading.
- Wallets: 14% of about 1.26 million wallets were flagged as consistent with wash trading — [FinanceFeeds](https://financefeeds.com/columbia-study-alleges-25-of-polymarket-volume-was-wash-trading/)
- By category:
  - Sports markets about 45% of all-time volume, elections about 17%, crypto about 3% — [FinanceFeeds](https://financefeeds.com/columbia-study-alleges-25-of-polymarket-volume-was-wash-trading/)
  - In some weeks, more than 90% of trades in sports and election categories appeared inauthentic — [CoinDesk](https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds)
- Example cluster: more than 43,000 wallets generated nearly $1M in volume, mostly at prices under 1 cent, and nearly all of it was flagged — [CoinDesk](https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds)
- Incentives:
  - Many flagged wallets made no real profit, which suggests the aim was to game future incentives such as token airdrops or platform rankings.
  - The paper points to speculation about a future Polymarket token.
  - No KYC and no trading fees increase vulnerability.
  - — [CoinDesk](https://www.coindesk.com/markets/2025/11/07/polymarket-s-trading-volume-may-be-25-fake-columbia-study-finds)
- Attribution: the authors do not say Polymarket itself was responsible. Cointelegraph's framing differs. The authors call the results estimates, not proof. Polymarket said it was reviewing the findings — [FinanceFeeds](https://financefeeds.com/columbia-study-alleges-25-of-polymarket-volume-was-wash-trading/); [Cointelegraph](https://cointelegraph.com/news/columbia-study-polymarket-wash-trading-research)

**B. Chaos Labs and Inca Digital forensic reports (Oct 2024, shared exclusively with Fortune; published Oct 30, 2024)**
- Chaos Labs:
  - Method: on-chain analysis that filtered out likely market makers, then flagged users by buy/sell ratios and by holdings relative to volume.
  - Finding: about one-third of volume, and of users, on the presidential market was likely wash trading.
  - — [Fortune](https://fortune.com/crypto/2024/10/30/polymarket-trump-election-crypto-wash-trading-researchers); [The Defiant](https://thedefiant.io/news/regulation/analysts-find-one-third-polymarket-s-presidential-market-volume-tied-to-wash-b2b65478)
- Inca Digital: found that a "significant portion of the volume" could be attributed to potential wash trading — [Fortune](https://fortune.com/crypto/2024/10/30/polymarket-trump-election-crypto-wash-trading-researchers)
- Volume gap: the firms questioned the reported $2.7B in presidential-market volume and estimated actual volume at about $1.75B. These are the firms' estimates, not audited figures — [Fox (syndicated)](https://www.fox6now.com/news/trump-harris-polymarket-election-betting)

### Inferences
- The Columbia peak (Dec 2024, right after the election) and the trough (May 2025) line up with on-and-off token or airdrop speculation. This is consistent with incentive-driven farming rather than price manipulation.
- Chaos Labs used a heuristic (buy/sell ratios) and Columbia used a network/graph method. They estimate different things (one market versus the whole platform) and should not be compared directly.

### Gaps
- Full author list and exact abstract of SSRN 5714122 could not be fetched (403). Peer-review status as of Oct 2026 is unknown.
- I found no Dune dashboard with a documented wash-trading methodology.
- I found no Bloomberg investigation specifically on wash trading (Bloomberg coverage found was on the Théo whale and on probes).
- I found no estimate of wash trading after Polymarket's US (QCEX) relaunch. A POLY token launch is still speculative in these sources.

---

## 2. Insider and informed trading: cases and academic detection studies

### Takeaway
In 2026 informed trading became the dominant integrity theme. Three things happened:
- **Academic work:** Mitts & Ofir (Columbia Law/Haifa) estimate $143M in anomalous "informed" profits (Feb 2024–Feb 2026). Gómez-Cram, Guo, Kung & Jensen (LBS/Yale) find accuracy driven by a 3% informed minority. Several arXiv preprints propose leakage scores and ex-ante detectors.
- **Enforcement:** the first DOJ/CFTC insider cases were filed: a Maduro raid soldier (Apr 2026) and a Google "Year in Search" engineer (May 2026).
- **Forensics:** Bubblemaps flagged military/Iran wallet clusters, and Polymarket referred dozens of accounts to DOJ (Aug 2026).

### Cited Findings

**Academic and on-chain studies**

- **Mitts, Joshua (Columbia Law) & Ofir, Moran (Univ. of Haifa), "From Iran to Taylor Swift: Informed Trading in Prediction Markets," SSRN abstract 6426778 (2026); Harvard Law School Forum on Corporate Governance post, Mar 25, 2026.**
  - Described as the first systematic empirical and legal study — [HLS Forum](https://corpgov.law.harvard.edu/2026/03/25/from-iran-to-taylor-swift-informed-trading-in-prediction-markets); [Columbia Law](https://www.law.columbia.edu/news/archive/professor-joshua-mitts-prediction-markets-and-informed-trading)
  - Data: more than 93,000 Polymarket markets and about 50,000 wallets, Feb 2024–Feb 2026 — [AOL/Fortune syndication](https://www.aol.com/articles/informed-traders-polymarket-netted-143-082601427.html)
  - Method: five screening criteria on trade timing and size. These flag big, bullish bets placed shortly before news. The authors admit the screen may be over- or under-inclusive — [AOL](https://www.aol.com/articles/informed-traders-polymarket-netted-143-082601427.html)
  - Findings:
    - About 210,000 flagged trades and a conservative $143M in "informed" profits.
    - Flagged accounts won 69.9% of the time, more than 60 standard deviations above chance.
    - Another summary describes the unit as 210,718 wallet–market pairs rather than trades. This discrepancy is unresolved.
    - — [AOL](https://www.aol.com/articles/informed-traders-polymarket-netted-143-082601427.html); [Vernimmen thesis literature summary](http://www.vernimmen.com/ftp/mif2026_rp_bock_guenthoer.pdf)
  - Case examples:
    - About six new wallets earned about $1.2M before the Feb 28, 2026 Iran strike.
    - "ricosuave666" made about $155K on Israel's June 2025 strike on Iran.
    - "Magamyman" made about $553K around the Feb 28 strike.
    - The paper also covers a Maduro account and a Taylor Swift engagement trader.
    - — [HLS Forum](https://corpgov.law.harvard.edu/2026/03/25/from-iran-to-taylor-swift-informed-trading-in-prediction-markets); [AOL](https://www.aol.com/articles/informed-traders-polymarket-netted-143-082601427.html)
- **Gómez-Cram, Roberto; Guo, Yunhan; Kung, Howard (London Business School); Jensen, Theis Ingerslev (Yale). SSRN abstract 6617059, revised Apr 25, 2026 (working paper).**
  - Data: every Polymarket transaction from 2023 to 2025, covering 1.72M accounts, 210,322 markets and about $13.76B in volume.
  - Method: a sign-randomization test (10,000 random flips of buy/sell direction per trader) and a held-out persistence test benchmarked against mutual funds.
  - Findings:
    - 3.14% of accounts are "skilled winners."
    - Skilled winners and market makers are under 3.5% of accounts but capture more than 30% of gains.
    - 44% of skilled accounts stay skilled out of sample, versus about 10% for active mutual funds.
    - 67% of accounts are losers that absorb all aggregate losses.
    - 1,950 suspected-insider accounts (opened just before a single event, dormant afterward) move prices about 7–12 times more per dollar than skilled traders, but only in isolated events.
    - In a Maduro case study, three accounts opened Dec 27–Jan 3 cleared more than $630K.
    - Their conclusion: "the wisdom of an informed minority, not the wisdom of the crowd."
  - — [The Block, Apr 26, 2026](https://theblock.co/post/398902/skilled-polymarket-traders-are-a-3-minority-and-everyone-else-funds-their-gains-study)
- **Nechepurenko, Maksym, "Information Leakage at Population Scale: An Evaluation of the Polymarket Insider-Relevant Subpopulation, 2020-2026," arXiv:2605.00459 (May 1, 2026, q-fin.TR).**
  - Applies a deadline-resolved Information Leakage Score (ILS-dl) to 12,708 markets (Oct 2020–Apr 2026), using the ForesightFlow Insider Cases inventory of 32 markets.
  - Findings:
    - Only 88 of 12,708 markets (0.7%) yield computable scores.
    - 1 of the 32 insider cases is in scope, and 14 of 32 are unclassifiable.
    - Event-date validation reaches 57.8% exact agreement, below the 90% target.
    - Raw ILS medians are negative in all cells.
    - Main lesson: resolution semantics, not computation, is the binding constraint.
    - Code and data are released under CC-BY/MIT (ForesightFlow GitHub).
  - — [arXiv 2605.00459](https://arxiv.org/abs/2605.00459)
- **Companion preprint: "Empirical Evaluation of Deadline-Resolved Information Leakage on Documented Polymarket Insider Cases," arXiv:2605.02286 (May 2026)** — [arXiv PDF](https://arxiv.org/pdf/2605.02286). Details not fetched.
- **Bock & Guenthoer, Master in International Finance research paper (HEC, AY 2025–26).**
  - Proposes an ex-ante insider detector that flags positioning before price jumps using only information available before resolution.
  - In documented cases it surfaces the same wallets about a week before existing methods.
  - Uses the public on-chain dataset from Wang et al. (2026).
  - — [Vernimmen PDF](http://www.vernimmen.com/ftp/mif2026_rp_bock_guenthoer.pdf) (per search summary; not fully fetched)
- **"The Anatomy of a Decentralized Prediction Market: Microstructure Evidence from the Polymarket Order Book," arXiv:2604.24366 (Apr 2026).**
  - Trade direction inferred from Polymarket's public off-chain order-book feed matches on-chain ground truth only about 59% of the time. This is an important data-quality caveat for detection studies — [arXiv](https://arxiv.org/html/2604.24366v1)
- **"Polymarket-v1 Database," arXiv:2606.04217 (Jun 2026).** A public dataset preprint — [arXiv PDF](https://arxiv.org/pdf/2606.04217). Details not fetched.

**Documented cases (chronological)**

- **Israel–Iran "Twelve-Day War," June 2025:** Israeli prosecutors indicted an IDF reservist and a civilian for allegedly using classified intelligence to bet on strike timing, earning more than $150K combined — [The Block](https://www.theblock.co/post/391650/fresh-accounts-netted-1-million-on-polymarket-hours-before-us-airstrikes-on-iran-bubblemaps)
- **Nobel Peace Prize, Oct 2025:**
  - María Corina Machado's odds jumped from about 3.6% to more than 70% about 10 hours before the announcement.
  - About three accounts reportedly earned about $90K. Figures vary by outlet.
  - The Norwegian Nobel Institute opened a probe into a possible leak.
  - — [Blockworks](https://blockworks.co/news/polymarket-nobel-probe); [The Block](https://www.theblock.co/post/374199/officials-probe-polymarket-over-suspicious-trades-predicting-nobel-peace-prize-winner-reports); [Decrypt](https://decrypt.co/343840/nobel-peace-prize-organizers-intestigating-polymarket-insider-trades)
- **Google "Year in Search," Oct–Dec 2025 (charged May 27, 2026):**
  - Google software engineer Michele Spagnuolo ("AlphaRaccoon") faces an SDNY criminal complaint (commodities fraud, wire fraud, money laundering) and a CFTC civil complaint.
  - He allegedly made about $1.2M in profit on at least 23 Year in Search contracts with near-perfect accuracy, risking about $2.75M.
  - He allegedly had access to nonpublic "Google Confidential" list data.
  - — [The Block](https://www.theblock.co/post/402806/google-engineer-insider-trading-polymarket); [Gambling Insider](https://gamblinginsider.com/news/163425/google-polymarket-insider-trading-alpharaccoon-jpg); [Davis Wright Tremaine](https://www.dwt.com/blogs/financial-services-law-advisor/2026/05/doj-cftc-case-employee-prediction-market-trading)
- **Maduro / Venezuela, Jan 2026:**
  - A freshly created account bet about $32K at about 7 cents and made more than $400K within 24 hours — [The Block](https://www.theblock.co/post/391650/fresh-accounts-netted-1-million-on-polymarket-hours-before-us-airstrikes-on-iran-bubblemaps)
  - Indictment unsealed Apr 23, 2026 (SDNY), *US v. Gannon Ken Van Dyke*, an active-duty Army Special Forces Master Sergeant who allegedly helped plan "Operation Absolute Resolve."
    - He allegedly made about $33K in "Yes" buys and about $409,881 in profit.
    - He allegedly used a VPN and tried to delete accounts.
    - Five counts: CEA misuse of government information, theft of government information, commodities fraud under Rule 180.1, wire fraud, and §1957 money laundering on about $300K.
    - A parallel CFTC complaint is the CFTC's first event-contract insider case and its first use of the "Eddie Murphy Rule" (CEA §4c(a)(3)–(4)).
    - SDNY acknowledged Polymarket's cooperation.
    - — [Debevoise & Plimpton, Apr 27, 2026](https://www.debevoise.com/insights/publications/2026/04/polymarket-insider-trading-charges-illustrate-doj); [NYU Compliance & Enforcement blog](https://wp.nyu.edu/compliance_enforcement/2026/05/14/polymarket-insider-trading-charges-illustrate-doj-and-cftc-prediction-markets-enforcement-strategy/)
  - The defense plans to argue that Polymarket contracts are not "swaps" and that Rule 180.1 exceeds CFTC authority — [DeFi Rate](https://defirate.com/news/cftcs-first-event-contract-insider-trading-lawsuit-challenged-whether-polymarket-trades-swaps/)
- **US/Israel strikes on Iran, Feb 28, 2026:**
  - Bubblemaps flagged six fresh wallets, most funded within 24 hours, that bought "Yes" on "US strikes Iran by February 28, 2026?"
  - Bubblemaps puts their profit at $1.2M. The Block's own check found $989,191, with the largest wallet at $494,375.
  - Bubblemaps' CEO said certainty is "almost impossible."
  - — [The Block](https://www.theblock.co/post/391650/fresh-accounts-netted-1-million-on-polymarket-hours-before-us-airstrikes-on-iran-bubblemaps)
- **Iran ceasefire, Apr 2026:** newly created accounts bet big in the hours before Trump's announcement — [ADN (AP)](https://www.adn.com/nation-world/2026/04/08/newly-created-polymarket-accounts-bet-big-on-iran-ceasefire-in-the-hours-before-trumps-announcement/)
- **Military contracts cluster, May 2026:** Bubblemaps flagged a cluster that earned $2.4M with a 98% win rate on US military-operation contracts. There is no definitive proof of insider status — [Decrypt](https://decrypt.co/368255/polymarket-users-insider-trading-2-4-million-iran-predictions); [Cointelegraph](https://cointelegraph.com/news/bubblemaps-polymarket-cluster-win-military-bets)
- **August 2026:**
  - Research found that more than 150 wallets on Polymarket International may have traded on military secrets. Some headlines cite 152 wallets and about $8M **[UNVERIFIED: original report not located]** — [IBTimes](https://www.ibtimes.com/more-150-polymarket-wallets-may-have-traded-us-military-secrets-research-finds-3806617); [AllSides](https://www.allsides.com/news/2026-08-24-0700/banking-and-finance-more-150-polymarket-wallets-may-have-traded-military-secrets-research-finds)
  - CNN (Aug 21, 2026), citing a source, reported that Polymarket referred dozens of possible military insider-trading accounts to DOJ — [CNN](https://edition.cnn.com/2026/08/21/politics/polymarket-doj-military-prediction-market)
- **Platform response:** on Apr 30, 2026 Polymarket partnered with Chainalysis to police insider trading ahead of its US return, while seeking about a $15B valuation — [The Block](https://www.theblock.co/news/business/2026-04-30-polymarket-taps-chainalysis-to-police-insider-trading-seeks-15-billion-valuation-399619)
- **Polymarket US rules:** they bar trading on confidential information obtained in breach of a duty and trading by people who can influence an outcome — [Polymarket Exchange Market Integrity page](https://www.polymarketexchange.com/market-integrity.html)
- **CEO stance:** Coplan has argued that insiders "having an edge on the market is a good thing" for price discovery — [AOL](https://www.aol.com/articles/informed-traders-polymarket-netted-143-082601427.html)

### Inferences
- Detection methods fall into three families:
  - Wallet-level anomaly screens: timing, size, win rate, fresh accounts (Mitts–Ofir, Bubblemaps).
  - Account-skill statistics: sign randomization (Gómez-Cram et al.).
  - Market-level leakage scores: ILS (Nechepurenko).
- Coverage is the weak point of the market-level approach (only 0.7% of markets are computable), and trade-direction errors in off-chain feeds (about 59% agreement) are a data-quality threat to all of them.
- Most flagged insider cases involve geopolitical or military events. Mitts–Ofir and the Bubblemaps cases suggest these are where government-information "Eddie Murphy Rule" liability bites hardest.

### Gaps
- **MrBeast case:** no source found in this session. Unverified.
- **Taylor Swift engagement trader:** known only as a case study in Mitts–Ofir. Details not retrieved.
- **Sports insider cases:** none found.
- **Election-call insider cases:** none found.
- The full text of Mitts–Ofir (SSRN 6426778) and Gómez-Cram et al. (SSRN 6617059) was not fetched. Exact titles and full methods for the Gómez-Cram paper are unknown.
- Outcome or status of the Van Dyke motion to dismiss on the "swaps" question as of Oct 2026 is unknown.

---

## 3. Price manipulation attempts and manipulation resistance

### Takeaway
The best-known "manipulation" episode is the 2024 "Théo" Trump whale. That was a directional bet that moved odds, not a proven manipulation. The strongest academic manipulation evidence is the Stanford/SMU study of 5-minute Bitcoin contracts (2026). It shows settlement manipulation through spot-price pushes on Binance, and the problem is fixed by longer contract windows.

### Cited Findings
- **Théo / "Fredi9999" whale (Oct–Nov 2024):**
  - A French national bet more than $30M on Trump, first through 4 accounts and later reported as 11 (Fredi9999, Theo4, PrincessCaro, Michie, etc.).
  - WSJ reported his bets skewed the odds toward Trump. Polymarket's review concluded it was a directional position based on personal views.
  - — [Fortune, Nov 2, 2024](https://fortune.com/2024/11/02/french-whale-polymarket-30-million-donald-trump-election-bet-kamala-harris); [Cointelegraph](https://cointelegraph.com/news/polymarket-french-whale-donald-trump-election-odds)
  - Profit estimates: about $48–49M — [Quartz](https://qz.com/donald-trump-election-betting-polymarket-whale-trader-1851691650); [DL News](https://dlnews.com/articles/markets/polymarket-whale-is-poised-to-collect-49m-jackpot-on-trumps-election-victory/). A later Bloomberg analysis put it at about $85M across 11 accounts. This rests on one secondary relay.
  - France's ANJ said it was examining the site's compliance with French gambling law — [Cointelegraph](https://cointelegraph.com/news/polymarket-french-whale-donald-trump-election-odds)
- **Dai, David & Jia, Ruizhe (Stanford) and Yu, Shihao (SMU), working paper on 5-minute Bitcoin contracts (coverage Jul–Aug 2026):**
  - Data: about 16,000 five-minute contracts in the two months after launch.
  - Findings:
    - 821 wallets, about 0.3% of 243,000 traders, fit the manipulation pattern.
    - Mechanism: one-sided Binance trades in the final seconds push the Chainlink settlement price, followed by quick reversals.
    - Dollar figures conflict: $8.2M "extracted" versus about $1.28M in wealth transfer from ordinary traders. The two are unreconciled and may measure different things.
    - Extending contracts to 15 minutes largely eliminated the effect.
    - The authors could not prove that the Binance traders are the same people as the Polymarket holders.
  - — [Bloomberg Law](https://news.bloomberglaw.com/crypto/stanford-study-says-polymarket-crypto-bets-are-being-manipulated); [Cointelegraph](https://cointelegraph.com/news/stanford-study-5-minute-bitcoin-prediction-markets-enable-settlement-manipulation); [SMU SKBI clip](https://skbi.smu.edu.sg/sites/skbi.smu.edu.sg/files/%5Bcurrent-domain%3Amachine_name%5D/news_room/20260730_CryptoNexa_Stanford%20study%20pins%20Polymarket%20bitcoin%20settlement%20manipulation%20on%20contract%20design.pdf)
  - The product launch date is reported inconsistently (Feb 2025 vs. Jul 2024 vs. "February" 2026).
- **Wash-trade-driven price signals:** Chaos Labs' one-third wash estimate on the presidential market raises the question of whether quoted volume and odds were inflated — [Fortune](https://fortune.com/crypto/2024/10/30/polymarket-trump-election-crypto-wash-trading-researchers)

### Inferences
- Manipulation that targets the *settlement source* (Chainlink, or the UMA vote in section 4) appears more effective and better documented than manipulation that targets the *traded price*. Large traded-price moves (Théo) were absorbed and ultimately "correct."

### Gaps
- No Polymarket-specific academic study of whale price impact or manipulation resistance in election markets was found (e.g., an event study of Théo trades). Classic manipulation-resistance experiments (Hanson et al.) are not Polymarket-specific and were not searched.
- The Stanford/SMU paper title and URL were not located.

---

## 4. UMA Optimistic Oracle resolution disputes and governance attacks

### Takeaway
Two high-profile disputes drove oracle reform:
- **Ukraine minerals deal (Mar 2025):** a whale with about 5M UMA reportedly forced a false "Yes" on a $7M market.
- **Zelenskyy suit (Jul 2025):** a market with about $237–242M in volume was flipped to "No."

UMA responded with MOOV2 (UMIP-189, Aug 2025), which whitelists proposers. Token concentration (about 95% held by whales per Sentora) is the core centralization critique.

### Cited Findings
- **Mechanism:** anyone can propose a resolution by posting a $750 USDC.e bond. Disputes go to a vote of UMA token holders through the DVM — [The Block](https://www.theblock.co/post/348171/polymarket-says-governance-attack-by-uma-whale-to-hijack-a-bets-resolution-is-unprecedented)
- **Ukraine mineral deal market (Mar 24–25, 2025):**
  - About $7M market. "Yes" jumped from 9% to 100% and the market resolved Yes, although no deal existed.
  - A whale reportedly cast about 5M UMA through three wallets, about 25% of the vote. This rests on social-media and secondary reports, not on-chain verification here.
  - Polymarket called it "unprecedented" and refused refunds ("this wasn't a market failure").
  - — [The Block](https://www.theblock.co/post/348171/polymarket-says-governance-attack-by-uma-whale-to-hijack-a-bets-resolution-is-unprecedented); [The Defiant](https://thedefiant.io/news/defi/polymarket-s-usd7m-ukraine-mineral-deal-debacle-traced-to-oracle-whale); [CoinDesk, Mar 27, 2025](https://www.coindesk.com/markets/2025/03/27/polymarket-uma-communities-lock-horns-after-usd7m-ukraine-bet-resolves); [Decrypt](https://decrypt.co/311634/polymarket-allegations-oracle-manipulation)
- **Zelenskyy suit market (Jun–Jul 2025):**
  - Did Zelenskyy wear a suit at the June 24 NATO summit? The market initially resolved Yes, was overturned to No after a second review, and was finalized as No.
  - Reported volume was $237M (Decrypt) to $242M.
  - Critics alleged foul play by UMA voters.
  - Per Sentora data, 95% of UMA tokens are controlled by whales.
  - — [Decrypt](https://decrypt.co/329210/polymarket-rules-no-237m-bet-zelenskyy-suit?amp=1); [The Defiant](https://thedefiant.io/news/nfts-and-web3/polymarket-controversy-heats-up-after-the-zelenskyy-suit-market-resolves)
- **Reform:** UMA's Managed Optimistic Oracle V2 (MOOV2), approved via UMIP-189 in Aug 2025, limits Polymarket resolution proposals to whitelisted, experienced proposers — [The Block](https://www.theblock.co/post/366507/polymarket-uma-oracle-update)
- **Leakage-study link:** Nechepurenko (arXiv 2605.00459) found that resolution semantics make 14 of 32 documented insider-case markets "unclassifiable." This is an academic signal that ambiguous resolution criteria harm integrity measurement — [arXiv](https://arxiv.org/abs/2605.00459)

### Inferences
- MOOV2 constrains *proposers* but not *DVM voters*. Whale voting power in disputes therefore appears to remain the residual centralization risk, though this was not verified against UMA documentation.

### Gaps
- No peer-reviewed or arXiv paper quantifying UMA voter concentration or dispute outcomes on Polymarket was found.
- No official UMA/Polymarket post-mortem was found.
- Disputes after Aug 2025 (and whether MOOV2 reduced dispute rates) were not found.
- The Polymarket US (QCEX DCM) resolution process presumably differs from UMA. Not verified.

---

## 5. Regulatory and legal developments and scholarship

### Takeaway
Polymarket went through four phases:
- **2022:** CFTC settlement ($1.4M) and a US geoblock.
- **Nov 2024:** FBI search of Coplan's home over the US-user probe.
- **Jul 2025:** DOJ/CFTC probes closed and the $112M QCEX acquisition.
- **Nov 2025:** CFTC designation as a DCM for US operations.

In 2026 the legal fronts were state preemption fights (QCX LLC v. Campbell, D. Mass.; Nevada), the first event-contract insider prosecutions, CFTC rulemaking to replace Rule 40.11, and proposed insider-trading bills in Congress. I found no Polymarket-specific law review article, but there is a law-school forum piece (Mitts–Ofir) plus law-firm commentary.

### Cited Findings
- **2022 CFTC settlement (Jan 2022):**
  - $1.4M penalty for offering unregistered event-based binary options; more than 900 markets were offered to US users.
  - Polymarket agreed to wind down non-compliant markets and block US users.
  - — [CRS IF13187](https://www.everycrsreport.com/reports/IF13187.html); [Finance Magnates](https://www.financemagnates.com/cryptocurrency/fbi-raids-polymarket-ceos-home-seizes-phone/)
  - Primary CFTC order not fetched. The respondent entity name (Blockratize Inc.) is **[UNVERIFIED in this session]**.
- **FBI search (Nov 13–14, 2024):**
  - Agents seized Coplan's phone and electronics at his NYC home. There was no arrest or charge.
  - The probe reportedly concerned US users accessing the platform via VPN despite the 2022 order.
  - Polymarket called it political retribution.
  - — [The Block](https://www.theblock.co/post/326404/fbi-seizes-polymarket-ceos-phone-and-electronics-report); [UPI](https://www.upi.com/amp/Top_News/US/2024/11/14/Polymarket-FBI-raid/9741731564938/)
- **Probes closed (Jul 2025):** Bloomberg reported that DOJ and CFTC both closed their investigations — [The Block](https://www.theblock.co/post/362703/us-justice-department-and-cftc-close-probes-into-polymarket-bloomberg); [Cointelegraph](https://cointelegraph.com/news/polymarket-reenter-us-acquisition-qcex-exchange)
- **QCEX acquisition (Jul 21, 2025):**
  - $112M for a CFTC-licensed DCM and clearinghouse in Boca Raton, FL.
  - — [Axios](https://axios.com/2025/07/21/prediction-market-polymarket-us); [Legal Sports Report](https://www.legalsportsreport.com/238057/polymarket-back-in-us-after-112m-exchange-acquisition/)
  - Better Markets urged a CFTC probe of this "FTX-like backdoor" — [Better Markets](https://bettermarkets.org/newsroom/cftc-should-investigate-polymarkets-ftx-like-backdoor-strategy-to-gain-control-of-a-u-s-registered-entity-without-regulatory-scrutiny/)
- **US designation (Nov 2025):** the CFTC granted Polymarket DCM designation to operate in the US — [CRS IF13187 (Mar 20, 2026)](https://www.everycrsreport.com/files/2026-03-20_IF13187_33a896165ea2f60e2a49cd3b548cf38ce56a169b.html)
- **CFTC rulemaking (2026):**
  - A proposal to replace Rule 40.11's flat ban on five categories of event contract with contract-by-contract review. Factors include settlement design, public value, and manipulation or insider risk.
  - Comment deadline Jul 27, 2026.
  - — [CRS IF13187](https://www.everycrsreport.com/reports/IF13187.html)
  - The CFTC has also issued a proposed rule and a staff advisory stating that event contracts are swaps subject to anti-fraud rules (dates not given) — [Debevoise](https://www.debevoise.com/insights/publications/2026/04/polymarket-insider-trading-charges-illustrate-doj)
  - CFTC Enforcement Director David Miller (Mar 31, 2026) called the idea that insider trading is allowed on prediction markets a "myth" — [Debevoise](https://www.debevoise.com/insights/publications/2026/04/polymarket-insider-trading-charges-illustrate-doj)
- **State fights:**
  - In Feb 2026 Polymarket (QCX LLC) sued the Massachusetts AG in D. Mass. (*QCX LLC v. Campbell*), arguing CFTC exclusive jurisdiction. This came after a Massachusetts state judge (Barry-Smith) rejected Kalshi's preemption defense.
  - A Nevada judge allowed regulators to temporarily ban Polymarket's sports contracts.
  - Tennessee is also named.
  - — [Bloomberg Law](https://news.bloomberglaw.com/bloomberg-government-news/polymarket-sues-mssachusetts-to-preempt-state-shutdown); [Decrypt](https://decrypt.co/357503/polymarket-sues-massachusetts-looming-kalshi-sports-ban)
  - CFTC Chair Mike Selig said the agency will file amicus briefs against state actions: "We will see you in court" — [Axios, Feb 17, 2026](https://www.axios.com/2026/02/17/cftc-prediction-markets-mike-selig)
- **Congress and local:**
  - Bipartisan bills would extend insider-trading definitions to prediction markets — [Columbia Law](https://www.law.columbia.edu/news/archive/professor-joshua-mitts-prediction-markets-and-informed-trading)
  - The House Oversight Committee and the NYC Council are scrutinizing prediction markets — [CNN](https://www.cnn.com/2026/08/21/politics/polymarket-doj-military-prediction-market) (via search summary)
- **Scholarship and commentary:**
  - Mitts & Ofir (legal and empirical) — [HLS Forum](https://corpgov.law.harvard.edu/2026/03/25/from-iran-to-taylor-swift-informed-trading-in-prediction-markets)
  - NYU Program on Corporate Compliance & Enforcement blog (May 14, 2026) — [NYU](https://wp.nyu.edu/compliance_enforcement/2026/05/14/polymarket-insider-trading-charges-illustrate-doj-and-cftc-prediction-markets-enforcement-strategy/)
  - CRS "Prediction Markets: Policy Issues for Congress" (IF13187) — [CRS](https://www.everycrsreport.com/reports/IF13187.html)
  - Law-firm memos: [Pryor Cashman](https://www.pryorcashman.com/publications/reading-the-tea-leaves-forthcoming-regulatory-scrutiny-of-prediction-markets), [Nat'l Law Review](https://natlawreview.com/article/how-courts-and-regulators-are-redefining-us-prediction-markets), [Davis Wright Tremaine](https://www.dwt.com/blogs/financial-services-law-advisor/2026/05/doj-cftc-case-employee-prediction-market-trading)

### Inferences
- The legal theory for insider trading on Polymarket rests on three pillars: event contracts as swaps, CEA §6(c)(1)/Rule 180.1 misappropriation, and the "Eddie Murphy Rule" for government information. The Van Dyke defense directly challenges the first pillar, which makes that motion a key 2026–27 legal test.
- Federal and state jurisdiction remains unresolved. The CFTC is siding with platforms, while state courts (Massachusetts, Nevada) have so far sided with state gaming regulators at preliminary stages.

### Gaps
- No law review article focused specifically on Polymarket was found via web search (HeinOnline/Westlaw not accessible). SSRN searches for "event contracts" + "preemption" would be the next step.
- No ruling found in *QCX LLC v. Campbell* as of Oct 2026.
- Final status of the CFTC 40.11 replacement rule after the July 2026 comment close is unknown.
- Primary CFTC 2022 order and CFTC press releases for the 2026 cases were not fetched directly; secondary law-firm summaries were used.
- France's ANJ ban outcome is unknown. Other international actions (e.g., Singapore, Belgium, Switzerland, Thailand blocks) were not researched.
