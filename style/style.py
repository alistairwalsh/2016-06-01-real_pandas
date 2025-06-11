"""Utility to apply custom notebook CSS styles."""

from pathlib import Path
from IPython.core.display import HTML

CSS_PATHS = ["style/style-table.css", "style/style-notebook.css"]


def _load_css() -> str:
    """Return the combined CSS from all style files."""
    parts = []
    for path in CSS_PATHS:
        parts.append(Path(path).read_text())
    return "".join(parts)


def apply_style() -> HTML:
    """Return an IPython ``HTML`` object with the notebook style."""
    css = _load_css()
    return HTML(f"<style>{css}</style>")
