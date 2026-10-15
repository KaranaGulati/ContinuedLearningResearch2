"""Figures for the reading-direction study. Usage: python make_figures.py <results dir>"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

res = Path(sys.argv[1])
R = json.loads((res / "results_adjusted.json").read_text())

INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#fcfcfb"
BLUE, ORANGE = "#2a78d6", "#eb6834"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "figure.facecolor": SURFACE, "axes.facecolor": SURFACE})


def bias_ci(entry):
    b = entry["position_bias_pp"]
    h = 196 * entry["se"]
    return b, b - h, b + h, entry["users"]


# Figure 1: position bias by group, desktop vs mobile
rows = [("Left-to-right countries", "H1_LTR_balanced", None),
        ("Arabic-script countries", "H2_ARABIC_vs_LTR", "ARABIC"),
        ("Israel (Hebrew)", "ISR_vs_LTR", "ISR"),
        ("Iran, Pakistan, Afghanistan", "RTL_OTHER_excl_ISR_vs_LTR", "RTL_OTHER")]
fig, axes = plt.subplots(1, 2, figsize=(9, 3.4), sharey=True)
for ax, tpl, title in [(axes[0], "desktop", "Desktop: outcomes side by side"),
                       (axes[1], "mobile", "Mobile: outcomes shown one at a time")]:
    for i, (label, key, g) in enumerate(rows):
        e = R[tpl][key] if g is None else R[tpl][key][g]
        b, lo, hi, n = bias_ci(e)
        y = len(rows) - 1 - i
        color = BLUE if g is None else ORANGE
        ax.plot([lo, hi], [y, y], color=color, lw=2, solid_capstyle="round")
        ax.plot(b, y, "o", ms=8, color=color, mec=SURFACE, mew=2)
        ax.text(hi + 0.08, y, f"{b:+.2f}  (n={n:,})", va="center", fontsize=8.5, color=INK2)
    ax.axvline(0, color=MUTED, lw=1, ls=(0, (3, 3)))
    ax.set_xlim(-1.9, 1.6)
    ax.set_title(title, fontsize=10, color=INK, loc="left")
    ax.set_xlabel("Position bias (percentage points)")
    ax.grid(axis="x", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0)
axes[0].set_yticks(range(len(rows)))
axes[0].set_yticklabels([r[0] for r in rows][::-1])
fig.suptitle("Figure 1. Side preference by group, randomised scenarios 2 to 13 (95% CIs, users as clusters)",
             x=0.01, ha="left", fontsize=10.5, color=INK)
fig.text(0.01, 0.01, "Below 0 = chose the right-hand outcome (desktop) or the second-shown outcome (mobile) more often.",
         fontsize=8.5, color=INK2)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(res / "fig1_position_bias_by_group.png", dpi=200)

# Figure 2: country-level balanced rates, desktop, countries with >= 100 users
c = pd.read_csv(res / "country_balanced_desktop.csv")
c = c[(c.users >= 100) & (c.grp != "EXCLUDED")].copy()
c["bias"] = 100 * (c.balanced_rate - 0.5)
c = c.sort_values("bias").reset_index(drop=True)
fig, ax = plt.subplots(figsize=(9, 3.6))
ltr = c[c.grp == "LTR"]
rtl = c[c.grp != "LTR"]
ax.scatter(ltr.index, ltr.bias, s=22, color=BLUE, alpha=0.75, label="Left-to-right countries", zorder=2, edgecolors=SURFACE, linewidths=0.8)
ax.scatter(rtl.index, rtl.bias, s=40, color=ORANGE, label="Right-to-left countries", zorder=3, edgecolors=SURFACE, linewidths=1.2)
prev = -10
flip = False
for i, r in rtl.iterrows():
    flip = (not flip) if i - prev <= 3 else False
    prev = i
    dy = (8 if r.bias < 0 else -13) * (-1.6 if flip else 1)
    ax.annotate(r.country, (i, r.bias), textcoords="offset points", xytext=(0, dy),
                ha="center", fontsize=7.5, color=INK2)
ax.axhline(0, color=MUTED, lw=1, ls=(0, (3, 3)))
ax.set_xticks([])
ax.set_xlabel(f"{len(c)} countries with at least 100 desktop users, sorted by position bias\n"
              "(small countries are noisy: with 100 users the SE is about 1.5 pp)")
ax.set_ylabel("Position bias (pp)")
ax.grid(axis="y", color=GRID, lw=0.8)
ax.set_axisbelow(True)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, loc="upper left", fontsize=8.5, labelcolor=INK2)
ax.set_title("Figure 2. Country-level side preference on desktop, randomised scenarios 2 to 13",
             loc="left", fontsize=10.5, color=INK)
fig.tight_layout()
fig.savefig(res / "fig2_country_bias_desktop.png", dpi=200)
print("saved")
