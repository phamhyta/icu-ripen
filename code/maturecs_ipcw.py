"""RQ2: IPCW point debiasing of the completed-cases estimate."""
# NOTE: skeleton release -- weighted_auroc below is implemented for reference;
# the replay drivers, cached scores, per-stay delays, and replay seeds will be
# released upon publication.
import numpy as np


def weighted_auroc(yy, ss, w):
    """Weighted Mann--Whitney AUROC with pair weights w_i * w_j.

    Sorting the negatives once and cumulating their weights makes the
    pairwise sum O((n_pos + n_neg) log n_neg); ties count half.
    """
    pos, neg = yy == 1, yy == 0
    if pos.sum() == 0 or neg.sum() == 0:
        return np.nan
    sp, wp = ss[pos], w[pos]
    sn, wn = ss[neg], w[neg]
    o = np.argsort(sn)
    sn, wn = sn[o], wn[o]
    cw = np.concatenate([[0.0], np.cumsum(wn)])
    lt = np.searchsorted(sn, sp, "left")
    le = np.searchsorted(sn, sp, "right")
    wins = cw[lt] + 0.5 * (cw[le] - cw[lt])
    return float((wp * wins).sum() / (wp.sum() * cw[-1]))


def replay_estimators(rate, horizon, seed, n_grid=140, wcap=20.0):
    raise NotImplementedError('released upon publication')


def summarize(rate, horizon, seeds=8):
    raise NotImplementedError('released upon publication')
