import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 10000)

plt.figure(figsize=(8, 6.5))

y1 = (24 - x ** 2) ** 0.5
y2 = -(24 - x ** 2) ** 0.5
y3 = 4 + (4 - (x - 4) ** 2) ** 0.5
y4 = 4 - (4 - (x - 4) ** 2) ** 0.5
y5 = -4 + (4 - (x - 4) ** 2) ** 0.5
y6 = -4 - (4 - (x - 4) ** 2) ** 0.5
y7 = 4 + (4 - (x + 4) ** 2) ** 0.5
y8 = 4 - (4 - (x + 4) ** 2) ** 0.5
y9 = -4 + (4 - (x + 4) ** 2) ** 0.5
y10 = -4 - (4 - (x + 4) ** 2) ** 0.5
y11 = 6 + (4 - x ** 2) ** 0.5
y12 = 6 - (4 - x ** 2) ** 0.5
y13 = - 6 + (4 - x ** 2) ** 0.5
y14 = - 6 - (4 - x ** 2) ** 0.5
y15 = (4 - (x - 6) ** 2) ** 0.5
y16 = -(4 - (x - 6) ** 2) ** 0.5
y17 = (4 - (x + 6) ** 2) ** 0.5
y18 = -(4 - (x + 6) ** 2) ** 0.5

plt.plot(x, y1, '-r')
plt.plot(x, y2, '-r', label='bunga')

for y in (y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18):
    plt.plot(x, y, color='#4aa0f0')

for y in (y1, y2):
    plt.fill_between(x, y, color='pink')

plt.fill_between(x, y3, y4, color='#ec33e3')
plt.fill_between(x, y5, y6, color='#ec33e3')
plt.fill_between(x, y7, y8, color='#ec33e3')
plt.fill_between(x, y9, y10, color='#ec33e3')
plt.fill_between(x, y11, y12, color='#ec33e3')
plt.fill_between(x, y13, y14, color='#ec33e3')
plt.fill_between(x, y15, y16, color='#ec33e3')
plt.fill_between(x, y17, y18, color='#ec33e3')

plt.legend(loc='upper left')
plt.grid()

plt.show()
