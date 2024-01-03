import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [7, 3, 5, 3, 6]

method_name = input('enter plot type: ')
method = getattr(plt, method_name)

method(x, y)

plt.show()