"""Tests for PII detection."""

from __future__ import annotations

import pytest

from ftdata.core.models import Dataset
from ftdata.quality.pii import detect_pii


class TestDetectPii:
    @pytest.mark.skip(reason="PII detection not yet implemented")
    def test_clean_dataset(self, sample_dataset: Dataset) -> None:
        result = detect_pii(sample_dataset)
        assert result.passed is True

    @pytest.mark.skip(reason="PII detection not yet implemented")
    def test_detects_email(self) -> None:
        # Uses quality_issues.jsonl fixture
        pass

    @pytest.mark.skip(reason="PII detection not yet implemented")
    def test_detects_ssn(self) -> None:
        # Uses quality_issues.jsonl fixture
        pass
