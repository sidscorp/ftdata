"""Rich CLI summary report."""

from __future__ import annotations

from rich.console import Console

from ftdata.core.models import ProfileReport


def print_report(report: ProfileReport, console: Console | None = None) -> None:
    """Print a ProfileReport as a Rich-formatted CLI summary.

    Args:
        report: ProfileReport to display.
        console: Optional Rich Console (creates one if not provided).
    """
    raise NotImplementedError
