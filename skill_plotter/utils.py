"""Module for utility functions and constants."""

import typer
from . import __version__


def version_callback(value: bool):
    """
    Callback for the --version option.
    """
    if value:
        typer.echo(f"skill-plotter, version {__version__}")
        typer.echo("For further usage, type: skill-plotter --help")
        typer.echo(r"Or visit https://skillplotter.readthedocs.io/usage/")
        raise typer.Exit()


def c_print(text: str, color: str = typer.colors.WHITE):
    """
    Prints the given text in the given color.
    """
    typer.echo(typer.style(text, fg=color))


def success_print(text: str):
    """
    Prints the given text in green.
    """
    c_print(text, typer.colors.GREEN)


def failure_print(text: str):
    """
    Prints the given text in red.
    """
    c_print(text, typer.colors.RED)


def info_print(text: str):
    """
    Prints the given text in blue.
    """
    c_print(text, typer.colors.BLUE)
