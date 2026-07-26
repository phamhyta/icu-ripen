"""Self-normalized doubly-robust (PPI-style) RIPEN estimator."""
# NOTE: skeleton release -- hajek_mean below is implemented for reference; the
# DR estimator itself, replay drivers, cached scores, per-stay delays, and
# replay seeds will be released upon publication.
import numpy as np


def hajek_mean(vals, w):
    """Self-normalized weighted mean (the Hajek functional both modes share)."""
    w = np.asarray(w, float)
    return float(np.sum(w * vals) / np.sum(w))


def estimate(a, t, mode, wrong_F=False):
    raise NotImplementedError('released upon publication')


def anytime(mode, wrong_F=False, nrep=200, alpha=0.1):
    raise NotImplementedError('released upon publication')
