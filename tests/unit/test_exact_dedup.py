"""Tests for exact duplicate detection."""

from __future__ import annotations

import pytest

from ftdata.core.models import Dataset
from ftdata.dedup.exact import find_exact_duplicates


class TestFindExactDuplicates:
    @pytest.mark.skip(reason="Exact dedup not yet implemented")
    def test_no_duplicates(self, sample_dataset: Dataset) -> None:
        result = find_exact_duplicates(sample_dataset)
        assert result.total_duplicates == 0

    @pytest.mark.skip(reason="Exact dedup not yet implemented")
    def test_with_duplicates(self) -> None:
        # Uses with_duplicates.jsonl fixture
        pass
