import sys
import os
import time
import math
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter, plot, bar, stem, fill_between, stackplot, stairs

class Timer:
    def __init__(self):
        pass

    def run(self, func, output, *args, count=1, **kwargs):
        # checks if dir for data file exists; if not, create one
        dir = 'data/' if os.path.exists("data/") else os.mkdir

        # generates and accesses csv file for writing 
        with open(f"{dir}{output}", 'w', newline='') as csvfile:
            # set file mode to writing
            writer = csv.writer(csvfile)

            # declare data headers
            results = [['iteration', 'runtime (seconds)']]

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
    def plot(self, file, chart_type='scatter', chart_style='dark_background', title='X vs Y', point_color=None): # point_color defaults to blue
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

        
        charttype = getattr(plt, chart_type) # calls plt function based on userinput
        charttype(x, y, None, point_color) # sets color of data points/line

        # algorithm to determine number and intervals of ticks
        plt.xticks(range(x[0], x[-1]+1, math.ceil(len(x)/50))) # rounds up to prevent step of 0

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.legend('test')
        plt.show()