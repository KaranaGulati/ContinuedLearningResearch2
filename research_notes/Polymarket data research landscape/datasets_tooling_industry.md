# Polymarket Data: Datasets, APIs, Open-Source Tooling, Dashboards and Industry Analyses (status as of Oct 2026)

> Scope note: about 22 search/fetch calls, done 2026-10-15. Most of the official-API detail comes from docs.polymarket.com pages fetched that day. Where a claim comes only from a third-party listing or marketing page, it is marked **[unverified/secondary]**. Two changes in 2026 matter most and are easy to miss if you rely on older blog posts: (1) the **CLOB V2 / pUSD migration on 2026-04-28**, and (2) **Data API v1 retirement on 2026-10-24**, nine days after these notes were written.

## 1. Official Polymarket APIs (Gamma, CLOB, Data API, WebSockets, SDKs) and their historical-depth limits

### Takeaway
Polymarket has three REST surfaces plus WebSockets:
- **Gamma**: market/event metadata.
- **CLOB**: live books, prices and price history.
- **Data API**: trades, positions, activity, holders, leaderboard and OI. It is mid-migration to `/v2`, with v1 retiring 2026-10-24.

Rate limits are generous and IP-based through Cloudflare. Fine-grained price history is short-lived: 1-minute data has only a ≥7-day retention floor, full history comes only in 3h/12h buckets, and none of the fetched docs describe historical order-book snapshots. A 2026 SDK reset archived `py-clob-client`, and V1 SDKs no longer work against production.

### Cited Findings
**Base URLs and rate limits (all per 10 s, IP-based, Cloudflare throttles/queues rather than rejects)** — [Polymarket rate limits](https://docs.polymarket.com/quickstart/introduction/rate-limits)
- Gamma `https://gamma-api.polymarket.com`:
  - General: 4,000
  - `/events`: 500
  - `/markets`: 300
  - `/markets`+`/events` listing: 900
  - `/comments`: 200
  - `/tags`: 200
  - `/public-search`: 350
- Data API `https://data-api.polymarket.com`:
  - v1 general: 1,000 (`/trades` 200; `/positions` 150; `/closed-positions` 150)
  - v2 general: 800 (`/v2/trades` 300; `/v2/positions` 200; `/v2/activity` 200; `/v2/prices-history` 200)
- CLOB `https://clob.polymarket.com`:
  - General: 9,000
  - `/book` and `/price`: 1,500 each
  - `/books`: 500
  - `/prices-history`: 1,000
  - `/data/trades`: 500
  - Trading `POST /order`: 5,000/10 s burst and 120,000/10 min sustained
- Others:
  - Bridge API: 50
  - Relayer `/submit`: 25/min
  - User PNL API: 200
- The rate-limits page lists no WebSocket limits.

**Price history (CLOB `/prices-history`), per the current docs** — [Polymarket: Prices & order books](https://docs.polymarket.com/market-data/prices-order-books.md)
- Request shape:
  - One outcome token per request (`token_id`).
  - The time window is set by exactly one of: `interval` (`1d`, `1w`, `1m`, `max`), `start`/`end` in epoch seconds, or `as_of`.
  - An explicit `start`/`end` range spans **at most 15 days**.
- Bucket width:
  - The parameter is now `bucket_seconds` (60–86,400), not `fidelity`.
  - Floors: 600 s for `max`/`1m`, and 300 s for `1w`.
- How far back each resolution goes:
  - `max` returns full history in **12-hour buckets** by default.
  - Explicit 10,800 s or 43,200 s buckets also cover full history.
  - **Finer widths return only the last 30 days.**
- Retention floors:
  - ≥7 days for 1-min data.
  - ≥60 days for 5-min data.
  - ≥90 days for 30-min data.
  - 3h and 12h data are kept permanently.
  - A request the store can't fill returns an empty or sparse page.
- Output: points carry `timestamp`, `price` and `resolution_seconds`, where 0 means an exact tick. The API paginates by `cursor`.
- Order-book endpoints: `GET /book`, `POST /books` (≤500), `/midpoint(s)`, `/spread(s)`, `/last-trade-price(s)`. Each book returns `min_order_size`, `tick_size`, `neg_risk`, `last_trade_price` and a `hash` for change detection. The page describes **no historical order-book endpoint**.
- An older py-clob-client issue reported that resolved markets returned only ≥12h granularity, and that a 1h request with `interval=max` came back empty for a big election market. This matches the documented retention scheme. — [py-clob-client issue #216](https://github.com/Polymarket/py-clob-client/issues/216)
- Older third-party docs still describe the legacy `fidelity` (minutes) parameter and the `1h/6h/1d/1w/1m/max` intervals. These differ from the current `bucket_seconds` docs, so treat old tutorials as stale. — [anysite docs](https://docs.anysite.io/api-reference/polymarket/polymarketmarketshistory) **[secondary]**
- The Data API v2 also has a new `GET /v2/prices-history` route, with no v1 equivalent. — [Data API v1→v2 migration](https://docs.polymarket.com/migrate/data-api-v1-to-v2.md)

**Data API v1 → v2 (breaking changes)** — [Data API v1→v2 migration](https://docs.polymarket.com/migrate/data-api-v1-to-v2.md)
- **v1 retires 2026-10-24.**
- Route mapping:
  - `/trades`→`/v2/trades`
  - `/activity`→`/v2/activity`
  - `/positions`, `/closed-positions` and `/v1/market-positions`→`/v2/positions`, with a `status`/`condition` filter
  - `/holders`→`/v2/holders`; add `include_pnl=true` for entry/PnL data
  - `/v1/leaderboard`→`/v2/leaderboard`
  - `/value`→`/v2/value`
  - `/oi`→`/v2/oi`
  - `/traded`→`/v2/user-stats`
  - Live-volume, builder and "combo" routes also have v2 equivalents.
- Pagination:
  - v1 used `limit`/`offset` with **offset capped at 10,000 rows**. This is a major gotcha for anyone backfilling trades through v1.
  - v2 uses an opaque cursor (`pagination.next_cursor`).
- Response shape:
  - v2 wraps responses in `data`.
  - Fields are now snake_case.
  - `market`→`condition`, which accepts ≤20 condition IDs.
  - A miss returns `null` or an empty list, not an error.
- `GET /v1/accounting/snapshot` stays on v1.
- SDK support for Data API v2 starts at `@polymarket/client` / `polymarket-client` v0.10.0.

**WebSockets / real-time**
- AsyncAPI specs:
  - Market channel: `ws-live-v2.polymarket.com/asyncapi.json`
  - User channel: `asyncapi-user.json`
  - Sports channel: `asyncapi-sports.json`
- An RTDS overview exists, along with a migration guide **"RTDS → PolyBolt"**. This suggests the Real-Time Data Service is being replaced. — [Polymarket llms.txt index](https://docs.polymarket.com/llms.txt)
- Tardis.dev records these WS channels: `book`, `price_change`, `last_trade_price`, `best_bid_ask`, `tick_size_change`, `new_market`, `market_resolved`, `sport_result`. — [Tardis Polymarket docs](https://docs.tardis.dev/historical-data-details/polymarket.md)
- The official TS `@polymarket/real-time-data-client` supports topics such as `activity` trades and `orders_matched`. — [search summary of npm/GitHub listing](https://docs.polymarket.com/market-data/realtime-data.md) **[secondary]**

**CLOB V2 migration (2026-04-28)** — [Polymarket V2 migration](https://docs.polymarket.com/v2-migration)
- Cutover: live about 11:00 UTC, with about 1 hour of paused trading. All open V1 orders were wiped.
- New exchange contracts:
  - Standard: `0xE111180000d2663C0091e4f400237545B87B996B`
  - NegRisk: `0xe2222d279d744050d28e00520010520000310F59`
  - EIP-712 domain version "2"
- Collateral: **pUSD** (Polymarket USD, backed by USDC) replaces USDC.e. API traders must `wrap()` through a Collateral Onramp.
- Order struct: `nonce`, `feeRateBps` and `taker` were removed. `timestamp` (ms), `metadata` and `builder` were added.
- Fees are now set at match time. A `builderCode` field replaced the `POLY_BUILDER_*` headers.
- WebSocket URLs and API keys did not change.
- New SDK packages: `@polymarket/clob-client-v2` (npm) and `py-clob-client-v2` (PyPI). The legacy `clob-client`/`py-clob-client` "no longer work against production".
- Secondary coverage of the same cutover — [Struct v0.5 blog](https://www.struct.to/blog/v0.5-release), [BlockEden blog](https://blockeden.xyz/blog/2026/05/13/polymarket-clob-v2-pusd-prediction-markets-infrastructure/), [The Defiant on pUSD](https://thedefiant.io/news/defi/polymarket-unveils-collateral-token-to-replace-bridged-usdc) **[secondary]**

**SDK status**
- `Polymarket/py-clob-client` was **archived 2026-05-25**. Its notice: "no longer functional and should not be used". It points to the new unified SDK `github.com/Polymarket/py-sdk`. — [py-clob-client repo](https://github.com/Polymarket/py-clob-client)
- Naming conflict across official pages:
  - The migration guide says `py-clob-client-v2`.
  - The archived repo points to `py-sdk`.
  - The Data API guide says `polymarket-client` / `@polymarket/client`.
  - Sources: [V2 migration](https://docs.polymarket.com/v2-migration); [py-clob-client](https://github.com/Polymarket/py-clob-client); [Data API migration](https://docs.polymarket.com/migrate/data-api-v1-to-v2.md)

**Identifiers**
- The trading ID is a **token ID** for CTF markets but a **position ID** for "Polymarket Protocol V2 markets".
- Gamma returns `clobTokenIds`, a JSON-encoded string, for CTF markets and `positionIds` for V2 markets.
- Order-book responses carry `market` (in the examples it equals the 0x condition ID) and a `neg_risk` boolean.
- Source: [Polymarket: Prices & order books](https://docs.polymarket.com/market-data/prices-order-books.md)

### Inferences
- Backfill strategy:
  - For tick-level or sub-12h price history on resolved markets, the official API is not enough after about 30 days.
  - Instead, rebuild prices from on-chain fills (Section 2/3), or buy WS-recorded data (Tardis, Telonex).
- Any "full historical order book" research must rely on vendors that recorded the WS feed: Tardis from 2026-05-25, Telonex from 2025-10-11. Official sources appear to offer no L2 book history.
- Code written before May 2026 needs review, because the SDKs, the order struct and the Data API pagination all changed:
  - most GitHub bots
  - Kaggle notebooks
  - py-clob-client tutorials
- "Polymarket Protocol V2 markets" with `positionIds` suggests a new non-CTF market type. Researchers should check per market which ID scheme applies.

### Gaps
- No exact Gamma API field list was fetched. The OpenAPI spec is at https://docs.polymarket.com/api-spec/gamma-openapi.yaml. From prior knowledge **[unverified]**, its fields include `id`, `slug`, `conditionId`, `questionID`, `clobTokenIds`, `outcomes`, `outcomePrices`, `volume`, `liquidity`, `negRisk`, `negRiskMarketID`, `umaResolutionStatus`, `endDate` and `closedTime`.
- Not confirmed:
  - whether a batch prices-history endpoint still exists (a Chinese-language doc page `post-batch-prices-history` appeared in search)
  - what PolyBolt is
- Polymarket US (the CFTC-regulated venue) API and data availability was not investigated. Dune says it does not yet cover Polymarket US.
- I found no official documentation of a historical L2 order-book product.

## 2. On-chain sources (contracts, subgraphs/Goldsky, Dune, Allium, others)

### Takeaway
On-chain fills (`OrderFilled`/`OrdersMatched` on the CTF Exchange and NegRisk exchange on Polygon) are the only complete, free, inception-to-date trade record for the CLOB era (Nov 2022 onward). The access layer has changed:
- Goldsky now says the **legacy public Polymarket subgraphs return incomplete or incorrect data after the V2 migration**, and it steers users to Turbo Pipeline datasets.
- **Dune's curated `polymarket_polygon.*` tables** (about 24h refresh) are the easiest SQL entry point.
- **Allium** and **Goldsky CryptoHouse** are the other SQL options Polymarket officially lists.

### Cited Findings
**Goldsky**
- Polymarket moved to v2 contracts on 2026-04-28 and "no longer uses subgraphs". Existing public subgraph endpoints "will return incomplete or incorrect data". — [Goldsky Polymarket docs](https://docs.goldsky.com/chains/polymarket)
- Recommended instead: Turbo Pipelines datasets — [same source](https://docs.goldsky.com/chains/polymarket)
  - `polymarket.order_filled` (v2.0.0, recommended): every partial or full fill, maker and taker side
  - `polymarket.orders_matched`: taker side only
  - `polymarket.user_balances`: ERC-1155 balances
  - `polymarket.user_positions`: avg price, realized PnL, total bought
- Pipeline mechanics: pipelines are YAML deployed with `goldsky turbo apply` to sinks. Fast scan supports only `block_number` ranges, not timestamps.
- Scale: about 1.2B position entities to backfill, and about 150M per month to maintain.
- Pricing: through a calculator; no published rate limits.
- The legacy subgraph family, now deprecated, was `main`, `beefy_pnl`, `slimmed_pnl`, `activity` (splits, merges, redemptions) and `orderbook` (fills), plus hourly open-interest snapshots, according to a community MCP wrapper. — [graph-polymarket-mcp](https://glama.ai/mcp/servers/@PaulieB14/graph-polymarket-mcp) **[secondary]**
- Polymarket's own "Data Resources" page lists:
  - Goldsky: streaming pipelines plus **CryptoHouse**, a ClickHouse SQL dataset
  - Dune: SQL and dashboards, with sample Volume/TVL/OI queries
  - Allium: SQL historical analytics
  - Dashboards by Blockworks, Artemis, Dune, DeFiLlama, The Block, Token Terminal and Allium, plus four community Dune dashboards
  - It warns that "third-party schemas can lag contract upgrades" and tells readers to check indexed addresses against the Contracts page.
  - Source: [Polymarket blockchain data resources](https://docs.polymarket.com/resources/blockchain-data.md)

**Dune curated tables**
- Overview — [Dune Polymarket overview](https://docs.dune.com/data-catalog/curated/prediction-markets/polymarket/overview), [market_trades](https://docs.dune.com/data-catalog/curated/prediction-markets/polymarket/market_trades)
  - Maintainer and refresh: Dune maintains them, with about 24h refresh, on Polygon.
  - Built from: decoded CTF Exchange and NegRisk events plus Polymarket API metadata.
  - Tables: `market_trades`, `market_details`, `positions`, and hourly, daily and latest price tables.
  - `condition_id` is the primary key.
  - The tables are views, so always filter `block_time`.
  - Coverage is **Polymarket Global since Nov 2022**. Polymarket US is not covered.
  - `market_trades` includes three match types: complementary, **MINT** and **MERGE**.
- The Dune docs show inconsistent column names between schema versions, e.g. `maker/taker` vs `action/contract_address`, and `user_address` vs `address` in positions. Check the live schema. — [Dune docs (per search summary)](https://docs.dune.com/data-catalog/curated/prediction-markets/polymarket/positions)
- Dune also has a cross-venue `prediction_markets` curated schema. — [Dune prediction_markets overview](https://docs.dune.com/data-catalog/curated/prediction-markets/prediction_markets/overview)

**Substreams (StreamingFast/The Graph)**
- A `polymarket` package exists (v0.3.0), and its notes record the V2 cutover around 11:00 UTC. — [substreams.dev](https://substreams.dev/packages/polymarket/v0.3.0) **[secondary]**

### Inferences
- Any Dune query, Goldsky pipeline or self-built indexer has to cover **both V1 exchange addresses (before 2026-04-28) and the V2 addresses**, or the time series will break at the migration.
- For volume and price work, decide explicitly whether to include MINT/MERGE "trades". They are not secondary-market exchanges between two traders.

### Gaps
- Not fetched this session, recalled from prior knowledge only **[unverified]**:
  - V1 contract addresses: CTF Exchange `0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E`; NegRisk CTF Exchange `0xC5d563A36AE78145C45a50134d48A1215220f80a`; NegRiskAdapter `0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296`; Conditional Tokens `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045`
  - Check all of these on the [Contracts page](https://docs.polymarket.com/resources/contracts.md).
- Not checked this session:
  - Allium, Flipside, Bitquery and Google BigQuery Polygon public dataset pricing, coverage and current status
  - Flipside's 2025 product changes and whether it still offers free Polygon SQL
- I could not confirm the rchen8 Dune Polymarket dashboard URL or whether it is still maintained.

## 3. Third-party datasets, vendors, aggregators and analytics sites

### Takeaway
The strongest free bulk dataset is **SII-WANGZJ/Polymarket_data** on Hugging Face: about 279 GB of decoded on-chain fills, 2022-11-21 → 2026-10-04, MIT license. For order-book history, the paid options are **Tardis.dev** (from 2026-05-25) and **Telonex** (from 2025-10-11). **Dome**, the best-known unified Polymarket+Kalshi API, was acquired by Polymarket (Feb 2026), and its API reached end of life on 2026-04-28. Many wallet-analytics sites (HashDive, Polymarket Analytics, Betmoar, whale trackers) exist, but I found only marketing-grade documentation for them.

### Cited Findings
**Hugging Face SII-WANGZJ/Polymarket_data** — [HF dataset card](https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/blob/main/README.md)
- Size and coverage:
  - About 279 GB, 6.6B records, about 4.0M markets.
  - Coverage starts at CLOB launch, 2022-11-21, and runs to 2026-10-04. Release dated 2026-10-05; refreshed ad hoc.
  - **Excludes the AMM/FPMM era (2020–Nov 2022).**
- Files:
  - `trades.parquet`: 45.8 GB, ~1.27B rows, recommended
  - `orderfilled.parquet`: 127 GB raw, with 32-byte little-endian amounts
  - `markets.parquet`: ~4.05M rows, latest metadata only
  - `quant.parquet`: YES-normalized
  - `users.parquet`: wallet-keyed
- Sources: Polygon RPC logs plus Gamma API metadata.
- Gotchas:
  - About 18K fills whose tokens are missing from Gamma appear only in the raw file.
  - Hash and address format changed in this release, so re-download all files together.
  - The companion GitHub toolkit converts on-chain data to Parquet. — [search listing](https://docsearch.algolia.com/mcp/docs/repo/sii-wangzj/polymarket_data) **[secondary]**

**warproxxx/poly_data** — [gittrend listing](https://gittrend.io/repo/warproxxx/poly_data) **[secondary]**
- Python retriever for markets, order events and trades.
- About 1.8k stars and 370 forks; last push 2026-04-27, one day before the V2 cutover. Post-V2 compatibility is unverified.

**Tardis.dev** — [Tardis Polymarket docs](https://docs.tardis.dev/historical-data-details/polymarket.md)
- Coverage: Polymarket data **from 2026-05-25**.
- Formats:
  - Raw WS replay.
  - Normalized CSVs: `trades`, `book_ticker`, `incremental_book_L2`, `quotes`, `book_snapshot_5/25`.
- Access: first-of-month CSVs are free without an API key; everything else is paid.
- Symbols are CLOB token IDs, so you need Gamma to map them.
- Token discovery through the grouped trades file misses tokens with no trades that day.

**Telonex** — [Telonex datasets](https://telonex.io/datasets)
- Coverage:
  - Polymarket trades, quotes and order books from **2025-10-11**
  - on-chain fills from inception
  - crypto resolution prices from 2026-04-02
  - Polymarket perpetuals data from 2026-06-21
- Free samples; full pricing not shown.

**Dome**
- YC F25 unified API for Polymarket and Kalshi data. Polymarket acquired it on 2026-02-19 — [The Block](https://theblock.co/post/390546/polymarket-buys-fresh-prediction-market-api-startup-dome-marking-second-official-acquisition), [CasinoBeats](https://casinobeats.com/2026/02/20/polymarket-acquires-dome-to-expand-developer-tools-for-prediction-markets/)
- Dome docs: "all Dome APIs will reach end of life on April 28th, 2026", with users pointed to Polymarket's new APIs — [Dome docs](https://docs.domeapi.io/index.md)
- Alternatives listed by pm.wiki **[secondary/unverified]**:
  - PolyRouter (7 platforms)
  - SimpleFunctions
  - "poly-archive"
  - Source: [pm.wiki compare](https://pm.wiki/compare/dome-vs-poly-archive)

**Kaggle / other dataset hosts**
- I found no dedicated official Kaggle Polymarket price dataset.
- A Kaggle mirror exists of a Hugging Face "settled markets" dataset covering Kalshi+Polymarket: CC-BY-4.0, monthly partitions, refreshed daily. — [SimpleFunctions](https://simplefunctions.dev/opensource/kaggle-settled-markets) **[secondary]**
- IEEE DataPort has a 200-market resolved YES/NO dataset with implied probability 7 days before resolution. — [IEEE DataPort](https://ieee-dataport.org/documents/raw-200-market-dataset-collected-polymarket-api)
- `manja316/polymarket-historical-data`: free markets.csv; full prices and order books are sold on Gumroad; market counts are inconsistent (8,701 vs 13,964). — [ecosyste.ms listing](https://awesome.ecosyste.ms/projects/github.com%2Fmanja316%2Fpolymarket-historical-data) **[secondary]**
- Apify paid scrapers: [pixflor](https://apify.com/pixflor/polymarket-markets-scraper), [haketa](https://apify.com/haketa/polymarket-scraper)
- Bruin `ingestr` has a Polymarket source connector — [getbruin docs](https://getbruin.com/docs/ingestr/supported-sources/polymarket.html)

**Analytics and whale-tracker sites**
- HashDive: wallet-level intelligence, smart-money and whale tracking, large YES/NO holders. — [QuickNode builders guide](https://www.quicknode.com/builders-guide/best/top-10-polymarket-whale-trackers), [dev.to tools guide](https://dev.to/itsragnar/best-polymarket-trading-tools-in-2026-analytics-copy-trading-execution-arbitrage-bots-e43) **[secondary/marketing]**
- Struct: v0.5 added CLOB v2 support, analytics and oracle events. — [Struct blog](https://www.struct.to/blog/v0.5-release) **[secondary]**
- pm.wiki is a community directory of prediction-market projects. — [pm.wiki whale tracker](https://pm.wiki/projects/polymarket-whale-tracker) **[secondary]**

### Inferences
- A cheap, reasonably complete research stack:
  - HF SII-WANGZJ (or Dune) for fills
  - Gamma for metadata
  - CLOB `max` 12h buckets for long-horizon prices
  - Tardis/Telonex only if microstructure or L2 data is needed
- Polymarket buying Dome and shipping v2 APIs (combos, builder routes, `/v2/prices-history`) suggests that third-party unified APIs have become less essential for Polymarket-only work. Cross-venue work still needs a third-party aggregator or your own normalization.

### Gaps
- Not checked this session (no pricing, fields or status confirmed):
  - PolymarketAnalytics.com
  - Betmoar
  - Oddpool
  - Adjacent
  - Verso
  - Zenodo replication packages
  - paid vendors such as Kaiko, Amberdata and CoinAPI
- I found no dedicated Kaggle Polymarket dataset; the search index may have missed it.
- AMM-era (2020–2022) data: no curated source found. It would need FPMM contract event decoding.

## 4. Open-source GitHub tooling

### Takeaway
Official open-source projects include `Polymarket/agents` (an AI trading-agent framework, MIT), the official `poly-market-maker`, `real-time-data-client`, and the CLOB clients. The clients were archived or replaced in 2026. Community repos include `warproxxx/poly_data` (fills downloader), `warproxxx/poly-maker` (market maker configured from Google Sheets), the SII-WANGZJ toolkit, WS libraries such as `polyws`, and a growing number of MCP servers. Most were built for V1 and need checking against V2.

### Cited Findings
- `Polymarket/agents`: official AI-agent trading framework, MIT. Needs Python 3.9, an OpenAI key and a Polygon wallet; uses Chroma for RAG over news/API data. — [Algolia docsearch listing](https://docsearch.algolia.com/mcp/docs/repo/polymarket/agents), [SourcePulse](https://www.sourcepulse.org/projects/972586) **[secondary]**
- `warproxxx/poly-maker`: market-making bot configured through Google Sheets; about 1.1k stars and 425 forks. — [gittrend](https://gittrend.io/repo/warproxxx/poly-maker) **[secondary]**
- `polyws` (PyPI): Python CLOB WebSocket streaming for bots and pipelines. — [PyPI polyws](https://pypi.org/project/polyws/)
- `grokify/polymarket-go`: Go client. — [pkg.go.dev](https://pkg.go.dev/github.com/grokify/polymarket-go)
- `harish-garg/Awesome-Polymarket-Tools`: curated list. — [GitHub](https://github.com/harish-garg/Awesome-Polymarket-Tools)
- MCP servers for LLM agents (Graph subgraphs, price and order-book subscriptions) — [graph-polymarket-mcp](https://glama.ai/mcp/servers/@PaulieB14/graph-polymarket-mcp), [Polymarket-MCP](https://images.glama.ai/mcp/servers/phon3/Polymarket-MCP)
- Official SDK transitions (Section 1): `py-clob-client` archived 2026-05-25 → `py-sdk` / `py-clob-client-v2` — [py-clob-client](https://github.com/Polymarket/py-clob-client), [V2 migration](https://docs.polymarket.com/v2-migration)

### Inferences
- Treat any bot or backtester that signs orders and was last updated before 2026-04-28 as broken for live trading. Its data-reading parts, such as Gamma calls and on-chain decoding of V1 events, may still work for history.

### Gaps
- I did not verify repo-level details (stars, last commit, license) for `Polymarket/poly-market-maker`, `Polymarket/real-time-data-client`, `Polymarket/ctf-exchange`, `Polymarket/neg-risk-ctf-adapter` or `Polymarket/polymarket-subgraph`, or for community arbitrage scanners and backtesters.

## 5. Notable industry/hobbyist analyses and dashboards

### Takeaway
Most widely cited non-academic analyses:
- The **Columbia/Barnard wash-trading paper** (Nov 2025, SSRN, not peer-reviewed): about 25% of volume was artificial on average over three years, peaking near 60% in a month.
- **Dune/Keyrock 2025** prediction-market reports: >$44B industry volume in 2025, Polymarket about $21.5B Jan–Nov.
- Newsletters such as **Alea Research** on the V2 stack rebuild.

I could not find dedicated 2025–26 Galaxy, Messari or The Block research reports on Polymarket in this pass.

### Cited Findings
**Columbia/Barnard wash-trading paper**
- Authors: Sirolly, Ma, Sethi and Kanoria, "Network-Based Detection of Wash-Trading" (SSRN, Nov 2025).
- Findings:
  - Wash trading averaged **~25% of Polymarket buy/sell activity over 3 years**.
  - It reached nearly **60% of volume in a peak month**, with the surge starting around July 2024.
  - The authors blame structural features (crypto wallets, no KYC) rather than Polymarket itself.
- Sources: [Columbia Business School](https://business.columbia.edu/faculty/press/polymarket-volume-inflated-artificial-activity-study-finds), [Fortune](https://fortune.com/2025/11/07/polymarket-wash-trading-inflated-prediction-markets-columbia-research), [CoinTelegraph](https://cointelegraph.com/news/columbia-study-polymarket-wash-trading-research), [Bloomberg](https://www.bloomberg.com/news/articles/2025-11-07/polymarket-volume-inflated-by-artificial-activity-study-finds)

**Dune/Keyrock 2025 reports**
- Total prediction-market notional volume above $44B in 2025, with Polymarket and Kalshi about 85–90% of it.
- Polymarket about $21.5B Jan–Nov 2025, and 95M trades.
- Prediction-market MAUs grew from 4k to 612k.
- Polymarket volume by category: sports 39%, politics 34%, crypto 18%.
- Polymarket retention beats more than 85% of crypto protocols.
- Bernstein gives a higher figure: $51B in 2025.
- Sources: [The Defiant](https://thedefiant.io/news/research-and-opinion/polymarket-hit-usd25-7b-in-march-volume-as-retail-traders-bet-on-sports-politics-and-crypto), [Sacra](https://sacra.com/c/polymarket/) **[secondary relays; original Dune/Keyrock PDFs not fetched]**

**Other figures and write-ups**
- Q1 2026: sports was the largest category at $10.1B volume and politics $5B. Polymarket reached $25.7B in March 2026 monthly volume. — [The Defiant](https://thedefiant.io/news/research-and-opinion/polymarket-hit-usd25-7b-in-march-volume-as-retail-traders-bet-on-sports-politics-and-crypto) **[secondary]**
- "Most Polymarket users lose money as top accounts win big" (2026). — [PYMNTS](https://pymnts.com/markets/2026/most-polymarket-users-lose-money-as-top-accounts-win-big) **[secondary; underlying data source not checked]**
- Alea Research newsletter: "Polymarket: Rebuilding the Stack", on CLOB V2 and pUSD. — [Alea Research](https://alearesearch.io/newsletters/polymarket-rebuilding-the-stack)
- Polymarket's own docs list third-party dashboards from Blockworks, Artemis, Dune, DeFiLlama, The Block, Token Terminal and Allium. — [Polymarket blockchain data](https://docs.polymarket.com/resources/blockchain-data.md)
- Dune's Prediction Markets hub. — [dune.com/data/prediction-markets](https://dune.com/data/prediction-markets)

### Inferences
- Volume figures from different sources differ by window, by whether MINT/MERGE are counted, and by whether wash trades are included. Any report should state which definition it uses, e.g. notional vs. shares, one-sided vs. two-sided, and whether wash-filtered.

### Gaps
- Not fetched or verified:
  - Galaxy Research, Messari, The Block Research reports
  - Polymarket's own "accuracy" page and its calibration methodology
  - rchen8 / Richard Chen Dune dashboards
  - Substack quant write-ups
- These are known from prior knowledge but were not confirmed in this session.

## 6. Practical gotchas (IDs, negRisk, resolution, wash trading, splits/merges, AMM era)

### Takeaway
The main traps in Polymarket data work:
1. ID confusion: Gamma market `id` vs `conditionId` vs per-outcome token or position IDs.
2. negRisk multi-outcome events run on a separate exchange and adapter, where conversions create synthetic flows.
3. MINT/MERGE fills mixed into "trades".
4. Wash-trading contamination of volume, ~25% on average.
5. The V1→V2 contract and collateral break on 2026-04-28.
6. Short retention of fine-grained price history.
7. The 10k offset cap on the Data API v1.
8. The AMM era (pre-Nov 2022) missing from most curated datasets.

### Cited Findings
- **IDs**:
  - Tardis, Dune and CLOB endpoints key on different IDs: Tardis symbols are CLOB token IDs, mapped through Gamma — [Tardis](https://docs.tardis.dev/historical-data-details/polymarket.md); Dune uses `condition_id` as primary key — [Dune](https://docs.dune.com/data-catalog/curated/prediction-markets/polymarket/overview); the CLOB uses `token_id`/`assetId` — [Polymarket](https://docs.polymarket.com/market-data/prices-order-books.md)
  - V2 "Protocol" markets use `positionIds` instead of `clobTokenIds` — [Polymarket](https://docs.polymarket.com/market-data/prices-order-books.md)
- **negRisk**:
  - Separate NegRisk exchange contracts exist in both V1 and V2 — [V2 migration](https://docs.polymarket.com/v2-migration)
  - Dune builds its tables from both CTF and NegRisk events — [Dune](https://docs.dune.com/data-catalog/curated/prediction-markets/polymarket/overview)
  - The HF dataset carries a negative-risk flag per market — [HF](https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/blob/main/README.md)
- **Splits/merges/mints**:
  - Dune `market_trades` mixes complementary, MINT and MERGE matches — [Dune](https://docs.dune.com/data-catalog/curated/prediction-markets/polymarket/overview)
  - The old activity subgraph tracked splits, merges and redemptions separately — [graph-polymarket-mcp](https://glama.ai/mcp/servers/@PaulieB14/graph-polymarket-mcp) **[secondary]**
- **Double counting**:
  - `order_filled` records both maker and taker sides, while `orders_matched` records the taker only — [Goldsky](https://docs.goldsky.com/chains/polymarket)
  - Choosing between them changes volume by about 2×, which is my inference.
- **Wash trading**: ~25% average and ~60% peak month — [Columbia](https://business.columbia.edu/faculty/press/polymarket-volume-inflated-artificial-activity-study-finds)
- **V2 break**: new exchange addresses, pUSD collateral replacing USDC.e, and changed order fields — [V2 migration](https://docs.polymarket.com/v2-migration). Third-party schemas lag upgrades — [Polymarket](https://docs.polymarket.com/resources/blockchain-data.md)
- **Retention**: sub-3h price buckets are kept for only about 7–90 days, and explicit ranges are capped at 15 days — [Polymarket](https://docs.polymarket.com/market-data/prices-order-books.md)
- **Data API v1 offset cap**: 10,000 rows; v1 sunsets 2026-10-24 — [migration](https://docs.polymarket.com/migrate/data-api-v1-to-v2.md)
- **AMM era**: the HF dataset excludes 2020–Nov 2022 FPMM trades — [HF](https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/blob/main/README.md). Dune covers from Nov 2022 — [Dune](https://docs.dune.com/data-catalog/curated/prediction-markets/polymarket/overview)
- **Metadata snapshot**: `markets.parquet` holds only the latest metadata per market, so it cannot rebuild metadata as it stood at the time of trading — [HF](https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/blob/main/README.md)

### Inferences
- Recommended canonical keys:
  - `condition_id` for the market
  - token or position ID for the outcome
  - `negRiskMarketID` or event ID for grouping mutually exclusive outcomes
- Keep a crosswalk table that spans V1 and V2.

### Gaps
- UMA Optimistic Oracle resolution timing (2-hour liveness, the dispute/DVM escalation path, and the gap between "closed" and "resolved" timestamps) was not verified from primary sources in this session.
- The negRisk "convert" mechanics and their effect on volume accounting were not checked.
