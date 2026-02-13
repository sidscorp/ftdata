"""Integration tests for the CLI."""

from __future__ import annotations

from click.testing import CliRunner

from ftdata.cli import cli


class TestCli:
    def test_help(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Profile and validate" in result.output

    def test_version(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "0.1.0" in result.output

    def test_profile_stub(self, minimal_dataset_path: str) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["profile", str(minimal_dataset_path)])
        assert "Not yet implemented" in result.output

    def test_check_stub(self, minimal_dataset_path: str) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["check", str(minimal_dataset_path)])
        assert "Not yet implemented" in result.output

    def test_dedup_stub(self, minimal_dataset_path: str) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["dedup", str(minimal_dataset_path)])
        assert "Not yet implemented" in result.output

    def test_stats_stub(self, minimal_dataset_path: str) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["stats", str(minimal_dataset_path)])
        assert "Not yet implemented" in result.output

    def test_contamination_stub(self, minimal_dataset_path: str) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["contamination", str(minimal_dataset_path)])
        assert "Not yet implemented" in result.output

    def test_diversity_stub(self, minimal_dataset_path: str) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["diversity", str(minimal_dataset_path)])
        assert "Not yet implemented" in result.output

    def test_report_stub(self, minimal_dataset_path: str) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["report", str(minimal_dataset_path)])
        assert "Not yet implemented" in result.output

    def test_init_stub(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["init"])
        assert "Not yet implemented" in result.output
