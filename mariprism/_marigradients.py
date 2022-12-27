"""

Authors : P. Cáceres-Burgos, P. Palma-Bifani

Here is the complete list and construction of gradients of Mariprism, 


"""
import numpy as np
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def make_gradient(color_list, name=''):
    """
    Function that makes a linear gradient out of the colors in a dictionary.

    input:
    -----
    color_list: [dict] Dictionary with key:value of the name and the rgb numbers of the
    color. The order of the colors in the dictionary will be respected.
    name: [string] Name of the new gradient 

    output:
    ------
    maricmap: [ListedColormap]
    
    """

    n_colors = len(color_list)
    if n_colors ==0 :
        print('list of colors is empty')
        return 
    if n_colors == 1: 
        print('need more than two colors')
        # here maybe we can return a single cmap of the color
        # going to a white/black gradient ?

        return 
    else:
        n_transisions = n_colors - 1
        dict_trans = {}
        name_colors = list(color_list.keys())
        for i in range(n_transisions):
            N = 256
            tcolor = np.ones((N,4))
            color1 = color_list[name_colors[i]] # color 1 
            color2 = color_list[name_colors[i+1]] # color 2 

            # make linear transision between both colors for every
            # rgb color value
            tcolor[:, 0] = np.linspace(color1[0], color2[0], N) 
            tcolor[:, 1] = np.linspace(color1[1], color2[1], N) 
            tcolor[:, 2] = np.linspace(color1[2], color2[2], N) 
            tcolor[:, 3] = np.linspace(0.9, 0.9, N) 

            tcolor_cmp= ListedColormap(tcolor) # transision ready for color1->color2

            # save transision cmap in dictionary 
            dict_trans['tcolor_{}_{}'.format(name_colors[i], name_colors[i+1])] = tcolor_cmp

        name_transisions = list(dict_trans.keys())
        
        # in this step we take all transision colors and stack them to create the 
        # desired gradient
        for j in (range(n_transisions-1)):
            if j == 0:
                tcolor_cmap1 = dict_trans[name_transisions[j]]
                tcolor_cmap2 = dict_trans[name_transisions[j+1]]

                stacked = np.vstack((tcolor_cmap2(np.linspace(1, 0, 128)), tcolor_cmap1(np.linspace(1, 0, 128))))
            else:
                tcolor_cmap = dict_trans[name_transisions[j+1]]
                stacked = np.vstack((tcolor_cmap(np.linspace(1, 0, 128)), stacked))
    
        maricmap = ListedColormap(stacked, name = 'maripism_{}'.format(name))
    return maricmap


def plot_colortable(colors, sort_colors=True, emptycols=0):
    """
    
    function that shows the colors available
    
    input:
    -----
    colors: [dict] dictionary with the key:value (key being the name of the color) and value being
    the rgb numbers of the colors (x,y,z)
    sort_colors: [bool] (default: True) Sorts colors
    emptycolos: 
    
    output:
    ------
    fig: [fig] returns matplotlib figures with the colors and their swaps
    
    
    """

    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))),
                         name)
                        for name, color in colors.items())
        names = [name for hsv, name in by_hsv]
    else:
        names = list(colors)

    n = len(names)
    ncols = 4 - emptycols
    nrows = n // ncols + int(n % ncols > 0)

    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig