"""RQ4: RIPEN anytime-valid confidence sequence (calendar-snapshot IPCW + peeling), Brier + AUROC."""
# NOTE: skeleton stub -- the full implementation, cached scores, per-stay
# delays, and replay seeds will be released upon publication.

def ipcw_weights(a, t, idx, wcap=20.0):
    raise NotImplementedError('released upon publication')

def hajek_mean_ci(vals, w, alpha_look):
    raise NotImplementedError('released upon publication')

def _wauroc(yy, ss, w):
    raise NotImplementedError('released upon publication')

def weighted_auroc_ci(yy, ss, w, alpha_look, nboot=120, seed=0):
    raise NotImplementedError('released upon publication')

def run_replay(seed, alpha=0.1, rate=12, horizon=90, metric='brier', ipcw=True):
    raise NotImplementedError('released upon publication')

def coverage(metric='brier', nrep=200, alpha=0.1):
    raise NotImplementedError('released upon publication')

