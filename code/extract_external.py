"""Build the Challenge-2012 and eICU-CRD demo monitoring cohorts."""
# NOTE: skeleton release -- save below is implemented for reference; the
# cohort builders themselves require the source datasets and will be released
# upon publication.
import os
import numpy as np
from sklearn.metrics import brier_score_loss, roc_auc_score

OUT = os.path.join(os.path.dirname(__file__), "..", "artifacts")


def save(name, ids, score, y, dur_h, outdir=OUT):
    """Filter to finite rows, write the cohort npz, and print the audit line."""
    ids = np.array(ids)
    score = np.array(score, float)
    y = np.array(y, int)
    dur_h = np.array(dur_h, float)
    ok = np.isfinite(score) & np.isfinite(dur_h) & (dur_h > 0)
    ids, score, y, dur_h = ids[ok], score[ok], y[ok], dur_h[ok]
    np.savez(os.path.join(outdir, f"cohort_{name}.npz"), id=ids, score=score, y=y, dur_h=dur_h)
    au = roc_auc_score(y, score)
    br = brier_score_loss(y, score)
    md, ms = np.median(dur_h[y == 1]), np.median(dur_h[y == 0])
    print(f"[{name}] n={len(ids)} prev={y.mean():.3f} AUROC={au:.4f} Brier={br:.4f} | "
          f"delay median died={md:.0f}h surv={ms:.0f}h -> deaths mature "
          f"{'LATER' if md > ms else 'EARLIER'} (diff {md-ms:+.0f}h)")


def main():
    raise NotImplementedError('released upon publication')
