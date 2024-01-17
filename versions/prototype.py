import sys
import time
import csv
import matplotlib.pyplot as plt

def waste_time(num, iterations):
    for x in range(num):
        sum([x**4 for x in range(iterations)])



def function_runner(func, count, output, *args, **kwargs):
    with open(f"{output}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # declare headers
        results = [['iteration', 'runtime (seconds)']]

        for x in range(count):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            elapsed_s = round(end-start, 6)
            results.append([x+1, elapsed_s])
    
        writer.writerows(results)

    x, y = [], []
    x_label, y_label = str(), str()

    try:
        with open(f"{output}.csv", 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')

            for row in plots:
                
                try: 
                    x.append(int(row[0]))
                    y.append(float(row[1]))
                except ValueError:
                    x_label, y_label = row[0], row[1]

        plt.style.use('Solarize_Light2')
        plt.scatter(x, y, None, 'olive')  
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title('Function Runtimes')
        plt.legend('runtime')
        plt.show()

    except FileNotFoundError:
        sys.exit('Error: file does not exist.')

function_runner(waste_time, 20, 'test.csv', 10, 1000)