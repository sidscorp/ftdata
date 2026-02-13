"""Rule-based quality checks: empty, truncated, encoding, format errors."""

from __future__ import annotations

from ftdata.core.models import Dataset, QualityResult


def check_quality_rules(
    dataset: Dataset,
    disabled_rules: list[str] | None = None,
    max_response_tokens: int = 4096,
    min_response_tokens: int = 1,
) -> QualityResult:
    """Run rule-based quality checks on a dataset.

    Checks include: empty responses (FT001), truncation (FT002),
    encoding errors (FT003), format errors (FT004), excessive length (FT005),
    short responses (FT006), missing system messages (FT011).

    Args:
        dataset: Dataset to check.
        disabled_rules: List of rule IDs to skip.
        max_response_tokens: Maximum allowed response tokens (FT005).
        min_response_tokens: Minimum required response tokens (FT006).

    Returns:
        QualityResult with all detected issues.
    """
    raise NotImplementedError
