"""Format-specific parsers that normalize to internal Sample model."""

from __future__ import annotations

from typing import Any

from ftdata.core.models import Sample


def parse_chatml(raw: dict[str, Any], index: int) -> Sample:
    """Parse a ChatML-format JSON object into a Sample.

    ChatML format: {"messages": [{"role": "...", "content": "..."}]}

    Args:
        raw: Raw JSON dict from file.
        index: Sample index in dataset.

    Returns:
        Normalized Sample.
    """
    raise NotImplementedError


def parse_alpaca(raw: dict[str, Any], index: int) -> Sample:
    """Parse an Alpaca-format JSON object into a Sample.

    Alpaca format: {"instruction": "...", "input": "...", "output": "..."}

    Args:
        raw: Raw JSON dict from file.
        index: Sample index in dataset.

    Returns:
        Normalized Sample.
    """
    raise NotImplementedError


def parse_sharegpt(raw: dict[str, Any], index: int) -> Sample:
    """Parse a ShareGPT-format JSON object into a Sample.

    ShareGPT format: {"conversations": [{"from": "...", "value": "..."}]}

    Args:
        raw: Raw JSON dict from file.
        index: Sample index in dataset.

    Returns:
        Normalized Sample.
    """
    raise NotImplementedError
