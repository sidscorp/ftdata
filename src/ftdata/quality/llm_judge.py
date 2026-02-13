"""Optional LLM-as-judge scoring (requires [llm] extra)."""

from __future__ import annotations

from ftdata.core.models import Dataset, QualityResult


def score_with_llm(
    dataset: Dataset,
    model: str = "claude-sonnet-4-5-20250929",
    sample_size: int | None = None,
) -> QualityResult:
    """Score dataset samples using an LLM as judge.

    Requires the [llm] extra (anthropic).

    Args:
        dataset: Dataset to score.
        model: LLM model to use for judging.
        sample_size: Number of samples to judge (None = all).

    Returns:
        QualityResult with LLM-generated quality assessments.

    Raises:
        LLMUnavailableError: If [llm] extra is not installed.
    """
    raise NotImplementedError
