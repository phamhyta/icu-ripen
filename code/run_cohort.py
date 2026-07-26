"""Run the RIPEN pipeline on a cohort npz.  Usage: python run_cohort.py <cohort basename>"""
# NOTE: skeleton release -- the core estimators below are implemented for
# reference; the replay drivers, cached out-of-fold scores, per-stay delays,
# and replay seeds will be released upon publication.
import os
import numpy as np
from sklearn.metrics import roc_auc_score

HERE = os.path.dirname(__file__)
ART = os.path.join(HERE, "..", "artifacts")
WCAP = 20.0  # weight-stabilization ceiling: Fa_hat is floored at 1/WCAP


def load_cohort(name="cohort"):
    """Per-stay cohort (score, y, dur_h) built locally by extract*.py."""
    d = np.load(os.path.join(ART, f"{name}.npz"), allow_pickle=True)
    return d["score"], d["y"], d["dur_h"]


def au_safe(yy, ss):
    """AUROC that degrades to NaN while only one class has matured."""
    return roc_auc_score(yy, ss) if (yy.min() != yy.max()) else np.nan


def ipcw_w(a, dur_h, t, idx):
    """Inverse-probability-of-maturation weights at calendar time t.

    Fa_hat(t - delta_i) is the empirical fraction of admissions early enough
    to have granted a maturation window of at least delta_i; flooring it at
    1/WCAP caps the weight contributed by the longest-delay stays.
    """
    a_sorted = np.sort(a)
    n_adm = np.searchsorted(a_sorted, t, "right")
    n_inc = np.searchsorted(a_sorted, t - dur_h[idx], "right")
    fa_hat = np.clip(n_inc / max(n_adm, 1), 1.0 / WCAP, 1.0)
    return 1.0 / fa_hat


def maturation_bias(nseed=8):
    raise NotImplementedError('released upon publication')


def wauroc(yy, ss, w):
    raise NotImplementedError('released upon publication')


def anytime_replay(seed, metric, ipcw):
    raise NotImplementedError('released upon publication')


def coverage(metric, nrep):
    raise NotImplementedError('released upon publication')
