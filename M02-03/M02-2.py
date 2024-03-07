import matplotlib.pyplot as plt
import numpy as np

# Garis 1
x1 = np.array([2, 5])
y1 = 4 + (4/3) * (x1 - 2)

# Garis 2
x2 = np.array([-1, 3])
y2 = 1 - (1/2) * (x2 - 3)

# Plotting
plt.plot(x1, y1, label='Garis 1')
plt.plot(x2, y2, label='Garis 2')

# Titik-titik
plt.scatter([2, 5], [4, 8], color='red')
plt.scatter([-1, 3], [3, 1], color='blue')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
