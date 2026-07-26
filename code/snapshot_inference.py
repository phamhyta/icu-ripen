"""RQ3: fixed-time calendar-snapshot inference with bootstrap CIs."""
# NOTE: skeleton release -- ht_brier below is implemented for reference; the
# snapshot construction, bootstrap CIs, cached scores, per-stay delays, and
# replay seeds will be released upon publication.
import numpy as np


def snapshot(a, t, wcap=20.0):
    raise NotImplementedError('released upon publication')


def ht_brier(loss, idx, w):
    """Hajek self-normalized IPCW Brier over the matured index set."""
    return float(np.sum(w * loss[idx]) / np.sum(w))


def boot_ci(idx, w, B=300, alpha=0.1, seed=0):
    raise NotImplementedError('released upon publication')


def experiment(nrep=200, rate=12, horizon=90, cfracs=(0.5, 0.7, 0.85, 0.95)):
    raise NotImplementedError('released upon publication')
