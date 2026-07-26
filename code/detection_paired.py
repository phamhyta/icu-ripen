"""Paired McNemar significance tests for the detection claims."""
# NOTE: skeleton release -- the exact McNemar test below is implemented for
# reference; the replay bookkeeping, cached scores, and replay seeds will be
# released upon publication.
import numpy as np
from scipy.stats import binomtest


def mcnemar(det_a, det_b):
    """Exact McNemar test on paired boolean detect indicators."""
    det_a = np.asarray(det_a, bool)
    det_b = np.asarray(det_b, bool)
    only_a = int(np.sum(det_a & ~det_b))
    only_b = int(np.sum(~det_a & det_b))
    nd = only_a + only_b
    p = binomtest(only_a, nd, 0.5).pvalue if nd > 0 else 1.0
    return dict(rate_a=float(det_a.mean()), rate_b=float(det_b.mean()),
                discordant=nd, only_a=only_a, only_b=only_b, p=float(p))


def paired_delay(a_key, b_key):
    raise NotImplementedError('released upon publication')
