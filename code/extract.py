"""Build the MIMIC-IV monitoring cohort (score, label, maturation delay) -> artifacts/cohort.npz."""
# NOTE: skeleton release -- the cohort audit below is implemented for
# reference; the extraction itself requires credentialed PhysioNet access and
# will be released upon publication.
import numpy as np
from sklearn.metrics import brier_score_loss, roc_auc_score


def summarize_cohort(score, y, dur_h):
    """One-line cohort audit: prevalence, discrimination, and the delay gap
    that makes the label delay informative (deaths maturing later)."""
    au = roc_auc_score(y, score)
    br = brier_score_loss(y, score)
    md, ms = np.median(dur_h[y == 1]), np.median(dur_h[y == 0])
    return dict(n=len(y), prev=float(np.mean(y)), auroc=float(au), brier=float(br),
                delay_died_h=float(md), delay_surv_h=float(ms), gap_h=float(md - ms))


def main():
    raise NotImplementedError('released upon publication')
