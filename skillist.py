import numpy as np
import matplotlib.pyplot as plt


# enter a dict of your skills and the rating
# between zero (none) and ten (best)
skills = {
    'C/C++': 3.5,
    'Python': 8.5,
    'SQL': 5,
    'Matlab': 8,
    'MS Office': 9.5,
    'VB/VBA': 9,
    'Ansys': 8,
    'CAD': 5.5,
    'German': 10,
    'English': 9.5,
    'French': 5.5
}

# define height of the background and height of the skill bar
# the value is between 0 and 1 (1 equals 100%)
heigh_b = 0.7
heigh_s = 0.6
# sets the font color, the color of the background bar and the color of the skill bar
# current values are in rgb (0 to 1) so divied the RGB by 255.
# other values may be used, like color name strings or hexavalues
color_font = (64/255, 64/255, 64/255)
color_bg = (64/255, 64/255, 64/255) # 'grey'
color_bar = (54/255, 125/255, 162/255) # 'tab:blue'

def generate_pic(
    skills,
    heigh_b=0.7,
    heigh_s=0.6,
    color_font=(64/255, 64/255, 64/255),
    color_bg=(64/255, 64/255, 64/255),
    color_bar=(54/255, 125/255, 162/255)
    ):
    """Plot and displays the given skill bar. Also saves it as svg  
    
    Args:
        skills (dict): Dictionary of skillnames and level of skills.
        heigh_b (float): Percentage of the height of the background bar. Should be greater than the skill bar. Defaults to 0.7.
        heigh_s (float): Percentage of the height of the skill bar. Should be lesser than the backgroud bar. Defaults to 0.6.
        color_font (color): Color of the font color. Defaults to dark grey.
        color_bg (color): Color of the font backgroundbar. Defaults to dark grey.
        color_bar (color): Color of the font skillbar. Defaults to blue.
    """
    # generates lists of the names and skills out of the dict
    skillnames = [k for k, _ in skills.items()]
    myskill = [v for _, v in skills.items()]
    # also generates the fixex values for the background bars
    maxskill = [10.05 for x in range(len(skillnames))]
    # and the fixed values for the front border
    border = [0.05 for x in range(len(skillnames))]

    # gets the len, divides it into two parts
    l_s = len(skillnames)
    l_h = int(np.ceil(l_s / 2))

    # generate thje diagram, splits the values into two lists to plot.
    # this should be done in the future over one loop 
    # the loop decides what to put when and how many columns
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,l_h))

    val1, val2 = myskill[0:l_h], myskill[l_h:l_s]
    label1, label2 = skillnames[0:l_h], skillnames[l_h:l_s]
    filler1, filler2 = maxskill[0:l_h], maxskill[l_h:l_s]
    border1, border2 = border[0:l_h], border[l_h:l_s]
    if len(val1) != len(val2):
        val2.append(0)
        label2.append("")
        filler2.append(0)
        border2.append(0)
        
    # gets y_positions (1 to n-1) for both, they are usually identical
    y_pos1 = np.arange(len(val1))
    y_pos2 = np.arange(len(val2))

    # plot the diagrams and format the axis accordingly
    plot_dia(ax1, y_pos1, val1, filler1, border1, label1, heigh_s, heigh_b, color_bg, color_bar, color_font)
    plot_dia(ax2, y_pos2, val2, filler2, border2, label2, heigh_s, heigh_b, color_bg, color_bar, color_font)
    plt.tight_layout()
        
    plt.savefig("skills.svg", format="svg", transparent=True)
    # plt.show()


def plot_dia(ax, y_pos, val, filler, border, label, h1, h2, bg, bar, cfont):
    """plot and styles the diagram.
    
    Args:
        ax (axis): axis to plot on.
        y_pos (list): List of all y positions (0 to n).
        val (list): List of all values.
        filler (list): List of constant values.
        border (list): List of constant values.
        label (list): List of Labels for the skills.
        h1 (float): Percentage of the height of the skillbar.
        h2 (float): Percentage of the height of the backgroundbar.
        bg (color): Color of the background.
        bar (color): Color of the Skillbar.
        cfont (color): Color of the font.
    """
    # plots the skill label
    ax.barh(y_pos, val, tick_label=label, zorder=2, height=h1, color=bar)
    # plots the background
    ax.barh(y_pos, filler, tick_label=label, zorder=1, height=h2, color=bg)
    # plots the front border, alternatively in the first plot there could be 
    # used the "left" keyword to shift it from zero the the border
    ax.barh(y_pos, border, tick_label=label, zorder=3, height=h2, color=bg)
    # invert axis because last list element is on the top
    ax.invert_yaxis()
    # remove all thicks, set fontcolor and size of y label
    for ticx in ax.xaxis.get_major_ticks():
        ticx.tick1line.set_visible(False)
        ticx.tick2line.set_visible(False)
    for ticy in ax.yaxis.get_major_ticks():
        ticy.tick1line.set_visible(False)
        ticy.tick2line.set_visible(False)
        ticy.label.set_fontsize(36)
        ticy.label.set_color(cfont)

    # removes the border and the x-axis around the diagram
    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # plt.setp(ax.get_xticklabels(), color="w", fontsize=8)
    ax.get_xaxis().set_visible(False)
        

if __name__ == "__main__":
    generate_pic(skills, heigh_b, heigh_s, color_font, color_bg, color_bar)