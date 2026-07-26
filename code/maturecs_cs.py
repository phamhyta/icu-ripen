"""Anytime-valid coverage of the true Brier under label maturation (naive vs. IPCW monitor)."""
# NOTE: skeleton release -- the look-schedule helper below is implemented for
# reference; the replay and experiment drivers, cached scores, per-stay
# delays, and replay seeds will be released upon publication.
import numpy as np


def look_times(m, cfracs):
    """Calendar look times at which the given completion fractions are reached."""
    m_sorted = np.sort(np.asarray(m, float))
    n = len(m_sorted)
    return np.array([m_sorted[max(int(cf * n) - 1, 0)] for cf in cfracs])


def replay(seed, rate=12, horizon=90, wcap=20.0):
    raise NotImplementedError('released upon publication')


def experiment(nrep=200, warm=0.1):
    raise NotImplementedError('released upon publication')
