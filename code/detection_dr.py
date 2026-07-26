"""Time-to-detection with the self-normalized doubly-robust estimator."""
# NOTE: skeleton release -- the two lower bounds below are implemented for
# reference; scenario generation, replay drivers, cached scores, and replay
# seeds will be released upon publication.
import numpy as np


def make_scenario(r, kind, change_frac=0.5, strength=0.6, flip_q=0.25):
    raise NotImplementedError('released upon publication')


def lower_bound(vals, w, z):
    """One-sided lower confidence bound for a Hajek weighted mean."""
    th = np.sum(w * vals) / np.sum(w)
    var = np.sum(w ** 2 * (vals - th) ** 2) / np.sum(w) ** 2
    return th - z * np.sqrt(max(var, 1e-12))


def dr_lower(gi, r_resid, w, N, z):
    """One-sided lower bound for the DR estimate g-bar + Hajek residual mean."""
    rbar = np.sum(w * r_resid) / np.sum(w)
    th = gi.mean() + rbar
    phi = (gi - gi.mean()) + (N * w / np.sum(w)) * (r_resid - rbar) * (w > 0)
    return th - z * phi.std() / np.sqrt(N)


def run(seed, kind, alpha=0.1):
    raise NotImplementedError('released upon publication')


def experiment(kind, nrep=200):
    raise NotImplementedError('released upon publication')
