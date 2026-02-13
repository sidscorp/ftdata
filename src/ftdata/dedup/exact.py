"""Exact duplicate detection using content hashing."""

from __future__ import annotations

from ftdata.core.models import Dataset, DedupResult


def find_exact_duplicates(dataset: Dataset) -> DedupResult:
    """Find exact duplicate samples using SHA-256 content hashing.

    Samples with identical content_hash values are grouped into clusters.

    Args:
        dataset: Dataset to check for duplicates.

    Returns:
        DedupResult with clusters of exact duplicates.
    """
    raise NotImplementedError
