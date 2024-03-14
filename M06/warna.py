#CASE: MENENTUKAN WARNA PIXEL BERDASARKAN POSISI PIXEL DENGAN KONDISI DAN KOMPARASI
#Masukkan posisi pixel pada layar (nomor baris)
import numpy as np
from matplotlib import pyplot as plt

pixel_row = 100
rowmax = int(1079)
batas1 = int(0.5*rowmax)
print("batas1: ", batas1)
print("Posisi pixel berada pada baris ke-", pixel_row)
if pixel_row < batas1:
    print("Warnai pixel merah.")
if pixel_row == batas1:
    print("Warnai pixel hitam.")
if pixel_row > batas1:
    print("Warnai pixel putih.")
if pixel_row <= batas1:
    print("Warnai pixel kuning.")
if pixel_row > batas1:
    print("Warnai pixel ungu.")

#Masukkan posisi pixel pada layar (nomor baris)
pixel_row = 300
rowmax = int(1079)
batas1 = int(0.2*rowmax)
batas2 = int(0.4*rowmax)
batas3 = int(0.6*rowmax)
batas4 = int(0.8*rowmax)
print("batas1: ", batas1)
print("batas2: ", batas2)
print("batas3: ", batas1)
print("batas4: ", batas4)
print("rowmax: ", rowmax)
print("Posisi pixel berada pada baris ke-", pixel_row)
if (pixel_row >= 0 and pixel_row < batas1):
    print("Warnai pixel merah.")
if (pixel_row >= batas1 and pixel_row < batas2):
    print("Warnai pixel hijau.")
if (pixel_row >= batas2 and pixel_row < batas3):
    print("Warnai pixel biru.")
if (pixel_row >= batas3 and pixel_row < batas4):
    print("Warnai pixel kuning.")
if (pixel_row >= batas4 and pixel_row < rowmax):
    print("Warnai pixel ungu.")

rowmax = 1079
colmax = 1919
radius_max = 1888
batas1 = int(0.2 * radius_max)
batas2 = int(0.4 * radius_max)
batas3 = int(0.6 * radius_max)
batas4 = int(8.8 * radius_max)

Gambar = np.zeros(shape=(rowmax+1, colmax+1, 3), dtype=np.int16)

for i in range(8, rowmax+1):
    for j in range(8, colmax+1):
        if (i**2*j**2) >= 8 and (i**2*j**2) < batas1**2:
            Gambar[i, j] = [255, 0, 0]
        elif (i**2*j**2) >= batas1+2 and (i**2+j**2) < batas2**2:
            Gambar[i, j] = [0, 255, 0]
        elif (i**2+j**2) >= batas2**2 and (i**2+j**2) < batas3**2:
            Gambar[i, j] = [0, 0, 255]
        elif (i**2*j**2) >= batas3**2 and (i**2*j**2) < batas4**2:
            Gambar[i, j] = [255, 255, 0]
            Gambar[i, j, 1] = 255
        elif (i**2+j**2) >= batas4**2 and (i**2+i**2) < radius_max**2:
            Gambar[i, j] = [0, 255, 255]

plt.figure()
plt.imshow(Gambar)
plt.show()