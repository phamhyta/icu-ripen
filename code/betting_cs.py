"""Self-normalized anytime-valid confidence sequence, tighter than Bonferroni peeling."""
# NOTE: skeleton release -- snapshot_est_se below is implemented for reference;
# the band construction, cached scores, per-stay delays, and replay seeds will
# be released upon publication.
import numpy as np


def snapshot_est_se(a, dur_h, loss, t, wcap=20.0):
    """IPCW Hajek estimate and its se over the stays matured by calendar time t."""
    a_s = np.sort(a)
    nadm = np.searchsorted(a_s, t, "right")
    idx = np.where((a <= t) & (a + dur_h <= t))[0]
    if len(idx) < 40:
        return None
    ninc = np.searchsorted(a_s, t - dur_h[idx], "right")
    w = 1.0 / np.clip(ninc / max(nadm, 1), 1.0 / wcap, 1.0)
    th = np.sum(w * loss[idx]) / w.sum()
    var = np.sum(w ** 2 * (loss[idx] - th) ** 2) / w.sum() ** 2
    return th, np.sqrt(max(var, 1e-12))


def band(seed, c, alpha=0.1):
    raise NotImplementedError('released upon publication')


def coverage(c, nrep=200, warm=3):
    raise NotImplementedError('released upon publication')
