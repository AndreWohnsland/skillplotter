![GitHub release (latest by date)](https://img.shields.io/github/v/release/AndreWohnsland/skillplotter)
![GitHub Release Date](https://img.shields.io/github/release-date/AndreWohnsland/skillplotter)
![Python Version](https://img.shields.io/badge/python-%3E%3D%203.9-blue)
![GitHub](https://img.shields.io/github/license/AndreWohnsland/skillplotter)
![GitHub issues](https://img.shields.io/github/issues-raw/AndreWohnsland/skillplotter)
[![Documentation Status](https://readthedocs.org/projects/skillplotter/badge/?version=latest)](https://skillplotter.readthedocs.io)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AndreWohnsland_skillplotter&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=AndreWohnsland_skillplotter)
![GitHub Repo stars](https://img.shields.io/github/stars/AndreWohnsland/skillplotter?style=social)

# The Skill Plotter: Overview

The Skill Plotter is a Python Command Line Interface (CLI) tool to create skill plots for your CV or other documents.
It can be used to easily and interactively create the plots.
Instead of using some designer software like Illustrator or just the office package we are going to use matplotlib and python.
Because, well, we can.

## Installation

The skill plotter package is available as a CLI command and can be installed via pip:


```bash
pip install skill-plotter
```

## Usage

Just use the CLI command to run the plotter, the help shows you all possible things to do:

```bash
skill-plotter --help
# Add a skill
skill-plotter add Python 9
# or use it interactively
skill-plotter interactive-add
# Remove a skill
skill-plotter remove Python
# or use it interactively
skill-plotter interactive-remove
# Do the plot
skill-plotter
```

If you want to have a complete walkthrough, you can have a look at the [usage documentation](https://skillplotter.readthedocs.io/usage/).

## Development

### Minimal Requirements

```
- Python 3.9
- matplotlib 3.8
```

## Examples

Here you can see an example of the generated skill plot:

![skillist](https://github.com/AndreWohnsland/skillplotter/blob/master/docs/img/skills_example.png?raw=true)
