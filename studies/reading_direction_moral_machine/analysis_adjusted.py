"""Stay-balanced position-bias analyses (deviation from pre-registration, see 03_results.md).

The randomisation check showed the stay outcome sat on the left in 53.9% of scenarios, not 50%.
Because users prefer the stay (omission) outcome, the raw left-click rate mixes position bias with
stay preference. The balanced rate averages P(click left | stay on left) and P(click left | stay on
right), which cancels the stay preference:  B = 0.5 * (p1 + p0),  position bias = B - 0.5.

Usage: python analysis_adjusted.py <scenario parquet> <output dir>
"""
import json
import sys
from pathlib import Path

import duckdb
import numpy as np
import pandas as pd
from scipy import stats

scen, outdir = sys.argv[1], Path(sys.argv[2])
outdir.mkdir(parents=True, exist_ok=True)
con = duckdb.connect()
rng = np.random.default_rng(20261015)
R = {}


def user_strata(template, extra_where=""):
    """Per user: left clicks and decisions when stay was on the left (1) and on the right (0)."""
    return con.sql(f"""
        SELECT UserID, grp, any_value(country) AS country,
               sum(CASE WHEN stay_on_left = 1 THEN clicked_left END) AS k1,
               count(CASE WHEN stay_on_left = 1 THEN 1 END) AS n1,
               sum(CASE WHEN stay_on_left = 0 THEN clicked_left END) AS k0,
               count(CASE WHEN stay_on_left = 0 THEN 1 END) AS n0
        FROM read_parquet('{scen}')
        WHERE template = '{template}' AND grp <> 'EXCLUDED' {extra_where}
        GROUP BY UserID, grp""").df().fillna(0)


def balanced(d):
    """Decision-level balanced rate with a user-clustered (delta-method) standard error."""
    k1, n1, k0, n0 = (d[c].values.astype(float) for c in ["k1", "n1", "k0", "n0"])
    p1, p0 = k1.sum() / n1.sum(), k0.sum() / n0.sum()
    b = 0.5 * (p1 + p0)
    z = 0.5 * ((k1 - p1 * n1) / n1.sum() + (k0 - p0 * n0) / n0.sum())
    g = len(d)
    se = np.sqrt(g / (g - 1) * np.sum(z ** 2))
    return {"users": int(g), "decisions": int(n1.sum() + n0.sum()), "p_left_given_stay_left": p1,
            "p_left_given_stay_right": p0, "balanced_rate": b, "se": se,
            "ci95": [b - 1.96 * se, b + 1.96 * se], "position_bias_pp": 100 * (b - 0.5),
            "z_vs_half": (b - 0.5) / se, "p_vs_half": 2 * stats.norm.sf(abs((b - 0.5) / se))}


def user_balanced(d):
    d = d[(d.n1 > 0) & (d.n0 > 0)]
    return d, 0.5 * (d.k1 / d.n1 + d.k0 / d.n0)


def compare(df, a, b="LTR"):
    sa, sb = balanced(df[df.grp == a]), balanced(df[df.grp == b])
    diff = sa["balanced_rate"] - sb["balanced_rate"]
    se = np.sqrt(sa["se"] ** 2 + sb["se"] ** 2)
    _, ra = user_balanced(df[df.grp == a])
    _, rb = user_balanced(df[df.grp == b])
    t = stats.ttest_ind(ra, rb, equal_var=False)
    pooled_sd = np.sqrt((ra.var(ddof=1) + rb.var(ddof=1)) / 2)
    return {a: sa, b: sb,
            "decision_level": {"diff_pp": 100 * diff, "se_pp": 100 * se, "ci95_pp": [100 * (diff - 1.96 * se), 100 * (diff + 1.96 * se)],
                               "z": diff / se, "p": 2 * stats.norm.sf(abs(diff / se))},
            "user_level_welch": {"users": [int(len(ra)), int(len(rb))], "mean": [ra.mean(), rb.mean()],
                                 "diff_pp": 100 * (ra.mean() - rb.mean()), "t": t.statistic, "df": t.df,
                                 "p": t.pvalue, "cohens_d": (ra.mean() - rb.mean()) / pooled_sd}}


def country_table(df):
    c = df.groupby(["country", "grp"])[["k1", "n1", "k0", "n0"]].sum().reset_index()
    c["users"] = df.groupby(["country", "grp"]).size().values
    c = c[(c.n1 > 0) & (c.n0 > 0)].copy()
    c["p1"], c["p0"] = c.k1 / c.n1, c.k0 / c.n0
    c["balanced_rate"] = 0.5 * (c.p1 + c.p0)
    c["se"] = 0.5 * np.sqrt(c.p1 * (1 - c.p1) / c.n1 + c.p0 * (1 - c.p0) / c.n0)
    return c


def country_test(c, a, b="LTR", min_users=100, n_perm=10000):
    c = c[c.users >= min_users]
    xa, xb = c[c.grp == a].balanced_rate.values, c[c.grp == b].balanced_rate.values
    t = stats.ttest_ind(xa, xb, equal_var=False)
    obs = xa.mean() - xb.mean()
    pool = np.concatenate([xa, xb]).copy()
    perm = np.empty(n_perm)
    for i in range(n_perm):
        rng.shuffle(pool)
        perm[i] = pool[:len(xa)].mean() - pool[len(xa):].mean()
    return {"countries": [int(len(xa)), int(len(xb))], "mean": [xa.mean(), xb.mean()],
            "diff_pp": 100 * obs, "welch_t": t.statistic, "welch_p": t.pvalue,
            "perm_p": float(np.mean(np.abs(perm) >= abs(obs))), "mannwhitney_p": stats.mannwhitneyu(xa, xb).pvalue}


for template in ["Desktop", "Mobile"]:
    key = template.lower()
    df = user_strata(template)
    R[key] = {}
    ltr = df[df.grp == "LTR"]
    s = balanced(ltr)
    _, r = user_balanced(ltr)
    t = stats.ttest_1samp(r, 0.5)
    R[key]["H1_LTR_balanced"] = {**s, "user_level": {"users": int(len(r)), "mean": r.mean(), "t": t.statistic, "p": t.pvalue}}
    R[key]["H2_ARABIC_vs_LTR"] = compare(df, "ARABIC")
    R[key]["H3_RTL_OTHER_vs_LTR"] = compare(df, "RTL_OTHER")
    R[key]["ISR_vs_LTR"] = compare(df.assign(grp=np.where(df.country == "ISR", "ISR", df.grp)), "ISR")
    R[key]["RTL_OTHER_excl_ISR_vs_LTR"] = compare(
        df[df.country != "ISR"], "RTL_OTHER")
    R[key]["ALL_RTL_vs_LTR"] = compare(df.assign(grp=np.where(df.grp.isin(["ARABIC", "RTL_OTHER"]), "ALL_RTL", df.grp)), "ALL_RTL")
    c = country_table(df)
    c.sort_values("balanced_rate").to_csv(outdir / f"country_balanced_{key}.csv", index=False)
    R[key]["H2_country_level"] = country_test(c, "ARABIC")
    R[key]["H3_country_level"] = country_test(c, "RTL_OTHER")
    R[key]["ALL_RTL_country_level"] = country_test(c.assign(grp=np.where(c.grp.isin(["ARABIC", "RTL_OTHER"]), "ALL_RTL", c.grp)), "ALL_RTL")

# Exploratory E1 (scenario order) and E2 (description shown), desktop, balanced rates per group
rows = []
for col in ["scenario_order", "description_shown"]:
    levels = con.sql(f"SELECT DISTINCT {col} FROM read_parquet('{scen}') WHERE {col} IS NOT NULL ORDER BY 1").fetchall()
    for (lv,) in levels:
        df = user_strata("Desktop", f"AND {col} = {lv}")
        for g in ["LTR", "ARABIC", "RTL_OTHER"]:
            d = df[df.grp == g]
            if len(d) < 30 or d.n1.sum() == 0 or d.n0.sum() == 0:
                continue
            s = balanced(d)
            rows.append({"variable": col, "level": lv, "grp": g, "balanced_rate": s["balanced_rate"], "se": s["se"], "decisions": s["decisions"]})
pd.DataFrame(rows).to_csv(outdir / "exploratory_balanced.csv", index=False)

# E2 test: does reading the description change the ARABIC-vs-LTR gap?
e2 = {}
for lv in [0, 1]:
    df = user_strata("Desktop", f"AND description_shown = {lv}")
    e2[f"description_shown_{lv}"] = compare(df, "ARABIC")["decision_level"]
R["E2_ARABIC_gap_by_description"] = e2


def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return float(o)
    if isinstance(o, np.integer):
        return int(o)
    return o


(outdir / "results_adjusted.json").write_text(json.dumps(clean(R), indent=2))
print(json.dumps(clean(R), indent=1))
