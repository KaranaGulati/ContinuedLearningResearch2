# Testable hypotheses from the Polymarket literature review

Drafted 15 Oct 2026 from `reports/Polymarket data research landscape.md` and the notes behind it.

Each hypothesis below targets a gap the review found nothing on, or a disagreement between existing papers. Each one names a directional prediction, the result that would kill it, the data, and the test. They are ordered by how soon we can run them with free data. H7 has a deadline: it must be pre-registered before the midterms on 3 Nov 2026.

## Rules that apply to every test

These come straight from the failure modes the literature has already hit.

1. **Trade direction comes from the chain.** Use `maker_direction` / `taker_direction` from on-chain `OrderFilled` data. Tick-rule and feed-based inference are about 50–59% accurate on Polymarket (Dubach, arXiv 2604.24366; Qin & Yang, arXiv 2606.04217), which is close to a coin flip.
2. **Volume is one-sided and wash-filtered.** Count each fill once (the HF `trades.parquet` already drops the taker summary events). Report results with and without wallets flagged by a simple wash screen (same-wallet or tight-cluster round trips), since wash trading may be anywhere from 1% to 25% of volume depending on the method.
3. **Stitch V1 and V2.** Any series that crosses 28 Apr 2026 must include all four exchange contracts. The HF dataset does this as of its 5 Oct 2026 release.
4. **Weight by market, not only by trade.** The favorite-longshot result flips sign depending on whether you weight by trade or by parent event (Cardozo & Rivero-Wildemauwe, arXiv 2609.12878), so report both.
5. **Pre-register anything forward-looking.** At minimum H7, and ideally H1 and H4 too, because those analysis choices are easy to tune after seeing the data.

## Data we can use without paying

- **HF `SII-WANGZJ/Polymarket_data`**: every CLOB fill from 21 Nov 2022 to 4 Oct 2026, including V2. It has maker, taker, both directions, price, size, and in `orderfilled.parquet` the per-fill `maker_fee`, `taker_fee` and `protocol_fee`, so fees can be observed directly rather than assumed. `markets.parquet` has the question text, `end_date`, `neg_risk`, `event_id` and final `outcome_prices`. It has **no category tags**, so we need to pull tags from the Gamma API and join them on `condition_id`.
- **Gamma API**: tags and categories, `questionID` (for the UMA join), and resolution status.
- **Polygon logs** (RPC or Dune): UMA Optimistic Oracle and UMA CTF Adapter events for proposals, disputes and settlements.
- **Binance public data** (data.binance.vision): 1-second klines for BTC and ETH.
- **Dune `polymarket_polygon.*`**: for anything after 4 Oct 2026, such as the midterms.

`trades.parquet` alone is 46 GB, so query it with DuckDB or Polars in a streaming or lazy mode rather than loading it into pandas. Disk in this cloud container is limited, so the full download belongs on a local machine or a cloud bucket.

---

## H1. The 2026 taker fees widened mispricing most where the fee is largest

**Claim.** Polymarket added taker fees in stages: crypto from 5 Jan 2026, sports from 18 Feb, and most other categories from 30 Mar. Geopolitics stayed fee-free (Pine Analytics). The fee is a function of p(1−p), so it is largest for mid-priced contracts and near zero at the extremes. If fees matter, then after a category is treated:
- (a) small taker trades fall relative to the fee-free control,
- (b) the share of volume provided by makers rises, because rebates pay makers,
- (c) short-run price reversals after taker trades get bigger, a sign that the effective spread widened,
- (d) and all three effects are strongest at prices near 0.5 and close to zero near 0.05 or 0.95.

**What kills it.** No change relative to geopolitics, or effects that do not scale with the fee curve. The second check is the stronger one, because the fee curve gives a dose–response inside each treated market that a category-wide shock (such as an election cycle) would not produce.

**Test.** A staggered difference-in-differences (Callaway–Sant'Anna or a stacked design) on category-by-price-bucket-by-day panels, run 60 days either side of each start date. The treatment intensity is the fee actually paid, read from `taker_fee` on-chain. Matched-pair arbitrage gaps (YES + NO taker prices within the same block window) give a cheap no-arbitrage-band measure without order-book history.

**Why it's new.** The only existing analysis is a practitioner blog that looked at volume and revenue, with no spreads and no control group.

**Effort.** Medium. All of this can be done with HF data plus the Gamma tags.

## H2. Long-dated markets look underconfident partly because capital is locked up

**Claim.** Le (arXiv 2602.19520) finds political prices are compressed toward 50%. Here is a mechanical reason that would produce this. Buying a 95¢ favorite that resolves in eight months ties up 95¢ to earn 5¢. That is roughly the same annualized return as a T-bill, but with tail risk on top, so favorites in long-dated markets should stay cheap. Shorting a longshot means buying the favorite side, so the same constraint keeps longshots too expensive. The predictions are:
- (a) realized excess returns on contracts priced at 85¢ or more rise with time to resolution;
- (b) the annualized realized return on those favorites is at least the short-term risk-free rate;
- (c) compression toward 50% is close to zero for markets resolving within a week and grows with horizon, within the same category;
- (d) when US short rates fell over 2025–26, the long-horizon compression shrank.

**What kills it.** Compression that does not depend on horizon once category is controlled for. Or a horizon gradient that stays the same when rates change, which would point to beliefs or attention rather than carry.

**Test.** For every resolved market, take prices at fixed horizons (180, 90, 30, 7 and 1 days before `end_date`), reconstructed as the volume-weighted price of on-chain trades in a window around each point. Regress outcome minus price on price bucket × log(horizon), with category fixed effects, and add the 3-month T-bill rate for (d). If Polymarket pays holding rewards on some long-dated markets (check the current docs), those markets are a ready-made treatment group and should show less compression.

**Why it's new.** Traders talk about this a lot, but none of the papers in the review test it. If it holds, part of the "underconfidence" finding is a financing cost rather than a forecasting error, which changes how the calibration literature should be read.

**Effort.** Low. HF data plus a T-bill series from FRED.

## H3. Sports shows no favorite-longshot bias only where a sharp sportsbook line anchors the price

**Claim.** Cardozo & Rivero-Wildemauwe find the favorite-longshot bias is absent in Polymarket sports but present in politics and crypto, and nobody has explained why. Our explanation is that arbitrageurs tie main-line game markets to sharp books such as Pinnacle and Betfair, and that anchor removes the bias. Sports markets with no liquid outside line should therefore show the bias just like politics does. Those include season futures, awards and MVP races, player props, minor leagues and esports.

**What kills it.** No bias in unanchored sports markets either. That would point to something about sports traders rather than to an outside anchor. The other possibility is that the gap disappears once we compare within the same price bucket, which would mean it was only a difference in how many longshot contracts each group has (the "head-to-head games have few longshots" story).

**Test.** Sort sports markets into "anchored" and "unanchored" groups from their question text and tags, and decide the rules before looking at outcomes. Estimate calibration curves and the return to buying contracts under 10¢ for each group, both trade-weighted and event-weighted. Require a minimum number of contracts in each price bucket so the composition explanation is controlled.

**Optional extension.** Join historical closing odds (free CSVs exist for European football) and test whether the Polymarket price converges to the de-vigged closing line.

**Effort.** Low. HF data plus the Gamma tags.

## H4. The April 2026 insider-trading enforcement deterred insider-like trading, and what remains is harder to detect

**Claim.** Three events in close succession could have changed behavior: the first insider-trading indictment for an event contract on 23 Apr 2026 (Van Dyke, the Maduro raid), Polymarket hiring Chainalysis on 30 Apr, and DOJ referrals in August. If these deterred anyone, then in categories where information is held by a few people (military, geopolitics, government actions, awards):
- (a) the profit share of "insider-like" trades should fall after April compared with sports and crypto, where information is public;
- (b) the activity that remains should be spread across more fresh wallets that share a funding source, with less size per wallet.

**What kills it.** No change after April relative to the control categories, or a drop that also happens in the controls, which would suggest a platform-wide shift such as V2 launching on 28 Apr.

**Test.** First, define an insider-like trade in advance, for example:
- the wallet is less than 7 days old,
- it has positions in at most 2 markets,
- it buys below 20¢,
- and the market later jumps above 90¢ within 72 hours.

Run a difference-in-differences from Feb 2025 to Oct 2026, insider-prone categories against sports and crypto. For (b), build a funding graph from wallets' first USDC or pUSD deposits on Polygon and count clusters, which both Gómez-Cram et al. and the SoK survey say is missing.

**Problem to handle.** V2 launched five days after the indictment. Use the V2 date as a separate break, and check whether the drop shows up in V1-era markets that were still trading in May.

**Why it's new.** Mitts & Ofir and Gómez-Cram et al. disagree on how big insider trading is. Neither looks at what happened after enforcement started.

**Effort.** Medium. The funding graph means pulling Polygon transfer data.

## H5. Prices carry a resolution-risk discount, and the August 2025 oracle reform reduced it

**Claim.** After the real-world event is over but before UMA settles the market, the winning side trades below $1. If that gap includes a premium for dispute risk, and not just time value, then:
- (a) the post-event discount should be larger in markets that later get disputed than in matched undisputed markets, so the market sees the trouble coming;
- (b) the discount and the dispute rate should both fall after UMA's MOOV2 reform (Aug 2025), which limited proposers to a whitelist;
- (c) markets with vague resolution wording should carry bigger discounts. Vagueness can be scored from the question and rules text with an LLM rubric fixed in advance.

**What kills it.** The same discount in disputed and undisputed markets once time to settlement is controlled for, and no change at the MOOV2 break.

**Test.**
- Pull UMA Optimistic Oracle and CTF Adapter events (proposals, disputes, resets, settlements) from Polygon and join them on `questionID`.
- Measure the discount as 1 minus the winning token's volume-weighted price between the event ending and the first proposal.
- Run a before-and-after comparison around MOOV2, plus matched comparisons of disputed against undisputed markets.

**Why it's new.** The Ukraine minerals and Zelenskyy-suit disputes have only press coverage, and no paper puts a number on dispute rates or what disputes do to prices.

**Effort.** Medium. The UMA event decoding is a one-time cost and gives a dataset we can reuse.

## H6. Short-horizon crypto markets lag Binance by seconds, and a few wallets collect most of the lag profit

**Claim.** A 15-minute BTC up/down market is effectively a digital option on BTC. Its fair value at any second can be calculated from the Binance spot price, the strike (the opening price), recent realized volatility and the time left. The predictions are:
- (a) the gap between the Polymarket price and that fair value predicts the direction of the next trade and the next price move;
- (b) the gap decays with a half-life of a few seconds that shortened through 2026 as bots arrived;
- (c) the ten most profitable taker wallets in these markets take more than half of all taker profit, and they trade in the direction of the gap.

**What kills it.** A gap that does not predict trade direction, meaning Polymarket prices react to Binance as fast as the data can resolve, or taker profits that are not concentrated.

**Test.**
- Line up on-chain fills (Polygon block timestamps are accurate to about 2 seconds) with Binance 1-second klines.
- Compute the fair value with a Black-Scholes digital using realized volatility.
- Estimate the decay with event-time regressions after Binance moves larger than k standard deviations, and work out profit concentration from wallet-level PnL.
- If the reported TWAP settlement switch on 7 Aug 2026 is confirmed, use it as a natural experiment on manipulation near settlement, and compare with Dai, Jia & Yu's 5-minute results.

**Why it's new.** No peer-reviewed paper studies these markets' microstructure, and the reported "bots dominate" figures are unaudited.

**Effort.** Low to medium. Both data sources are free. Block-time resolution limits how short a lag we can see.

## H7 (deadline 3 Nov). Extremizing Polymarket's midterm prices improves their score

**Claim.** If Polymarket political markets are underconfident in a stable way (Le, 2026), then an extremizing transform fitted on 2024 should score better on 2026 midterm House, Senate and governor markets than raw prices do. The transform is logit(p′) = k · logit(p) with k > 1, and the score is log loss and Brier at 7 days and 1 day before the election.

**What kills it.** A fitted k that comes out at about 1 on 2024 data, or a 2026 log-loss improvement whose confidence interval includes zero. Either result is worth reporting, because it tells us whether the 2024 underconfidence carries over.

**Test.**
1. Fit k on 2024 state-level presidential, Senate and House markets (2022 is out because the CLOB only started after those midterms). Use on-chain prices at matching horizons.
2. Pre-register k, the market list rules, the horizons and the metric on OSF or AsPredicted **before 3 Nov**.
3. After the races resolve, score the 2026 markets using Dune data, since HF ends 4 Oct.
4. Use block bootstrap by state, because races within a state are correlated (Chernov et al. show that ignoring cross-state correlation biases results by more than 10 pp).
5. If a Kalshi price series is available, run the same test on it as a second venue.

**Why it's new.** No state-by-state scoring of 2024 exists. It's also a clean out-of-sample test of a published finding, and few such tests have been done.

**Effort.** Low, but it is time-bound. The pre-registration has to happen this month.

## H8. LLMs add information beyond the market price only in thin markets

**Claim.** Halawi et al. and the AIA Forecaster both find that blending an LLM forecast with the market price beats the price alone, but no study says where the gain comes from. Our prediction is that the best weight on the LLM falls as liquidity rises: it is meaningfully positive in the bottom third of markets by liquidity and indistinguishable from zero in the top third. The idea is that a model's reasoning only adds value where too few informed traders have priced the question.

**What kills it.** An LLM weight that does not depend on liquidity, or a weight of zero in every group (no gain anywhere, matching the "Copier Line" audit).

**Test.**
- Take 600 to 1,000 binary markets that were created and resolved **after the model's training cutoff**, which rules out leakage, split into equal groups by volume or trade count.
- At 7 days before resolution, record the on-chain price and the LLM's forecast. The LLM sees no price and either has no retrieval or uses search filtered by date.
- Fit the logit-pooling weight for each liquidity group and test whether it slopes down with liquidity.

**Why it's new.** It turns the "LLM + market beats market" result into a statement about where model reasoning actually helps, which matters for anyone building forecasting agents.

**Effort.** Medium, mostly the API cost. Make sure the questions really are past the cutoff, and also check that the retrieval itself doesn't leak information from after the forecast date.

---

## Suggested order

| Order | Hypothesis | Why then |
|---|---|---|
| Now (this week) | **H7**: fit k on 2024 and pre-register | Has to be filed before 3 Nov |
| 1 | **H2** capital lock | Cheapest test, uses data we already know, and the result changes how the calibration literature should be read |
| 2 | **H3** sports anchor | Same pipeline as H2 with one added variable, and it explains a published puzzle |
| 3 | **H1** fee rollout | Biggest novelty, reuses the H2/H3 panel, and the fee is observable on-chain |
| 4 | **H6** crypto latency | Self-contained, with free data on both sides |
| 5 | **H5** UMA discount | The UMA event dataset is reusable on its own |
| 6 | **H4** insider deterrence | Needs the funding graph, and the V2 break overlaps the treatment date |
| 7 | **H8** LLM by liquidity | Needs questions resolving after the model's cutoff, so it gets better the longer we wait |

H2, H3 and H1 share a single build: a market-by-horizon panel of on-chain prices with category tags and outcomes. Building that panel is the first piece of engineering to do.

## Things to verify before relying on them

- The fee formula and category rollout dates come from one practitioner blog (Pine Analytics), and other sources give conflicting category rates. The on-chain `taker_fee` field is the ground truth.
- The 7 Aug 2026 TWAP switch date for crypto markets is unverified.
- Whether Polymarket currently pays holding rewards on long-dated markets (relevant to H2) has not been checked.
- Whether the Gamma `questionID` maps directly onto UMA adapter events for every market type, including negRisk, has not been confirmed.
