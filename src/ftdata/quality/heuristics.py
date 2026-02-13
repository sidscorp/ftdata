"""Heuristic quality signals: length ratios, repetition, coherence."""

from __future__ import annotations

from ftdata.core.models import Dataset, QualityResult


def check_heuristics(dataset: Dataset) -> QualityResult:
    """Run heuristic quality checks on a dataset.

    Checks include: high repetition (FT007), imbalanced turns (FT010),
    low diversity (FT012).

    Args:
        dataset: Dataset to check.

    Returns:
        QualityResult with heuristic findings.
    """
    raise NotImplementedError
