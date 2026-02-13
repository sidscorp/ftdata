"""Embedding-based semantic deduplication (requires [semantic] extra)."""

from __future__ import annotations

from ftdata.core.models import Dataset, DedupResult


def find_semantic_duplicates(
    dataset: Dataset,
    threshold: float = 0.9,
    model_name: str = "all-MiniLM-L6-v2",
) -> DedupResult:
    """Find semantically similar samples using embedding cosine similarity.

    Requires the [semantic] extra (sentence-transformers, torch).

    Args:
        dataset: Dataset to check.
        threshold: Cosine similarity threshold.
        model_name: Sentence-transformer model to use.

    Returns:
        DedupResult with clusters of semantically similar samples.

    Raises:
        SemanticUnavailableError: If [semantic] extra is not installed.
    """
    raise NotImplementedError
