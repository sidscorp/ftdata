"""Language detection per sample."""

from __future__ import annotations

from ftdata.core.models import Dataset, LanguageProfile


def detect_languages(dataset: Dataset) -> LanguageProfile:
    """Detect the language distribution across dataset samples.

    Args:
        dataset: Dataset to analyze.

    Returns:
        LanguageProfile with language counts and primary language.
    """
    raise NotImplementedError
