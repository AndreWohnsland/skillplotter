# The Skillplotter: Overview

This little script will help you visualize the skills of you for your CV, presentations or similar. Instead of using some designer software like Illustrator or just the office package we are going to use matplotlib and python. Because, well, we can.

The process is quite simple and fast, you just need to generate a dict (`skills`) and map the level of your skill to each skill keyword. An example is already in the script. The skills range from zero (not good) to ten (very good). Additionally you can style the height of the background bar `height_b` and the height of the skill bar `height_s`, the color of the background bar `color_bg`, the color of the skill bar `color_bar` and the color of the names for your skills `color_font`.

Alternatively you could also import the driving function `generate_pic` from this script and use it with all the above values to generate your own visual list of skills within your script. 

## Minimal Requirements

```
- Python 3.6
- matplotlib 3.1
```

## Install matplotlib

As long as you are using anaconda, matplotlib should be already included. Otherwise you can always install it from pip with `pip install matplotlib` to get the corresponding packages.

## Examples

Here you can see an example of the generated svg. Currently there are always two equal divided columns, in the future there will be the option to choose between one to three columns.

![skillist](https://github.com/AndreWohnsland/skillplotter/blob/master/skills.png "your skillist")

## Usage

Feel free to use and experiment with this. If you are using it for an publication or similar I'd be glad if you can quote this project.