# Study plan: Do prediction market prices discount the future?

A short empirical paper (4–6 pages, APA short-report format) built from hypothesis H2 in `polymarket_hypotheses.md`. The statistics are one-sample t-tests, one paired t-test and one simple regression.

## The idea in one paragraph

A Polymarket contract pays $1 if an event happens. If prices were pure probabilities, a contract priced at 85¢ would win 85% of the time whether the market resolves tomorrow or in six months. Buying it, though, ties up 85¢ until resolution, and money tied up for six months has a cost: the same cash could earn interest, or simply be spent sooner. People who are impatient, or who just want to be paid for waiting, will pay less for a favorite that pays out later. That predicts favorites should be **underpriced by more the further away resolution is**. The size of that underpricing gives an **implied discount rate** for the traders, which we can compare with the T-bill rate and with the much higher discount rates psychology finds in lab studies of intertemporal choice.

## Hypotheses

- **H1.** At long horizons (90 days before resolution), favorites win more often than their price implies. The mean of (outcome − price) is greater than 0.
- **H2.** At short horizons (1 day before resolution) there is no such gap. The mean of (outcome − price) is about 0.
- **H3.** Underpricing grows with time to resolution, so the regression slope of (outcome − price) on months to resolution is greater than 0.
- **Exploratory.** The implied annual discount rate is higher than the 3-month T-bill rate. A rate about equal to the T-bill suggests rational carry; a rate well above it suggests impatience or a risk premium.

Pure carry would produce underpricing of about price × rate × time. For an 85¢ favorite with the T-bill at 4.5%, that is about **1 percentage point at 90 days** and about 2 points at 180 days. Underpricing well beyond that is the interesting result.

## Method

**Sample (the "participants" are markets).**
- Resolved binary Polymarket markets from the order-book era (Nov 2022 – Oct 2026), excluding multi-outcome (negRisk) markets, with at least $1,000 traded and a clean 0/1 resolution.
- Counts from the dataset's market file, checked 15 Oct 2026: **17,500** markets were open at least 30 days, **5,993** at least 90 days and **1,751** at least 180 days.
- Multi-outcome markets add about 9,000 markets at 90 days, but those come from only about 1,000 events, so they are a robustness check with standard errors clustered by event.

**Data.**
- Trades: the free Hugging Face dataset `SII-WANGZJ/Polymarket_data`, which records every on-chain fill with its price.
- Market questions, end dates and outcomes: `markets.parquet` from the same dataset.
- Interest rates: the 3-month T-bill series (FRED, DTB3).

**Measures.**
- *Price at horizon h*: the volume-weighted average price of trades in the 24 hours before h days to `end_date`, with h ∈ {1, 30, 90, 180}. A snapshot needs at least 3 trades; otherwise that market–horizon is dropped.
- *Favorite*: whichever side is priced ≥ 0.50 at that snapshot.
- *Outcome*: 1 if the favorite won, else 0.
- *Underpricing* = outcome − price, measured in percentage points.

**Planned analyses.**
1. One-sample t-tests of mean underpricing against 0 at each horizon (H1, H2), with a Bonferroni correction across the four horizons.
2. A paired t-test on markets that have both a 90-day and a 1-day snapshot: is underpricing larger at 90 days?
3. A linear regression of underpricing on months to resolution, pooling all horizons, with standard errors clustered by market (H3).
4. The implied annual discount rate per horizon, r = (win rate / mean price)^(365/h) − 1 with a bootstrap 95% CI, compared with the average T-bill rate over the same period.

**Power.** At 90 days, n ≈ 6,000 and the standard deviation of (outcome − price) is about 0.35, so the standard error is about 0.45 points. That gives 80% power to detect underpricing of about **1.3 points** (two-sided α = .05). The test can detect effects somewhat larger than pure carry predicts, so a null at 90 days rules out large impatience but not a carry-sized effect. The 30-day horizon has three times the sample but a smaller predicted effect, so H3's pooled regression is the most powerful single test.

**Robustness (one short paragraph in the paper).**
- Restrict to markets with at least $10,000 traded.
- Add the multi-outcome markets, clustering by event.
- Drop political markets, since political markets are already known to be underconfident (Le, 2026), and long-dated markets are disproportionately political.

## What each result would mean

| Result | Interpretation |
|---|---|
| Underpricing grows with horizon and the implied rate ≈ T-bill | Prices are discounted probabilities, and part of the published "underconfidence" is a financing cost rather than a forecasting error |
| Underpricing grows and the implied rate ≫ T-bill | Traders behave impatiently, or demand a large premium for tail, platform and resolution risk, which links to lab findings on discount rates (Frederick, Loewenstein & O'Donoghue, 2002) |
| No horizon effect | Prices behave like probabilities at every horizon, and the long-dated compression in earlier work comes from something else (for example category) |

## Paper layout (about 5 pages)

| Section | Length | Contents |
|---|---|---|
| Abstract | 150 words | Question, sample, the key numbers, implied rate |
| Introduction | ~1 page | Prices as beliefs vs prices as discounted payoffs; calibration literature (Le 2026; Cardozo & Rivero-Wildemauwe 2026); intertemporal choice; hypotheses |
| Method | ~1 page | Sample, measures, analysis plan, power |
| Results | ~1.5 pages | **Table 1:** n, mean price, win rate, underpricing and implied rate by horizon. **Figure 1:** underpricing (±95% CI) against horizon, with the pure-carry prediction drawn as a dashed line. Then the regression, the paired test and robustness |
| Discussion | ~1 page | Interpretation, the carry-vs-impatience question, limitations, implications for reading market prices as probabilities |

**Limitations to state openly.**
- We can't separate impatience from risk premia (platform, oracle and tail risk) with this design.
- Long-dated markets differ in topic from short-dated ones.
- Only markets that last to a given horizon can contribute to it, so the sample at long horizons is a selected set.
- Thin markets give stale prices; the 3-trade rule and the $10k robustness check address this only partly.

## Data pipeline (the only real engineering)

1. Pick the eligible markets from `markets.parquet` (done above).
2. Stream `trades.parquet`, which is 46 GB. Keep only `timestamp`, `market_id`, `price`, `usd_amount` and `nonusdc_side`, and only the eligible markets.
3. For each market and horizon, compute the 24-hour VWAP for the YES token, converting NO-token trades with 1 − price.
4. Join outcomes and T-bill rates, then run the analyses (pandas plus statsmodels or scipy).

Everything above uses free data, and the analysis script will be short.

## Status of the inputs

- The market counts above were computed from the dataset's `markets.parquet` in this session.
- Polymarket's own price-history endpoint returned 403 from this cloud container, so the plan uses on-chain trades rather than the API.
