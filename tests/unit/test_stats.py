"""Tests for profiling statistics."""

from __future__ import annotations

import pytest

from ftdata.core.models import Dataset
from ftdata.profiling.stats import compute_length_profile, compute_turn_profile, profile_dataset


class TestComputeLengthProfile:
    @pytest.mark.skip(reason="Stats not yet implemented")
    def test_basic(self, sample_dataset: Dataset) -> None:
        profile = compute_length_profile(sample_dataset)
        assert profile.total_tokens.total > 0


class TestComputeTurnProfile:
    @pytest.mark.skip(reason="Stats not yet implemented")
    def test_basic(self, sample_dataset: Dataset) -> None:
        profile = compute_turn_profile(sample_dataset)
        assert profile.min >= 0


class TestProfileDataset:
    @pytest.mark.skip(reason="Stats not yet implemented")
    def test_full_profile(self, sample_dataset: Dataset) -> None:
        result = profile_dataset(sample_dataset)
        assert result.sample_count > 0
