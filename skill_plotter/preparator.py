import json
from pathlib import Path
from typing import Any, Optional
import typer
import click

from .utils import success_print, failure_print, info_print

_APP_NAME = "skill-plotter"
_app_dir = typer.get_app_dir(_APP_NAME)
# if the dir does not exist, create it
if not Path(_app_dir).exists():
    Path(_app_dir).mkdir(parents=True)
DEFAULT_SKILL_FILE_NAME = "skills"
_DEFAULT_CATEGORY = "default"


def _get_target_file(file_name: str = DEFAULT_SKILL_FILE_NAME) -> Path:
    """Returns the target file path."""
    return Path(_app_dir) / f"{file_name}.json"


def split_dict_evenly(d: dict, n: int) -> list[dict]:
    """Split a dictionary into n evenly sized chunks."""
    items = list(d.items())
    chunk_size = len(items) // n
    remainder = len(items) % n
    splitted = []
    start = 0
    for i in range(n):
        end = start + chunk_size
        if i < remainder:
            end += 1
        splitted.append(dict(items[start:end]))
        start = end
    # append empty element if it is not evenly splitted
    max_len = len(splitted[0])
    for i in splitted:
        if len(i) < max_len:
            i[''] = 0
    return splitted


def sort_skills_by_category(skills: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Sorts the given skills by category.
    Returns a sorted dict without the categories"""
    # skills are of struct {skill: {category: str, level: float}}
    # the skills can have more attributes, but we are only interested in those both
    # sort by category and then by level
    # in addition also list the skills with default category first
    return dict(
        sorted(
            skills.items(),
            key=lambda x: (x[1]["category"] != _DEFAULT_CATEGORY, x[1]["category"], -x[1]["level"])
        )
    )


def reduce_data(data: dict[str, dict[str, Any]]) -> dict[str, float]:
    """Reduces the dict to only key and value"""
    return {k: v["level"] for k, v in data.items()}


def read_file(file_name: str = DEFAULT_SKILL_FILE_NAME) -> dict[str, dict[str, Any]]:
    """Reads the file from the given path and returns a dict.
    If the file path does not exist returns an empty dict.
    """
    skill_file = _get_target_file(file_name)
    if not skill_file.exists():
        return {}
    with open(skill_file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def write_file(data: dict, file_name: str = DEFAULT_SKILL_FILE_NAME) -> None:
    """Writes the given dict to the file path."""
    skill_file = _get_target_file(file_name)
    if not skill_file.exists():
        skill_file.touch()
    with open(skill_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


def add_skill(
    skill: str,
    level: float,
    category: str = _DEFAULT_CATEGORY,
    file_name: str = DEFAULT_SKILL_FILE_NAME
):
    """Adds the skill to the skill list.
    If it already exists, the level will be overwritten.
    """
    data = read_file(file_name)
    data[skill] = {"level": level, "category": category}
    write_file(data, file_name)
    success_print(f"Added skill {skill} with level {level}")


def interactive_add_skill(
    file_name: str = DEFAULT_SKILL_FILE_NAME,
    used_category: Optional[str] = None,
):
    """Interactively adds skills to the skill list."""
    info_print(f"Using interactive mode, use Ctrl+C to exit, skills will be added to {file_name}")
    if used_category is not None:
        info_print(f"Using category {used_category}")
    while True:
        skill = typer.prompt("Enter skill name")
        level = 0
        while level <= 0 or level > 10:
            level = typer.prompt("Enter level [0-10]", type=float)
            if level <= 0 or level > 10:
                failure_print("Level must be between 0 and 10 and not 0")
        if used_category is None:
            category = typer.prompt("Enter category", default=_DEFAULT_CATEGORY)
        else:
            category = used_category
        # this should usually not be happening, but just in case
        if not category:
            category = _DEFAULT_CATEGORY
        add_skill(skill, level, category, file_name)
        # need to reset category!
        category = None


def remove_skill(skill: str, file_name: str = DEFAULT_SKILL_FILE_NAME):
    """Removes the skill from the skill list."""
    data = read_file(file_name)
    if skill in data:
        del data[skill]
        write_file(data, file_name)
        success_print(f"Removed skill {skill}")
    else:
        failure_print(f"Skill {skill} not found")


def interactive_remove(file_name: str = DEFAULT_SKILL_FILE_NAME):
    """Interactively removes skills from the skill list."""
    info_print(f"Using interactive mode, use Ctrl+C to exit, skills will be removed from {file_name}")
    list_all_skills(file_name)
    data = read_file(file_name)
    available_skills = list(data.keys())
    while True:
        skill = typer.prompt("Enter skill name", show_choices=False, type=click.Choice(available_skills))
        remove_skill(skill, file_name)
        available_skills.remove(skill)


def delete_group(group: str):
    """Deletes the given group file (json) from the app dir
    Informs user if it was successful or not"""
    skill_file = _get_target_file(group)
    if skill_file.exists():
        skill_file.unlink()
        success_print(f"Deleted group {group}")
    else:
        failure_print(f"Group {group} not found")
        list_all_groups()


def list_all_groups():
    """Search the app dir for all existing groups and print them.
    Valid files are json ones"""
    files = Path(_app_dir).glob("*.json")
    info_print("Existing groups:")
    for file in files:
        file_name = file.stem
        suffix = "" if file_name != DEFAULT_SKILL_FILE_NAME else " (default)"
        typer.echo(f"- {file.stem}{suffix}")


def list_all_skills(group: str):
    """List all skills of the group"""
    data = read_file(group)
    if len(data) == 0:
        failure_print(f"No skills found in group {group}, it probably does not exist!")
        list_all_groups()
        return
    data = sort_skills_by_category(data)
    # create template to show data in a table, start at the end
    # and use padding to align the values like a table
    template = "|{:^20}|{:^10}|{:^20}|"
    separator = "-" * 54
    info_print(f"Skills of group {group}:")
    typer.echo(separator)
    typer.echo(template.format("Skill", "Level", "Category"))
    typer.echo(separator)
    for skill, value in data.items():
        typer.echo(template.format(skill, value["level"], value["category"]))
    typer.echo(separator)
