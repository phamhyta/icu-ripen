"""Double-robustness under a misspecified arrival/weight model."""
# NOTE: skeleton release -- sample_arrivals below is implemented for reference;
# the misspecified estimators, cached scores, per-stay delays, and replay
# seeds will be released upon publication.
import numpy as np


def sample_arrivals(r, n, W, amp=0.9):
    """Time-varying admission intensity ~ 1 + amp*sin: sample by thinning."""
    a = []
    while len(a) < n:
        cand = r.uniform(0, W, n * 2)
        acc = r.uniform(0, 1, n * 2) < (1 + amp * np.sin(2 * np.pi * cand / (W / 6))) / (1 + amp)
        a.extend(cand[acc].tolist())
    return np.array(a[:n])


def est(a, t, mode, wrong=True):
    raise NotImplementedError('released upon publication')


def coverage(nrep=150, alpha=0.1):
    raise NotImplementedError('released upon publication')
