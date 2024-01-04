# standard libraries
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
from helpers import *

class Timer:
    def __init__(self):
        pass

    @classmethod
    def run(self, func, output, *args, count=1, **kwargs):
 
        # splits user input into folder and filename for verification
        file, dir = split_output(output)
        
        # if the folder AND file already exists and file has stuff in it:
        if os.path.exists(output) and os.stat(output).st_size != 0:

            # warn user about overwriting
            print(f"Function {func.__name__}: overwrite or append?")
            choice = override_input() # ask for either yes or no for overwrite
            
            # if wanting to append, WRITE NEW CODE
            if choice == 'a':
                # ----------------------------------- TODO: NEW UPDATE CODE HERE ------------------------------------- #
                with open(output, 'r', newline='') as csvfile:
                    rows = csv.reader(csvfile, delimiter=',')
                    row_count = sum(1 for row in rows) - 1
                
                # ensures number of iterations in the file matches the user provided count
                if row_count != count:
                    sys.exit('Error: Inputted count does not match file row count.')
                # otherwise if they do match, execute proper code
                with open(output, 'r') as csvfile:
                    rows = csv.reader(csvfile, delimiter=',')

                    new_rows = [] # array to store new data rows

                    # for each existing row
                    for row in rows:
                        try:
                            float(row[1]) # try converting one of its values to a number, to check if we are at the header

                            # run the function and append it to the row's data
                            elapsed_s = time_function(func, *args, **kwargs)
                            row.append(elapsed_s)

                        except: # if we are at the header, append the function name to the header
                            row.append(func.__name__)
                        
                        new_rows.append(row) # append the new row to the list of new rows

                # write the new_rows list to the csv file
                with open(output, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(new_rows)
                    return 0

            pass # otherwise if overwrite wants to happen, run code like usual
        
        # else if neither exist
        elif os.path.exists(dir)==0 and os.path.exists(file)==0:
            if len(dir) >= 1: os.makedirs(dir) # make the directory
        
        # else if the folder exists, but the file does not, or file also exists but is empty:
        # generates/accesses csv file for writing 
        with open(output, 'w', newline='') as csvfile:
            # set file mode to writing
            writer = csv.writer(csvfile)

            # declare data headers
            results = [['iteration', f'{func.__name__}']]

            # execute function specified amt of times
            for x in range(count):

                # measure elapsed time while running each iteration
                elapsed_s = time_function(func, *args, **kwargs)
                results.append([x+1, elapsed_s]) # add elapsed time data to the file data
        
            writer.writerows(results) # write time data to csv file


    # does not require func *args because it plots directly from file with static results
    @classmethod
    def plot(self, file, plot_type='scatter', chart_style='dark_background', title='X vs Y', point_colors=None): # point_color defaults to blue
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
            for col in legend:
                y_data.append(data[col].tolist())
        
        # if user did not specify point colors, use our own method of random sampling
        if point_colors == None:
            plot_colors = random.sample(colors, len(legend))
        else: # if they did specify colors, use those
            plot_colors = point_colors
        
        # 3. Plot the data
        plt.style.use(chart_style)

        # get attribute from plt based on plot_type userinput
        plottype = getattr(plt, plot_type)

        # for each y dataset
        for y in y_data:
            # generate plot
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
        plt.show()