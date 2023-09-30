import json
from pathlib import Path
import typer

from .utils import success_print, failure_print, info_print

_APP_NAME = "skill-plotter"
_app_dir = typer.get_app_dir(_APP_NAME)
# if the dir does not exist, create it
if not Path(_app_dir).exists():
    Path(_app_dir).mkdir(parents=True)
DEFAULT_SKILL_FILE_NAME = "skills"


def _get_target_file(file_name: str = DEFAULT_SKILL_FILE_NAME) -> Path:
    """Returns the target file path."""
    return Path(_app_dir) / f"{file_name}.json"


def read_file(file_name: str = DEFAULT_SKILL_FILE_NAME) -> dict[str, float]:
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


def remove_skill(skill: str, file_name: str = DEFAULT_SKILL_FILE_NAME):
    """Removes the skill from the skill list."""
    data = read_file(file_name)
    if skill in data:
        del data[skill]
        write_file(data, file_name)
        success_print(f"Removed skill {skill}")
    else:
        failure_print(f"Skill {skill} not found")


def add_skill(skill: str, level: float, file_name: str = DEFAULT_SKILL_FILE_NAME):
    """Adds the skill to the skill list.
    If it already exists, the level will be overwritten.
    """
    data = read_file(file_name)
    data[skill] = level
    write_file(data, file_name)
    success_print(f"Added skill {skill} with level {level}")


def list_all_groups():
    """Search the app dir for all existing groups and print them.
    Valid files are json ones"""
    files = Path(_app_dir).glob("*.json")
    info_print("Existing groups:")
    for file in files:
        file_name = file.stem
        suffix = "" if file_name != DEFAULT_SKILL_FILE_NAME else " (default)"
        typer.echo(f"- {file.stem}{suffix}")


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
