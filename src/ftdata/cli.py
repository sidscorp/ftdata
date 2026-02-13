"""Click CLI for ftdata."""

from __future__ import annotations

import click
from rich.console import Console

from ftdata import __version__

console = Console()


class Context:
    """Shared CLI context."""

    def __init__(
        self,
        config_path: str | None = None,
        quiet: bool = False,
        json_output: bool = False,
    ) -> None:
        self.config_path = config_path
        self.quiet = quiet
        self.json_output = json_output
        self.console = Console(quiet=quiet)


pass_context = click.make_pass_decorator(Context, ensure=True)


@click.group()
@click.option("--config", "config_path", type=click.Path(), help="Path to .ftdata.yaml")
@click.option("--quiet", "-q", is_flag=True, help="Suppress non-essential output")
@click.option("--json", "json_output", is_flag=True, help="Output as JSON")
@click.version_option(version=__version__, prog_name="ftdata")
@click.pass_context
def cli(
    ctx: click.Context,
    config_path: str | None,
    quiet: bool,
    json_output: bool,
) -> None:
    """Profile and validate LLM fine-tuning datasets."""
    ctx.ensure_object(Context)
    ctx.obj = Context(config_path=config_path, quiet=quiet, json_output=json_output)


@cli.command()
@click.argument("path", type=click.Path(exists=True))
@pass_context
def profile(ctx: Context, path: str) -> None:
    """Full profiling report for a dataset."""
    ctx.console.print("[yellow]Not yet implemented[/yellow]")


@cli.command()
@click.argument("path", type=click.Path(exists=True))
@pass_context
def stats(ctx: Context, path: str) -> None:
    """Quick statistical summary of a dataset."""
    ctx.console.print("[yellow]Not yet implemented[/yellow]")


@cli.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), help="Output path for cleaned dataset")
@click.option(
    "--method",
    type=click.Choice(["exact", "minhash", "semantic"]),
    default="exact",
    help="Deduplication method",
)
@pass_context
def dedup(ctx: Context, path: str, output: str | None, method: str) -> None:
    """Deduplication analysis."""
    ctx.console.print("[yellow]Not yet implemented[/yellow]")


@cli.command()
@click.argument("path", type=click.Path(exists=True))
@pass_context
def check(ctx: Context, path: str) -> None:
    """Run quality checks on a dataset."""
    ctx.console.print("[yellow]Not yet implemented[/yellow]")


@cli.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--benchmark", "-b", multiple=True, help="Specific benchmarks to check against")
@pass_context
def contamination(ctx: Context, path: str, benchmark: tuple[str, ...]) -> None:
    """Check for benchmark contamination."""
    ctx.console.print("[yellow]Not yet implemented[/yellow]")


@cli.command()
@click.argument("path", type=click.Path(exists=True))
@pass_context
def diversity(ctx: Context, path: str) -> None:
    """Analyze topic diversity and clustering."""
    ctx.console.print("[yellow]Not yet implemented[/yellow]")


@cli.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), help="Output path for HTML report")
@pass_context
def report(ctx: Context, path: str, output: str | None) -> None:
    """Generate an HTML report."""
    ctx.console.print("[yellow]Not yet implemented[/yellow]")


@cli.command()
@pass_context
def init(ctx: Context) -> None:
    """Create a .ftdata.yaml configuration file."""
    ctx.console.print("[yellow]Not yet implemented[/yellow]")
