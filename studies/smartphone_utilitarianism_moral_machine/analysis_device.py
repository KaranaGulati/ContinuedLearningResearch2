"""Pre-registered analyses for the smartphone utilitarianism study (see 01_preregistration.md).

Usage: python analysis_device.py <first.parquet> <SharedResponsesSurvey.csv> <output dir>
first.parquet is SharedResponsesFullFirstSessions.csv (OSF 3hvt2) reduced to the needed columns
(see ../reading_direction_moral_machine/prepare.py for the reduction).
"""
import json
import sys
from pathlib import Path

import duckdb
import numpy as np
import pandas as pd
from scipy import stats

first, survey_csv, outdir = sys.argv[1], sys.argv[2], Path(sys.argv[3])
outdir.mkdir(parents=True, exist_ok=True)
con = duckdb.connect()
R = {}
SESOI = 0.02  # equivalence bound, pre-registered


def scenario_table(src, extra_cols=""):
    """One row per utilitarian scenario: saved_more and more_needs_swerve."""
    return f"""
        SELECT ResponseID, any_value(UserID) AS UserID, any_value(UserCountry3) AS country,
               any_value(Template) AS template, any_value(ScenarioOrder) AS scenario_order,
               max(DescriptionShown) AS description_shown,
               max(CASE WHEN AttributeLevel = 'More' THEN Saved END) AS saved_more,
               max(CASE WHEN AttributeLevel = 'More' THEN 1 - Intervention END) AS more_needs_swerve,
               count(*) AS n_rows, sum(Saved) AS n_saved {extra_cols}
        FROM {src}
        WHERE ScenarioType = 'Utilitarian' AND ScenarioTypeStrict = 'Utilitarian'
          AND Template IN ('Desktop', 'Mobile')
        GROUP BY ResponseID
        HAVING count(*) = 2 AND sum(Saved) = 1 AND count(CASE WHEN AttributeLevel = 'More' THEN 1 END) = 1"""


def fe_ols(df, y, xcols, fe, cluster):
    """OLS with one set of fixed effects (absorbed by demeaning) and cluster-robust SEs."""
    d = df[[y] + xcols + [fe, cluster]].dropna()
    cols = [y] + xcols
    dm = d[cols] - d.groupby(fe)[cols].transform("mean")
    X, Y = dm[xcols].to_numpy(float), dm[y].to_numpy(float)
    XtX_inv = np.linalg.pinv(X.T @ X)
    beta = XtX_inv @ X.T @ Y
    e = Y - X @ beta
    scores = pd.DataFrame(X * e[:, None]).groupby(d[cluster].to_numpy()).sum().to_numpy()
    G = scores.shape[0]
    meat = scores.T @ scores * G / (G - 1)
    V = XtX_inv @ meat @ XtX_inv
    se = np.sqrt(np.diag(V))
    return {c: {"b": beta[i], "se": se[i], "z": beta[i] / se[i], "p": 2 * stats.norm.sf(abs(beta[i] / se[i])),
                "ci95": [beta[i] - 1.96 * se[i], beta[i] + 1.96 * se[i]]} for i, c in enumerate(xcols)} | {
        "_n": int(len(d)), "_clusters": int(G), "_fe_groups": int(d[fe].nunique())}


def tost(b, se, bound=SESOI):
    p_low = stats.norm.sf((b + bound) / se)   # H0: b <= -bound
    p_high = stats.norm.cdf((b - bound) / se)  # H0: b >= +bound
    return {"bound": bound, "p_lower": p_low, "p_upper": p_high, "p_tost": max(p_low, p_high),
            "ci90": [b - 1.645 * se, b + 1.645 * se]}


def run_main(df, label):
    df = df.copy()
    df["mobile"] = (df.template == "Mobile").astype(int)
    out = {}
    # Descriptive
    rates = df.groupby("template").agg(decisions=("saved_more", "size"), users=("UserID", "nunique"),
                                       saved_more=("saved_more", "mean")).reset_index()
    out["raw_rates"] = rates.to_dict("records")
    u = df.groupby(["UserID", "template"]).saved_more.mean().reset_index()
    t = stats.ttest_ind(u[u.template == "Mobile"].saved_more, u[u.template == "Desktop"].saved_more, equal_var=False)
    out["raw_user_welch"] = {"diff_pp": 100 * (u[u.template == "Mobile"].saved_more.mean() - u[u.template == "Desktop"].saved_more.mean()),
                             "t": t.statistic, "df": t.df, "p": t.pvalue}
    # H1 primary: country-paired
    cu = df.groupby(["country", "template"]).agg(users=("UserID", "nunique"), rate=("saved_more", "mean")).reset_index()
    w = cu.pivot(index="country", columns="template", values=["users", "rate"]).dropna()
    w = w[(w[("users", "Desktop")] >= 100) & (w[("users", "Mobile")] >= 100)]
    d_c = w[("rate", "Mobile")] - w[("rate", "Desktop")]
    t = stats.ttest_1samp(d_c, 0)
    out["H1_country_paired"] = {"countries": int(len(d_c)), "mean_diff_pp": 100 * d_c.mean(), "sd_pp": 100 * d_c.std(ddof=1),
                                "t": t.statistic, "df": len(d_c) - 1, "p": t.pvalue,
                                "share_countries_positive": float((d_c > 0).mean()),
                                "ci95_pp": [100 * x for x in t.confidence_interval()]}
    pd.DataFrame({"country": d_c.index, "diff": d_c.values,
                  "users_desktop": w[("users", "Desktop")].values, "users_mobile": w[("users", "Mobile")].values,
                  "rate_desktop": w[("rate", "Desktop")].values, "rate_mobile": w[("rate", "Mobile")].values}
                 ).to_csv(outdir / f"country_diffs_{label}.csv", index=False)
    # H1 supporting: FE model
    fe = fe_ols(df, "saved_more", ["mobile"], "country", "UserID")
    out["H1_fe_model"] = fe
    out["H1_tost"] = tost(fe["mobile"]["b"], fe["mobile"]["se"])
    # H2: interaction
    df["mobile_x_swerve"] = df.mobile * df.more_needs_swerve
    out["H2_fe_model"] = fe_ols(df, "saved_more", ["mobile", "more_needs_swerve", "mobile_x_swerve"], "country", "UserID")
    cs = df.groupby(["country", "more_needs_swerve", "template"]).agg(users=("UserID", "nunique"), rate=("saved_more", "mean")).reset_index()
    p = cs.pivot_table(index="country", columns=["more_needs_swerve", "template"], values="rate")
    p = p.loc[d_c.index].dropna()
    dd = (p[(1, "Mobile")] - p[(1, "Desktop")]) - (p[(0, "Mobile")] - p[(0, "Desktop")])
    t = stats.ttest_1samp(dd, 0)
    out["H2_country_paired"] = {"countries": int(len(dd)), "mean_diff_in_diff_pp": 100 * dd.mean(), "t": t.statistic, "p": t.pvalue}
    out["rates_by_device_and_swerve"] = df.groupby(["template", "more_needs_swerve"]).saved_more.agg(["mean", "size"]).reset_index().to_dict("records")
    return out


# Main sample: first sessions
util_first = con.sql(scenario_table(f"read_parquet('{first}')")).df()
util_first = util_first[util_first.country.notna()]
R["main_scen_2_13"] = run_main(util_first[util_first.scenario_order.between(2, 13)], "main")
R["sensitivity_all_13"] = run_main(util_first, "all13")

# H3: survey subset, demographics
sv = con.sql(f"""
    WITH s AS (
      SELECT ResponseID, UserID, UserCountry3, Template, TRY_CAST(ScenarioOrder AS INT) AS ScenarioOrder,
             TRY_CAST(TRY_CAST(Intervention AS DOUBLE) AS INT) AS Intervention, AttributeLevel,
             ScenarioType, ScenarioTypeStrict, TRY_CAST(TRY_CAST(Saved AS DOUBLE) AS INT) AS Saved,
             TRY_CAST(TRY_CAST(DescriptionShown AS DOUBLE) AS INT) AS DescriptionShown,
             Review_age, Review_education, Review_gender, Review_income, Review_political, Review_religious
      FROM read_csv('{survey_csv}', header=true, all_varchar=true))
    SELECT u.*, d.age, d.education, d.gender, d.income, d.political, d.religious
    FROM ({scenario_table('s')}) u
    JOIN (SELECT ResponseID,
                 any_value(TRY_CAST(Review_age AS DOUBLE)) AS age,
                 any_value(Review_education) AS education, any_value(Review_gender) AS gender,
                 any_value(Review_income) AS income,
                 any_value(TRY_CAST(Review_political AS DOUBLE)) AS political,
                 any_value(TRY_CAST(Review_religious AS DOUBLE)) AS religious
          FROM s GROUP BY ResponseID) d USING (ResponseID)
    """).df()
sv = sv[sv.scenario_order.between(2, 13) & sv.country.notna()].copy()
sv["mobile"] = (sv.template == "Mobile").astype(int)
for col in ["political", "religious"]:
    sv.loc[sv[col] == 0.5, col] = np.nan            # 0.5 is the untouched default
sv.loc[~sv.gender.isin(["male", "female", "others"]), "gender"] = np.nan
sv.loc[sv.education.isin(["default"]) | sv.education.isna(), "education"] = np.nan
sv.loc[sv.income.isin(["default", "over10000"]) | sv.income.isna(), "income"] = np.nan
sv.loc[~sv.age.between(18, 75), "age"] = np.nan
sv = sv.dropna(subset=["age", "gender", "education", "income", "political", "religious"])
dummies = pd.get_dummies(sv[["gender", "education", "income"]], drop_first=True, dtype=float)
sv = pd.concat([sv, dummies], axis=1)
xcols = ["mobile", "age", "political", "religious"] + list(dummies.columns)
R["H3_survey_adjusted"] = fe_ols(sv, "saved_more", xcols, "country", "UserID")
R["H3_survey_unadjusted"] = fe_ols(sv, "saved_more", ["mobile"], "country", "UserID")
R["H3_sample"] = {"decisions": int(len(sv)), "users": int(sv.UserID.nunique()),
                  "mobile_share": float(sv.mobile.mean()),
                  "mean_age_by_device": sv.groupby("template").age.mean().to_dict(),
                  "share_male_by_device": sv.assign(m=(sv.gender == "male")).groupby("template").m.mean().to_dict()}

# Exploratory: device gap for the other preferences (first sessions, scenarios 2-13, country FE)
expl = {}
spec = {"Age": "Young", "Fitness": "Fit", "Social Status": "High", "Species": "Hoomans", "Gender": "Female"}
for st, lvl in spec.items():
    q = f"""
        SELECT ResponseID, any_value(UserID) AS UserID, any_value(UserCountry3) AS country, any_value(Template) AS template,
               max(CASE WHEN AttributeLevel = '{lvl}' THEN Saved END) AS saved_target
        FROM read_parquet('{first}')
        WHERE ScenarioType = '{st}' AND ScenarioTypeStrict = '{st}' AND Template IN ('Desktop','Mobile')
              AND ScenarioOrder BETWEEN 2 AND 13 AND UserCountry3 IS NOT NULL
        GROUP BY ResponseID HAVING count(*) = 2 AND sum(Saved) = 1"""
    d = con.sql(q).df()
    d["mobile"] = (d.template == "Mobile").astype(int)
    m = fe_ols(d, "saved_target", ["mobile"], "country", "UserID")
    expl[f"{st}: spare {lvl}"] = {"desktop_rate": d[d.mobile == 0].saved_target.mean(), "mobile_rate": d[d.mobile == 1].saved_target.mean(),
                                  "fe_diff_pp": 100 * m["mobile"]["b"], "se_pp": 100 * m["mobile"]["se"], "p": m["mobile"]["p"], "n": m["_n"]}
# Pedestrians vs passengers and stay (omission): all scenarios with PedPed = 0
q = f"""
    SELECT ResponseID, any_value(UserID) AS UserID, any_value(UserCountry3) AS country, any_value(Template) AS template,
           max(CASE WHEN Intervention = 1 THEN Saved END) AS saved_by_staying
    FROM read_parquet('{first}')
    WHERE Template IN ('Desktop','Mobile') AND ScenarioOrder BETWEEN 2 AND 13 AND UserCountry3 IS NOT NULL
    GROUP BY ResponseID HAVING count(*) = 2 AND sum(Saved) = 1"""
d = con.sql(q).df()
d["mobile"] = (d.template == "Mobile").astype(int)
for col, name in [("saved_by_staying", "All scenarios: choose stay (inaction)")]:
    m = fe_ols(d, col, ["mobile"], "country", "UserID")
    expl[name] = {"desktop_rate": d[d.mobile == 0][col].mean(), "mobile_rate": d[d.mobile == 1][col].mean(),
                  "fe_diff_pp": 100 * m["mobile"]["b"], "se_pp": 100 * m["mobile"]["se"], "p": m["mobile"]["p"], "n": m["_n"]}
R["exploratory_other_preferences"] = expl


def clean(o):
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    return o


(outdir / "results.json").write_text(json.dumps(clean(R), indent=2))
print(json.dumps(clean(R), indent=1))
