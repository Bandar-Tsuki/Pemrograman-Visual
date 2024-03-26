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

"""
nomor 1
1. Import Library:

matplotlib.pyplot as plt: Library ini diimpor untuk membuat dan menampilkan visualisasi, khususnya gambar.
numpy as np: Library ini diimpor untuk perhitungan numerik dan manipulasi array, digunakan di sini untuk membuat array gambar.

2. Dimensi Gambar:

row = int(800): Mengatur jumlah baris (tinggi) gambar menjadi 800 piksel.
col = int(1300): Mengatur jumlah kolom (lebar) gambar menjadi 1300 piksel.

3. Mendefinisikan Dimensi Persegi:

DBrow1, DBrow2, DBcol1, DBcol2: Mendefinisikan indeks baris dan kolom awal dan akhir untuk persegi pertama.
Brow1, Brow2, Bcol1, Bcol2: Mendefinisikan indeks baris dan kolom awal dan akhir untuk persegi kedua.

4. Membuat Array Gambar:

Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8): Membuat array 3 dimensi berisi nol, mewakili gambar hitam dengan 800 baris, 1300 kolom, dan 3 channel warna (untuk nilai merah, hijau, dan biru).

5. Mengisi Persegi:

Dua loop for pertama: Melakukan perulangan melalui piksel di dalam koordinat persegi pertama (biru tua).
Dua loop for kedua: Melakukan perulangan melalui piksel di dalam koordinat persegi kedua (biru cukup muda).

6. Menampilkan Gambar:

plt.figure(): Membuat jendela figure baru untuk gambar.
plt.imshow(Gambar): Menampilkan array Gambar sebagai gambar di dalam jendela figure itu.
plt.show(): Menampilkan jendela figure yang dibuat, secara efektif menampilkan gambar akhir.
"""
