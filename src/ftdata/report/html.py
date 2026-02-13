"""HTML report generation via Jinja2."""

from __future__ import annotations

from pathlib import Path

from ftdata.core.models import ProfileReport


def render_html_report(
    report: ProfileReport,
    output_path: Path | None = None,
    template_path: Path | None = None,
) -> str:
    """Render a ProfileReport as an HTML document.

    Args:
        report: ProfileReport to render.
        output_path: Optional path to write HTML file.
        template_path: Optional custom Jinja2 template.

    Returns:
        Rendered HTML string.
    """
    raise NotImplementedError
