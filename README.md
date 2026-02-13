# ftdata

Profile and validate LLM fine-tuning datasets.

## Install

```bash
pip install -e ".[dev]"
```

For semantic dedup and clustering (optional):

```bash
pip install -e ".[semantic]"
```

For LLM-as-judge scoring (optional):

```bash
pip install -e ".[llm]"
```

## Usage

```bash
ftdata --help
ftdata profile data.jsonl
ftdata check data.jsonl
ftdata dedup data.jsonl
ftdata report data.jsonl
```

## Development

```bash
pytest
ruff check src/ tests/
mypy src/
```

## License

MIT
