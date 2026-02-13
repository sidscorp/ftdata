"""Embedding-based topic clustering (requires [semantic] extra for HDBSCAN)."""

from __future__ import annotations

from ftdata.core.models import Dataset, DiversityResult


def cluster_topics(
    dataset: Dataset,
    model_name: str = "all-MiniLM-L6-v2",
    min_cluster_size: int = 5,
) -> DiversityResult:
    """Cluster dataset samples by topic using embeddings and HDBSCAN.

    Requires the [semantic] extra (sentence-transformers, hdbscan).

    Args:
        dataset: Dataset to cluster.
        model_name: Sentence-transformer model for embeddings.
        min_cluster_size: Minimum samples per cluster.

    Returns:
        DiversityResult with topic clusters and diversity score.

    Raises:
        SemanticUnavailableError: If [semantic] extra is not installed.
    """
    raise NotImplementedError
