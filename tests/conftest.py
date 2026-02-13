"""Shared test fixtures and auto-markers."""

from __future__ import annotations

from pathlib import Path

import pytest

from ftdata.config import FtdataConfig
from ftdata.core.models import Dataset, DatasetFormat, Message, Sample

FIXTURES_DIR = Path(__file__).parent / "fixtures" / "datasets"


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Auto-apply markers based on test directory."""
    for item in items:
        test_path = str(item.fspath)
        if "/unit/" in test_path:
            item.add_marker(pytest.mark.unit)
        elif "/integration/" in test_path:
            item.add_marker(pytest.mark.integration)
        elif "/e2e/" in test_path:
            item.add_marker(pytest.mark.e2e)


@pytest.fixture
def fixtures_dir() -> Path:
    """Path to the test fixtures/datasets directory."""
    return FIXTURES_DIR


@pytest.fixture
def minimal_dataset_path() -> Path:
    """Path to the minimal test dataset fixture."""
    return FIXTURES_DIR / "minimal.jsonl"


@pytest.fixture
def chatml_dataset_path() -> Path:
    """Path to the simple ChatML test dataset."""
    return FIXTURES_DIR / "simple_chatml.jsonl"


@pytest.fixture
def alpaca_dataset_path() -> Path:
    """Path to the simple Alpaca test dataset."""
    return FIXTURES_DIR / "simple_alpaca.jsonl"


@pytest.fixture
def duplicates_dataset_path() -> Path:
    """Path to the dataset with duplicates."""
    return FIXTURES_DIR / "with_duplicates.jsonl"


@pytest.fixture
def quality_issues_dataset_path() -> Path:
    """Path to the dataset with quality issues."""
    return FIXTURES_DIR / "quality_issues.jsonl"


@pytest.fixture
def default_config() -> FtdataConfig:
    """Default FtdataConfig for testing."""
    return FtdataConfig()


@pytest.fixture
def sample_message() -> Message:
    """A sample Message for testing."""
    return Message(role="user", content="Hello, world!")


@pytest.fixture
def sample_sample() -> Sample:
    """A sample Sample for testing."""
    return Sample(
        messages=[
            Message(role="system", content="You are a helpful assistant."),
            Message(role="user", content="What is 2+2?"),
            Message(role="assistant", content="2+2 equals 4."),
        ],
        format=DatasetFormat.CHATML,
        raw_content='{"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is 2+2?"}, {"role": "assistant", "content": "2+2 equals 4."}]}',
        index=0,
    )


@pytest.fixture
def sample_dataset(sample_sample: Sample) -> Dataset:
    """A sample Dataset for testing."""
    return Dataset(
        samples=[sample_sample],
        format=DatasetFormat.CHATML,
        path=FIXTURES_DIR / "minimal.jsonl",
    )
