"""Tests for core Pydantic data models."""

from __future__ import annotations

from pathlib import Path

import pytest

from ftdata.core.models import (
    BenchmarkMatch,
    ContaminationResult,
    Dataset,
    DatasetFormat,
    DedupMethod,
    DedupResult,
    DiversityResult,
    DuplicateCluster,
    LanguageProfile,
    LengthProfile,
    Message,
    ProfileReport,
    ProfileResult,
    QualityIssue,
    QualityResult,
    QualityRule,
    QualitySeverity,
    Sample,
    TokenStats,
    TopicCluster,
    TurnProfile,
    VocabProfile,
)


class TestMessage:
    def test_creation(self) -> None:
        msg = Message(role="user", content="Hello!")
        assert msg.role == "user"
        assert msg.content == "Hello!"

    def test_system_message(self) -> None:
        msg = Message(role="system", content="You are helpful.")
        assert msg.role == "system"


class TestSample:
    def test_minimal(self) -> None:
        sample = Sample()
        assert sample.messages == []
        assert sample.format == DatasetFormat.CHATML
        assert sample.index == 0

    def test_content_hash_deterministic(self) -> None:
        s1 = Sample(raw_content="hello world")
        s2 = Sample(raw_content="hello world")
        assert s1.content_hash == s2.content_hash

    def test_content_hash_changes(self) -> None:
        s1 = Sample(raw_content="version 1")
        s2 = Sample(raw_content="version 2")
        assert s1.content_hash != s2.content_hash

    def test_turn_count(self) -> None:
        sample = Sample(
            messages=[
                Message(role="user", content="Hi"),
                Message(role="assistant", content="Hello!"),
            ]
        )
        assert sample.turn_count == 2

    def test_turn_count_empty(self) -> None:
        sample = Sample()
        assert sample.turn_count == 0

    def test_has_system_true(self) -> None:
        sample = Sample(
            messages=[
                Message(role="system", content="You are helpful."),
                Message(role="user", content="Hi"),
            ]
        )
        assert sample.has_system is True

    def test_has_system_false(self) -> None:
        sample = Sample(
            messages=[
                Message(role="user", content="Hi"),
                Message(role="assistant", content="Hello!"),
            ]
        )
        assert sample.has_system is False


class TestDataset:
    def test_empty(self) -> None:
        ds = Dataset()
        assert ds.sample_count == 0
        assert ds.samples == []

    def test_with_samples(self) -> None:
        ds = Dataset(
            samples=[Sample(), Sample(), Sample()],
            format=DatasetFormat.ALPACA,
        )
        assert ds.sample_count == 3
        assert ds.format == DatasetFormat.ALPACA

    def test_path(self) -> None:
        ds = Dataset(path=Path("/tmp/data.jsonl"))
        assert ds.path == Path("/tmp/data.jsonl")


class TestTokenStats:
    def test_defaults(self) -> None:
        stats = TokenStats()
        assert stats.min == 0
        assert stats.max == 0
        assert stats.mean == 0.0
        assert stats.total == 0

    def test_custom(self) -> None:
        stats = TokenStats(
            min=10, max=500, mean=150.5, median=120.0, p95=400.0, p99=480.0, total=15050
        )
        assert stats.p95 == 400.0


class TestLengthProfile:
    def test_defaults(self) -> None:
        profile = LengthProfile()
        assert isinstance(profile.prompt_tokens, TokenStats)
        assert isinstance(profile.response_tokens, TokenStats)
        assert isinstance(profile.total_tokens, TokenStats)


class TestTurnProfile:
    def test_defaults(self) -> None:
        profile = TurnProfile()
        assert profile.min == 0
        assert profile.mean == 0.0


class TestVocabProfile:
    def test_defaults(self) -> None:
        profile = VocabProfile()
        assert profile.unique_tokens == 0
        assert profile.type_token_ratio == 0.0
        assert profile.top_tokens == []


class TestLanguageProfile:
    def test_defaults(self) -> None:
        profile = LanguageProfile()
        assert profile.languages == {}
        assert profile.primary_language is None

    def test_with_data(self) -> None:
        profile = LanguageProfile(
            languages={"en": 80, "fr": 20},
            primary_language="en",
            primary_percentage=80.0,
        )
        assert profile.primary_language == "en"


class TestProfileResult:
    def test_defaults(self) -> None:
        result = ProfileResult()
        assert result.sample_count == 0
        assert result.total_tokens == 0
        assert isinstance(result.length, LengthProfile)


class TestDuplicateCluster:
    def test_defaults(self) -> None:
        cluster = DuplicateCluster()
        assert cluster.indices == []
        assert cluster.similarity == 1.0
        assert cluster.method == DedupMethod.EXACT

    def test_custom(self) -> None:
        cluster = DuplicateCluster(
            indices=[0, 3, 7],
            similarity=0.95,
            method=DedupMethod.MINHASH,
        )
        assert len(cluster.indices) == 3


class TestDedupResult:
    def test_empty(self) -> None:
        result = DedupResult()
        assert result.estimated_savings == 0

    def test_estimated_savings(self) -> None:
        result = DedupResult(
            clusters=[
                DuplicateCluster(indices=[0, 1]),
                DuplicateCluster(indices=[3, 4, 5]),
            ],
            total_duplicates=3,
        )
        assert result.estimated_savings == 3  # (2-1) + (3-1)


class TestQualityIssue:
    def test_creation(self) -> None:
        issue = QualityIssue(
            rule=QualityRule.FT001,
            severity=QualitySeverity.ERROR,
            message="Empty response",
            sample_index=5,
        )
        assert issue.rule == QualityRule.FT001
        assert issue.severity == QualitySeverity.ERROR
        assert issue.sample_index == 5


class TestQualityResult:
    def test_empty_passes(self) -> None:
        result = QualityResult()
        assert result.passed is True
        assert result.error_count == 0
        assert result.warning_count == 0

    def test_with_errors(self) -> None:
        result = QualityResult(
            issues=[
                QualityIssue(
                    rule=QualityRule.FT001,
                    severity=QualitySeverity.ERROR,
                    message="Empty response",
                    sample_index=0,
                ),
                QualityIssue(
                    rule=QualityRule.FT007,
                    severity=QualitySeverity.WARNING,
                    message="High repetition",
                    sample_index=1,
                ),
            ]
        )
        assert result.error_count == 1
        assert result.warning_count == 1
        assert result.passed is False

    def test_warnings_only_passes(self) -> None:
        result = QualityResult(
            issues=[
                QualityIssue(
                    rule=QualityRule.FT007,
                    severity=QualitySeverity.WARNING,
                    message="High repetition",
                    sample_index=0,
                ),
            ]
        )
        assert result.passed is True
        assert result.warning_count == 1


class TestBenchmarkMatch:
    def test_creation(self) -> None:
        match = BenchmarkMatch(
            benchmark_name="mmlu",
            sample_index=42,
            overlap_score=0.85,
            matched_text="some text",
        )
        assert match.benchmark_name == "mmlu"
        assert match.overlap_score == 0.85

    def test_score_bounds(self) -> None:
        with pytest.raises(ValueError):
            BenchmarkMatch(benchmark_name="x", sample_index=0, overlap_score=1.5)
        with pytest.raises(ValueError):
            BenchmarkMatch(benchmark_name="x", sample_index=0, overlap_score=-0.1)


class TestContaminationResult:
    def test_empty_not_contaminated(self) -> None:
        result = ContaminationResult()
        assert result.is_contaminated is False

    def test_with_matches(self) -> None:
        result = ContaminationResult(
            matches=[
                BenchmarkMatch(benchmark_name="mmlu", sample_index=0, overlap_score=0.9),
            ]
        )
        assert result.is_contaminated is True


class TestTopicCluster:
    def test_creation(self) -> None:
        cluster = TopicCluster(
            label="coding",
            sample_indices=[0, 1, 2],
            centroid_summary="Programming topics",
        )
        assert cluster.label == "coding"
        assert len(cluster.sample_indices) == 3


class TestDiversityResult:
    def test_defaults(self) -> None:
        result = DiversityResult()
        assert result.diversity_score == 0.0
        assert result.clusters == []


class TestProfileReport:
    def test_defaults(self) -> None:
        report = ProfileReport()
        assert report.sample_count == 0
        assert report.dedup is None
        assert report.quality is None

    def test_summary(self) -> None:
        report = ProfileReport(
            dataset_path="/tmp/data.jsonl",
            dataset_format=DatasetFormat.CHATML,
            sample_count=100,
            profile=ProfileResult(total_tokens=50000),
        )
        s = report.summary
        assert s["path"] == "/tmp/data.jsonl"
        assert s["samples"] == 100
        assert s["total_tokens"] == 50000

    def test_summary_with_optional_results(self) -> None:
        report = ProfileReport(
            dataset_path="/tmp/data.jsonl",
            sample_count=100,
            dedup=DedupResult(total_duplicates=5),
            quality=QualityResult(
                issues=[
                    QualityIssue(
                        rule=QualityRule.FT001,
                        severity=QualitySeverity.ERROR,
                        message="Empty",
                        sample_index=0,
                    ),
                ]
            ),
        )
        s = report.summary
        assert s["duplicates"] == 5
        assert s["quality_errors"] == 1

    def test_sample_count_validation(self) -> None:
        with pytest.raises(ValueError, match="sample_count"):
            ProfileReport(sample_count=-1)


class TestEnums:
    def test_dataset_format_values(self) -> None:
        assert DatasetFormat.CHATML == "chatml"
        assert DatasetFormat.ALPACA == "alpaca"
        assert DatasetFormat.SHAREGPT == "sharegpt"
        assert DatasetFormat.PARQUET == "parquet"

    def test_quality_severity_values(self) -> None:
        assert QualitySeverity.INFO == "info"
        assert QualitySeverity.WARNING == "warning"
        assert QualitySeverity.ERROR == "error"

    def test_quality_rule_values(self) -> None:
        assert QualityRule.FT001 == "FT001"
        assert QualityRule.FT012 == "FT012"

    def test_dedup_method_values(self) -> None:
        assert DedupMethod.EXACT == "exact"
        assert DedupMethod.MINHASH == "minhash"
        assert DedupMethod.SEMANTIC == "semantic"
