print("\033c")
import numpy as np
import matplotlib.pyplot as plt

x1 = 100; y1 = 200
x2 = 700; y2 = 700

lw = int(10)

hw = int(lw/2)
row = 1080
col = 1920
print('col, row=',col, ',',row)

Gambar = np.zeros(shape=(row,col,3),dtype=np.int16)

for i in range(x1-hw, x1+hw):
    for j in range(y1-hw, y1+hw):
        if ((i-x1)**2 + (j-y1)**2) < hw **2:
            Gambar[j, i, 0] = 255

for i in range(x2-hw, x2+hw):
    for j in range(y2-hw, y2+hw):
        if ((i-x2)**2 + (j-y2)**2) < hw **2:
            Gambar[j, i, 0] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()