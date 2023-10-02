# Usage

In this section, you will get a brief introduction to the usage of the package.
If you want to have deeper insight into the functionality of the functions, you can always use the `--help` flag.

!!! note
    This package is quite flexible, but the base case is quite easy.
    So if you want a fast test, use `skill-plotter add` and then `skill-plotter` to see first results. 

## Prerequisites

The package can be installed via pip:

```bash
pip install skill-plotter
```

Take note that both, Python and pip needs to be installed on the system.

## Entering Skills

To enter a skill with the according level to your list, you can use the `add` command:

```bash
skill-plotter add Python 9
```

This will add the skill `Python` with the level `9` to your list.

### Adding, Using Multiple Skill Files

If you want to manage multiple skill files or picture, you can use the `--skill-group` or short `-g` option:

```bash
skill-plotter add Python 9 -g group1
```

This will add the skill `Python` with the level `9` to the skill group `group1`. Groups are used to either manage multiple users data or just to simply generate multiple skill plots.

### Adding, Using Categories

If you want to group multiple skills together, you can also provide the category option, using the `--category` or short `-c` option:

```bash
skill-plotter add Python 9 -c programming -g group1
```

This will add the skill `Python` with the level `9` and the category `programming` to the skill group `group1`.
If you don't provide a category, the category will be set to `default`.
The default category will always be shown first.

## Entering Skills Interactively

You can also enter skills interactively by using the `interactive-add` command:

```bash
skill-plotter interactive-add
# Enter the skill name: Python
# Enter the skill level: 9
# Enter category [default]: programming 
```

This will add the skill `Python` with the level `9` and the category `programming` to the skill group `default`.
If you leave the category blank, it will use the default one.

When you want to add multiple skills using a specific group or category, you can also provide the according options:

```bash
skill-plotter interactive-add -g group1 -c programming
```
This will add all skills to the group `group1` and use the category `programming`.
You will not be prompted for the category during the interactive session.

## Removing Skills

The same way you can add skills, you can also remove them using the `remove` command:

```bash
skill-plotter remove Python
```

This will remove the skill `Python` from your list.

### Removing, Using Multiple Skill Files

If you want to delete from other skill files or picture, you can use the `--skill-group` or short `-g` option:

```bash
skill-plotter remove Python -g group1
```

This will remove the skill `Python` from the skill group `group1`.

## Removing Skills Interactively

You can also remove skills interactively by using the `interactive-remove` command:

```bash
skill-plotter interactive-remove
# Here a list of all skills will be shown
# Enter skill name: Python
```

This will remove the skill `Python` from your list.

When you want to remove skills from a specific group, you can also provide the according option:

```bash
skill-plotter interactive-remove -g group1
```

This will use the skill group `group1` to remove skills from.

## Plotting your Skills

To plot your defined skills, you can use the `skill-plotter` command:

```bash
skill-plotter
```

This command will use your previously entered skills and plot them to a file called `skills.svg` in the current working directory.
In addition, there are many options you can use to customize the output.
We will explore the most important of them, but you can always use `skill-plotter --help` to get a full list of all options.

### Plotting, Using Multiple Skill Files

As before, you can specify the skill group you want to plot using the `--skill-group` or short `-g` option.
This gives you the option to manage multiple profiles or pictures.

```bash
skill-plotter -g group1
```


### Define Plotting Order

By default, the skills will be plotted in the order you entered them.
If you want to group the skills by category, you can use the `--categories` or short `-c` option:

```bash
skill-plotter -c
```

This will group the skills by your defined categories, as well the skills will be sorted within the category by decreasing level.
If the default category exist, skills within this category will be shown first.

This will use the skill group `group1` to plot the skills.

### Defining the Output File

You can also specify the output file name using the `--file-name` or short `-n` option and the type of the output file using the `--file-type` or short `-t` option.
Supported file types are `svg`, `png`, `jpg` and `pdf`.

```bash
skill-plotter -n my_skills -t png
```

This will save the output to a file called `my_skills.png`.

### Define the Style

You have also the possibility to alter the output plot.
Some options are:

- `--bar-height`: The height of the bars in the plot
- `--bg-height`: The height of the background bars in the plot
- `--bar-color`: The color of the bars in the plot
- `--bg-color`: The color of the background bars in the plot
- `--font-color`: The color of the font in the plot

You can experiment with those values and find the best fit for you.
I recommend using hex color codes for the colors.

```bash
skill-plotter --bar-height 0.5 --bg-height 0.7 --bar-color "#000000" --bg-color "#FFFFFF" --font-color "#000000"
```

## Showing Data

Especially when you have multiple skill groups, or haven't used them for a long time you might want to see the data you entered.

You can use the `list-groups` command to see all skill groups you have defined:

```bash
skill-plotter list-groups
```

And you can use the `list-skills` command to see all skills you have defined within a group:

```bash
skill-plotter list-skills -g group1
```

If no group is specified, the default group (skills) will be used.

<!-- # CLI Reference

This page provides documentation for our command line tools.

::: mkdocs-click
    :module: skill_plotter.main
    :command: app -->