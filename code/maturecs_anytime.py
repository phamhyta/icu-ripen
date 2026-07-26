"""RQ4: RIPEN anytime-valid confidence sequence (calendar-snapshot IPCW + peeling), Brier + AUROC."""
# NOTE: skeleton release -- the weight and per-look CI helpers below are
# implemented for reference; the replay drivers, cached scores, per-stay
# delays, and replay seeds will be released upon publication.
import numpy as np
from scipy.stats import norm


def ipcw_weights(a, dur_h, t, idx, wcap=20.0):
    """Inverse-probability-of-maturation weights at calendar time t."""
    a_sorted = np.sort(a)
    nadm = np.searchsorted(a_sorted, t, side="right")
    ninc = np.searchsorted(a_sorted, t - dur_h[idx], side="right")
    H = ninc / max(nadm, 1)
    return 1.0 / np.clip(H, 1.0 / wcap, 1.0)


def hajek_mean_ci(vals, w, alpha_look):
    """Hajek weighted mean of bounded vals in [0,1] + delta-method normal CI."""
    W = w.sum()
    th = np.sum(w * vals) / W
    var = np.sum(w ** 2 * (vals - th) ** 2) / W ** 2
    se = np.sqrt(max(var, 1e-12))
    z = norm.ppf(1 - alpha_look / 2)
    return th, max(0.0, th - z * se), min(1.0, th + z * se)


def _wauroc(yy, ss, w):
    raise NotImplementedError('released upon publication')


def weighted_auroc_ci(yy, ss, w, alpha_look, nboot=120, seed=0):
    raise NotImplementedError('released upon publication')


def run_replay(seed, alpha=0.1, rate=12, horizon=90, metric='brier', ipcw=True):
    raise NotImplementedError('released upon publication')


def coverage(metric='brier', nrep=200, alpha=0.1):
    raise NotImplementedError('released upon publication')
