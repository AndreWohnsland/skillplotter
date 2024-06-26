"""Module for utility functions and constants."""

from enum import Enum

import typer

from . import __version__


class PictureTypes(str, Enum):
    """Save file types."""

    SVG = "svg"
    PNG = "png"
    JPG = "jpg"
    PDF = "pdf"


class StyleTypes(str, Enum):
    """Different types of styling for the plot."""

    OUTLINE = "outline"
    ROUND = "round"
    XKCD = "xkcd"


def version_callback(value: bool):
    """Use Callback for the --version option."""
    if value:
        typer.echo(f"skill-plotter, version {__version__}")
        typer.echo("For further usage, type: skill-plotter --help")
        typer.echo(r"Or visit https://skillplotter.readthedocs.io/usage/")
        raise typer.Exit()


def c_print(text: str, color: str = typer.colors.WHITE):
    """Print the given text in the given color."""
    typer.echo(typer.style(text, fg=color))


def success_print(text: str):
    """Print the given text in green."""
    c_print(text, typer.colors.GREEN)


def failure_print(text: str):
    """Print the given text in red."""
    c_print(text, typer.colors.RED)


def info_print(text: str):
    """Print the given text in blue."""
    c_print(text, typer.colors.BLUE)
