import os
import sys
import matplotlib.pyplot as plt
import time

sys.path.append('src/runmetricsvisualizer')
from timer import Timer
from plot import generate_plot

# test function
def waste_time(num, iterations):
    for x in range(num):
        sum([x**4 for x in range(iterations)])

def other_function(iterations, sleep):
    for x in range(iterations):
        sum([x**5 for x in range(iterations)])
        time.sleep(sleep)

def third_order(iterations, sleep):
    for x in range(iterations):
        sum([x**5 for x in range(iterations)])
        time.sleep(sleep)

# Timer.run(other_function, 'data/first_test.csv', 2, 0.1, count=50)
Timer.run(waste_time, 'data/first_test.csv', 100, 1000, count=50)

# CODE FOR GRAPHING MULTIPLE Y AXES ON ONE GRAPH
# Timer.plot('data/first_test.csv')



# fig, ax = plt.subplots()

# twin2 = ax.twinx()

# x = [0, 1, 2, 3, 4]
# y1 = [5, 2, 7, 2, 4]
# y2 = [3, 5, 2, 3, 6]

# # p1, = ax.plot([0, 1, 2], [0, 1, 2], "C0", label="Density")
# p1 = ax.scatter(x, y1, None, None)
# p3 = twin2.scatter(x, y2, None, None)
# ax.set(xlabel="Iteration", ylabel="Runtime")



# plt.show()