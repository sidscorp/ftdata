"""Custom exception hierarchy for ftdata."""


class FtdataError(Exception):
    """Base exception for all ftdata errors."""


class DatasetLoadError(FtdataError):
    """Failed to load or parse a dataset file."""

    def __init__(self, path: str, reason: str) -> None:
        self.path = path
        self.reason = reason
        super().__init__(f"Failed to load {path}: {reason}")


class FormatDetectionError(FtdataError):
    """Cannot auto-detect dataset format."""

    def __init__(self, path: str) -> None:
        self.path = path
        super().__init__(f"Cannot detect format for {path}")


class UnsupportedFormatError(FtdataError):
    """Dataset format not supported."""

    def __init__(self, format_name: str) -> None:
        self.format_name = format_name
        super().__init__(f"Unsupported format: {format_name}")


class EmptyDatasetError(FtdataError):
    """Dataset contains no samples."""

    def __init__(self, path: str) -> None:
        self.path = path
        super().__init__(f"Dataset is empty: {path}")


class SemanticUnavailableError(FtdataError):
    """Semantic analysis features not available (missing optional deps)."""

    def __init__(self) -> None:
        super().__init__(
            "Semantic features require the [semantic] extra: pip install ftdata[semantic]"
        )


class LLMUnavailableError(FtdataError):
    """LLM-as-judge features not available (missing optional deps)."""

    def __init__(self) -> None:
        super().__init__("LLM judge features require the [llm] extra: pip install ftdata[llm]")


class BenchmarkNotFoundError(FtdataError):
    """Unknown benchmark name."""

    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(f"Unknown benchmark: {name}")


class ConfigError(FtdataError):
    """Invalid or missing configuration."""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(f"Configuration error: {reason}")
