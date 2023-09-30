# pylint: disable=unused-argument

from typing import Optional, Annotated
from enum import Enum
import typer

from .utils import version_callback
from .preparator import DEFAULT_SKILL_FILE_NAME
from .plotter import generate_skill_picture, BLUE, DARK_GRAY
from . import preparator

app = typer.Typer()


class PictureTypes(str, Enum):
    """Save file types."""

    SVG = "svg"
    PNG = "png"
    JPG = "jpg"


_SKILL_GROUP_ARG = Annotated[str, typer.Option("--skill-group", "-g", help="Use to build different skill groups")]


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    file_type: Annotated[
        PictureTypes, typer.Option("--file-type", "-t", help="File type of the output file")
    ] = PictureTypes.SVG,
    save_name: Annotated[str, typer.Option("--file-name", "-n", help="Name of the output file")] = "skills",
    skill_group: _SKILL_GROUP_ARG = DEFAULT_SKILL_FILE_NAME,
    columns: Annotated[int, typer.Option("--columns", "-c", help="Number of columns", min=1, max=10)] = 2,
    bar_height: Annotated[float, typer.Option("--bar-height", help="Height of the bar", min=0, max=1)] = 0.6,
    background_height: Annotated[
        float, typer.Option("--bg-heigh", help="Height of the bars background", min=0, max=1)
    ] = 0.7,
    bar_color: Annotated[str, typer.Option("--bar-color", help="Color of the bar", min=0, max=1)] = BLUE,
    background_color: Annotated[
        str, typer.Option("--bg-color", help="Color of the bars background", min=0, max=1)
    ] = DARK_GRAY,
    font_color: Annotated[str, typer.Option("--font-color", help="Color of the font", min=0, max=1)] = DARK_GRAY,
    version: Annotated[Optional[bool], typer.Option("--version", "-V", callback=version_callback)] = None,
):
    """
    Plots the set skills to a svg file.
    Can also be used to manage, edit and delete skills.
    You can also define different skill groups, which are handled separately.
    """
    if ctx.invoked_subcommand is not None:
        return
    typer.echo(f"Using <{skill_group}> skill group")
    typer.echo(f"Plotting skills to {save_name}.{file_type}")
    data = preparator.read_file(skill_group)
    typer.echo(data)
    generate_skill_picture(
        data, columns, save_name, file_type, bar_height,
        background_height, background_color, bar_color, font_color
    )


@app.command()
def add(
    skill: Annotated[str, typer.Argument(help="Name of the skill to add")],
    level: Annotated[float, typer.Argument(help="Level of the skill, between 0 and 10", min=0, max=10)],
    skill_group: _SKILL_GROUP_ARG = DEFAULT_SKILL_FILE_NAME,
):
    """
    Adds the skill to the skill list.
    If it already exists, the level will be overwritten.
    """
    preparator.add_skill(skill, level, skill_group)


@app.command()
def remove(
    skill: Annotated[str, typer.Argument(help="Name of the skill to remove")],
    skill_group: _SKILL_GROUP_ARG = DEFAULT_SKILL_FILE_NAME,
):
    """
    Removes the skill from the skill list
    """
    preparator.remove_skill(skill, skill_group)


@app.command()
def list_groups():
    """
    Show all existing groups
    """
    preparator.list_all_groups()


# command to delete groups
@app.command()
def delete_group(
    group: Annotated[str, typer.Argument(help="Name of group to delete")],
):
    """
    Delete a group
    """
    preparator.delete_group(group)
