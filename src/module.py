import sys
import os
import time
import math
import csv
import matplotlib.pyplot as plt

from helpers import *

class Timer:
    def __init__(self):
        pass
    
    def run(self, func, output, *args, count=1, **kwargs):
 
        # splits user input into folder and filename for verification
        file, dir = split_output(output)
        
        # if the folder AND file already exists and file has stuff in it:
        if os.path.exists(output) and os.stat(output).st_size != 0:

            # warn user about overwriting
            print("Warning: File contents will be overwritten. Proceed?")
            choice = override_input() # ask for either yes or no for overwrite
            
            # if no overwrite, cancel operation
            if choice == 'n':
                sys.exit('Overwrite cancelled. Operation closed.')
            
            pass # otherwise if overwrite wants to happen, run code like usual
        
        # else if neither exist
        elif os.path.exists(dir)==0 and os.path.exists(file)==0:
            if len(dir) >= 1: os.makedirs(dir) # make the directory

        # generates/accesses csv file for writing 
        with open(output, 'w', newline='') as csvfile:
            # set file mode to writing
            writer = csv.writer(csvfile)

            # declare data headers
            results = [['iteration', f'{func.__name__}']]

            # execute function specified amt of times
            for x in range(count):

                # measure elapsed time while running each iteration
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                elapsed_s = round(end-start, 6)
                results.append([x+1, elapsed_s]) # add elapsed time data to the file data
        
            writer.writerows(results) # write time data to csv file

    # does not require func *args because it plots directly from file with static results
    def plot(self, file, chart_style='dark_background', title='X vs Y', point_color=None): # point_color defaults to blue
        # initialize blank array and labels for assignment later
        x, y, x_label, y_label = [], [], str(), str()

        # error handling if file does not exist
        try:
            f = open(f"data/{file}", 'r')
        except FileNotFoundError:
            sys.exit('Error: file does not exist')

        # if file DOES exist
        with open(f"data/{file}", 'r') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')

            # add each row's data to respective arrays
            for row in rows:
                try: 
                    x.append(int(row[0]))
                    y.append(float(row[1]))
                except ValueError:
                    # add top row to labels
                    x_label, y_label = row[0], row[1]  

        plt.style.use(chart_style)
        plt.scatter(x, y, None, point_color) # sets color of data points/line

        # algorithm to determine number and intervals of ticks
        plt.xticks(range(x[0], x[-1]+1, math.ceil(len(x)/50))) # rounds up to prevent step of 0

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.legend('test')
        plt.show()