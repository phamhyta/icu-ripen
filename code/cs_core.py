"""Waudby-Smith--Ramdas hedged-betting confidence sequence for a bounded (weighted) mean."""
# NOTE: skeleton release -- the peeling helpers below are implemented for
# reference; the hedged-betting CS itself, cached scores, per-stay delays,
# and replay seeds will be released upon publication.
import numpy as np


def peel_alpha(alpha, K):
    """Bonferroni-peeled per-look level for a K-look schedule."""
    return alpha / K


def intersect_running(los, his):
    """Cumulative intersection of per-look intervals.

    The running band never re-expands over looks; an empty overlap keeps the
    previous band instead of resetting.
    """
    lo_run, hi_run, band = 0.0, 1.0, []
    for lo, hi in zip(los, his):
        nlo, nhi = max(lo_run, lo), min(hi_run, hi)
        if nlo <= nhi:
            lo_run, hi_run = nlo, nhi
        band.append((lo_run, hi_run))
    return band


def wsr_cs(x, w=None, alpha=0.1, grid=None, lam_cap=0.75):
    raise NotImplementedError('released upon publication')
