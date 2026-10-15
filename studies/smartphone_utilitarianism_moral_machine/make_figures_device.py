"""Figures for the smartphone study. Usage: python make_figures_device.py <results dir>"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

res = Path(sys.argv[1])
R = json.loads((res / "results.json").read_text())
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#fcfcfb"
BLUE, ORANGE = "#2a78d6", "#eb6834"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "figure.facecolor": SURFACE, "axes.facecolor": SURFACE})

# Figure 1: mobile minus desktop, within country, for each preference
m = R["main_scen_2_13"]["H1_fe_model"]["mobile"]
rows = [("Spare the larger group (utilitarian)", 100 * m["b"], 100 * m["se"], True)]
labels = {"Species: spare Hoomans": "Spare humans over pets", "Age: spare Young": "Spare the young",
          "Gender: spare Female": "Spare women", "Social Status: spare High": "Spare higher status",
          "Fitness: spare Fit": "Spare the fit", "All scenarios: choose stay (inaction)": "Choose to stay on course"}
for k, lab in labels.items():
    e = R["exploratory_other_preferences"][k]
    rows.append((lab, e["fe_diff_pp"], e["se_pp"], False))
fig, ax = plt.subplots(figsize=(8.5, 3.6))
for i, (lab, b, se, main) in enumerate(rows):
    y = len(rows) - 1 - i
    col = ORANGE if main else BLUE
    ax.plot([b - 1.96 * se, b + 1.96 * se], [y, y], color=col, lw=2, solid_capstyle="round")
    ax.plot(b, y, "o", ms=8, color=col, mec=SURFACE, mew=2)
    ax.text(max(b + 1.96 * se, 0) + 0.12, y, f"{b:+.2f}", va="center", fontsize=8.5, color=INK2)
ax.axvline(0, color=MUTED, lw=1, ls=(0, (3, 3)))
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows][::-1])
ax.set_xlim(-3, 3.2)
ax.set_xlabel("Mobile minus desktop, percentage points (country fixed effects, 95% CI)")
ax.grid(axis="x", color=GRID, lw=0.8)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.set_title("Figure 1. Mobile minus desktop, by preference (scenarios 2 to 13)",
             loc="left", fontsize=10.5, color=INK)
fig.text(0.01, 0.01, "Orange = pre-registered outcome. Blue = exploratory. Positive = mobile users chose this more often.",
         fontsize=8.5, color=INK2)
fig.tight_layout(rect=(0, 0.05, 1, 1))
fig.savefig(res / "fig1_device_gap_by_preference.png", dpi=200)

# Figure 2: country-level mobile minus desktop gap in sparing the larger group
c = pd.read_csv(res / "country_diffs_main.csv").sort_values("diff").reset_index(drop=True)
c["pp"] = 100 * c["diff"]
fig, ax = plt.subplots(figsize=(8.5, 3.4))
pos = c.pp > 0
ax.scatter(c.index[pos], c.pp[pos], s=26, color=ORANGE, edgecolors=SURFACE, linewidths=0.8, label="Mobile users more utilitarian", zorder=3)
ax.scatter(c.index[~pos], c.pp[~pos], s=26, color=BLUE, edgecolors=SURFACE, linewidths=0.8, label="Desktop users more utilitarian", zorder=3)
mean = R["main_scen_2_13"]["H1_country_paired"]["mean_diff_pp"]
ax.axhline(0, color=MUTED, lw=1, ls=(0, (3, 3)))
ax.axhline(mean, color=INK2, lw=1)
ax.text(1, mean + 0.25, f"mean {mean:+.2f} pp", fontsize=8.5, color=INK2)
for k, (_, r) in enumerate(c[c.country.isin(["USA", "BRA", "DEU", "FRA", "RUS", "JPN", "IND", "GBR"])].iterrows()):
    ax.annotate(r.country, (_, r.pp), textcoords="offset points", xytext=(0, 7 if k % 2 == 0 else -13), ha="center", fontsize=7.5, color=INK2)
ax.set_xticks([])
ax.set_xlabel(f"{len(c)} countries with at least 100 users on each device, sorted by gap")
ax.set_ylabel("Mobile minus desktop (pp)")
ax.grid(axis="y", color=GRID, lw=0.8)
ax.set_axisbelow(True)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, loc="upper left", fontsize=8.5, labelcolor=INK2)
ax.set_title("Figure 2. Within-country gap in sparing the larger group", loc="left", fontsize=10.5, color=INK)
fig.tight_layout()
fig.savefig(res / "fig2_country_gaps.png", dpi=200)
print("saved")
