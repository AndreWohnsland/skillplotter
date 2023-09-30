import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from typing import Union

DARK_GRAY = "#404040"
BLUE = "#367DA2"

_COLOR = Union[str, tuple[float, float, float]]


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


def generate_diagram(
    ax: Axes,
    skills: dict,
    bar_height: float = 0.6,
    background_height: float = 0.7,
    background_color: _COLOR = DARK_GRAY,
    bar_color: _COLOR = DARK_GRAY,
    font_color: _COLOR = BLUE,
):
    """plot and styles the diagram.

    Args:
        ax (axis): axis to plot on.
        skills (dict): Dictionary with the skills and the values.
        bar_height (float): Percentage of the height of the skill bar.
        background_height (float): Percentage of the height of the background bar.
        background_color (color): Color of the background.
        bar_color (color): Color of the skill bar.
        font_color (color): Color of the font.
    """
    label = list(skills.keys())
    val = list(skills.values())
    border_width = (background_height - bar_height) / 2
    # also generates the fixed values for the background bars
    bar_max_len = 10
    filler = [bar_max_len + border_width if x != 0 else 0 for x in val]
    # and the fixed values for the front border
    border = [border_width if x != 0 else 0 for x in val]

    n_positions = range(len(skills))
    # plots the skill label
    ax.barh(n_positions, val, tick_label=label, zorder=2, height=bar_height, color=bar_color)
    # plots the background
    ax.barh(n_positions, filler, tick_label=label, zorder=1, height=background_height, color=background_color)
    # plots the front border, alternatively in the first plot there could be
    # used the "left" keyword to shift it from zero the the border
    ax.barh(n_positions, border, tick_label=label, zorder=3, height=background_height, color=background_color)
    # invert axis because last list element is on the top
    ax.invert_yaxis()
    # remove all thicks, set font color and size of y label
    for ticx in ax.xaxis.get_major_ticks():
        ticx.tick1line.set_visible(False)
        ticx.tick2line.set_visible(False)
    for ticy in ax.yaxis.get_major_ticks():
        ticy.tick1line.set_visible(False)
        ticy.tick2line.set_visible(False)
    for ticklabel in ax.yaxis.get_majorticklabels():
        ticklabel.set_fontsize(36)
        ticklabel.set_color(font_color)

    # removes the border and the x-axis around the diagram
    ax.spines["bottom"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # plt.setp(ax.get_xticklabels(), color="w", fontsize=8)
    ax.get_xaxis().set_visible(False)


def generate_skill_picture(
    skills: dict,
    n_splits: int,
    save_name: str,
    file_type: str,
    bar_height: float = 0.6,
    background_height: float = 0.7,
    background_color: _COLOR = DARK_GRAY,
    bar_color: _COLOR = DARK_GRAY,
    font_color: _COLOR = BLUE,
):
    split_skills = split_dict_evenly(skills, n_splits)
    split_len = len(split_skills[0])

    # generate the diagram, splits the values into two lists to plot.
    # this should be done in the future over one loop
    # the loop decides what to put when and how many columns
    _, axes = plt.subplots(1, n_splits, figsize=(10 * n_splits, split_len))

    # will get an iterable error since when using only one column, axes is not a list
    # just put the Axes object into a list to fix this
    if isinstance(axes, Axes):
        axes = [axes]

    for ax, skills in zip(axes, split_skills):
        generate_diagram(ax, skills, bar_height, background_height, background_color, bar_color, font_color)
    plt.tight_layout()
    plt.savefig(f"{save_name}.{file_type}", format=file_type, transparent=True)
