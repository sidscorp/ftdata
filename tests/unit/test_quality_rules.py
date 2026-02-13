"""Tests for rule-based quality checks."""

from __future__ import annotations

import pytest

from ftdata.core.models import Dataset
from ftdata.quality.rules import check_quality_rules


class TestCheckQualityRules:
    @pytest.mark.skip(reason="Quality rules not yet implemented")
    def test_clean_dataset(self, sample_dataset: Dataset) -> None:
        result = check_quality_rules(sample_dataset)
        assert result.passed is True

    @pytest.mark.skip(reason="Quality rules not yet implemented")
    def test_disabled_rules(self, sample_dataset: Dataset) -> None:
        result = check_quality_rules(sample_dataset, disabled_rules=["FT001"])
        assert result is not None

    @pytest.mark.skip(reason="Quality rules not yet implemented")
    def test_empty_response_detected(self) -> None:
        # Uses quality_issues.jsonl fixture
        pass
