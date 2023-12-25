import os
import sys
import matplotlib.pyplot as plt

sys.path.append('src')
from module import Timer


# test function
def waste_time(num, iterations):
    for x in range(num):
        sum([x**4 for x in range(iterations)])

# instantiate obj
timer = Timer()

timer.run(waste_time, 'data/second_test.csv', 100, 5000, count=50)

# timer.plot('second_test.csv', point_color='olive')


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