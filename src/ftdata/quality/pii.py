"""PII detection: emails, phones, SSNs, API keys."""

from __future__ import annotations

from ftdata.core.models import Dataset, QualityResult


def detect_pii(dataset: Dataset) -> QualityResult:
    """Scan dataset samples for personally identifiable information.

    Detects: email addresses, phone numbers, SSNs, API keys,
    and other common PII patterns.

    Args:
        dataset: Dataset to scan.

    Returns:
        QualityResult with PII findings (FT009).
    """
    raise NotImplementedError
