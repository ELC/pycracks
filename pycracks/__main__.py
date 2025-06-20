import logging
from pathlib import Path
from typing import Annotated, Optional

import typer
from packaging.version import parse

from . import __version__
from .logger import logger
from .pycracks import run

app = typer.Typer(add_completion=False)

TEST_COMMAND = (
    "pytest --cov --cov-report term-missing:skip-covered "
    "--cov-report xml:coverage-report.xml --junitxml=coverage.xml ./tests"
)


@app.callback(invoke_without_command=True)
def main(  # pylint: disable=too-many-positional-arguments
    test_command: Annotated[
        str, typer.Option("--test-command", "-c", help="Command that runs the test")
    ] = TEST_COMMAND,
    paths: Annotated[
        Optional[list[str]], typer.Option("--path", "-p", help="Paths to checkout")
    ] = None,
    target_version: Annotated[
        str, typer.Option("--target-version", "-t", help="Version to release")
    ] = "1.0.0",
    version: Annotated[
        bool, typer.Option("--version", "-V", help="Shows the version of pycracks")
    ] = False,
    verbose: Annotated[
        bool, typer.Option("--verbose", "-v", help="Print INFO logging statements")
    ] = False,
    extra_verbose: Annotated[
        bool, typer.Option("-vv", help="Print DEBUG logging statements")
    ] = False,
) -> None:
    if not paths:
        paths = ["tests"]

    if version:
        typer.echo(__version__)
        raise typer.Exit

    if verbose:
        logging.basicConfig(level=logging.INFO)

    if extra_verbose:
        logging.basicConfig(level=logging.DEBUG)

    parsed_target_version = parse(target_version)
    paths_ = (Path(path) for path in paths)

    run_succeded = run(test_command, paths_, parsed_target_version)

    if not run_succeded:
        logger.error("Breaking Changes detected and major not updated")
        raise typer.Exit(code=1)

    logger.info("No incompatibilities between changes and version")
    raise typer.Exit


if __name__ == "__main__":
    app()
