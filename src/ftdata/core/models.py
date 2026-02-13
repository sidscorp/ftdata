"""All Pydantic data models for ftdata.

This is the foundation module. Every other module imports from here,
never the reverse. All models are in one file to prevent circular imports.
"""

from __future__ import annotations

import hashlib
from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, computed_field, field_validator

# --- Enums ---


class DatasetFormat(str, Enum):
    """Supported fine-tuning dataset formats."""

    CHATML = "chatml"
    ALPACA = "alpaca"
    SHAREGPT = "sharegpt"
    JSONL_MESSAGES = "jsonl_messages"
    PARQUET = "parquet"
    HF_DATASET = "hf_dataset"


class QualitySeverity(str, Enum):
    """Severity levels for quality findings."""

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class QualityRule(str, Enum):
    """Built-in quality check rules."""

    FT001 = "FT001"  # Empty response
    FT002 = "FT002"  # Truncated content
    FT003 = "FT003"  # Encoding error
    FT004 = "FT004"  # Format error
    FT005 = "FT005"  # Excessive length
    FT006 = "FT006"  # Short response
    FT007 = "FT007"  # High repetition
    FT008 = "FT008"  # Language mismatch
    FT009 = "FT009"  # PII detected
    FT010 = "FT010"  # Imbalanced turns
    FT011 = "FT011"  # Missing system message
    FT012 = "FT012"  # Low diversity


class DedupMethod(str, Enum):
    """Deduplication methods."""

    EXACT = "exact"
    MINHASH = "minhash"
    SEMANTIC = "semantic"


# --- Core Data Models ---


class Message(BaseModel):
    """A single message within a training sample."""

    role: str
    content: str


class Sample(BaseModel):
    """A single training example."""

    messages: list[Message] = Field(default_factory=list)
    format: DatasetFormat = DatasetFormat.CHATML
    raw_content: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)
    index: int = 0

    @computed_field  # type: ignore[prop-decorator]
    @property
    def content_hash(self) -> str:
        """SHA-256 hash of the raw content for dedup."""
        return hashlib.sha256(self.raw_content.encode()).hexdigest()[:16]

    @computed_field  # type: ignore[prop-decorator]
    @property
    def turn_count(self) -> int:
        """Number of messages in this sample."""
        return len(self.messages)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def has_system(self) -> bool:
        """Whether this sample has a system message."""
        return any(m.role == "system" for m in self.messages)


class Dataset(BaseModel):
    """A collection of training samples."""

    samples: list[Sample] = Field(default_factory=list)
    format: DatasetFormat = DatasetFormat.CHATML
    path: Path | None = None

    @computed_field  # type: ignore[prop-decorator]
    @property
    def sample_count(self) -> int:
        """Total number of samples."""
        return len(self.samples)


# --- Profiling Models ---


class TokenStats(BaseModel):
    """Token count distribution statistics."""

    min: int = 0
    max: int = 0
    mean: float = 0.0
    median: float = 0.0
    p95: float = 0.0
    p99: float = 0.0
    total: int = 0


class LengthProfile(BaseModel):
    """Token length statistics for prompt/response/total."""

    prompt_tokens: TokenStats = Field(default_factory=TokenStats)
    response_tokens: TokenStats = Field(default_factory=TokenStats)
    total_tokens: TokenStats = Field(default_factory=TokenStats)


class TurnProfile(BaseModel):
    """Turn count distribution statistics."""

    min: int = 0
    max: int = 0
    mean: float = 0.0
    median: float = 0.0


class VocabProfile(BaseModel):
    """Vocabulary statistics."""

    unique_tokens: int = 0
    type_token_ratio: float = 0.0
    top_tokens: list[tuple[str, int]] = Field(default_factory=list)


class LanguageProfile(BaseModel):
    """Detected language distribution."""

    languages: dict[str, int] = Field(default_factory=dict)
    primary_language: str | None = None
    primary_percentage: float = 0.0


class ProfileResult(BaseModel):
    """Aggregate profiling result."""

    length: LengthProfile = Field(default_factory=LengthProfile)
    turns: TurnProfile = Field(default_factory=TurnProfile)
    vocab: VocabProfile = Field(default_factory=VocabProfile)
    language: LanguageProfile = Field(default_factory=LanguageProfile)
    sample_count: int = 0
    total_tokens: int = 0


# --- Dedup Models ---


class DuplicateCluster(BaseModel):
    """A cluster of duplicate or near-duplicate samples."""

    indices: list[int] = Field(default_factory=list)
    similarity: float = 1.0
    method: DedupMethod = DedupMethod.EXACT


class DedupResult(BaseModel):
    """Deduplication analysis result."""

    clusters: list[DuplicateCluster] = Field(default_factory=list)
    total_duplicates: int = 0
    duplicate_percentage: float = 0.0

    @computed_field  # type: ignore[prop-decorator]
    @property
    def estimated_savings(self) -> int:
        """Estimated number of samples that can be removed."""
        return sum(len(c.indices) - 1 for c in self.clusters if len(c.indices) > 1)


# --- Quality Models ---


class QualityIssue(BaseModel):
    """A single quality finding."""

    rule: QualityRule
    severity: QualitySeverity
    message: str
    sample_index: int
    details: dict[str, Any] = Field(default_factory=dict)


class QualityResult(BaseModel):
    """Aggregate quality check results."""

    issues: list[QualityIssue] = Field(default_factory=list)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def error_count(self) -> int:
        """Number of error-severity issues."""
        return sum(1 for i in self.issues if i.severity == QualitySeverity.ERROR)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def warning_count(self) -> int:
        """Number of warning-severity issues."""
        return sum(1 for i in self.issues if i.severity == QualitySeverity.WARNING)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def passed(self) -> bool:
        """Whether the dataset passed quality checks (no errors)."""
        return self.error_count == 0


# --- Contamination Models ---


class BenchmarkMatch(BaseModel):
    """A match between a sample and a benchmark test set."""

    benchmark_name: str
    sample_index: int
    overlap_score: float = Field(ge=0.0, le=1.0)
    matched_text: str = ""


class ContaminationResult(BaseModel):
    """Contamination analysis result."""

    matches: list[BenchmarkMatch] = Field(default_factory=list)
    benchmark_summary: dict[str, int] = Field(default_factory=dict)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def is_contaminated(self) -> bool:
        """Whether any contamination was detected."""
        return len(self.matches) > 0


# --- Diversity Models ---


class TopicCluster(BaseModel):
    """A topic cluster from embedding-based analysis."""

    label: str = ""
    sample_indices: list[int] = Field(default_factory=list)
    centroid_summary: str = ""


class DiversityResult(BaseModel):
    """Diversity analysis result."""

    clusters: list[TopicCluster] = Field(default_factory=list)
    diversity_score: float = 0.0
    topic_distribution: dict[str, float] = Field(default_factory=dict)


# --- Report Model ---


class ProfileReport(BaseModel):
    """Aggregates all analysis results into a single report."""

    dataset_path: str = ""
    dataset_format: DatasetFormat = DatasetFormat.CHATML
    sample_count: int = 0
    profile: ProfileResult = Field(default_factory=ProfileResult)
    dedup: DedupResult | None = None
    quality: QualityResult | None = None
    contamination: ContaminationResult | None = None
    diversity: DiversityResult | None = None

    @computed_field  # type: ignore[prop-decorator]
    @property
    def summary(self) -> dict[str, Any]:
        """Summary dict of key metrics."""
        result: dict[str, Any] = {
            "path": self.dataset_path,
            "format": self.dataset_format.value,
            "samples": self.sample_count,
            "total_tokens": self.profile.total_tokens,
        }
        if self.dedup is not None:
            result["duplicates"] = self.dedup.total_duplicates
        if self.quality is not None:
            result["quality_errors"] = self.quality.error_count
            result["quality_warnings"] = self.quality.warning_count
        if self.contamination is not None:
            result["contaminated"] = self.contamination.is_contaminated
        if self.diversity is not None:
            result["diversity_score"] = self.diversity.diversity_score
        return result

    @field_validator("sample_count")
    @classmethod
    def validate_sample_count(cls, v: int) -> int:
        """Sample count must be non-negative."""
        if v < 0:
            msg = "sample_count must be non-negative"
            raise ValueError(msg)
        return v
