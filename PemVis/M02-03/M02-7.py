import numpy as np
import matplotlib.pyplot as plt

# Randomly generate four line coordinates
np.random.seed(42)  # Set a seed for reproducibility
x1, y1 = np.random.randint(100, 700, size=(2, 4))
x2, y2 = np.random.randint(100, 700, size=(2, 4))

pd = 20
pr = 255
pg = 255
pb = 0
lw = 20
lr = 255
lg = 255
lb = 0

col = 800
row = 800

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd / 2)
    hw = int(lw / 2)

    for l in range(4):
        # Draw main lines
        for i in range(min(x1[l], x2[l]) - hd, max(x1[l], x2[l]) + hd + 1):
            for j in range(min(y1[l], y2[l]) - hd, max(y1[l], y2[l]) + hd + 1):
                if ((i - x1[l]) ** 2 + (j - y1[l]) ** 2) < hd ** 2:
                    Gambar[j, i, 0] = pr
                    Gambar[j, i, 1] = pg
                    Gambar[j, i, 2] = pb

        for i in range(min(x1[l], x2[l]) - hd, max(x1[l], x2[l]) + hd + 1):
            for j in range(min(y1[l], y2[l]) - hd, max(y1[l], y2[l]) + hd + 1):
                if ((i - x1[l]) ** 2 + (j - y1[l]) ** 2) < hd ** 2:
                    Gambar[j, x1[l], 0] = lr
                    Gambar[j, x1[l], 1] = lg
                    Gambar[j, x1[l], 2] = lb

        for i in range(min(x1[l], x2[l]) - hd, max(x1[l], x2[l]) + hd + 1):
            for j in range(min(y1[l], y2[l]) - hd, max(y1[l], y2[l]) + hd + 1):
                if ((i - x2[l]) ** 2 + (j - y2[l]) ** 2) < hd ** 2:
                    Gambar[j, x2[l], 0] = lr
                    Gambar[j, x2[l], 1] = lg
                    Gambar[j, x2[l], 2] = lb

    return Gambar

hasil = buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()