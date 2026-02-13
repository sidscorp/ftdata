"""Token length distributions, vocabulary stats, and turn counts."""

from __future__ import annotations

from ftdata.core.models import Dataset, LengthProfile, ProfileResult, TurnProfile, VocabProfile


def compute_length_profile(dataset: Dataset) -> LengthProfile:
    """Compute token length statistics for prompts, responses, and totals.

    Args:
        dataset: Dataset to profile.

    Returns:
        LengthProfile with min/max/mean/median/p95/p99 stats.
    """
    raise NotImplementedError


def compute_turn_profile(dataset: Dataset) -> TurnProfile:
    """Compute turn count distribution across samples.

    Args:
        dataset: Dataset to profile.

    Returns:
        TurnProfile with min/max/mean/median.
    """
    raise NotImplementedError


def compute_vocab_profile(dataset: Dataset) -> VocabProfile:
    """Compute vocabulary statistics.

    Args:
        dataset: Dataset to profile.

    Returns:
        VocabProfile with unique tokens, TTR, and top tokens.
    """
    raise NotImplementedError


def profile_dataset(dataset: Dataset) -> ProfileResult:
    """Run full profiling on a dataset.

    Args:
        dataset: Dataset to profile.

    Returns:
        Complete ProfileResult.
    """
    raise NotImplementedError
