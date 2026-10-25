# IJIES version

This repository is the copy of
[`manet-openset-ids`](https://github.com/kraghu356/manet-openset-ids) that accompanies the
condensed (10-page) manuscript *Open-Set Evaluation of Learned Routing-Attack Detectors in Mobile Ad Hoc Networks* submitted to the International Journal of Intelligent Engineering and Systems (IJIES).
The code, datasets and result files are identical to the original repository; this copy adds the
IJIES figures, the map below from the paper's tables to the scripts that produce them, and
`SUPPLEMENT.md`, which holds every table of the full analysis, including those the
10-page limit left out (per-network confidence scores, reconstruction error per feature set,
fold-level values, bootstrap intervals, all four operating-point thresholds, Wilson intervals for
the stress conditions, per-attack independent-campaign results, alternative fusion rules, the
complete online-gate and attack-intensity tables, and computational cost).

All analyses requested in the review rounds are in this copy: leave-one-attack-out evaluation,
feature-observability audit, unheard-neighbour stress test, frozen detectors under stress, the
independent 42-run campaign, recalibration with three calibration pairs, Mahalanobis and
reciprocal-point baselines with sanity checks, fusion-rule test, ablation, evaluation with every
node, online classifier-plus-gate replay, attack-intensity campaign, training-seed repeats,
paired run-clustered bootstrap and computational cost.

## Paper item to command

| IJIES paper item | Command (from the repository root) | Full-analysis table |
|---|---|---|
| Table 1 (simulation parameters) | `ns3/` scenario generator, see top-level README | S1 |
| Table 2 (closed-set macro F1), Table 3 (open-set AUROC) | `python3 analysis/openset_eval.py && python3 analysis/openset_baselines.py && python3 analysis/make_tables.py` | S3, S4, S14 |
| RPL checks, fusion rule, paired bootstrap (text) | `python3 analysis/baseline_checks.py && python3 analysis/extra_metrics.py` | S7, S8, S14 |
| Table 4 (operating points) | `python3 analysis/fixed_detector_eval.py --indep runs_indep --stress-fix runs_nu_fix --stress-honest runs_nu && python3 analysis/make_fixed_tables.py` | S9 |
| Fig. 2 (robustness of the count) | `python3 analysis/nu_robustness_report.py --fixed runs_nu_fix --honest runs_nu && python3 analysis/make_ijies_figures.py` | — |
| Table 5 (frozen detectors under stress) | as Table 4 | S10, S11 |
| Table 6 (independent campaign and recalibration) | as Table 4, then `python3 analysis/recalibration.py runs_indep` | S12, S13 |
| Table 7 (ablation and every node) | `python3 analysis/knn_ablation.py && python3 analysis/ijies_checks.py allnodes && python3 analysis/make_ijies_tables.py` | S15, S16 |
| Table 8 (online classifier-plus-gate) | `python3 analysis/ijies_checks.py gate && python3 analysis/make_ijies_tables.py` | S17 |
| Dilution and training seeds (text) | `python3 analysis/ijies_checks.py dilution && python3 analysis/ijies_checks.py seeds` | — |
| Attack intensity (text) | `python3 analysis/intensity_eval.py runs_intensity && python3 analysis/make_ijies_tables.py` | S18 |
| Computational cost (text) | `python3 analysis/complexity.py && python3 analysis/rf_latency.py` | S19 |
| Fig. 1 (fold assignment) | `python3 analysis/make_ijies_figures.py` | — |

`MANIFEST.md` at the repository root lists the SHA-256 checksum of every input and output file;
the main dataset `results/dataset3.csv.gz` has checksum beginning `78e3f767`.
