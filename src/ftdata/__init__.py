"""ftdata — Profile and validate LLM fine-tuning datasets."""

__version__ = "0.1.0"

from ftdata.core.models import (
    Dataset,
    DatasetFormat,
    DedupResult,
    DiversityResult,
    ProfileReport,
    ProfileResult,
    QualityIssue,
    QualityResult,
    Sample,
)
from ftdata.exceptions import FtdataError

__all__ = [
    "Dataset",
    "DatasetFormat",
    "DedupResult",
    "DiversityResult",
    "FtdataError",
    "ProfileReport",
    "ProfileResult",
    "QualityIssue",
    "QualityResult",
    "Sample",
    "__version__",
]
