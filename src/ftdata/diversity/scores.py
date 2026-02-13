"""Diversity metrics computation."""

from __future__ import annotations

from ftdata.core.models import DiversityResult


def compute_diversity_score(result: DiversityResult) -> float:
    """Compute a normalized diversity score from clustering results.

    Higher scores indicate more diverse topic coverage.

    Args:
        result: DiversityResult with clusters.

    Returns:
        Diversity score between 0.0 and 1.0.
    """
    raise NotImplementedError
