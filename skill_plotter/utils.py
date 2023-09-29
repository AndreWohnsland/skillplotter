"""Module for utility functions and constants."""

import typer

__version__ = "0.1.0"


def version_callback(value: bool):
    """
    Callback for the --version option.
    """
    if value:
        typer.echo(f"skill-plotter, version {__version__}")
        raise typer.Exit()
