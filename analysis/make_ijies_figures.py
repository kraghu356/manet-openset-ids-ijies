"""Figures of the IJIES manuscript, 600 dpi, one IJIES column wide.

    python3 analysis/make_ijies_figures.py   # writes figures/ijies/fig1_protocol and fig2_robustness
"""
import os, numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, "..", "results"); OUT = os.path.join(HERE, "..", "figures", "ijies"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.serif": ["Liberation Serif"], "font.size": 10,
                     "axes.linewidth": 0.6, "axes.edgecolor": "#333333", "pdf.fonttype": 42,
                     "xtick.labelsize": 10, "ytick.labelsize": 10, "legend.fontsize": 10})
CM = 1 / 2.54

def save(fig, n):
    fig.savefig(os.path.join(OUT, n + ".png"), dpi=600, bbox_inches="tight", pad_inches=0.02)
    fig.savefig(os.path.join(OUT, n + ".pdf"), bbox_inches="tight", pad_inches=0.02); plt.close(fig)

# Fig. 1: fold assignment (single column, 8.2 cm)
fig, ax = plt.subplots(figsize=(8.2 * CM, 4.6 * CM)); ax.set_xlim(-3.2, 20.2); ax.set_ylim(0.85, 7.9); ax.axis("off")
cols = {"train": "#9cc3ee", "val": "#f0b23a", "test": "#d9534f"}
folds = [(range(1, 13), range(13, 17)), (range(5, 17), range(17, 21)), (range(9, 21), range(1, 5)),
         (list(range(1, 5)) + list(range(13, 21)), range(5, 9))]
for fi, (tr, va) in enumerate(folds):
    y = 6.0 - fi * 1.1
    ax.text(-0.3, y + 0.35, f"Fold {fi + 1}", ha="right", va="center")
    for s in range(1, 21):
        p = "train" if s in tr else "val" if s in va else "test"
        ax.add_patch(plt.Rectangle((s - 1 + 0.07, y), 0.86, 0.72, color=cols[p], lw=0))
for s in (1, 5, 9, 13, 17, 20):
    ax.text(s - 0.5, 6.95, str(s), ha="center")
ax.text(10, 7.55, "Simulation seed", ha="center")
for i, (k, lab) in enumerate([("train", "Training"), ("val", "Validation"), ("test", "Test")]):
    x0 = -1.2 + i * 7.3
    ax.add_patch(plt.Rectangle((x0, 1.05), 0.8, 0.6, color=cols[k], lw=0)); ax.text(x0 + 1.1, 1.35, lab, va="center")
save(fig, "fig1_protocol")

# Fig. 2: robustness of nu (full width, 17 cm)
LBL = {"baseline": "Baseline", "shadow_2dB": "Shadowing 2 dB", "shadow_4dB": "Shadowing 4 dB",
       "shadow_6dB": "Shadowing 6 dB", "rayleigh_fading": "Rayleigh fading", "loss_5pct": "Frame loss 5 per cent",
       "loss_10pct": "Frame loss 10 per cent", "speed_5_15": "Speed 5-15 m/s", "speed_10_20": "Speed 10-20 m/s",
       "dense_1000m": "Dense field", "large_200n": "200 nodes", "hello_on": "AODV hello",
       "heard_memory_30s": "Memory 30 s", "heard_memory_10s": "Memory 10 s", "relay_wormhole": "Relay wormhole"}
d = pd.read_csv(os.path.join(R, "nu_robustness.csv")).set_index("condition")
missing = [c for c in d.index if c not in LBL]; assert not missing, missing
d = d.loc[[c for c in LBL if c in d.index]]
LBL = {k: v.replace(" per cent", "%").replace("-", "–") for k, v in LBL.items()}
y = np.arange(len(d))[::-1]; h = 0.36
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.2 * CM, 13.0 * CM), gridspec_kw=dict(hspace=0.62))
a1.barh(y + h / 2, 100 * d.tpr_node, h, color="#2a6fbf", label="Endpoint flagged in any window")
a1.barh(y - h / 2, 100 * d.tpr_win, h, color="#7fc4a4", label="Endpoint windows with \u03bd > 0")
a1.set_xlim(0, 105); a1.set_xlabel("(a) Wormhole endpoints (%)")
a2.barh(y + h / 2, 100 * d.fpr_node, h, color="#2a6fbf", label="Alarm at first window with \u03bd > 0")
a2.barh(y - h / 2, 100 * d.fpr_node_2w, h, color="#e0894e", label="Two consecutive windows")
a2.set_xlim(0, 52); a2.set_xlabel("(b) Honest nodes flagged (%)")
for ax in (a1, a2):
    ax.spines[["top", "right"]].set_visible(False); ax.xaxis.grid(True, color="#dddddd", lw=0.5); ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="lower center", bbox_to_anchor=(0.42, 1.0), ncol=1, handlelength=1.2, borderaxespad=0.2)
    ax.set_yticks(y); ax.set_yticklabels([LBL[c] for c in d.index], fontsize=8); ax.set_ylim(-0.7, len(d) - 0.3)
    ax.tick_params(axis="y", length=2, pad=2)
save(fig, "fig2_robustness")
