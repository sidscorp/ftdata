"""Benchmark registry and pre-computed data."""

BENCHMARK_REGISTRY: dict[str, str] = {
    "mmlu": "Massive Multitask Language Understanding",
    "hellaswag": "HellaSwag commonsense reasoning",
    "arc": "AI2 Reasoning Challenge",
    "truthfulqa": "TruthfulQA",
    "gsm8k": "Grade School Math 8K",
    "humaneval": "HumanEval code generation",
}


def get_benchmark_names() -> list[str]:
    """Return list of available benchmark names.

    Returns:
        List of registered benchmark names.
    """
    return list(BENCHMARK_REGISTRY.keys())


def load_benchmark_data(name: str) -> list[str]:
    """Load pre-computed benchmark test set data for n-gram comparison.

    Args:
        name: Benchmark name from registry.

    Returns:
        List of benchmark test strings.

    Raises:
        BenchmarkNotFoundError: If benchmark name is unknown.
    """
    raise NotImplementedError
