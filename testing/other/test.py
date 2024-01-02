import matplotlib.pyplot as plt

x = range(100)
y = range(100,200)
fig = plt.figure()
ax1 = fig.add_subplot()

ax1.scatter(x[:4], y[:4], label='first')
ax1.scatter(x[40:],y[40:], label='second')
plt.legend(loc='upper left')
plt.show()