"""Tests for config discovery and loading."""

from __future__ import annotations

from pathlib import Path

from ftdata.config import (
    CONFIG_FILENAME,
    ContaminationConfig,
    DedupConfig,
    FtdataConfig,
    ProfilingConfig,
    QualityConfig,
    ReportConfig,
    discover_config,
    load_config,
)


class TestFtdataConfig:
    def test_defaults(self) -> None:
        config = FtdataConfig()
        assert config.format is None
        assert isinstance(config.profiling, ProfilingConfig)
        assert isinstance(config.dedup, DedupConfig)
        assert isinstance(config.quality, QualityConfig)
        assert isinstance(config.contamination, ContaminationConfig)
        assert isinstance(config.report, ReportConfig)

    def test_profiling_defaults(self) -> None:
        config = ProfilingConfig()
        assert config.token_encoding == "cl100k_base"
        assert config.language_detection is True

    def test_dedup_defaults(self) -> None:
        config = DedupConfig()
        assert config.method == "exact"
        assert config.minhash_threshold == 0.8
        assert config.minhash_num_perm == 128

    def test_quality_defaults(self) -> None:
        config = QualityConfig()
        assert config.disabled_rules == []
        assert config.max_response_tokens == 4096
        assert config.min_response_tokens == 1

    def test_contamination_defaults(self) -> None:
        config = ContaminationConfig()
        assert config.benchmarks == []
        assert config.ngram_size == 13

    def test_report_defaults(self) -> None:
        config = ReportConfig()
        assert config.output_format == "html"
        assert config.template_path is None

    def test_custom_config(self) -> None:
        config = FtdataConfig(
            format="alpaca",
            dedup=DedupConfig(method="minhash", minhash_threshold=0.9),
            quality=QualityConfig(disabled_rules=["FT001", "FT002"]),
        )
        assert config.format == "alpaca"
        assert config.dedup.method == "minhash"
        assert config.dedup.minhash_threshold == 0.9
        assert "FT001" in config.quality.disabled_rules


class TestDiscoverConfig:
    def test_finds_config_in_current_dir(self, tmp_path: Path) -> None:
        config_file = tmp_path / CONFIG_FILENAME
        config_file.write_text("format: chatml\n")
        result = discover_config(tmp_path)
        assert result == config_file

    def test_finds_config_in_parent(self, tmp_path: Path) -> None:
        config_file = tmp_path / CONFIG_FILENAME
        config_file.write_text("format: chatml\n")
        child = tmp_path / "sub" / "dir"
        child.mkdir(parents=True)
        result = discover_config(child)
        assert result == config_file

    def test_returns_none_when_missing(self, tmp_path: Path) -> None:
        result = discover_config(tmp_path)
        assert result is None


class TestLoadConfig:
    def test_load_from_file(self, tmp_path: Path) -> None:
        config_file = tmp_path / CONFIG_FILENAME
        config_file.write_text("format: alpaca\ndedup:\n  method: minhash\n")
        config = load_config(config_file)
        assert config.format == "alpaca"
        assert config.dedup.method == "minhash"

    def test_load_returns_defaults_when_missing(self) -> None:
        config = load_config(Path("/nonexistent/.ftdata.yaml"))
        assert config == FtdataConfig()

    def test_load_empty_file(self, tmp_path: Path) -> None:
        config_file = tmp_path / CONFIG_FILENAME
        config_file.write_text("")
        config = load_config(config_file)
        assert config == FtdataConfig()
