# Supplementary tables (IJIES version)

The condensed IJIES manuscript keeps eight tables. This file gives every table of the full analysis,
generated from the result files in `results/`, so that the omitted detail remains available.
Table numbers here are those of the full analysis (S1-S19).

## Table S1. Simulation parameters, fixed across all 120 runs

| Parameter                           | Value                       |
|:------------------------------------|:----------------------------|
| Simulator, routing                  | ns-3.48, AODV               |
| Nodes, field                        | 100, $1500 \times 1500$ m   |
| PHY, rate, transmit power           | 802.11b, 11 Mbps, 23 dBm    |
| Path loss: $\eta$, $P_0$, shadowing | 2.5, 46.68 dB, none         |
| Mobility, speed, pause              | waypoint, $U(1,5)$ m/s, 2 s |
| Traffic                             | 10 flows, 4 pkt/s, 512 B    |
| Duration, window                    | 300 s, 10 s                 |
| Seeds per scenario, runs            | 20, 120                     |

## Table S2. Feature inventory. O: observable from the node’s own protocol and physical-layer state; S: simulator-derived. F-obs marks the 15 inputs used for all main results. fwd_ok and fwd_drop are recorded but never used, because fwd_drop is zero for every honest node and so encodes the label

| Feature                           | Source | F-all | F-obs |
|:----------------------------------|:------:|:-----:|:-----:|
| fwd_seen, fwd_ratio, rreq_recv    |   O    |  yes  |  yes  |
| rreq_sent, no_route, nb_count     |   O    |  yes  |  yes  |
| nb_churn, rssi_min, rssi_dist_max |   O    |  yes  |  yes  |
| nb_no_rssi ($\nu$), speed\*       |   O    |  yes  |  yes  |
| 4 moving averages                 |   O    |  yes  |  yes  |
| nb_mean_dist, nb_max_dist         |   S    |  yes  |  no   |
| fwd_ok, fwd_drop                  |   O    |  no   |  no   |

## Table S3. Closed-set macro F1 over four folds (six classes, every attack known in training)

| Detector                      |     Macro F1      |
|:------------------------------|:-----------------:|
| Random forest, 300 trees      | 0.974 $\pm$ 0.009 |
| Long short-term memory        | 0.964 $\pm$ 0.024 |
| $k$-nearest neighbours, $k=5$ | 0.959 $\pm$ 0.036 |
| Convolutional network         | 0.954 $\pm$ 0.025 |
| Gated recurrent unit          | 0.944 $\pm$ 0.027 |
| Support vector machine        | 0.940 $\pm$ 0.036 |
| Decision tree                 | 0.935 $\pm$ 0.009 |

## Table S4. AUROC of each novelty score for each held-out attack against normal nodes, mean over four folds (per-fold values and standard deviations are in the repository). Values below 0.5 rank the unseen attack as more normal than normal traffic. A dash marks a score that is constant on both classes, counted as 0.5 in the mean. Bold marks the best value in each column

| Score                    | Black hole | Flooding  | Grey hole | Sinkhole  | Wormhole  | Mean  |
|:-------------------------|:----------:|:---------:|:---------:|:---------:|:---------:|:-----:|
| MSP, CNN                 |   0.031    |   0.001   |   0.640   |   0.232   |   0.489   | 0.279 |
| MSP, LSTM                |   0.053    |   0.124   |   0.507   |   0.452   |   0.483   | 0.324 |
| MSP, GRU                 |   0.056    |   0.272   |   0.419   |   0.384   |   0.460   | 0.318 |
| Energy, CNN              |   0.019    |   0.000   |   0.478   |   0.087   |   0.458   | 0.208 |
| Energy, LSTM             |   0.085    |   0.154   |   0.563   |   0.474   |   0.486   | 0.352 |
| Energy, GRU              |   0.209    |   0.357   |   0.648   |   0.580   |   0.410   | 0.441 |
| OpenMax, CNN             |   0.840    |   0.000   |   0.896   |   0.132   |   0.477   | 0.469 |
| OpenMax, LSTM            |   0.502    |   0.095   |   0.729   |   0.484   |   0.483   | 0.459 |
| OpenMax, GRU             |   0.629    |   0.265   |   0.881   |   0.388   |   0.449   | 0.522 |
| Forest vote              |   0.979    |   0.662   |   0.967   |   0.769   |   0.496   | 0.775 |
| Forest vote entropy      |   0.978    |   0.661   |   0.966   |   0.780   |   0.498   | 0.776 |
| SVM margin               | **0.999**  | **0.999** | **0.987** |   0.995   |   0.503   | 0.897 |
| $k$-NN distance          | **1.000**  | **1.000** |   0.957   | **0.999** |   0.923   | 0.976 |
| Reconstruction           |   0.613    |   0.990   |   0.345   |   0.995   |   0.478   | 0.684 |
| $\nu$                    |     –      |     –     |     –     |     –     |   0.969   | 0.594 |
| Vote + recon.            |   0.963    |   0.979   |   0.959   |   0.989   |   0.478   | 0.873 |
| Vote + $\nu$             |   0.979    |   0.662   |   0.967   |   0.769   |   0.960   | 0.867 |
| Recon. + $\nu$           |   0.613    |   0.990   |   0.345   |   0.994   |   0.963   | 0.781 |
| Hybrid, Eq. (9)          |   0.963    |   0.979   |   0.959   |   0.989   |   0.957   | 0.969 |
| $k$-NN + $\nu$, Eq. (10) | **0.999**  | **1.000** |   0.957   |   0.999   | **0.972** | 0.985 |

## Table S5. Detection rate / false-positive rate at the validation-normal 95th percentile, mean over four folds. Last column: mean detection rate over the five attacks

| Score           |    BH     |   Flood   |    GH     |   Sink    |   Worm    | Mean DR |
|:----------------|:---------:|:---------:|:---------:|:---------:|:---------:|:-------:|
| MSP, GRU        | 0.03/0.07 | 0.01/0.06 | 0.34/0.05 | 0.01/0.06 | 0.07/0.06 |  0.09   |
| Energy, GRU     | 0.06/0.07 | 0.01/0.06 | 0.46/0.05 | 0.04/0.06 | 0.00/0.06 |  0.12   |
| OpenMax, GRU    | 0.24/0.08 | 0.01/0.06 | 0.71/0.05 | 0.01/0.06 | 0.07/0.06 |  0.21   |
| Forest vote     | 0.89/0.04 | 0.03/0.04 | 0.94/0.05 | 0.15/0.05 | 0.00/0.04 |  0.40   |
| $k$-NN distance | 1.00/0.05 | 1.00/0.20 | 0.90/0.05 | 1.00/0.10 | 0.62/0.05 |  0.90   |
| Reconstruction  | 0.06/0.05 | 1.00/0.04 | 0.00/0.04 | 1.00/0.08 | 0.00/0.04 |  0.41   |
| $\nu$           | 0.00/0.00 | 0.00/0.00 | 0.00/0.00 | 0.00/0.00 | 0.94/0.00 |  0.19   |
| Hybrid          | 0.70/0.05 | 0.99/0.04 | 0.92/0.04 | 0.94/0.06 | 0.94/0.04 |  0.90   |
| $k$-NN + $\nu$  | 1.00/0.05 | 1.00/0.20 | 0.90/0.05 | 1.00/0.09 | 0.94/0.05 |  0.97   |

## Table S6. Reconstruction-error AUROC under three feature sets, autoencoder trained on clean traffic only, mean $\pm$ standard deviation over four folds

| Attack     |    F-all (17)     |    F-obs (15)     | F-obs without $\nu$ (14) |
|:-----------|:-----------------:|:-----------------:|:------------------------:|
| Black hole | 0.748 $\pm$ 0.077 | 0.613 $\pm$ 0.071 |    0.570 $\pm$ 0.078     |
| Flooding   | 0.988 $\pm$ 0.006 | 0.990 $\pm$ 0.007 |    0.989 $\pm$ 0.007     |
| Grey hole  | 0.351 $\pm$ 0.040 | 0.345 $\pm$ 0.058 |    0.339 $\pm$ 0.054     |
| Sinkhole   | 0.994 $\pm$ 0.004 | 0.995 $\pm$ 0.003 |    0.994 $\pm$ 0.003     |
| Wormhole   | 0.949 $\pm$ 0.044 | 0.478 $\pm$ 0.089 |    0.400 $\pm$ 0.116     |

## Table S7. Fold-level mean AUROC over the five held-out attacks, four-fold mean, mean average precision (PR-AUC) at the natural test prevalence, and mean AUROC with the 14 onboard-only features (speed removed)

| Score                    | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean  | PR-AUC | No speed |
|:-------------------------|:------:|:------:|:------:|:------:|:-----:|:------:|:--------:|
| Forest vote              | 0.837  | 0.753  | 0.791  | 0.717  | 0.775 | 0.158  |  0.770   |
| $k$-NN distance          | 0.977  | 0.948  | 0.992  | 0.985  | 0.976 | 0.715  |  0.983   |
| Reconstruction           | 0.713  | 0.694  | 0.655  | 0.676  | 0.684 | 0.224  |  0.683   |
| $\nu$                    | 0.600  | 0.575  | 0.600  | 0.600  | 0.594 | 0.195  |  0.594   |
| Hybrid, Eq. (9)          | 0.970  | 0.932  | 0.984  | 0.990  | 0.969 | 0.462  |  0.964   |
| $k$-NN + $\nu$, Eq. (10) | 0.989  | 0.957  | 0.996  | 0.999  | 0.985 | 0.858  |  0.988   |

## Table S8. Mean AUROC with a run-clustered bootstrap 95% interval (1,000 replicates) for the three strongest detectors

| Attack     |    $k$-NN distance     |     $k$-NN + $\nu$     |         Hybrid         |
|:-----------|:----------------------:|:----------------------:|:----------------------:|
| Black hole | 1.000 \[0.999, 1.000\] | 0.999 \[0.999, 1.000\] | 0.963 \[0.951, 0.974\] |
| Flooding   | 1.000 \[0.999, 1.000\] | 1.000 \[0.999, 1.000\] | 0.979 \[0.971, 0.985\] |
| Grey hole  | 0.957 \[0.904, 0.995\] | 0.957 \[0.910, 0.996\] | 0.959 \[0.910, 0.991\] |
| Sinkhole   | 0.999 \[0.999, 1.000\] | 0.999 \[0.998, 0.999\] | 0.989 \[0.984, 0.993\] |
| Wormhole   | 0.923 \[0.851, 0.966\] | 0.972 \[0.899, 1.000\] | 0.957 \[0.879, 1.000\] |

## Table S9. Operating points at four validation-normal percentiles, four folds pooled. DR: detection rate (mean and minimum over the five held-out attacks); FPR: worst false-positive rate over the five; false alerts: honest nodes flagged per 300 s run (mean and maximum over the five); precision at the natural prevalence, mean over the five

| Detector        | Pct. | Mean DR | Min DR | Max FPR | Alerts | Max alerts | Precision |
|:----------------|:----:|:-------:|:------:|:-------:|:------:|:----------:|:---------:|
| $k$-NN distance |  90  |  0.94   |  0.77  |  0.249  |  12.7  |    22.4    |   0.05    |
|                 |  95  |  0.90   |  0.61  |  0.202  |  8.1   |    18.3    |   0.09    |
|                 |  99  |  0.77   |  0.00  |  0.048  |  1.7   |    4.3     |   0.29    |
|                 | 99.5 |  0.74   |  0.00  |  0.013  |  0.6   |    1.1     |   0.43    |
| $k$-NN + $\nu$  |  90  |  0.97   |  0.93  |  0.249  |  12.7  |    22.4    |   0.06    |
|                 |  95  |  0.97   |  0.90  |  0.202  |  8.0   |    18.2    |   0.10    |
|                 |  99  |  0.96   |  0.86  |  0.045  |  1.6   |    4.1     |   0.36    |
|                 | 99.5 |  0.92   |  0.78  |  0.012  |  0.6   |    1.1     |   0.54    |
| Hybrid          |  90  |  0.96   |  0.94  |  0.128  |  8.7   |    11.6    |   0.07    |
|                 |  95  |  0.89   |  0.69  |  0.063  |  4.2   |    5.7     |   0.13    |
|                 |  99  |  0.39   |  0.00  |  0.011  |  0.9   |    1.0     |   0.19    |
|                 | 99.5 |  0.35   |  0.00  |  0.005  |  0.3   |    0.4     |   0.32    |

## Table S10. Frozen detectors on the wormhole stress conditions (wormhole held out of training). Each cell: node-level AUROC / honest-node false-positive rate at the validation 95th percentile. Runs: endpoint runs; $n$: wormhole endpoints scored

| Condition       | Runs | $n$ | $k$-NN distance | $k$-NN + $\nu$ |    Hybrid    |
|:----------------|:----:|:---:|:---------------:|:--------------:|:------------:|
| Baseline        |  3   |  6  |  0.974 / 0.01   |  1.000 / 0.01  | 1.000 / 0.01 |
| Shadowing 2 dB  |  3   |  6  |  0.840 / 0.21   |  0.999 / 0.21  | 0.999 / 0.01 |
| Shadowing 4 dB  |  3   |  6  |  0.533 / 0.89   |  0.999 / 0.89  | 0.999 / 0.01 |
| Shadowing 6 dB  |  8   | 16  |  0.472 / 1.00   |  0.844 / 1.00  | 0.799 / 0.85 |
| Frame loss 5%   |  2   |  4  |  0.975 / 0.06   |  1.000 / 0.06  | 1.000 / 0.05 |
| Frame loss 10%  |  2   |  4  |  0.971 / 0.07   |  1.000 / 0.07  | 1.000 / 0.07 |
| Speed 5–15 m/s  |  2   |  4  |  0.256 / 0.99   |  1.000 / 0.99  | 1.000 / 0.18 |
| Speed 10–20 m/s |  3   |  6  |  0.365 / 1.00   |  1.000 / 1.00  | 1.000 / 0.98 |
| Dense field     |  2   |  4  |  0.727 / 0.58   |  1.000 / 0.58  | 1.000 / 0.00 |
| 200 nodes       |  3   |  6  |  0.451 / 0.30   |  0.511 / 0.30  | 0.548 / 0.09 |
| Rayleigh fading |  3   |  6  |  0.626 / 0.58   |  1.000 / 0.58  | 1.000 / 0.01 |
| Hello messages  |  2   |  4  |  0.815 / 0.16   |  1.000 / 0.15  | 1.000 / 0.01 |
| Memory 30 s     |  2   |  4  |  0.970 / 0.01   |  0.968 / 0.06  | 0.968 / 0.06 |
| Memory 10 s     |  8   | 16  |  0.987 / 0.01   |  0.769 / 0.47  | 0.769 / 0.48 |
| Relay wormhole  |  8   | 15  |  0.720 / 0.01   |  0.719 / 0.01  | 0.513 / 0.01 |

## Table S11. Detection rate (DR) and honest-node false-positive rate (FPR) at the validation 95th percentile, with Wilson 95% intervals, for the replicated stress conditions. $n$: endpoints; $m$: honest nodes

|                 |     |     |                     |                        |                     |                        |
|:----------------|:---:|:---:|:-------------------:|:----------------------:|:-------------------:|:----------------------:|
|                 |     |     |   $k$-NN + $\nu$    |                        |       Hybrid        |                        |
| Condition       | $n$ | $m$ |         DR          |          FPR           |         DR          |          FPR           |
| Baseline        |  6  | 928 | 1.00 \[0.61, 1.00\] | 0.008 \[0.004, 0.015\] | 1.00 \[0.61, 1.00\] | 0.013 \[0.007, 0.022\] |
| Shadowing 6 dB  | 16  | 784 | 1.00 \[0.81, 1.00\] | 1.000 \[0.995, 1.000\] | 0.94 \[0.72, 0.99\] | 0.851 \[0.824, 0.874\] |
| Speed 10–20 m/s |  6  | 490 | 1.00 \[0.61, 1.00\] | 1.000 \[0.992, 1.000\] | 1.00 \[0.61, 1.00\] | 0.982 \[0.965, 0.990\] |
| 200 nodes       |  6  | 590 | 0.33 \[0.10, 0.70\] | 0.300 \[0.264, 0.338\] | 0.50 \[0.19, 0.81\] | 0.095 \[0.074, 0.121\] |
| Memory 10 s     | 16  | 742 | 1.00 \[0.81, 1.00\] | 0.470 \[0.435, 0.506\] | 1.00 \[0.81, 1.00\] | 0.476 \[0.440, 0.512\] |
| Relay wormhole  | 15  | 753 | 0.00 \[0.00, 0.20\] | 0.007 \[0.003, 0.015\] | 0.00 \[0.00, 0.20\] | 0.011 \[0.005, 0.021\] |

## Table S12. Frozen detectors on the independent campaign. AUROC per held-out attack and its mean; DR: mean detection rate and FPR: worst false-positive rate over the five attacks, at the validation 95th and 99th percentiles. Same: 24 runs at the main-campaign settings; Shifted: 18 runs with 2 dB shadowing and speeds of 2–8 m/s

|         |                 |       |       |       |       |       |       |           |      |           |       |
|:--------|:----------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:---------:|:----:|:---------:|:-----:|
|         |                 |       |       |       |       |       |       | 95th pct. |      | 99th pct. |       |
| Runs    | Detector        |  BH   | Flood |  GH   | Sink  | Worm  | Mean  |    DR     | FPR  |    DR     |  FPR  |
| Same    | $k$-NN distance | 1.000 | 1.000 | 0.931 | 0.996 | 0.971 | 0.979 |   0.91    | 0.20 |   0.74    | 0.033 |
|         | $k$-NN + $\nu$  | 1.000 | 1.000 | 0.931 | 0.996 | 1.000 | 0.985 |   0.96    | 0.20 |   0.94    | 0.033 |
|         | Hybrid          | 0.916 | 0.977 | 0.943 | 0.968 | 1.000 | 0.960 |   0.88    | 0.09 |   0.26    | 0.007 |
| Shifted | $k$-NN distance | 1.000 | 1.000 | 0.917 | 0.953 | 0.580 | 0.890 |   0.93    | 0.59 |   0.84    | 0.357 |
|         | $k$-NN + $\nu$  | 0.997 | 0.993 | 0.912 | 0.951 | 0.754 | 0.921 |   0.93    | 0.59 |   0.91    | 0.356 |
|         | Hybrid          | 0.992 | 0.994 | 0.997 | 0.986 | 0.708 | 0.935 |   0.92    | 0.03 |   0.15    | 0.006 |

## Table S13. Frozen and recalibrated detectors on the 18 shifted-environment runs. Recalibration recomputes rank references and thresholds from 200 honest nodes of two separate normal runs in the shifted environment; the models are not retrained. DR: mean detection rate; FPR: worst false-positive rate over the five held-out attacks; alerts: honest nodes falsely flagged per 300 s run

|                 |              |       |           |       |        |           |       |        |
|:----------------|:-------------|:-----:|:---------:|:-----:|:------:|:---------:|:-----:|:------:|
|                 |              |       | 95th pct. |       |        | 99th pct. |       |        |
| Detector        | References   | AUROC |    DR     |  FPR  | Alerts |    DR     |  FPR  | Alerts |
| $k$-NN distance | frozen       | 0.890 |   0.93    | 0.594 |  54.4  |   0.84    | 0.357 |  31.5  |
|                 | recalibrated | 0.890 |   0.72    | 0.122 |  10.0  |   0.68    | 0.027 |  2.3   |
| $k$-NN + $\nu$  | frozen       | 0.921 |   0.93    | 0.595 |  54.4  |   0.91    | 0.356 |  31.1  |
|                 | recalibrated | 0.917 |   0.85    | 0.119 |  9.8   |   0.81    | 0.030 |  2.2   |
| Hybrid          | frozen       | 0.935 |   0.92    | 0.034 |  1.6   |   0.15    | 0.006 |  0.3   |
|                 | recalibrated | 0.933 |   0.92    | 0.112 |  6.6   |   0.88    | 0.016 |  1.1   |

## Table S14. Recent open-set baselines and alternative fusion rules, four folds. AUROC per held-out attack and mean; DR: mean detection rate and FPR: worst false-positive rate at the validation 95th percentile

| Score                        |  BH   | Flood |  GH   | Sink  | Worm  | Mean  |  DR  | FPR  |
|:-----------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:----:|:----:|
| $k$-NN distance (reference)  | 1.000 | 1.000 | 0.957 | 0.999 | 0.923 | 0.976 | 0.90 | 0.20 |
| Mahalanobis distance         | 0.999 | 0.995 | 0.958 | 0.999 | 0.960 | 0.982 | 0.95 | 0.15 |
| Reciprocal points (RPL)      | 0.000 | 0.013 | 0.178 | 0.022 | 0.662 | 0.175 | 0.03 | 0.05 |
| $k$-NN + $\nu$, max (Eq. 10) | 0.999 | 1.000 | 0.957 | 0.999 | 0.972 | 0.985 | 0.97 | 0.20 |
| $k$-NN + $\nu$, sum          | 0.999 | 1.000 | 0.957 | 0.999 | 0.972 | 0.985 | 0.97 | 0.20 |
| Hybrid, max (Eq. 9)          | 0.963 | 0.979 | 0.959 | 0.989 | 0.957 | 0.969 | 0.90 | 0.06 |
| Hybrid, mean of ranks        | 0.841 | 0.919 | 0.636 | 0.962 | 0.962 | 0.864 | 0.47 | 0.08 |
| Hybrid, sum                  | 0.841 | 0.919 | 0.636 | 0.962 | 0.962 | 0.864 | 0.47 | 0.08 |

## Table S15. Ablation of the distance-plus-invariant detector, four folds. AUROC per held-out attack and mean; DR: mean detection rate and FPR: worst false-positive rate at the validation 95th percentile. Feature groups: forwarding (forwarding count, ratio and its average), route discovery (requests received and sent, route failures, and their averages), neighbourhood (neighbour count and churn), radio (weakest received signal and the distance derived from it), mobility (speed)

| Variant                                     |  BH   | Flood |  GH   | Sink  | Worm  | Mean  |  DR  | FPR  |
|:--------------------------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:----:|:----:|
| $k = 1$                                     | 0.999 | 0.999 | 0.962 | 0.998 | 0.972 | 0.986 | 0.97 | 0.21 |
| $k = 3$                                     | 0.999 | 1.000 | 0.960 | 0.999 | 0.972 | 0.986 | 0.97 | 0.20 |
| $k = 5$ (paper)                             | 0.999 | 1.000 | 0.957 | 0.999 | 0.972 | 0.985 | 0.97 | 0.20 |
| $k = 10$                                    | 0.999 | 0.999 | 0.954 | 0.999 | 0.971 | 0.984 | 0.97 | 0.20 |
| $k = 20$                                    | 0.999 | 0.999 | 0.952 | 0.999 | 0.969 | 0.983 | 0.96 | 0.18 |
| without forwarding                          | 0.819 | 1.000 | 0.356 | 0.999 | 0.966 | 0.828 | 0.61 | 0.21 |
| without route discovery                     | 0.999 | 0.782 | 0.981 | 0.856 | 0.967 | 0.917 | 0.76 | 0.12 |
| without neighbourhood                       | 0.999 | 0.999 | 0.965 | 0.998 | 0.960 | 0.984 | 0.97 | 0.19 |
| without radio                               | 1.000 | 0.999 | 0.959 | 0.998 | 0.973 | 0.986 | 0.97 | 0.21 |
| without mobility                            | 0.999 | 0.999 | 0.966 | 0.999 | 0.976 | 0.988 | 0.97 | 0.21 |
| without $\nu$ as an input                   | 0.999 | 1.000 | 0.957 | 0.999 | 0.972 | 0.985 | 0.97 | 0.20 |
| without the $\nu$ term (distance rank only) | 0.999 | 1.000 | 0.957 | 0.999 | 0.923 | 0.975 | 0.90 | 0.20 |
| $\nu$ term with the two-window rule         | 0.999 | 1.000 | 0.957 | 0.999 | 0.972 | 0.985 | 0.97 | 0.20 |

## Table S16. Evaluation with every node, four folds. AUROC per held-out attack and mean; DR: mean detection rate and FPR: worst false-positive rate at the validation 95th percentile

| Nodes                        | Detector        |  BH   | Flood |  GH   | Sink  | Worm  | Mean  |  DR  | FPR  |
|:-----------------------------|:----------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:----:|:----:|
| Active nodes (main protocol) | $k$-NN distance | 1.000 | 1.000 | 0.957 | 0.999 | 0.923 | 0.976 | 0.90 | 0.20 |
|                              | $k$-NN + $\nu$  | 0.999 | 1.000 | 0.957 | 0.999 | 0.972 | 0.985 | 0.97 | 0.20 |
|                              | Hybrid          | 0.963 | 0.979 | 0.959 | 0.989 | 0.957 | 0.969 | 0.90 | 0.06 |
| All nodes                    | $k$-NN distance | 0.995 | 1.000 | 0.881 | 0.999 | 0.925 | 0.960 | 0.89 | 0.19 |
|                              | $k$-NN + $\nu$  | 0.995 | 0.999 | 0.881 | 0.999 | 0.973 | 0.969 | 0.95 | 0.19 |
|                              | Hybrid          | 0.927 | 0.986 | 0.904 | 0.989 | 0.964 | 0.954 | 0.82 | 0.08 |
| All nodes, activity as input | $k$-NN distance | 0.994 | 1.000 | 0.876 | 1.000 | 0.911 | 0.956 | 0.87 | 0.18 |
|                              | $k$-NN + $\nu$  | 0.994 | 0.999 | 0.875 | 0.999 | 0.972 | 0.968 | 0.95 | 0.18 |
|                              | Hybrid          | 0.899 | 0.985 | 0.924 | 0.988 | 0.959 | 0.951 | 0.79 | 0.07 |

## Table S17. Online classifier-plus-gate decision, four folds, scored after every window. Unknown: share of unseen-attack nodes labelled unknown; alarm: share raising any alarm; latency: median seconds from the start of the attack to the first alarm; FA: share of normal nodes raising any alarm during the run; known alarm: share of known-attack nodes raising an alarm; F1: known-class macro F1 of the forest alone and with unknown labels from the gate

| Pct. | Held-out attack | Unknown | Alarm | Latency (s) |  FA   | Known alarm |  F1  | F1, gated |
|:-----|:----------------|:-------:|:-----:|:-----------:|:-----:|:-----------:|:----:|:---------:|
| 95th | Black hole      |  1.00   | 1.00  |     10      | 0.061 |    0.98     | 0.97 |   0.30    |
|      | Flooding        |  1.00   | 1.00  |     38      | 0.152 |    0.98     | 0.97 |   0.34    |
|      | Grey hole       |  0.90   | 0.94  |     44      | 0.056 |    0.99     | 0.98 |   0.33    |
|      | Sinkhole        |  1.00   | 1.00  |     12      | 0.080 |    0.98     | 0.98 |   0.50    |
|      | Wormhole        |  0.94   | 0.94  |     10      | 0.052 |    0.99     | 0.98 |   0.47    |
| 99th | Black hole      |  0.94   | 1.00  |     10      | 0.019 |    0.98     | 0.97 |   0.72    |
|      | Flooding        |  0.99   | 0.99  |     128     | 0.029 |    0.98     | 0.97 |   0.67    |
|      | Grey hole       |  0.63   | 0.94  |     44      | 0.021 |    0.99     | 0.98 |   0.70    |
|      | Sinkhole        |  0.94   | 0.94  |     38      | 0.016 |    0.98     | 0.98 |   0.74    |
|      | Wormhole        |  0.94   | 0.94  |     10      | 0.019 |    0.99     | 0.98 |   0.89    |

## Table S18. Frozen detectors on the attack-intensity campaign (attack family held out of training). Each cell: AUROC / detection rate / honest-node false-positive rate at the validation 95th percentile. Runs: simulation runs; $n$: attacker nodes scored

| Condition                | Runs | $n$ |   $k$-NN distance   |   $k$-NN + $\nu$    |       Hybrid        |     |
|:-------------------------|:----:|:---:|:-------------------:|:-------------------:|:-------------------:|:---:|
| Grey hole, drop 0.25     |  4   | 20  | 0.979 / 0.85 / 0.03 | 0.980 / 0.85 / 0.03 | 0.998 / 1.00 / 0.02 |     |
| Grey hole, drop 0.75     |  4   | 20  | 1.000 / 1.00 / 0.02 | 1.000 / 1.00 / 0.02 | 0.990 / 0.95 / 0.02 |     |
| Flooding, 1 request/s    |  3   | 15  | 1.000 / 1.00 / 0.66 | 1.000 / 1.00 / 0.66 | 0.970 / 0.20 / 0.03 |     |
| Flooding, 2 requests/s   |  2   | 10  | 1.000 / 1.00 / 0.93 | 1.000 / 1.00 / 0.93 | 0.973 / 1.00 / 0.05 |     |
| Black hole, 2 attackers  |  2   |  4  | 1.000 / 1.00 / 0.02 | 1.000 / 1.00 / 0.02 | 0.998 / 1.00 / 0.02 |     |
| Black hole, 10 attackers |  2   | 20  | 1.000 / 1.00 / 0.07 | 1.000 / 1.00 / 0.07 | 0.893 / 0.40 / 0.09 |     |

## Table S19. Model size, training time and time to score one node (single core, fold 1, wormhole held out, 5,553 training nodes)

| Detector                 | Params | Size (kB) | Train (s) | Score (ms) |
|:-------------------------|:------:|:---------:|:---------:|:----------:|
| $\nu$                    |   –    |    0.4    |     –     |   0.0007   |
| Decision tree            |   –    |    6.5    |   0.02    |    0.08    |
| Support vector machine   |   –    |   88.8    |   0.22    |    0.43    |
| $k$-nearest neighbours   |   –    |  1131.9   |   0.01    |    0.90    |
| Random forest, 300 trees |   –    |  2022.3   |   0.80    |   45.68    |
| Convolutional network    | 17.5k  |   68.5    |   6.84    |    0.12    |
| Long short-term memory   | 56.3k  |   219.8   |    33     |    0.71    |
| Gated recurrent unit     | 42.8k  |   167.0   |    40     |    1.78    |
| Autoencoder              | 11.5k  |   45.1    |   6.40    |    1.41    |
