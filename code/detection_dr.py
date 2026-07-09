"""Time-to-detection with the self-normalized doubly-robust estimator."""
# NOTE: skeleton stub -- the full implementation, cached scores, per-stay
# delays, and replay seeds will be released upon publication.

def make_scenario(r, kind, change_frac=0.5, strength=0.6, flip_q=0.25):
    raise NotImplementedError('released upon publication')

def lower_bound(vals, w, z):
    raise NotImplementedError('released upon publication')

def dr_lower(gi, r_resid, w, N, z):
    raise NotImplementedError('released upon publication')

def run(seed, kind, alpha=0.1):
    raise NotImplementedError('released upon publication')

def experiment(kind, nrep=200):
    raise NotImplementedError('released upon publication')

