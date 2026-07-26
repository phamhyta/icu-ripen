"""RQ6: time-to-detection of an injected degradation (RIPEN vs. completed-only vs. oracle)."""
# NOTE: skeleton release -- the one-sided lower bound below is implemented for
# reference; degradation injection, replay drivers, cached scores, and replay
# seeds will be released upon publication.
import numpy as np


def degrade(score, mask, strength=0.6):
    raise NotImplementedError('released upon publication')


def ipcw_w(a, t, idx):
    raise NotImplementedError('released upon publication')


def run(seed, change_frac=0.5, strength=0.6, alpha=0.1):
    raise NotImplementedError('released upon publication')


def _lower(vals, w, z):
    """One-sided lower confidence bound for a Hajek weighted mean."""
    th = np.sum(w * vals) / w.sum()
    var = np.sum(w ** 2 * (vals - th) ** 2) / w.sum() ** 2
    return th - z * np.sqrt(max(var, 1e-12))


def experiment(nrep=200, strength=0.6):
    raise NotImplementedError('released upon publication')
