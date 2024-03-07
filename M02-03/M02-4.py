print("\033c")
import numpy as np
import matplotlib.pyplot as plt

ya, xa = 200, 200
yb, xb = 200, 600
yc, xc = 600, 600
yd, xd = 600, 200

pd, lw = 8, 8
pr, pg, pb = 255, 0, 255
lr, lg, lb = 255, 0, 255

col, row = 800, 800

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd / 2)
    hw = int(lw / 2)

    for i in range(x1 - hd, x1 + hd + 1):
        for j in range(y1 - hd, y1 + hd + 1):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, :] = [pr, pg, pb]

    for i in range(x2 - hd, x2 + hd + 1 ):
        for j in range(y2 - hd, y2 + hd + 1):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, :] = [pr, pg, pb]

    dy = y2 - y1
    dx = x2 - x1

    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2 + 1):
            j = int(my * (i - x1) + y1)
            x, y = i, j
            print('x, y =', x, ',', y)
            for i in range(x - hw, x + hw + 1):
                for j in range(y - hw, y + hw + 1):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, :] = [lr, lg, lb]

    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2 + 1):
            i = int(mx * (j - y1) + x1)
            x, y = i, j
            print('x, y =', x, ',', y)
            for i in range(x - hw, x + hw + 1):
                for j in range(y - hw, y + hw + 1):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, :] = [lr, lg, lb]

    return Gambar

hasil = buat_garis(ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()
