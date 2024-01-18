# standard libraries
import sys
import os
import csv

# helper functions
from helpers import *

# UI initializer
import user_interface

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


    # UI open method
    @classmethod
    def plot(self, file):
        user_interface.initialize_ui(file)