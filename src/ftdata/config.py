"""Configuration discovery and models for .ftdata.yaml."""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field


class ProfilingConfig(BaseModel):
    """Profiling-specific configuration."""

    token_encoding: str = "cl100k_base"
    language_detection: bool = True


class DedupConfig(BaseModel):
    """Deduplication configuration."""

    method: str = "exact"
    minhash_threshold: float = 0.8
    minhash_num_perm: int = 128


class QualityConfig(BaseModel):
    """Quality check configuration."""

    disabled_rules: list[str] = Field(default_factory=list)
    max_response_tokens: int = 4096
    min_response_tokens: int = 1


class ContaminationConfig(BaseModel):
    """Contamination check configuration."""

    benchmarks: list[str] = Field(default_factory=list)
    ngram_size: int = 13


class ReportConfig(BaseModel):
    """Report generation configuration."""

    output_format: str = "html"
    template_path: str | None = None


class FtdataConfig(BaseModel):
    """Top-level project configuration (.ftdata.yaml)."""

    format: str | None = None
    profiling: ProfilingConfig = Field(default_factory=ProfilingConfig)
    dedup: DedupConfig = Field(default_factory=DedupConfig)
    quality: QualityConfig = Field(default_factory=QualityConfig)
    contamination: ContaminationConfig = Field(default_factory=ContaminationConfig)
    report: ReportConfig = Field(default_factory=ReportConfig)


CONFIG_FILENAME = ".ftdata.yaml"


def discover_config(start: Path | None = None) -> Path | None:
    """Walk up from `start` (or CWD) looking for .ftdata.yaml.

    Returns the path to the config file, or None if not found.
    """
    current = (start or Path.cwd()).resolve()
    for directory in [current, *current.parents]:
        candidate = directory / CONFIG_FILENAME
        if candidate.is_file():
            return candidate
    return None


def load_config(path: Path | None = None) -> FtdataConfig:
    """Load configuration from a .ftdata.yaml file.

    If no path is provided, discovers config by walking up from CWD.
    Returns default config if no file is found.
    """
    if path is None:
        path = discover_config()

    if path is None or not path.is_file():
        return FtdataConfig()

    import yaml

    from ftdata.exceptions import ConfigError

    try:
        with open(path) as f:
            data = yaml.safe_load(f) or {}
        return FtdataConfig(**data)
    except Exception as e:
        raise ConfigError(f"Failed to load {path}: {e}") from e
