import matplotlib.pyplot as plt
import numpy as np

row = int(800)
col = int(1300)

# buat persegi biru tua
DBrow1 = int(0.25*row)
DBrow2 = int(0.375*row)
DBcol1 = int(0.230769*col)
DBcol2 = int(0.846153*col)

# buat persegi biru cukup tua
Brow1 = int(0.375*row)
Brow2 = int(0.75*row)
Bcol1 = int(0.230769*col)
Bcol2 = int(0.846153*col)

Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
for i in range(DBrow1, DBrow2):
    for j in range(DBcol1, DBcol2):
        Gambar[i, j, 2] = 98

for i in range(Brow1, Brow2):
    for j in range(Bcol1, Bcol2):
        Gambar[i, j, 2] = 178

plt.figure()
plt.imshow(Gambar)
plt.show()