"""print("\033c")
import numpy as np
import matplotlib.pyplot as plt

# Setup sumbu x
x = np.linspace(-20, 20, 10000)

# Membuat figure
plt.figure(figsize=(8, 8))
plt.title("MICKEY MOUSE")

# Fungsi untuk menghindari akar negatif
def safe_sqrt(arr):
    return np.where(arr >= 0, np.sqrt(arr), np.nan)

# Garis horizontal tengah
y = np.zeros_like(x)

# Kepala
y3 = 5 + safe_sqrt(25 - (x - 5) ** 2)
y4 = 5 - safe_sqrt(25 - (x - 5) ** 2)

plt.plot(x, y3, '-k', label='Kepala')
plt.plot(x, y4, '-k')

# Fungsi telinga
def telinga(t1, t2, label=None):
    y1 = t1 + safe_sqrt(4 - (x - t2) ** 2)
    y2 = t1 - safe_sqrt(4 - (x - t2) ** 2)
    plt.plot(x, y1, '-k', label=label)
    plt.plot(x, y2, '-k')

# Menambahkan telinga tanpa duplikasi label
telinga(10, 1, label="Telinga")
telinga(10, 9)

# Tambahkan grid dan legenda
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc='upper center')

# Menampilkan plot
plt.show()"""

"""print("\033c")
import numpy as np
import matplotlib.pyplot as plt

# Setup sumbu x
x = np.linspace(-20, 20, 10000)

# Membuat figure
plt.figure(figsize=(8, 8))
plt.title("MICKEY MOUSE")

# Fungsi untuk menghindari akar negatif
def safe_sqrt(arr):
    return np.where(arr >= 0, np.sqrt(arr), np.nan)

# Kepala
x_head = np.linspace(-1, 11, 1000)
y_head_top = 5 + safe_sqrt(25 - (x_head - 5) ** 2)
y_head_bottom = 5 - safe_sqrt(25 - (x_head - 5) ** 2)

plt.fill_between(x_head, y_head_top, y_head_bottom, color="black")

# Fungsi telinga
def telinga(t1, t2):
    x_ear = np.linspace(t2 - 2, t2 + 2, 1000)
    y_ear_top = t1 + safe_sqrt(4 - (x_ear - t2) ** 2)
    y_ear_bottom = t1 - safe_sqrt(4 - (x_ear - t2) ** 2)
    plt.fill_between(x_ear, y_ear_top, y_ear_bottom, color="black")

# Menambahkan telinga
telinga(10, 1)
telinga(10, 9)

# Hapus grid untuk tampilan lebih bersih
plt.axis("off")

# Menampilkan plot
plt.show()"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Membuat figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect(1)
ax.axis("off")

# Fungsi untuk menggambar lingkaran
def draw_circle(ax, center, radius, color="black", zorder=1):
    circle = plt.Circle(center, radius, color=color, zorder=zorder)
    ax.add_patch(circle)

# Fungsi untuk menggambar elips
def draw_ellipse(ax, center, width, height, color="black", angle=0, zorder=1):
    ellipse = plt.matplotlib.patches.Ellipse(center, width, height, angle=angle, color=color, zorder=zorder)
    ax.add_patch(ellipse)

# Telinga Mickey (lingkaran besar)
draw_circle(ax, (-6, 6), 4, color="black")  # Telinga kiri
draw_circle(ax, (6, 6), 4, color="black")   # Telinga kanan

# Kepala Mickey (lingkaran besar)
draw_circle(ax, (0, 0), 6, color="black")

# Wajah (lingkaran dalam yang lebih kecil berwarna krem)
draw_circle(ax, (0, -1), 5, color="#F4C29C", zorder=2)  # Warna krem

# Mata Mickey (dua elips putih)
draw_ellipse(ax, (-2, 2), 1.5, 3, color="white", zorder=3)
draw_ellipse(ax, (2, 2), 1.5, 3, color="white", zorder=3)

# Bola mata Mickey (dua elips hitam)
draw_ellipse(ax, (-2, 3), 0.7, 1.5, color="black", zorder=4)
draw_ellipse(ax, (2, 3), 0.7, 1.5, color="black", zorder=4)

# Hidung Mickey (elips hitam)
draw_ellipse(ax, (0, 1), 2, 1, color="black", zorder=4)

# Mulut Mickey (bentuk senyum)
x = np.linspace(-2, 2, 100)
y = -0.5 * (x**2) + -1.5  # Persamaan parabola untuk mulut
ax.plot(x, y, color="black", linewidth=3, zorder=5)

# Lidah (dua setengah elips merah)
draw_ellipse(ax, (-0.8, -3), 1.2, 1.5, color="red", zorder=4)
draw_ellipse(ax, (0.8, -3), 1.2, 1.5, color="red", zorder=4)

# Garis tengah lidah
ax.plot([0, 0], [-3.5, -2.5], color="black", linewidth=2, zorder=5)

# Menampilkan gambar
plt.show()
