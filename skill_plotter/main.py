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
    PDF = "pdf"


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
    group_categories: Annotated[bool, typer.Option("--categories", help="Group by categories")] = False,
    bar_height: Annotated[float, typer.Option("--bar-height", help="Height of the bar", min=0, max=1)] = 0.6,
    background_height: Annotated[
        float, typer.Option("--bg-height", help="Height of the bars background", min=0, max=1)
    ] = 0.7,
    bar_color: Annotated[str, typer.Option("--bar-color", help="Color of the bar")] = BLUE,
    background_color: Annotated[str, typer.Option("--bg-color", help="Color of the bars background")] = DARK_GRAY,
    font_color: Annotated[str, typer.Option("--font-color", help="Color of the font")] = DARK_GRAY,
    canvas_color: Annotated[Optional[str], typer.Option(help="Color behind the plot")] = None,
    version: Annotated[Optional[bool], typer.Option("--version", "-V", callback=version_callback)] = None,
):
    """
    Plots the set skills to a svg file.
    Can also be used to manage, edit and delete skills.
    You can also define different skill groups, which are handled separately.
    Different categories help you to group your skills into blocks within the same plot.
    """
    if ctx.invoked_subcommand is not None:
        return
    typer.echo(f"Using <{skill_group}> skill group")
    typer.echo(f"Plotting skills to {save_name}.{file_type}")
    data = preparator.read_file(skill_group)
    if group_categories:
        data = preparator.sort_skills_by_category(data)
    plot_data = preparator.reduce_data(data)
    generate_skill_picture(
        plot_data, columns, save_name, file_type, bar_height,
        background_height, background_color, bar_color, font_color,
        canvas_color,
    )


@app.command()
def add(
    skill: Annotated[str, typer.Argument(help="Name of the skill to add")],
    level: Annotated[float, typer.Argument(help="Level of the skill, between 0 and 10", min=0, max=10)],
    category: Annotated[str, typer.Option("--category", "-c", help="Category, used to group by")] = "default",
    skill_group: _SKILL_GROUP_ARG = DEFAULT_SKILL_FILE_NAME,
):
    """
    Adds the skill to the skill list.
    If it already exists, the data will be overwritten.
    """
    preparator.add_skill(skill, level, category, skill_group)

# add a command to interactively add skills
# will have category and skill group as optional arguments


@app.command()
def interactive_add(
    skill_group: _SKILL_GROUP_ARG = DEFAULT_SKILL_FILE_NAME,
    category: Annotated[Optional[str], typer.Option("--category", "-c", help="Always use this category")] = None,
):
    """
    Interactively add skills to the skill list.
    If they already exist, the data will be overwritten.
    If skill group is not given, the default skill group will be used.
    If category is not given, the category will prompted for each skill.
    """
    preparator.interactive_add_skill(skill_group, category)

# Management functionality


@app.command()
def list_groups():
    """
    Show all existing groups.
    """
    preparator.list_all_groups()


@app.command()
def list_skills(
    skill_group: _SKILL_GROUP_ARG = DEFAULT_SKILL_FILE_NAME,
):
    """
    Show all skills of given group.
    """
    preparator.list_all_skills(skill_group)

# Remove functionality


@app.command()
def remove(
    skill: Annotated[str, typer.Argument(help="Name of the skill to remove")],
    skill_group: _SKILL_GROUP_ARG = DEFAULT_SKILL_FILE_NAME,
):
    """
    Removes the skill from the skill list.
    """
    preparator.remove_skill(skill, skill_group)


@app.command()
def interactive_remove(
    skill_group: _SKILL_GROUP_ARG = DEFAULT_SKILL_FILE_NAME,
):
    """
    Interactively remove skills from the skill list.
    If skill group is not given, the default skill group will be used.
    """
    preparator.interactive_remove(skill_group)


@app.command()
def delete_group(
    group: Annotated[str, typer.Argument(help="Name of group to delete")],
):
    """
    Delete a group.
    """
    preparator.delete_group(group)
