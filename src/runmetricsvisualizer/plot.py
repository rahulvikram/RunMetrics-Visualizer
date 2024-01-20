import sys
import os
import time
import math
import csv
import random

# data science libraries
import matplotlib.pyplot as plt
import pandas as pd

# helper functions
from runmetricsvisualizer.helpers import *

# Final plotting method
def generate_plot(file, plot_type='scatter', chart_style='default', title='X vs Y', point_colors=None, savefile=None):
    # error handling if file does not exist
    try:
        f = open(file)
    except FileNotFoundError:
        sys.exit('Error: file does not exist')

    # if file DOES exist
    with open(file, 'r') as csvfile:
        # 1. Assign data labels for x, y, and legend
        rows = csv.reader(csvfile, delimiter=',')
        legend = next(rows)
        # assignment of x, y labels, and legend
        x_label = legend[0]
        legend.pop(0) # remove x label from legend
        y_label = 'runtime (s)'

        # 2. Load CSV columns into respective arrays
        y_data = []
        data = pd.read_csv(file)
        x = data[x_label].tolist() # array of x axis values
        
        # load arrays of y values into y_data
        # FIX: avoid redundant data loading due to duplicate function names
        for z in range(len(legend)):
            y_data.append(data[legend[z]].tolist())
    
    # for testing: if user did not specify point colors, use our own method of random sampling
    if point_colors == None:
        plot_colors = random.sample(colors, len(legend))
    else: # if they did specify colors, use those
        plot_colors = point_colors
    
    # 3. Plot the data
    plt.style.use(chart_style)

    # get attribute from plt based on plot_type userinput
    plottype = getattr(plt, plot_type)

    # for each y dataset
    if plot_type == 'stackplot':
        # generate plot
        plottype(x, y_data, colors=plot_colors, labels=legend)
    else:
        for y in y_data:
            plottype(x, y, color=plot_colors[0], label=legend[0])
    
            # move to next color and legend label
            plot_colors.pop(0)
            legend.pop(0)

    # algorithm to determine number and intervals of ticks
    plt.xticks(range(x[0], x[-1]+1, math.ceil(len(x)/50))) # rounds up to prevent step of 0

    # set labels, display chart
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(loc='upper left')

    # based on userinput (or lacktherof) either display or save plot
    if savefile == None:
        plt.show()
    else:
        plt.savefig(savefile)
        plt.cla()