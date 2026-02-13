"""Dataset format detection and loading."""

from __future__ import annotations

from pathlib import Path

from ftdata.core.models import Dataset, DatasetFormat


def detect_format(path: Path) -> DatasetFormat:
    """Auto-detect the format of a dataset file.

    Examines file extension and content structure to determine format.

    Args:
        path: Path to the dataset file.

    Returns:
        Detected DatasetFormat.

    Raises:
        FormatDetectionError: If format cannot be determined.
    """
    raise NotImplementedError


def load_dataset(path: Path, format: DatasetFormat | None = None) -> Dataset:
    """Load a dataset from file, optionally specifying format.

    If format is None, auto-detection is attempted.

    Args:
        path: Path to the dataset file.
        format: Optional explicit format.

    Returns:
        Loaded Dataset with normalized samples.

    Raises:
        DatasetLoadError: If loading fails.
        EmptyDatasetError: If dataset has no samples.
    """
    raise NotImplementedError
