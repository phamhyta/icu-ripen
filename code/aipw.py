"""Augmented IPCW (doubly-robust) monitor for the Brier under label maturation."""
# NOTE: skeleton release -- snapshot below is implemented for reference; the
# augmentation model, replay drivers, cached scores, per-stay delays, and
# replay seeds will be released upon publication.
import numpy as np


def snapshot(a, dur_h, t):
    """Admitted index set, matured mask, and empirical Fa_hat at calendar time t."""
    adm = np.where(a <= t)[0]
    mat = (a[adm] + dur_h[adm]) <= t
    a_sorted = np.sort(a)
    nadm = np.searchsorted(a_sorted, t, "right")
    F = np.searchsorted(a_sorted, t - dur_h[adm], "right") / max(nadm, 1)
    return adm, mat, F


def data_driven_g(a, t):
    raise NotImplementedError('released upon publication')


def estimate(a, t, mode):
    raise NotImplementedError('released upon publication')


def experiment(nrep=200, alpha=0.1):
    raise NotImplementedError('released upon publication')


def coverage(nrep=200, alpha=0.1):
    raise NotImplementedError('released upon publication')
