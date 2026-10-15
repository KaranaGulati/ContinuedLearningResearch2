"""Pre-registered analyses for the reading-direction study (see 01_preregistration.md).

Usage: python analysis.py <scenario parquet from prepare.py> <output dir>
Writes results.json and per-country / per-order CSVs to the output dir.
"""
import json
import sys
from pathlib import Path

import duckdb
import numpy as np
from scipy import stats

scen, outdir = sys.argv[1], Path(sys.argv[2])
outdir.mkdir(parents=True, exist_ok=True)
con = duckdb.connect()
rng = np.random.default_rng(20261015)
R = {}


def users(template):
    """User-level left-click counts for one device template."""
    return con.sql(f"""
        SELECT UserID, grp, any_value(country) AS country,
               sum(clicked_left) AS k, count(*) AS n
        FROM read_parquet('{scen}') WHERE template = '{template}' AND grp <> 'EXCLUDED'
        GROUP BY UserID, grp""").df()


def cluster_prop(k, n):
    """Decision-level proportion with a user-clustered standard error."""
    p = k.sum() / n.sum()
    g = len(k)
    var = (g / (g - 1)) * np.sum((k - p * n) ** 2) / n.sum() ** 2
    return p, np.sqrt(var)


def describe(df, grp):
    d = df[df.grp == grp]
    rate = d.k / d.n
    p, se = cluster_prop(d.k.values, d.n.values)
    return d, rate, {"users": int(len(d)), "decisions": int(d.n.sum()),
                     "decision_rate": p, "decision_se": se,
                     "ci95": [p - 1.96 * se, p + 1.96 * se],
                     "user_mean": rate.mean(), "user_sd": rate.std(ddof=1)}


def compare(df, a, b="LTR"):
    da, ra, sa = describe(df, a)
    db, rb, sb = describe(df, b)
    t = stats.ttest_ind(ra, rb, equal_var=False)
    pooled = np.sqrt((ra.var(ddof=1) + rb.var(ddof=1)) / 2)
    diff = sa["decision_rate"] - sb["decision_rate"]
    se = np.sqrt(sa["decision_se"] ** 2 + sb["decision_se"] ** 2)
    return {a: sa, b: sb,
            "welch_user_level": {"t": t.statistic, "df": t.df, "p": t.pvalue,
                                 "diff_user_means_pp": 100 * (ra.mean() - rb.mean()),
                                 "cohens_d": (ra.mean() - rb.mean()) / pooled},
            "lpm_decision_level": {"diff_pp": 100 * diff, "se_pp": 100 * se,
                                   "z": diff / se, "p": 2 * stats.norm.sf(abs(diff / se))}}


def country_level(df, a, b="LTR", min_users=100, n_perm=10000):
    c = df.groupby(["country", "grp"]).agg(k=("k", "sum"), n=("n", "sum"), users=("k", "size")).reset_index()
    c["rate"] = c.k / c.n
    c = c[c.users >= min_users]
    xa, xb = c[c.grp == a].rate.values, c[c.grp == b].rate.values
    t = stats.ttest_ind(xa, xb, equal_var=False)
    obs = xa.mean() - xb.mean()
    pooled = np.concatenate([xa, xb])
    perm = np.empty(n_perm)
    for i in range(n_perm):
        rng.shuffle(pooled)
        perm[i] = pooled[:len(xa)].mean() - pooled[len(xa):].mean()
    return c, {"countries": {a: int(len(xa)), b: int(len(xb))},
               "mean_rate": {a: xa.mean(), b: xb.mean()},
               "diff_pp": 100 * obs, "welch_t": t.statistic, "welch_p": t.pvalue,
               "perm_p_two_sided": float(np.mean(np.abs(perm) >= abs(obs))),
               "mannwhitney_p": stats.mannwhitneyu(xa, xb).pvalue,
               f"{a}_countries": c[c.grp == a][["country", "users", "rate"]].round(4).values.tolist()}


# Randomisation check: was the stay outcome equally likely to be on the left?
R["randomisation_check"] = con.sql(f"""
    SELECT template, avg(stay_on_left) AS p_stay_on_left, count(*) AS n
    FROM read_parquet('{scen}') GROUP BY template""").df().to_dict("records")

for template in ["Desktop", "Mobile"]:
    df = users(template)
    key = template.lower()
    R[key] = {}
    # H1
    d, rate, s = describe(df, "LTR")
    t = stats.ttest_1samp(rate, 0.5)
    R[key]["H1_LTR_vs_half"] = {**s, "t": t.statistic, "df": len(rate) - 1, "p": t.pvalue,
                               "cohens_d": (rate.mean() - 0.5) / rate.std(ddof=1)}
    # H2, H3
    R[key]["H2_ARABIC_vs_LTR"] = compare(df, "ARABIC")
    R[key]["H3_RTL_OTHER_vs_LTR"] = compare(df, "RTL_OTHER")
    c2, R[key]["H2_country_level"] = country_level(df, "ARABIC")
    c3, R[key]["H3_country_level"] = country_level(df, "RTL_OTHER")
    # Per-country table for the RTL_OTHER group regardless of size, and all countries for plotting
    allc = df.groupby(["country", "grp"]).agg(k=("k", "sum"), n=("n", "sum"), users=("k", "size")).reset_index()
    allc["rate"] = allc.k / allc.n
    allc["se"] = np.sqrt(allc.rate * (1 - allc.rate) / allc.n)
    allc.sort_values("rate").to_csv(outdir / f"country_rates_{key}.csv", index=False)

# Exploratory E1: scenario order, E2: description shown (desktop)
for col, name in [("scenario_order", "E1_by_scenario_order"), ("description_shown", "E2_by_description_shown")]:
    e = con.sql(f"""
        SELECT grp, {col} AS level, avg(clicked_left) AS rate, count(*) AS n
        FROM read_parquet('{scen}') WHERE template = 'Desktop' AND grp <> 'EXCLUDED'
        GROUP BY ALL ORDER BY grp, level""").df()
    e.to_csv(outdir / f"{name}.csv", index=False)
    R[name] = e.round(4).to_dict("records")

# Coding sanity check: overall share choosing to stay (omission) on desktop
R["sanity_clicked_stay_desktop"] = con.sql(f"""
    SELECT grp, avg(clicked_stay) AS p_clicked_stay, count(*) AS n
    FROM read_parquet('{scen}') WHERE template = 'Desktop' GROUP BY grp""").df().to_dict("records")


def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    return o


(outdir / "results.json").write_text(json.dumps(clean(R), indent=2))
print(json.dumps(clean({k: R[k] for k in ["randomisation_check", "desktop", "mobile"]}), indent=1)[:12000])
