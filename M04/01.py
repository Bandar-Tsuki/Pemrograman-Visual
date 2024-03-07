import numpy as np
import matplotlib.pyplot as plt

# Define the x-axis values
x = np.linspace(-8, 8, 10000)

# Define the figure size
plt.figure(figsize=(8, 6.5))

# Define the mathematical functions
y = x - x  # y = 0
y1 = (4 - x ** 2) ** 0.5
y2 = -(4 - x ** 2) ** 0.5
y3 = 5 + (4 - (x - 5) ** 2) ** 0.5
y4 = 5 - (4 - (x - 5) ** 2) ** 0.5
y5 = -5 + (4 - (x - 5) ** 2) ** 0.5
y6 = -5 - (4 - (x - 5) ** 2) ** 0.5
y7 = 5 + (4 - (x + 5) ** 2) ** 0.5
y8 = 5 - (4 - (x + 5) ** 2) ** 0.5
y9 = -5 + (4 - (x + 5) ** 2) ** 0.5
y10 = -5 - (4 - (x + 5) ** 2) ** 0.5

# Plot the functions
plt.plot(x, y, 'k')
plt.plot(x, y1, '-r', label='y1, y2')
plt.plot(x, y2, '-r')
plt.plot(x, y3, '-g', label='y3, y4')
plt.plot(x, y4, '-g')
plt.plot(x, y5, '-b', label='y5, y6')
plt.plot(x, y6, 'b')
plt.plot(x, y7, '-y', label='y7, y8')
plt.plot(x, y8, '-y')
plt.plot(x, y9, '-y', label='y9, y10')
plt.plot(x, y10, '-y')

# Add legend and grid
plt.legend(loc='upper center')
plt.grid()

# Display the plot
plt.show()