# RIPEN — Anytime-Valid Performance Monitoring of Deployed Clinical Risk Models Under Informative Label Delay

Public code repository for the paper **_Anytime-Valid Performance Monitoring of Deployed Clinical
Risk Models Under Informative Label Delay_** (under review). `RIPEN` (Reweighted
Inverse-Probability Estimation for moNitoring; labels *ripen* before they can be scored) is the
monitor the paper develops; earlier project material used the working name `MatureCS`, and the
`maturecs_*.py` module names retain it for provenance.

> **Status: skeleton release.** This repository currently contains the module structure, API
> signatures, reference implementations of the core estimators (the IPCW maturation weights, the
> Hájek self-normalized Brier, the weighted Mann–Whitney AUROC, and the one-sided lower confidence
> bound used for alarming), and documentation of the full pipeline. The complete replay pipeline,
> cached out-of-fold scores, per-stay delays, and replay seeds will be released here under an
> open-source license upon publication.

## What RIPEN does

A deployed clinical risk model must be watched for silent degradation, but its labels arrive
**late** (in-hospital mortality is known only when a stay resolves) and the delay is
**informative** (in the primary cohort fatal stays are longer, so they mature later). Scoring only
the resolved stays is therefore optimistically biased, while waiting for all labels is weeks
stale. **RIPEN** reweights each resolved stay by its inverse probability of having matured (IPCW),
re-expanding the delay-selected sample back to the admitted population, and peels a schedule of
calendar snapshots into a running confidence band that is valid at every look and **widens
honestly** when the reweighting is under-determined.

## Repository layout

```
code/           Python: extraction, estimators, anytime-valid CS, experiments, figures
artifacts/      Derived per-stay cohorts (NOT redistributed — see data governance below)
results/        Aggregate result JSON (coverage rates, bias curves, detection, paired tests)
```

### Pipeline modules (`code/`)

| Module | Role |
| --- | --- |
| `extract.py`, `extract_external.py` | Build the MIMIC-IV / Challenge-2012 / eICU-CRD demo monitoring cohorts |
| `cs_core.py` | Waudby-Smith–Ramdas hedged-betting confidence sequence for a bounded (weighted) mean |
| `maturation_bias.py` | RQ1 — magnitude and mechanism of the completed-cases maturation bias |
| `maturecs_ipcw.py` | RQ2 — IPCW point debiasing |
| `snapshot_inference.py` | RQ3 — fixed-time calendar-snapshot coverage |
| `maturecs_cs.py`, `maturecs_anytime.py`, `betting_cs.py` | RQ4 — anytime-valid confidence sequences (Brier + AUROC) |
| `run_cohort.py` | RQ5 — cross-cohort replication driver |
| `detection.py`, `detection_dr.py`, `detection_paired.py` | RQ6 — time-to-detection and paired McNemar significance |
| `aipw.py`, `aipw_misspec.py`, `dr_estimator.py` | Doubly-robust / prediction-powered (RIPEN-DR) variants |
| `make_figs.py` | Regenerate all publication figures from cached result JSONs |

## Reproducing (upon full release)

The experiments are **CPU-scale** (cached out-of-fold scores + per-stay delays; no GPU, no
retraining). All experiments in the paper were run on an Apple M4 (10-core) laptop with 16 GB RAM.

```bash
cd code
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt
python extract.py            # build the MIMIC-IV monitoring cohort (needs local data — see below)
python extract_external.py   # Challenge-2012 + eICU-CRD demo cohorts
python maturation_bias.py    # RQ1: the maturation bias
python maturecs_ipcw.py      # RQ2: IPCW debiasing
python snapshot_inference.py # RQ3: snapshot coverage
python maturecs_anytime.py   # RQ4: anytime-valid CS coverage (Brier + AUROC)
python run_cohort.py cohort  # RQ5: cross-cohort (also cohort_challenge2012 / cohort_eicu)
python detection_dr.py       # RQ6: time-to-detection (+ the RIPEN-DR variant)
python detection_paired.py   # paired McNemar significance
python make_figs.py          # regenerate all figures
```

## Data access and governance

The per-stay arrays the code consumes (`artifacts/*.npz`) are **derived from MIMIC-IV, a
credentialed PhysioNet database, and are intentionally NOT included in this repository**, in
compliance with the PhysioNet Credentialed Health Data Use Agreement (which prohibits
redistribution). To reproduce, obtain your own credentialed access to
[MIMIC-IV](https://physionet.org/content/mimiciv/) (and, optionally, the open
[eICU-CRD demo](https://physionet.org/content/eicu-crd-demo/) and open
[Challenge-2012](https://physionet.org/content/challenge-2012/)), then run the `extract*.py`
scripts to rebuild the cohorts locally. Only **aggregate** results (coverage rates, curves) and
plots are published here; no protected health information is redistributed.

This is a retrospective monitoring-**methodology** study, not a deployed clinical decision tool;
any clinical use would require prospective validation and local governance review.

## Citation

Citation information will be added upon publication.

## License

[MIT](LICENSE)
