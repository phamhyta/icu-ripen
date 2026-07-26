"""Generate publication figures from cached result JSONs."""
# NOTE: skeleton release -- save below is implemented for reference; the
# per-figure generators will be released upon publication.
import os

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")


def save(fig, name, outdir=FIG):
    """Write a figure as both vector PDF (for the paper) and PNG (quick look)."""
    os.makedirs(outdir, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(outdir, f"{name}.{ext}"), bbox_inches="tight", dpi=300)


def fig1_maturation_bias():
    raise NotImplementedError('released upon publication')


def fig2_ipcw_debias():
    raise NotImplementedError('released upon publication')


def fig3_coverage():
    raise NotImplementedError('released upon publication')


def fig4_anytime_band():
    raise NotImplementedError('released upon publication')


def fig5_crosscohort():
    raise NotImplementedError('released upon publication')


def fig6_detection():
    raise NotImplementedError('released upon publication')
