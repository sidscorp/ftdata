"""Tests for dataset loading."""

from __future__ import annotations

from pathlib import Path

import pytest

from ftdata.core.loader import detect_format, load_dataset
from ftdata.exceptions import EmptyDatasetError, FormatDetectionError


class TestDetectFormat:
    @pytest.mark.skip(reason="Loader not yet implemented")
    def test_detect_jsonl(self, chatml_dataset_path: Path) -> None:
        fmt = detect_format(chatml_dataset_path)
        assert fmt is not None

    @pytest.mark.skip(reason="Loader not yet implemented")
    def test_detect_unknown_raises(self, tmp_path: Path) -> None:
        unknown = tmp_path / "unknown.xyz"
        unknown.write_text("not a dataset")
        with pytest.raises(FormatDetectionError):
            detect_format(unknown)


class TestLoadDataset:
    @pytest.mark.skip(reason="Loader not yet implemented")
    def test_load_chatml(self, chatml_dataset_path: Path) -> None:
        dataset = load_dataset(chatml_dataset_path)
        assert dataset.sample_count == 5

    @pytest.mark.skip(reason="Loader not yet implemented")
    def test_load_empty_raises(self, tmp_path: Path) -> None:
        empty = tmp_path / "empty.jsonl"
        empty.write_text("")
        with pytest.raises(EmptyDatasetError):
            load_dataset(empty)
