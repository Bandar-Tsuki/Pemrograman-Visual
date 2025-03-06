print("\033c")
import numpy as np
import matplotlib.pyplot as plt

y1, x1 = 600, 200
y2, x2 = 200, 600

pd, pr, pg, pb = 6, 0, 50, 255
lw, lr, lg, lb = 6, 0, 50, 255

col, row = 800, 800
print('col, row =', col, ', ', row)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
    hd = int(pd / 2)
    hw = int(lw / 2)
    dy = abs(y2 - y1)
    dx = abs(x2 - x1)

    # Titik awal
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if 0 <= i < col and 0 <= j < row:
                if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                    Gambar[j, i, 0] = pr
                    Gambar[j, i, 1] = pg
                    Gambar[j, i, 2] = pb

    # Garis horizontal atau miring
    if dx >= dy:
        my = (y2 - y1) / dx if dx != 0 else 0
        for i in range(min(x1, x2), max(x1, x2)):
            j = int(my * (i - x1) + y1)
            x, y = i, j
            print('x, y =', x, ',', y)
            for xi in range(x - hw, x + hw):
                for yj in range(y - hw, y + hw):
                    if 0 <= xi < col and 0 <= yj < row:
                        if ((xi - x) ** 2 + (yj - y) ** 2) < hw ** 2:
                            Gambar[yj, xi, 0] = lr
                            Gambar[yj, xi, 1] = lg
                            Gambar[yj, xi, 2] = lb

    # Garis vertikal atau dominan vertikal
    else:
        mx = (x2 - x1) / dy if dy != 0 else 0
        for j in range(min(y1, y2), max(y1, y2)):
            i = int(mx * (j - y1) + x1)
            x, y = i, j
            print('x, y =', x, ',', y)
            for xi in range(x - hw, x + hw):
                for yj in range(y - hw, y + hw):
                    if 0 <= xi < col and 0 <= yj < row:
                        if ((xi - x) ** 2 + (yj - y) ** 2) < hw ** 2:
                            Gambar[yj, xi, 0] = lr
                            Gambar[yj, xi, 1] = lg
                            Gambar[yj, xi, 2] = lb

    return Gambar

# Panggil fungsi dan tampilkan hasilnya
Gambar = buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb)

plt.imshow(Gambar.astype(np.uint8))
plt.show()
