import sys
import time
import csv
import functools
import matplotlib.pyplot as plt

def function_runner(func, count, filename, *args):

    with open(f"{filename}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # declare headers
        results = [['iteration', 'runtime (seconds)']]

        for x in range(count):
            start = time.time()
            func(*args)
            end = time.time()
            elapsed_s = round(end-start, 6)
            results.append([x+1, elapsed_s])
    
        writer.writerows(results)

    x, y = [], []
    x_label, y_label = str(), str()

    try:
        with open('runtimes.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')

            for row in plots:
                
                try: 
                    x.append(int(row[0]))
                    y.append(float(row[1]))
                except ValueError:
                    x_label, y_label = row[0], row[1]

        plt.style.use('dark_background')
        plt.scatter(x, y, None, '#d62728')  
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title('Function Runtimes')
        plt.legend('runtime')
        plt.show()

    except FileNotFoundError:
        sys.exit('Error: file does not exist.')

def waste_time(num):
    for x in range(num):
        sum([x**2 for x in range(1000000)])

function_runner(waste_time, 100, 'runtimes', 4)