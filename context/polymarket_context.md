# Polymarket research context

Written 20 October 2026. This file briefs a new Claude chat on what I already know about Polymarket and its data, so we can start research without repeating the groundwork. I want to write a short empirical paper: 4 to 6 pages, psychology-paper format, simple statistics (t-tests, proportions, one regression), pre-registered before the data is analysed.

This chat works in a local folder that already contains the trade log, `trades.parquet` (see "Local setup" below). Everything needed is in this file. There is no other project material to look for.

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

About 78% of markets resolve No, and up/down or over/under markets are designed to sit near 50/50, so analyses should split by format.

### Multiple-choice questions

A question with more than two possible answers ("Who will win the 2024 US presidential election?") is built as a group of separate yes/no markets, one per answer, and only one of them can resolve Yes. Each answer has its own `market_id`. The group shares an `event_id` and an `event_title`. In the data, these markets have `neg_risk = 1` in `markets.parquet`, and their trades show `NEGRISK_CTF_EXCHANGE` (or its V2 version) in the `contract` column. 772,609 markets (19%) belong to such groups. A stand-alone question like "Will the Fed cut rates in December?" is a single market with `neg_risk = 0`.

The 2024 election group (`event_title` "Presidential Election Winner 2024", `event_id` 903193) has 17 markets:

| market_id | Question | Result | Volume |
|---|---|---|---|
| 253591 | Will Donald Trump win the 2024 US Presidential Election? | Yes | $1,531M |
| 253597 | Will Kamala Harris win the 2024 US Presidential Election? | No | $1,037M |
| 253642 | Will any other Republican Politician win...? | No | $242M |
| 253609 | Will Michelle Obama win...? | No | $153M |
| 253595 | Will Robert F. Kennedy Jr. win...? | No | $142M |
| 12 more | Haley, Biden, Newsom, DeSantis, Kanye West and others | No | $9M to $117M each |

The Yes prices in a group should add up to about $1 at any moment. When they don't, there is free money, which is what the arbitrage papers measured (about $40M from April 2024 to April 2025).

For analysis, the markets in one group are not independent questions: the 16 losing candidates above are one question split into pieces. Counting each as a separate market inflates the sample and mixes long shots with real contenders, so many studies analyse these groups at the event level, or report results both ways.

Price ranges ("Bitcoin price on Friday: $95k to $100k, ...") are built the same way. Ladders ("above $70k?", "above $72k?") are separate markets on the same date, and their prices together form a probability curve.

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

- Dataset page: https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data. This is a web page with the authors' description, column documentation and license. Its "Files and versions" tab (https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/tree/main) lists the five files. The page itself is not a download.
- Direct file links use the form `https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/resolve/main/<file name>`. Opening one starts the download of that file. The same address works for reading parts of a file remotely with DuckDB.
- Authors: Zhengjie Wang and colleagues (Shanghai Innovation Institute, with Westlake University, Shanghai Jiao Tong, Harbin Institute of Technology and Fudan).
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

### How the five files relate

They are not pieces of one file. Four are the same trade records stored in different forms, and one is a separate lookup table, so the 279 GB total is mostly the same information stored four ways.

```
                 Polygon blockchain
                        |
             orderfilled.parquet   (raw source, 127 GB, 2.03B rows)
            /           |           \
  trades.parquet   quant.parquet   users.parquet
  (46 GB, 1.27B)   (45 GB, 1.27B)  (61 GB, 2.03B)

  markets.parquet  (0.5 GB, 4.05M rows): separate, one row per question
```

| File | What it is | Use it for |
|---|---|---|
| `orderfilled.parquet` | Raw blockchain events: raw units, no question names, each match appears more than once (one event per maker order plus a summary event for the taker). The only file with per-trade fees. | Verifying against the chain; fee studies |
| `trades.parquet` | The raw events cleaned: one row per trade, prices in dollars, linked to its market, summary events removed. | Most research (default) |
| `quant.parquet` | The same trades rewritten from the Yes side: "buy No at 30¢" becomes "sell Yes at 70¢". | One price series per question |
| `users.parquet` | The same fills organised by wallet, one row for each trader's side. | Trader studies: profit and loss, disposition effect, loss chasing |
| `markets.parquet` | Not trades. One row per question: text, labels, outcome, dates, volume. | Looking up what a `market_id` is and how it resolved |

A typical project needs `trades.parquet` (or `quant.parquet`) plus `markets.parquet`. Download `markets.parquet` whole (0.5 GB). It is needed for almost any question, because `trades.parquet` only gives a `market_id` number, not the question text or outcome, and the two files join on `trades.market_id = markets.id`.

### What `trades.parquet` contains

Each row is one trade (one fill): 1,266,885,846 rows from 21 Nov 2022 to 4 Oct 2026. Real rows from election day 2024 in "Will Donald Trump win the 2024 US Presidential Election?" (`market_id` 253591), pulled remotely:

| time (UTC) | price | usd_amount | token_amount | maker | taker | nonusdc_side |
|---|---|---|---|---|---|---|
| 2024-11-05 00:00:01 | 0.591 | 1,754.89 | 2,969.36 | 0xc23b... SELL | 0x6753... BUY | token1 (Yes) |
| 2024-11-05 00:00:01 | 0.410 | 5.84 | 14.25 | 0x0b58... SELL | 0x4f4c... BUY | token2 (No) |
| 2024-11-05 00:00:03 | 0.591 | 0.99 | 1.68 | 0xc23b... SELL | 0xe310... BUY | token1 (Yes) |

The first row means someone bought 2,969 Yes shares at 59.1¢, paying $1,754.89, from a wallet whose sell order was resting on the book. That market had 150,892 trades worth $67.7M on 5 Nov 2024 (UTC).

The 17 columns:

- When: `timestamp` (Unix seconds, UTC), `block_number` (a Polygon block, roughly every 2 seconds).
- Which market: `market_id` (join to `markets.parquet`), `condition_id` (blockchain ID of the question), `event_id` (the multiple-choice group), `asset_id` (ID of the exact share traded), `nonusdc_side` (which share: `token1` is usually Yes, Up or Over; `token2` is No), `contract` (which exchange contract: `CTF_EXCHANGE` for stand-alone markets, `NEGRISK_CTF_EXCHANGE` for multiple-choice groups, and `_V2` versions from 28 Apr 2026).
- Price and size: `price` (price per share of the share traded, 0 to 1; a No trade at 0.41 means Yes was about 0.59, so convert with 1 − price or use `quant.parquet` for a Yes-only series), `token_amount` (shares), `usd_amount` (dollars paid).
- Who: `maker` (wallet whose order was resting), `taker` (wallet that traded against it), `maker_direction` and `taker_direction` (BUY or SELL, read from the blockchain, so the side that started the trade is known exactly).
- Proof: `transaction_hash` and `log_index` (the trade's location on the blockchain, publicly verifiable).

What you can build from it: the price of any market at any moment, volume by market or hour, each wallet's full history and profit or loss, buying vs selling pressure, and self-trades (`maker = taker`, the simplest wash-trading signal).

What it does not contain: names or identities (only wallet addresses), unfilled orders (so no spreads or order book depth), fees (only in `orderfilled.parquet`), question text, categories or outcomes (join `markets.parquet`; categories come from the Gamma API), and anything before 21 Nov 2022 or after 4 Oct 2026.

Columns in `markets.parquet`: `id` (joins to `market_id`), `question`, `slug`, `condition_id`, `token1`, `token2`, `answer1`, `answer2`, `closed`, `active`, `archived`, `outcome_prices` (for example `['1', '0']` means answer1 won; some closed markets show values like 0.9995 or 0.5 and need care), `volume`, `event_id`, `event_slug`, `event_title`, `created_at`, `end_date`, `updated_at`, `neg_risk`.

Example: the very first trade in the file was on 21 Nov 2022 in "Will Donald J. Trump win the U.S. 2024 Republican presidential nomination?", 100 Yes shares at 50¢, with the same wallet as maker and taker (a self-trade, probably a launch test).

### Local setup

The project folder should look like this (check with `ls`, since the actual names may differ):

```
<project folder>/
  polymarket_context.md     this file
  trades.parquet            45.8 GB, the trade log
  markets.parquet           0.5 GB, the market lookup table (download it too if it is missing)
```

`markets.parquet` is needed for almost any question, because `trades.parquet` only has a `market_id` number. Download link: https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/resolve/main/markets.parquet

Rules for working with a 46 GB file on a normal computer:

- Never load the whole trade file into pandas (`pd.read_parquet("trades.parquet")`). It would need far more memory than a laptop has.
- Use DuckDB or Polars, which read only the columns and rows a query needs and can work on files larger than memory.
- Build small extracts first (only the columns, markets or dates a study needs), save them as new Parquet files, and run the analysis on those.

```python
import duckdb
con = duckdb.connect()
con.sql("SET memory_limit = '8GB'")          # adjust to the machine
trades, markets = "trades.parquet", "markets.parquet"

# first rows
con.sql(f"SELECT * FROM read_parquet('{trades}') LIMIT 5").show()

# one day: 5 Nov 2024 UTC -> 498,736 trades, about $163M
con.sql(f"""SELECT count(*), sum(usd_amount) FROM read_parquet('{trades}')
            WHERE timestamp BETWEEN 1730764800 AND 1730851200""").show()

# join trades to their questions and outcomes, saved as a smaller extract
# (here: resolved two-outcome markets open at least 30 days, as in the time-horizon study)
con.sql(f"""COPY (
    SELECT t.timestamp, t.market_id, t.price, t.usd_amount, t.nonusdc_side,
           m.question, m.outcome_prices, m.created_at, m.end_date
    FROM read_parquet('{trades}') t
    JOIN read_parquet('{markets}') m ON t.market_id = m.id
    WHERE m.closed = 1 AND m.neg_risk = 0 AND m.volume >= 1000
      AND datediff('day', m.created_at, m.end_date) >= 30
) TO 'extract_horizon.parquet' (FORMAT parquet)""")
```

The trade file is stored in 1,261 chunks that each cover a short time window, so filtering by time skips most of the file and is fast. Filtering by `market_id` has to read that column for the whole file, which takes minutes, not seconds. The other three Hugging Face files (`orderfilled.parquet`, `quant.parquet`, `users.parquet`) are not in the folder. DuckDB can read parts of them over the internet if needed (`INSTALL httpfs; LOAD httpfs;`, then `read_parquet('<direct link>')`).

### Other sources

- **Gamma API** (https://gamma-api.polymarket.com): market metadata, tags and categories. The Hugging Face market file has **no category tags**, so join Gamma tags on `condition_id` when you need categories.
- **CLOB API** price history (`/prices-history`): returned HTTP 403 from a cloud server in an earlier test (likely geoblocking); it may work from a home connection. Full history only in 3-hour or 12-hour buckets; finer data is kept for days to weeks. The trade file is a better price source anyway.
- **Dune** `polymarket_polygon.*` tables: SQL over the same on-chain data, refreshed about daily, useful for anything after 4 Oct 2026.
- **Order book history** (unfilled orders, spreads): not in any free source. Paid: Tardis.dev (from 25 May 2026), Telonex (from 11 Oct 2025).
- Smaller ready-made sets: Jon Becker's prediction-market dataset on GitHub (Polymarket + Kalshi), SimpleFunctions "Settled Markets" (price at settlement and 24h before, CC-BY-4.0).

### Data pitfalls

1. Trade direction: take who bought and who sold from the on-chain `maker_direction` / `taker_direction`. Guessing direction from price changes (the tick rule) or from the public order-book feed is close to random on Polymarket (about 50 to 59% accurate in two 2026 papers).
2. Volume: say which definition you use. Counting both sides of each fill doubles it, and split/merge activity can be counted as trades.
3. Wash trading: estimates range from a median of about 1% of volume (same-wallet round trips) to about 25% (Columbia network method, with peaks near 60% in some weeks). Report results with and without a simple wash filter.
4. Weighting: results can flip sign between trade-weighted and market- or event-weighted analysis. Report both.
5. Selection: long-dated markets are mostly political, and short ones mostly crypto and sports. Control for category and format.
6. Prices are per share traded: a No trade at 0.41 means Yes was about 0.59. Convert No trades with 1 − price before building a Yes price series.

## What research already exists

This summarises a literature review from an earlier session. Almost all of the work is 2025 to 2026 preprints, not peer-reviewed.

Well covered (avoid as a stand-alone topic):
- **Calibration:** depends on category, horizon and price. Political markets are underconfident, with prices pulled toward 50% (Le 2026, arXiv 2602.19520).
- **Favourite-longshot bias:** contracts under 10¢ lose 19.3¢ per $1 (Cardozo & Rivero-Wildemauwe 2026, arXiv 2609.12878). The bias is absent in sports.
- **2024 election:** Polymarket beat polls on the headline contract, but across political markets only 67% beat a coin flip, versus 78% on Kalshi and 93% on PredictIt (Clinton & Huang, SocArXiv 2025).
- **Trader profits:** the top 1% of users take 76.5% of profits, and about 3% of accounts are skilled (Gómez-Cram et al., SSRN 6617059).
- **Arbitrage:** about $40M realised from April 2024 to April 2025 (Saguillo et al., AFT 2025).
- **LLM forecasting:** no LLM beats the market price at the same moment. In a ForecastBench audit of 527 entries, none significantly beat copying the price.
- **Insider and informed trading:** Mitts & Ofir (SSRN 6426778) flag about $143M of anomalous profit. The first US insider indictment for an event contract came in April 2026.
- **Wash trading:** Sirolly, Ma, Kanoria & Sethi (Columbia, SSRN 5714122) estimate about 25% of volume over three years.

Open (no study found):
- the 2026 fee rollout as a natural experiment
- whether long-dated favourites are underpriced because money is locked up (time discounting)
- why the favourite-longshot bias is absent in sports
- price discounts before disputed UMA resolutions
- short-horizon crypto markets against Binance prices
- Polymarket odds on tariffs or the Fed as shocks for asset prices
- election markets in other countries in 2025

## Candidate hypotheses

### Recommended for a short paper: time horizon and favourite underpricing

Buying a 95¢ favourite that resolves in months ties up money, so favourites should be underpriced by more the further away resolution is. The size of the gap gives an implied discount rate, which can be compared with the T-bill rate (rational cost of money) and with the much higher discount rates found in psychology studies of impatience.

Predictions:
- H1: at 90 days before resolution, favourites win more often than their price implies (mean of outcome − price > 0).
- H2: at 1 day before resolution, there is no gap.
- H3: the gap grows with time to resolution.

Pure cost of money predicts a gap of about price × rate × time, roughly 1 percentage point at 90 days for an 85¢ favourite with a 4.5% T-bill rate. A much larger gap would point to impatience or a risk premium.

Design:
- Sample: resolved two-outcome markets (`neg_risk = 0`) with at least $1,000 volume and a clean 0/1 outcome, from Nov 2022 onward. Counts from `markets.parquet`: 17,500 markets open at least 30 days, 5,993 at least 90 days, 1,751 at least 180 days. Multiple-choice markets can be added as a check, with errors clustered by event.
- Price at horizon h days (h = 1, 30, 90, 180): volume-weighted price of trades in the 24 hours before `end_date` minus h days, with at least 3 trades.
- Favourite: the side priced at 0.50 or more at that moment. Outcome: 1 if the favourite won.
- Tests: one-sample t-tests of (outcome − price) at each horizon; a paired t-test of 90 days vs 1 day within the same markets; a regression of (outcome − price) on months to resolution with errors clustered by market; implied annual discount rate per horizon with a bootstrap interval.
- Power: at 90 days (n ≈ 6,000, SD ≈ 0.35) the test detects a gap of about 1.3 points with 80% power.
- Checks: markets with at least $10,000 volume only; drop political markets (already known to be underconfident).

### Other ideas that need only this data

- Gambler's fallacy in repeating Up/Down markets: about 131,000 resolved Bitcoin Up/Down markets, with Up winning 50.1%. After a streak of "Up", does the next market open with a lower Up price?
- Fan-favourite overpricing in sports: are popular teams priced above how often they actually win?
- The disposition effect: do wallets sell winning positions sooner than losing ones?
- Loss chasing: after a big loss, are a wallet's next bets larger and on longer odds?
- Round-number clustering: do trade prices bunch at 5¢ and 10¢ steps, and more so for small trades?
- The 2026 fee rollout: did fees (on-chain in `orderfilled.parquet`) change small-trade activity or price reversals in the categories that got them, compared with fee-free geopolitics?

## How I want to work

1. Write the hypotheses, measures and tests down before looking at results, and report every planned test, including the ones that fail.
2. Check the data's own structure before trusting it: duplicates, how markets resolved, odd prices, gaps in time.
3. Report effect sizes, not only p-values. With millions of rows almost everything is significant. Add an equivalence test with a pre-chosen smallest effect of interest, so a null result still says something.
4. Check whether an effect is specific to the hypothesis or shows up everywhere.
5. When ideas are uncertain, explore a random half of the data first and confirm on the other half.
