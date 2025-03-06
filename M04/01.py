"""import numpy as np
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
plt.show()"""

import numpy as np
import matplotlib.pyplot as plt

# Definisikan nilai x
x = np.linspace(-8, 8, 10000)

# Ukuran figure
plt.figure(figsize=(8, 8))
plt.axhline(0, color='black', linewidth=0.8)  # Garis x-axis
plt.axvline(0, color='black', linewidth=0.8)  # Garis y-axis

# Fungsi matematika (menggunakan np.where untuk menghindari error akar negatif)
def safe_sqrt(arr):
    return np.where(arr >= 0, np.sqrt(arr), np.nan)  # Hanya mengambil nilai valid

y1 = safe_sqrt(4 - x**2)
y2 = -y1
y3 = 5 + safe_sqrt(4 - (x - 5)**2)
y4 = 5 - safe_sqrt(4 - (x - 5)**2)
y5 = -5 + safe_sqrt(4 - (x - 5)**2)
y6 = -5 - safe_sqrt(4 - (x - 5)**2)
y7 = 5 + safe_sqrt(4 - (x + 5)**2)
y8 = 5 - safe_sqrt(4 - (x + 5)**2)
y9 = -5 + safe_sqrt(4 - (x + 5)**2)
y10 = -5 - safe_sqrt(4 - (x + 5)**2)

# Warna dan label
functions = [
    (y1, '-r', 'y1, y2'), (y2, '-r', ''),
    (y3, '-g', 'y3, y4'), (y4, '-g', ''),
    (y5, '-b', 'y5, y6'), (y6, '-b', ''),
    (y7, '-y', 'y7, y8'), (y8, '-y', ''),
    (y9, '-c', 'y9, y10'), (y10, '-c', ''),
]

# Plot semua fungsi
for y, color, label in functions:
    plt.plot(x, y, color, label=label if label else None)

# Pengaturan plot
plt.legend(loc='upper center', fontsize=10)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.xticks(range(-8, 9, 2))
plt.yticks(range(-8, 9, 2))
plt.title("Plot Beberapa Fungsi Kurva", fontsize=14)
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)

# Tampilkan plot
plt.show()
