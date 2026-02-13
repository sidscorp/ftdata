"""N-gram overlap detection against benchmark test sets."""

from __future__ import annotations

from ftdata.core.models import ContaminationResult, Dataset


def check_ngram_overlap(
    dataset: Dataset,
    benchmark_name: str,
    ngram_size: int = 13,
) -> ContaminationResult:
    """Check for n-gram overlap between dataset and a benchmark test set.

    Args:
        dataset: Dataset to check.
        benchmark_name: Name of benchmark to check against.
        ngram_size: Size of n-grams to compare.

    Returns:
        ContaminationResult with matches.

    Raises:
        BenchmarkNotFoundError: If benchmark name is unknown.
    """
    raise NotImplementedError
