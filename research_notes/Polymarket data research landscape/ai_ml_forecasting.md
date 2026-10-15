# Polymarket Data in AI/LLM Forecasting, ML, and Autonomous Trading Agents (through Oct 2026)

Notes compiled 2026-10-15. Verification legend: **[V]** = details read on the primary source page (arXiv abstract/HTML, official blog); **[S]** = details only from search-result snippets/secondary summaries, not opened; **[CR]** = company/self-reported, not independently audited. arXiv IDs encode year+month (e.g., 2607.xxxxx = July 2026).

## 1. Forecasting benchmarks that draw on Polymarket questions, prices, or outcomes

### Takeaway
Polymarket is now a standard source of resolved binary questions and of a "market baseline" for LLM forecasting benchmarks (Halawi et al. 2024, ForecastBench, LEAF, Hindcast, RMF, PolyBench). Across nearly all careful studies, **the market price is still the bar LLMs fail to clear on their own**. LLMs roughly match or trail market Brier scores, and blending LLM + market beats either alone. Some benchmarks often grouped with these (Prophet Arena, KalshiBench) actually use **Kalshi** rather than Polymarket.

### Cited Findings

**Halawi, Zhang, Chen & Steinhardt (2024), "Approaching Human-Level Forecasting with Language Models"** — arXiv 2402.18563 (Feb 28 2024); NeurIPS 2024 poster [V]
- Retrieval-augmented LM system (search → reason → aggregate); evaluated on questions published after model cutoffs — [arXiv abs](https://arxiv.org/abs/2402.18563); [NeurIPS 2024](https://neurips.cc/virtual/2024/poster/95949)
- Question sources: Metaculus, Good Judgment Open, INFER, **Polymarket**, Manifold. Polymarket contributes 70 train / 229 val / 300 test questions — [arXiv HTML](https://arxiv.org/html/2402.18563v1)
- Raw data: 48,754 questions, 7,174,607 user forecasts (2015–2024); curated binary set 5,516 (train 3,762 / val 840 / test 914, test opened ≥ June 1 2023) — [arXiv HTML](https://arxiv.org/html/2402.18563v1)
- Test Brier: system **0.179** vs crowd aggregate **0.149**; weighted system+crowd **0.146** (best) — [arXiv HTML](https://arxiv.org/html/2402.18563v1)
- Selective setting (crowd uncertain, early retrieval, ≥5 articles): system 0.240 vs crowd 0.247 (22% of forecasts) — [arXiv HTML](https://arxiv.org/html/2402.18563v1). Note: some summaries quote only the 0.240/0.247 selective number as the headline; the all-question result is that the crowd wins.

**ForecastBench (Karger et al.; Forecasting Research Institute), ICLR 2025, living benchmark**
- Market questions drawn from Manifold, Metaculus, **Polymarket**, RAND Forecasting Initiative/INFER; dataset questions auto-generated from ACLED, DBnomics, FRED, Wikipedia, Yahoo Finance; biweekly rounds [S] — [EA Forum announcement](https://forum.effectivealtruism.org/posts/zwzgR8iuFEcJms3Hu/announcing-forecastbench-a-new-benchmark-for-ai-and-human); [ICLR 2025 slides](https://www.iclr.cc/media/iclr-2025/Slides/28507.pdf). Round sizes reported inconsistently (500 vs 1,000 questions) across secondary sources [S].
- FRI update: best model GPT-4.5 Brier **0.101** vs superforecasters **0.081**; projected LLM–superforecaster parity late 2026 (95% CI Dec 2025–Jan 2028); trend ≈0.016 Brier/yr; public median fell from #2 to #22 on leaderboard [S] — [FRI Substack](https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark)
- **July 2026:** FRI claims "AI models have likely reached parity with superforecasters on ForecastBench"; top tournament entry a Cassi AI system, with xAI and Google DeepMind models statistically indistinguishable from superforecasters [S] — [FRI parity post](https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity)
- Rebuttal: Good Judgment says supers still lead on **market questions** (80.3 vs 75.8 for nearest AI) and that early "parity" relied on a preliminary board [S] — [Good Judgment](https://goodjudgment.substack.com/p/what-forecastbench-doesnt-measure)
- **"The Copier Line" (EA Forum, ~Aug 21 2026, author "Dominus"; data as of Aug 11 2026)** [V]: ForecastBench market questions show forecasters a freeze price from 10 days before the due date. A forecaster who simply submits that shown price scores **70.93** on the Brier Index. Of 527 tested entries, **442 score significantly worse than the market price** (5% FDR) and **none significantly beat it**. 204/273 leaderboard entries (75%) score at or below the copier line. ForecastBench's own baseline LLMs score 51.5 without the price and 68.1 with it (still below copying). Superforecasters sit 4.67 points above the line, Cassi 5.67 — [EA Forum](https://forum.effectivealtruism.org/posts/8YuG9EuhyYqaNBt7F/the-copier-line-what-forecastbench-s-market-scores-actually)

**AIA Forecaster (Alur, Stadie, Kang, … Sekhon; 14 authors), arXiv 2511.07678 (Nov 10 2025)** [V]
- Matches human superforecasters on ForecastBench. On a new benchmark built from "liquid prediction markets," it **underperforms market consensus alone**, but an ensemble of AIA + market consensus beats consensus — [arXiv](https://arxiv.org/abs/2511.07678)
- Blends via simplex-constrained regression minimizing Brier [S] — [arXiv PDF](https://arxiv.org/pdf/2511.07678). Third-party reference to Alur et al. on a 76-question FB-Market subset: superforecaster median 0.0740, public 0.1035, market consensus 0.0965 [S] — [FRI/secondary via search](https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark)
- The abstract page does not name the market platform (Polymarket unconfirmed).

**Prophet Arena / "LLM-as-a-Prophet" (Yang, Mahns, Li, Gu, Wu, Xu; UChicago et al.), arXiv 2510.17638 v2 Dec 21 2025; ICLR 2026** [V]
- 1,367 resolved events (72,136 markets), cutoff Oct 11 2025; 23 LLMs — [arXiv HTML](https://arxiv.org/html/2510.17638v2); [ICLR 2026](https://iclr.cc/virtual/2026/poster/10009102)
- **Source is Kalshi** in the paper; Decrypt reports events from "Kalshi and Polymarket" — [Decrypt](https://decrypt.co/336298/ai-now-matches-prediction-markets-in-forecasting-real-events-study-finds?amp=1). These sources conflict; the paper text mentions no Polymarket.
- Brier: GPT-5(R) 0.184, Grok-4 0.189, Claude Sonnet 4 0.194, Gemini 2.5 Flash 0.197, Llama-4-Scout 0.219, **Market baseline 0.187**. All LLMs are better calibrated (ECE) than the market. GPT-5 average return 0.943, below break-even. Markets aggregate faster near resolution; LLMs are more conservative on near-certain outcomes — [arXiv HTML](https://arxiv.org/html/2510.17638v2)

**KalshiBench (Lukas Nel, Lotus AI), arXiv 2512.16030 (Dec 2025)** [S]: 300 **Kalshi** questions; Claude Opus 4.5, GPT-5.2, DeepSeek-V3.2, Qwen3-235B, Kimi-K2 all overconfident; Opus 4.5 best ECE 0.120, GPT-5.2-XHigh ECE 0.395; only one model has positive Brier Skill Score vs base rate — [arXiv](https://arxiv.org/html/2512.16030v1). Not Polymarket-based.

**Resolved Market Forecasting (RMF): "Can LLMs Predict the Future? A Brier Score Analysis of Prediction Markets" (Yuanbo Li, Zekun Li, Xiaoyan Cong; Brown), arXiv 2609.32885 (Sep 26 2026)** [V]
- 3,000 binary questions stratified from **>600,000 resolved Polymarket markets** (2021–2026), 9 domains; zero-shot, no retrieval/market context — [arXiv HTML](https://arxiv.org/html/2609.32885)
- Post-cutoff Brier (base-rate predictor in parens): Sonnet 4.5 .186 (.216), Sonnet 4.6 .189, Opus 4.1 .183, Opus 4.6 .192, Qwen2.5-7B .234 (worse than base rate), Qwen2.5-32B .210 (not significantly different). Pre-cutoff Brier is *higher* (e.g., Opus 4.1 .211). Category matters more than model size. **No comparison to market price** (listed as a limitation) — [arXiv HTML](https://arxiv.org/html/2609.32885)

**Hindcast (Ye, Dineen, Zhu, Lu, Song, Zhou; ASU), arXiv 2607.14051 (Jul 15 2026)** [V]
- Pool: 7,913 binary Polymarket markets / 1,916 events (3,427 resolved); eval set 216 balanced markets; retrieval over a frozen, monthly-snapshotted Reddit archive (~18.3M docs, Jan 2024–Jan 2026) with a strict `created_at < t0` cutoff — [arXiv HTML](https://arxiv.org/html/2607.14051)
- Polymarket implied probability at t0 (day before close) is the matched-time human baseline. 9 open-weight models (Qwen3 4B/8B/32B, Llama 3.x, Gemma-3, Ministral-8B, R1-Distill-Qwen-7B). Retrieval lowers Brier on 8 of 9 (Qwen3-32B 0.234→0.179, −23%). Retrieval hurts on hype-prone topics (Entertainment). No numeric market Brier reported in the main tables — [arXiv HTML](https://arxiv.org/html/2607.14051)

**LEAF: A Living Benchmark for Event-Augmented Forecasting (Tan, Parmar, Goyal, Li, Peng, Hartvigsen, Yoon, Pfister; UVA + Google Cloud AI Research), arXiv 2605.16358 v2 (Oct 1 2026)** [V]
- 500 expert-audited tasks across 5 domains; Polymarket API supplies the event-forecasting domain (66 entities), with cutoffs at 100%→10% of time-to-resolution, Brier-scored — [arXiv HTML](https://arxiv.org/html/2605.16358v2)
- ~16–17 LLMs (Claude 4.6–5, Gemini 3.x, Grok 4.x, Qwen3.5, Gemma-3) plus TimesFM 3.0 and Chronos-2. Verified event context gives +25% relative improvement on event forecasting. Pre-cutoff evaluation inflates equity-trend performance ~147%. Fact-checking cut future-info leakage from 8.6% to 1.6% — [arXiv HTML](https://arxiv.org/html/2605.16358v2)

**Bench to the Future (BTF) — Wildman, Bosse, Hambly, Schwarz, Phillips (FutureSearch), arXiv 2506.21558 (Jun 2025)** [S]: "pastcasting" with an offline web corpus per question. BTF-3 is reported as 1,907 questions (homepage) vs 1,007 (evals page), a conflict. June 2026 leaderboard: FutureSearch SOTA 0.120 pooled, Claude Fable 5 (high) 0.126, Opus 4.8 0.127 — [FutureSearch evals](https://evals.futuresearch.ai/); [Epoch BTF-3](https://epoch.ai/benchmarks/btf-3). Whether BTF questions come from Polymarket is **unverified**. FutureSearch also published a Polymarket forecasting tutorial — [FutureSearch](https://futuresearch.ai/blog/polymarket-forecasting-tutorial)

**FutureX (Zeng et al.), ICLR 2026** [S]: live, daily-updated benchmark for LLM agents, 25 models, automated question/answer pipeline to avoid contamination — [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/21315abf210cef71317e887e9cda78b3-Abstract-Conference.html). Polymarket as a question source is **not confirmed** in sources I saw.

**Pitfalls in Evaluating Language Model Forecasters (Paleka, Goel, Geiping, Tramèr), arXiv 2506.00723; ICLR 2026** [S]: temporal leakage (logical leakage in backtests, unreliable date-restricted retrieval, misjudged knowledge cutoffs) and poor extrapolation from benchmarks to real-world forecasting undermine "human-parity" claims — [arXiv](https://arxiv.org/html/2506.00723v1); [mlanthology](https://mlanthology.org/iclr/2026/paleka2026iclr-pitfalls/)

**Other 2026 arXiv items (snippet-level only)** [S]:
- *Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs* (2604.18576): uses market price as a prior; a "Crowd+emp" market-only baseline; the crowd anchor substantially improves results — [arXiv](https://arxiv.org/html/2604.18576v4)
- *Foresight Arena* (2605.00420): on-chain live benchmark for AI forecasting agents, no live results reported yet — [arXiv](https://arxiv.org/pdf/2605.00420)
- *Reinforcement Learning for LLM-based Event Forecasting* (2606.15917) — [arXiv](https://arxiv.org/pdf/2606.15917)
- arXiv 2511.18394 (Nov 2025) analyzes which question types LLMs answer confidently, referencing Metaculus AI benchmark & ForecastBench built on market questions incl. Polymarket — [arXiv](https://arxiv.org/pdf/2511.18394v1)

**Metaculus AI Forecasting Benchmark (context; uses Metaculus questions, not Polymarket)** [S]: Q3 2024 Pro median beat all 34 bots (31 significant); Q4 2024 top bot not significantly worse (p=0.079); Q1 2025 pros "crush" bots (bot team −17.7); Q2 2025 bot team −20.03 vs pros, o3 best model; Spring 2026 "FutureEval": pros beat bots, figures not confirmed. Metaculus says the base model matters more than scaffolding — [Q3 2024](https://forum.nunosempere.com/posts/E3hiRG68wc6zLWr6m/can-ai-outpredict-humans-results-from-metaculus-s-q3-ai); [Q4 2024](https://www.lesswrong.com/posts/P8YwCvHoF2FHQoHjF/metaculus-q4-ai-benchmarking-bots-are-closing-the-gap); [Q1 2025](https://forum.nunosempere.com/posts/mwcWxwdsEMexm98GF/q1-ai-benchmarking-results-human-pros-crush-bots); [Q2 2025](https://www.lesswrong.com/posts/Surnjh8A4WjgtQTkZ/q2-ai-benchmark-results-pros-maintain-clear-lead); [Spring 2026](https://www.greaterwrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is)

### Inferences
- The consistent pattern (Halawi 0.179 vs crowd 0.149; Prophet Arena ≈ market; AIA < market alone; the ForecastBench copier-line analysis) is that **LLMs have reached roughly crowd level, but not reliably above the market price at the same timestamp**. Ensembles with the market price do add signal.
- "Parity with superforecasters" claims (FRI, July 2026) and "beats market" claims depend heavily on what reference forecast is used (market price shown vs due-date price vs base rate). Benchmarks that compare only to base rates (RMF, KalshiBench) set a much weaker bar.
- Leakage is the dominant methodological concern. The newer Polymarket benchmarks (Hindcast, LEAF, PolyBench) build in explicit timestamp-locked retrieval for this reason.

### Gaps
- Could not confirm whether FutureX or Bench to the Future draw questions from Polymarket.
- Could not open the official ForecastBench leaderboard or the July 2026 FRI post directly. Numbers come from Substack snippets and EA Forum.
- "PROPHET" (as distinct from Prophet Arena) and Autocast-style Polymarket datasets: no specific Polymarket-based PROPHET dataset found. Autocast (Zou et al. 2022) is cited as a precursor without real-time market grounding — [PolyBench](https://arxiv.org/html/2604.14199v1).

## 2. LLM trading agents and AI-run Polymarket accounts

### Takeaway
Real-money and backtest studies through mid-2026 show **LLM trading agents mostly lose money or roughly break even** on prediction markets. In PolyBench, 2 of 7 models had positive returns, and in Prediction Arena all six live-trading models lost money on Kalshi. Agent tooling (Polymarket/agents, Olas Polystrat, MCP servers) is abundant, but independent performance evidence is thin and mostly self-reported.

### Cited Findings

**PolyBench (Pu Cheng, Juncheng Liu, Yunshen Long; Sichuan Univ.), arXiv 2604.14199 (Apr 3 2026)** [V]
- 38,666 binary Polymarket markets / 4,997 events; 5,097 prediction-ready snapshots pairing CLOB order-book state with Google News; data collected Feb 6–12 2026; resolutions via official Polymarket outcomes; trades simulated by sweeping the historical order book — [arXiv HTML](https://arxiv.org/html/2604.14199v1)
- 7 models (GPT-OSS-120B, DeepSeek-V3.2, MiMo-V2-Flash, MiniMax-M2.5, Trinity-Large-Preview, Gemini-3-Flash-Preview, Grok-4.1-Fast); 36,165 predictions. Only **MiMo-V2-Flash (+17.6% CWR)** and **Gemini-3-Flash (+6.2%)** were profitable; the others ranged −9.2% to −25.2%. Average confidence 0.81–0.87 regardless of outcome. Returns degrade with lot size because of slippage. No Brier scores; the authors avoid proper scoring rules — [arXiv HTML](https://arxiv.org/html/2604.14199v1)

**Prediction Arena (Zhang, Liu, Johansson, Yitayew, Ohly, Li; Arcada Labs/Harvard), arXiv 2604.07355 (Mar 28 2026)** [V]
- Live trading Jan 12–Mar 9 2026 on Kalshi (curated) and Polymarket (open discovery); $10,000 per agent — [arXiv HTML](https://arxiv.org/html/2604.07355v1)
- Kalshi: all 6 lost (best glm-4.7 −16.0%, worst grok-4-1-fast −30.8%); 71–97% of settled Kalshi positions were weather markets. **Polymarket (Feb 9–Mar 9): average −1.1%**; grok-4-20 −1.85% with a 71.4% settlement win rate; gpt-5.2 −0.42%; claude-opus-4-5 −2.68%. Cohort 2 (3-day paper trading): gemini-3.1-pro +6.02% on Polymarket, claude-opus-4-6 −10.06%. Accuracy drives performance, and token usage/research volume does not — [arXiv HTML](https://arxiv.org/html/2604.07355v1)

**LiveTradeBench (Yu et al.), arXiv 2511.03628 (Nov 2025)** [S]: live trading across US stocks and Polymarket; high LMArena scores do not imply better trading; covers only ~10 markets per PolyBench's comparison — [arXiv](https://www.arxiv.org/pdf/2511.03628); [PolyBench related work](https://arxiv.org/html/2604.14199v1). Also *When Agents Trade: Live Multi-Market Trading Benchmark for LLM Agents* (2510.11695) — [arXiv](https://arxiv.org/html/2510.11695v2) [S]

**PolySwarm, arXiv 2604.03888 (Apr 2026)** [S]: 50 LLM personas evaluate Polymarket binary markets; the authors claim swarm aggregation beats single models on calibration; also latency arbitrage. Needs independent replication — [arXiv](https://arxiv.org/abs/2604.03888); [Pith review](https://pith.science/paper/2604.03888)

**PolyGnosis 2.0, arXiv 2605.25958** [S]: agentic harness engineering for Polymarket + OSINT insight extraction, testing whether scaffolding improves reasoning without changing the base model — [arXiv](https://arxiv.org/pdf/2605.25958)

**Polymarket/agents (official, MIT license)** [S]: Python framework that sources news/web data via RAG, connects to the Gamma API, filters markets, performs "superforecaster-style" probability estimation, and trades on the gap vs market price; requires an OpenAI key and a Polygon wallet. Star counts differ by source (608 vs 3.4k); last push reported ~1 yr ago — [Polymarket Agents docs](https://docsearch.algolia.com/mcp/docs/repo/polymarket/agents); [gittrend](https://gittrend.io/repo/Polymarket/agents). Related community projects: Mist-kail PolyMarket-trading-AI-model (LangChain + Chroma RAG), ai-polymarket-agent (MCP server), PolyClaw (Chainstack CLI agent), grokify/polymarket-go — [sourcepulse](https://www.sourcepulse.org/projects/20158132); [QuickNode](https://www.quicknode.com/builders-guide/tools/polyclaw-by-chainstack); [pkg.go.dev](https://pkg.go.dev/github.com/grokify/polymarket-go)

**Olas / Valory Polystrat (launched on Polymarket Feb 2026)** [CR][S]: self-custodied autonomous agents. Valory's CEO reports 56–69% accuracy and "2–3x human traders" but "not yet at fleet-wide break even," and says naive prompting of off-the-shelf models is ~coin-flip. Omenstrat/Olas Predict run on Omen (Gnosis) using the Mech Marketplace. LayerHub claim: >30% of Polymarket wallets used AI agents; 7–13% of humans vs >37% of AI-agent users profitable (single analytics source) — [MEXC news](https://www.mexc.com/news/997996); [pm.wiki AIOmen](https://pm.wiki/ko/projects/aiomen); [digitaltoday](https://www.digitaltoday.co.kr/vn/view/63463/ai-upends-crypto-prediction-markets-single-trade-returns-376-percent)

**Lightning Rod Labs Foresight-32B (live Polymarket)** [CR]: on 251 live Polymarket questions (Jul–Aug 2025): Foresight-32B Brier 0.199, ECE 6.0%, vs o3 0.205; **the Polymarket market itself scored 0.170**, better than every model — [HF model card](https://huggingface.co/LightningRodLabs/foresight-32B/blob/main/README.md); [Lightning Rod blog](https://blog.lightningrod.ai/p/foresight-32b-beats-frontier-llms-on-live-polymarket-predictions)

### Inferences
- Across PolyBench, Prediction Arena, and Prophet Arena (market-return metric), LLM agents fall around or below break-even after spreads and slippage. Polymarket losses in Prediction Arena were much smaller than Kalshi losses, which plausibly reflects market selection (Kalshi weather) rather than skill.
- Claims about "AI bots dominating Polymarket" are mostly vendor or analytics-firm statements without audited methodology.

### Gaps
- No peer-reviewed audit of real AI-run Polymarket accounts or leaderboard bots was found. I did not find a "PolyAgent" paper specifically.
- Long-horizon real-money track records (>3 months) of LLM agents on Polymarket are absent from the literature I found.

## 3. Training ML/LLMs with Polymarket outcomes and prices (RL, calibration, soft labels, retrieval, leakage)

### Takeaway
The main training-side use of Polymarket is as **verifiable resolution labels for outcome-based RL/DPO** (Lightning Rod Labs / Turtel et al.). Market prices serve as baselines, priors, or ensemble components rather than as soft labels in published work. Retrieval-augmented forecasting with timestamp-locked corpora is the dominant inference method, and leakage/contamination is the central validity concern.

### Cited Findings
- **Turtel, Franklin, Schoenegger, "LLMs Can Teach Themselves to Better Predict the Future," arXiv 2502.05253 (Feb 7 2025)** [V]: self-play generates reasoning traces + forecasts, which are ranked by distance to the realized outcome and used for DPO. Phi-4 14B and DeepSeek-R1 14B gain 7–10% accuracy over base/control, ~GPT-4o level. The abstract page does not state the data source — [arXiv](https://arxiv.org/abs/2502.05253)
- **Turtel, Franklin, Skotheim, Hewitt, Schoenegger, "Outcome-based Reinforcement Learning to Predict the Future," arXiv 2505.17989 (May 23 2025; v4 Dec 1 2025)** [V]: RLVR on a 14B reasoning model with prediction-market questions + news headlines, synthetic question augmentation, and median-sampling. Matches/surpasses o1 accuracy with much better calibration; **>10% ROI in a Polymarket trading simulation** — [arXiv](https://arxiv.org/abs/2505.17989). Snippet-level details [S]: ~10,000 resolved Polymarket yes/no contracts + 100,000 synthetic prompts; ReMax ensemble Brier 0.193 on a 3,300-question hold-out; ECE ~half of o1's; $35 profit edge over o1 (95% CI +$2.0 to +$68.6, p=0.037) — [arXiv PDF v1](https://arxiv.org/pdf/2505.17989v1)
- **Foresight-32B** (Qwen3-32B + GRPO, Brier as reward, ~10k real + ~100k synthetic questions, information restricted to prediction time) [CR] — [HF model card](https://huggingface.co/LightningRodLabs/foresight-32B/blob/main/README.md). The company also claims #1 on Prophet Arena sports (Feb 2026) and ForecastBench top-5 (Jan 2026) [CR] — [Lightning Rod blog](https://blog.lightningrod.ai/p/ai-reaches-human-superforecaster-range)
- Market price as prior/ensemble component: Halawi system+crowd 0.146 < crowd 0.149 — [arXiv HTML](https://arxiv.org/html/2402.18563v1); AIA + market > market — [arXiv](https://arxiv.org/abs/2511.07678); Bayesian linguistic-belief agent anchored on crowd price [S] — [arXiv](https://arxiv.org/html/2604.18576v4)
- Showing the market price to LLMs raises ForecastBench baseline scores (51.5→68.1) but still below copying the price (70.93) — [EA Forum](https://forum.effectivealtruism.org/posts/8YuG9EuhyYqaNBt7F/the-copier-line-what-forecastbench-s-market-scores-actually)
- Leakage evidence: Dong et al. (2024) find contamination can inflate accuracy by up to 66.9% (cited in PolyBench) — [PolyBench](https://arxiv.org/html/2604.14199v1); LEAF finds +147% inflation for pre-cutoff equity tasks — [LEAF](https://arxiv.org/html/2605.16358v2); RMF finds pre-cutoff Brier is *worse*, not better, for Claude models — [RMF](https://arxiv.org/html/2609.32885); Pitfalls paper catalogs leakage modes — [arXiv](https://arxiv.org/html/2506.00723v1)
- Retrieval gains are topic-dependent: Hindcast (−23% Brier for Qwen3-32B, but regressions on Entertainment) — [arXiv](https://arxiv.org/html/2607.14051); Prophet Arena (news helps on average, not uniformly) — [arXiv](https://arxiv.org/html/2510.17638v2)

### Inferences
- Polymarket's value for training is its large volume of cleanly resolved binary outcomes (hundreds of thousands of markets per RMF), which suits RLVR with Brier rewards.
- Using market probabilities as soft labels/distillation targets is an obvious next step, but I found no published paper doing it explicitly.

### Gaps
- No primary source found on Polymarket prices as labels for sentiment analysis, news-impact estimation, or nowcasting in NLP/ML venues. This literature may exist in econ/finance (outside this scope) or may be sparse.
- No paper found that trains on market probabilities as soft labels for calibration.

## 4. Hugging Face / Kaggle datasets of Polymarket data for ML

### Takeaway
Several community datasets exist, ranging from billion-row trade histories to tiny question/price/resolution sets. None is a canonical, maintained ML forecasting benchmark; benchmark papers mostly build their own from the Gamma/CLOB APIs.

### Cited Findings
- **SII-WANGZJ/Polymarket_data** (Hugging Face): >1.1B records across orderfilled, trades, markets, quant, and users tables; loadable via `datasets`; lists academic prediction-market research as an intended use [S] — [HF README](https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data/blob/main/README.md)
- **PercyResearch/forecasting_v2**: question, prompt, Polymarket price snapshot, snapshot date, resolution date, 0/1 resolution; only 10 training examples [S] — [HF README](https://huggingface.co/datasets/PercyResearch/forecasting_v2/blob/main/README.md)
- **"Settled Markets" (SimpleFunctions, CC-BY-4.0)**: Kalshi + Polymarket rows with venue, ticker, title, category, price at settlement, price 24h before, resolved outcome; positioned for calibration studies [S] — [simplefunctions.dev](https://simplefunctions.dev/opensource/hf-settled-markets)
- **athetus** HF account: polymarket-trades and live feed datasets (schema not described) [S] — [HF](https://huggingface.co/athetus)
- **otrofimo/polymarket_data** GitHub toolkit [S] — [GitHub](https://github.com/otrofimo/polymarket_data)
- Paper-derived corpora: PolyBench (38,666 markets + order book + news) — [arXiv](https://arxiv.org/html/2604.14199v1); Hindcast (7,913 markets + 18.3M Reddit docs) — [arXiv](https://arxiv.org/html/2607.14051); RMF (3,000 from >600k resolved) — [arXiv](https://arxiv.org/html/2609.32885); Halawi (Polymarket subset 599 questions) — [arXiv](https://arxiv.org/html/2402.18563v1)

### Inferences
- Researchers needing leakage-safe evaluation should pair resolved Polymarket outcomes with timestamped price histories (e.g., "price 24h before settlement") rather than final prices, which embed the outcome.

### Gaps
- Kaggle Polymarket datasets were not searched successfully. Their sizes, licences, and maintenance status are unverified.
- Release status and licence of the PolyBench/Hindcast/RMF datasets were not confirmed.

## 5. Market crowd vs LLMs vs superforecasters: head-to-head summary

### Takeaway
Ordering on matched questions through Oct 2026: **superforecasters ≳ market price > best LLM systems > public ≈ base rate**, with LLM+market ensembles slightly beating the market. LLMs are often *better calibrated* than markets but not more accurate.

### Cited Findings
| Study | LLM best | Market/crowd | Supers | Source |
|---|---|---|---|---|
| Halawi 2024 (test, 914 q) | 0.179 | crowd 0.149; ensemble 0.146 | — | [arXiv](https://arxiv.org/html/2402.18563v1) |
| Prophet Arena (1,367 Kalshi events) | GPT-5 0.184 | market 0.187 | — | [arXiv](https://arxiv.org/html/2510.17638v2) |
| Foresight live Polymarket (251 q) [CR] | 0.199 | market 0.170 | — | [HF](https://huggingface.co/LightningRodLabs/foresight-32B/blob/main/README.md) |
| ForecastBench (FRI update) [S] | GPT-4.5 0.101 | — | 0.081 | [FRI](https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark) |
| ForecastBench market Qs (Aug 2026) | 0/527 significantly beat shown price | copier line 70.93 index | +4.67 above line | [EA Forum](https://forum.effectivealtruism.org/posts/8YuG9EuhyYqaNBt7F/the-copier-line-what-forecastbench-s-market-scores-actually) |
| FB-Market 76-q subset (Alur et al.) [S] | — | market 0.0965; public 0.1035 | 0.0740 | [FRI substack](https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark) |
| RMF (Polymarket, 3,000 q, no market comparison) | Opus 4.1 0.183 | base rate ~0.216 | — | [arXiv](https://arxiv.org/html/2609.32885) |

### Inferences
- Superforecasters still lead on ForecastBench market questions per Good Judgment (80.3 vs 75.8). FRI's July 2026 parity claim is strongest on dataset questions and contested on market questions.

### Gaps
- No single study puts Polymarket price, superforecasters, and frontier LLMs on identical Polymarket questions at identical timestamps with published Brier scores.
