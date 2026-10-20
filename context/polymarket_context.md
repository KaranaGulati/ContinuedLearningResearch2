# Polymarket research context

Written 20 October 2026. This file briefs a new Claude chat on what I already know about Polymarket and its data, so we can start research without repeating the groundwork. I want to write a short empirical paper: 4 to 6 pages, psychology-paper format, simple statistics (t-tests, proportions, one regression), pre-registered before the data is analysed.

Everything below was checked during an earlier research session. Items marked [unverified] come from a single secondary source.

## How Polymarket works

Polymarket is a prediction market. Each market is a question with two outcome shares.

- A share of the winning outcome pays $1 at resolution, and the losing share pays $0.
- The two prices add up to about $1, so the price of "Yes" is read as the crowd's probability. If Yes trades at 30¢, the market says about 30%.
- People trade when they think the price is wrong, not simply when they think the event will happen. Buying Yes at 30¢ makes sense if you think the true chance is above 30%.
- There is no bookmaker. Every share is created when two traders together put up $1: for example the Yes buyer pays 30¢ and the No buyer pays 70¢. That $1 sits in a smart contract on the Polygon blockchain, in Polymarket's dollar token (pUSD since April 2026, USDC.e before). The winner collects the whole $1, so trading is zero-sum between traders, minus fees.
- Later trades pass existing shares from seller to buyer. No new money enters the contract.
- Holding 3 Yes and 3 No in the same market is always worth exactly $3. Holding 5 Yes and 3 No is $3 plus 2 Yes of real exposure. Buying No at 30¢ is economically the same as selling Yes at 70¢, and the order book matches those orders against each other.
- Position actions besides trading: **split** ($1 into 1 Yes + 1 No), **merge** (1 Yes + 1 No back into $1), **redeem** (cash winning shares after resolution).
- Resolution: an outcome is proposed and can be disputed through the UMA optimistic oracle, where UMA token holders vote. Disputed cases exist, for example a $7M Ukraine minerals-deal market in March 2025. In August 2025 UMA limited who can propose outcomes to a whitelist (MOOV2).

### Market formats

Every market has two sides, but the labels vary. Counts from all 4,049,900 markets in the Hugging Face metadata file:

| Labels | Example | Markets |
|---|---|---|
| Yes / No | "Will Bitcoin be above $72,000 on April 8?" | 1,357,995 (34%) |
| Over / Under | "76ers vs. Wizards: O/U 240.5" | 1,214,162 (30%) |
| Up / Down | "Bitcoin Up or Down, 3AM ET" (hourly, 15-minute and 5-minute versions) | 798,149 (20%) |
| Team names, Favorite / Underdog, Odd / Even, Over 2.5 and others | sports | the remaining ~16% |

Multiple-choice questions ("Who will win the World Cup?") are groups of yes/no markets, one per option, of which only one can resolve Yes. These are flagged `neg_risk = 1` and number 772,609 markets (19%). Price ranges ("Bitcoin price on Friday: $95k to $100k, ...") and ladders ("above $70k?", "above $72k?") are built the same way.

About 78% of markets resolve No, and up/down or over/under markets are designed to sit near 50/50, so analyses should split by format.

### Orders

From docs.polymarket.com (checked 20 Oct 2026):

- **Limit orders** rest on the order book. Good Till Cancelled (GTC), or Good Till Date (GTD) with an expiry of at least about 3 minutes. Either can be **post-only**, which is rejected if it would trade immediately.
- **Market orders** trade immediately with a worst acceptable price. Fill and Kill (FAK) fills what it can and cancels the rest. Fill or Kill (FOK) fills completely or not at all.
- No stop-loss or take-profit on prediction markets.
- Prices move in ticks (usually 1¢). Only the unfilled part of an order can be cancelled. Price improvement goes to the taker.
- Selected crypto and finance up/down markets hold marketable orders for 250 ms before matching, and live sports markets have a configured delay. Orders cannot be cancelled during the delay.
- Maker = adds a resting order. Taker = trades against one.

### Fees and how Polymarket earns

- From 2020 to 2025 the global platform charged no trading fees and ran on investor money. Intercontinental Exchange reportedly agreed to invest up to $2B in October 2025 [unverified]. The Block reported in April 2026 that Polymarket sought a valuation near $15B.
- Taker fees started on crypto markets on 5 Jan 2026, sports on 18 Feb 2026 and most other categories on 30 Mar 2026. Geopolitics markets stay fee-free. The fee is largest near a price of 50¢ and close to zero near 0¢ or 100¢. 20 to 50% of fees go back to makers as rebates. One practitioner estimate (Pine Analytics, March 2026) put net revenue near $209M a year [single source]. The fee paid on every trade is recorded on-chain (`taker_fee`, `maker_fee` in `orderfilled.parquet`).
- A separate US exchange (via the 2025 QCEX acquisition, regulated by the CFTC) charges maker/taker fees, moving to volume tiers on 19 Oct 2026.
- Polymarket also has data deals (Dow Jones from January 2026: odds shown in WSJ, Barron's, MarketWatch; X/xAI partnership). Terms are not public.

### Perps

Polymarket also runs perpetual futures ("perps") on a separate exchange (api.perpetuals.polymarket.com), with the first contracts live from 1 Aug 2026. A perp tracks an asset's price, never expires, and can be traded long or short with leverage. Collateral is pUSD. Hourly funding payments keep the perp price close to the real price: when the perp trades above it, longs pay shorts. Positions are liquidated if losses use up the margin. The public instrument list on 20 Oct 2026 had 89 contracts (41 crypto, 38 single stocks, 6 indices, 4 commodities), with up to 50x leverage on BTC, ETH, S&P 500 and Nasdaq 100. Perps support take-profit, stop-loss, reduce-only and bracket orders. Perps are not part of the Hugging Face dataset below.

### 2026 changes that break older code and tutorials

- **28 Apr 2026: CLOB V2.** New exchange contracts (`0xE111180000d2663C0091e4f400237545B87B996B`, and `0xe2222d279d744050d28e00520010520000310F59` for multiple-choice markets), pUSD replaced USDC.e, the order format changed, and all open V1 orders were wiped. Any time series crossing this date must include both the V1 and V2 contracts.
- `py-clob-client` was archived on 25 May 2026. The successor SDK's name differs across official pages.
- Polymarket's Data API v1 is scheduled to retire on **24 Oct 2026**. v2 uses cursor pagination and renames `market` to `condition`.
- Goldsky's free public subgraphs return incomplete data after V2.

## Data

### Main dataset: Hugging Face `SII-WANGZJ/Polymarket_data`

- Page: https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data
- License: MIT. Built from Polygon blockchain logs and verified against the chain.
- Coverage: every order-book trade from 21 Nov 2022 to 4 Oct 2026 (V1 and V2 contracts). It does not cover the 2020 to 2022 period, when Polymarket used an automated market maker instead of an order book.

| File | Size | Rows | What it is | Direct download |
|---|---|---|---|---|
| `markets.parquet` | 0.5 GB | 4,049,900 | One row per market: question, labels, outcome, volume, dates, flags | https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/resolve/main/markets.parquet |
| `trades.parquet` | 45.8 GB | 1,266,885,846 | One row per trade (recommended) | https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/resolve/main/trades.parquet |
| `orderfilled.parquet` | 127.2 GB | 2.03B | Raw blockchain events, including per-fill fees | https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/resolve/main/orderfilled.parquet |
| `quant.parquet` | 44.7 GB | 1.27B | Trades converted to the Yes side (No price becomes 1 − price) | https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/resolve/main/quant.parquet |
| `users.parquet` | 60.8 GB | 2.03B | Every fill keyed by wallet, for trader-level work | https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/resolve/main/users.parquet |

The files are Parquet, not CSV. Pandas, Polars, DuckDB and R read them directly.

Columns in `trades.parquet`: `timestamp` (Unix seconds, UTC), `block_number`, `transaction_hash`, `log_index`, `contract` (CTF_EXCHANGE, NEGRISK_CTF_EXCHANGE, and their V2 versions), `market_id`, `condition_id`, `event_id`, `maker`, `taker` (wallet addresses), `price` (0 to 1), `usd_amount`, `token_amount`, `maker_direction`, `taker_direction` (BUY or SELL), `nonusdc_side` (token1 = first outcome, token2 = second), `asset_id`.

Columns in `markets.parquet`: `id` (joins to `market_id`), `question`, `slug`, `condition_id`, `token1`, `token2`, `answer1`, `answer2`, `closed`, `active`, `archived`, `outcome_prices` (for example `['1', '0']` means answer1 won; some closed markets show values like 0.9995 or 0.5 and need care), `volume`, `event_id`, `event_slug`, `event_title`, `created_at`, `end_date`, `updated_at`, `neg_risk`.

Example: the very first trade in the file was on 21 Nov 2022 in "Will Donald J. Trump win the U.S. 2024 Republican presidential nomination?", 100 Yes shares at 50¢, with the same wallet as maker and taker (a self-trade, probably a launch test).

### Querying the trade file without downloading it

DuckDB can read only the needed parts of the remote file over HTTP. Tested on 20 Oct 2026:

```python
import duckdb
con = duckdb.connect()
con.sql("INSTALL httpfs; LOAD httpfs;")
url = "https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/resolve/main/trades.parquet"

# first rows
con.sql(f"SELECT * FROM read_parquet('{url}') LIMIT 5").show()

# one day: 5 Nov 2024 UTC -> 498,736 trades, about $163M, in about 3 seconds
con.sql(f"""SELECT count(*), sum(usd_amount) FROM read_parquet('{url}')
            WHERE timestamp BETWEEN 1730764800 AND 1730851200""").show()
```

The file is stored in 1,261 chunks that each cover a short time window, so filtering by time is fast. Filtering by `market_id` has to read that column for the whole file, so for many markets it is better to download once and work locally.

### Other sources

- **Gamma API** (https://gamma-api.polymarket.com): market metadata, tags and categories. The Hugging Face market file has **no category tags**, so join Gamma tags on `condition_id` when you need categories. Reachable from a cloud container.
- **CLOB API** price history (`/prices-history`): returned HTTP 403 from the cloud container (likely geoblocked). Full history only in 3-hour or 12-hour buckets; finer data is kept for days to weeks.
- **Dune** `polymarket_polygon.*` tables: SQL over the same on-chain data, refreshed about daily, useful for anything after 4 Oct 2026.
- **Order book history** (unfilled orders, spreads): not in any free source. Paid: Tardis.dev (from 25 May 2026), Telonex (from 11 Oct 2025).
- Smaller ready-made sets: Jon Becker's prediction-market dataset on GitHub (Polymarket + Kalshi), SimpleFunctions "Settled Markets" (price at settlement and 24h before, CC-BY-4.0).

### Data pitfalls

1. Trade direction: take who bought and who sold from the on-chain `maker_direction` / `taker_direction`. Guessing direction from price changes (the tick rule) or from the public order-book feed is close to random on Polymarket (about 50 to 59% accurate in two 2026 papers).
2. Volume: say which definition you use. Counting both sides of each fill doubles it, and split/merge activity can be counted as trades.
3. Wash trading: estimates range from a median of about 1% of volume (same-wallet round trips) to about 25% (Columbia network method, with peaks near 60% in some weeks). Report results with and without a simple wash filter.
4. Weighting: results can flip sign between trade-weighted and market- or event-weighted analysis. Report both.
5. Selection: long-dated markets are mostly political, and short ones mostly crypto and sports. Control for category and format.

## What research already exists

A full literature review is in `reports/Polymarket data research landscape.md` in this repository. Almost all of it is 2025 to 2026 preprints, not peer-reviewed.

Well covered (avoid as a stand-alone topic):
- **Calibration:** depends on category, horizon and price. Political markets are underconfident, with prices pulled toward 50% (Le 2026).
- **Favourite-longshot bias:** contracts under 10¢ lose 19.3¢ per $1 (Cardozo & Rivero-Wildemauwe 2026). The bias is absent in sports.
- **2024 election:** Polymarket beat polls on the headline contract, but across political markets only 67% beat a coin flip, versus 78% on Kalshi and 93% on PredictIt (Clinton & Huang).
- **Trader profits:** the top 1% of users take 76.5% of profits, and about 3% of accounts are skilled.
- **Arbitrage:** about $40M realised from April 2024 to April 2025 (Saguillo et al.).
- **LLM forecasting:** no LLM beats the market price at the same moment. In a ForecastBench audit of 527 entries, none significantly beat copying the price.
- **Insider and informed trading:** Mitts & Ofir flag about $143M of anomalous profit. The first US insider indictment for an event contract came in April 2026.

Open (no study found):
- the 2026 fee rollout as a natural experiment
- whether long-dated favourites are underpriced because money is locked up (time discounting)
- why the favourite-longshot bias is absent in sports
- price discounts before disputed UMA resolutions
- short-horizon crypto markets against Binance prices
- Polymarket odds on tariffs or the Fed as shocks for asset prices
- election markets in other countries in 2025

## Candidate hypotheses

Details are in `hypotheses/polymarket_hypotheses.md`. The one sized for a short paper is written up in `hypotheses/study_plan_time_horizon.md`:

The idea is time horizon and favourite underpricing. Buying a 95¢ favourite that resolves in months ties up money, so favourites should be underpriced by more the further away resolution is. It makes three predictions:
- At 90 days before resolution, favourites win more often than their price implies.
- At 1 day before resolution, there is no gap.
- The gap grows with time to resolution.

The size of the gap gives an implied discount rate to compare with the T-bill rate. The tests are one-sample t-tests, a paired t-test and one regression. The sample is resolved binary markets with at least $1,000 volume: 17,500 open at least 30 days, 5,993 at least 90 days, and 1,751 at least 180 days. This needs prices at fixed horizons, rebuilt from `trades.parquet`.

Other hypotheses in the list that need only free data:
- Gambler's fallacy in repeating Up/Down markets. About 131k resolved Bitcoin markets, with Up winning 50.1%. Do prices lean against a streak?
- Fan-favourite overpricing in sports.
- The disposition effect: traders sell winners sooner than losers.
- Loss chasing after a big loss.
- Round-number clustering of trade prices.

## Lessons from my earlier studies

I ran two pre-registered studies on the Moral Machine dataset in this repository (`studies/`). They taught me five things:

1. Write the hypotheses and tests down and commit them before looking at results. Then report every pre-registered test, including the ones that fail.
2. Check the data's own design before trusting it. In the Moral Machine data the first scenario of every session was not randomised, and missing that would have produced a false positive (p = .042).
3. Add an equivalence test with a pre-chosen smallest effect of interest, so a null result says something ("the effect is smaller than 2 points"). Report effect sizes, not only p-values.
4. With millions of rows, everything is "significant". Judge results by effect size, and check whether an effect is specific to the hypothesis or shows up everywhere. My smartphone result looked utilitarian but was a general shift on most dimensions.
5. Choose questions someone needs answered, or explore half of the data first and confirm on the other half. Picking hypotheses only because they were untested produced weak ideas.

## Environment notes (Claude Code cloud session)

- DuckDB with `httpfs` can read the Hugging Face files remotely. pip installs of `duckdb`, `pandas`, `pyarrow`, `scipy` and `matplotlib` work.
- The cloud container has limited disk (about 30 GB free). Do not download the 46 GB trade file there. Query it remotely or work on a local machine.
- Polymarket's CLOB price API returned 403 from the container; the Gamma API and docs.polymarket.com worked.

## Files in this repository

- `reports/Polymarket data research landscape.md`: full literature review with citations.
- `research_notes/Polymarket data research landscape/`: detailed notes behind the review (accuracy, integrity, microstructure, AI forecasting, datasets, applied work).
- `hypotheses/polymarket_hypotheses.md`: testable hypotheses with designs.
- `hypotheses/study_plan_time_horizon.md`: plan for the time-horizon paper.
- `studies/`: the two Moral Machine studies, as worked examples of the pre-register, analyse, write-up process.
