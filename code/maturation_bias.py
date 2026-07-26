"""RQ1: magnitude of the completed-cases maturation bias (semi-synthetic calendar replay)."""
# NOTE: skeleton release -- auroc_safe below is implemented for reference; the
# calendar replay, cached scores, per-stay delays, and replay seeds will be
# released upon publication.
import numpy as np
from sklearn.metrics import roc_auc_score


def auroc_safe(yy, ss):
    """AUROC that degrades to NaN while only one class has matured."""
    return roc_auc_score(yy, ss) if (yy.min() != yy.max()) else np.nan


def replay(rate_per_day, horizon_days, n_grid=160, seed=0):
    raise NotImplementedError('released upon publication')


def summarize(rate, horizon):
    raise NotImplementedError('released upon publication')
