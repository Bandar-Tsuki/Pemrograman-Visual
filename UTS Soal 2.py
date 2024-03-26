import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 10000)

plt.figure(figsize=(8, 6.5))

y1 = (24 - x ** 2) ** 0.5
y2 = -(24 - x ** 2) ** 0.5
y3 = 4 + (4 - (x - 4) ** 2) ** 0.5
y4 = 4 - (4 - (x - 4) ** 2) ** 0.5
y5 = -4 + (4 - (x - 4) ** 2) ** 0.5
y6 = -4 - (4 - (x - 4) ** 2) ** 0.5
y7 = 4 + (4 - (x + 4) ** 2) ** 0.5
y8 = 4 - (4 - (x + 4) ** 2) ** 0.5
y9 = -4 + (4 - (x + 4) ** 2) ** 0.5
y10 = -4 - (4 - (x + 4) ** 2) ** 0.5
y11 = 6 + (4 - x ** 2) ** 0.5
y12 = 6 - (4 - x ** 2) ** 0.5
y13 = - 6 + (4 - x ** 2) ** 0.5
y14 = - 6 - (4 - x ** 2) ** 0.5
y15 = (4 - (x - 6) ** 2) ** 0.5
y16 = -(4 - (x - 6) ** 2) ** 0.5
y17 = (4 - (x + 6) ** 2) ** 0.5
y18 = -(4 - (x + 6) ** 2) ** 0.5

plt.plot(x, y1, '-r')
plt.plot(x, y2, '-r', label='bunga')

for y in (y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18):
    plt.plot(x, y, color='#4aa0f0')

for y in (y1, y2):
    plt.fill_between(x, y, color='pink')

plt.fill_between(x, y3, y4, color='#ec33e3')
plt.fill_between(x, y5, y6, color='#ec33e3')
plt.fill_between(x, y7, y8, color='#ec33e3')
plt.fill_between(x, y9, y10, color='#ec33e3')
plt.fill_between(x, y11, y12, color='#ec33e3')
plt.fill_between(x, y13, y14, color='#ec33e3')
plt.fill_between(x, y15, y16, color='#ec33e3')
plt.fill_between(x, y17, y18, color='#ec33e3')

plt.legend(loc='upper left')
plt.grid()

plt.show()

"""
1. Import Library:

matplotlib.pyplot as plt: Library ini diimpor untuk membuat dan menampilkan visualisasi, khususnya gambar.
numpy as np: Library ini diimpor untuk perhitungan numerik dan manipulasi array, digunakan di sini untuk membuat array gambar.

2. Mendefinisikan Nilai Sumbu x:

x = np.linspace(-8, 8, 10000)

Baris ini membuat array bernama `x` yang berisi 10.000 nilai yang tersebar merata antara -8 dan 8. Array ini mewakili sumbu horizontal (x) dari plot.

3. Mendefinisikan Fungsi Matematika (y1 hingga y18):

python
y1 = (24 - x ** 2) ** 0.5
y2 = -(24 - x ** 2) ** 0.5
... (definisi serupa untuk y3 hingga y18)

Bagian ini mendefinisikan 18 fungsi matematika menggunakan variabel `x`. Ekspresinya melibatkan pemangkatan `x` kuadrat, pengurangan dengan konstanta (`24` dalam contoh), dan pengambilan akar kuadrat. Nilai yang dihasilkan (`y1` hingga `y18`) akan digunakan untuk membuat bentuk setengah lingkaran pada plot.

4. Membuat Plot Garis (y):

plt.plot(x, y1, '-r')
plt.plot(x, y2, '-r', label='bunga')

for y in (y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18):
    plt.plot(x, y, color='#4aa0f0')


Baris ini membuat dua plot garis merah (`-r`) pada grafik. Menggunakan nilai x dan y dari `y1` dan `y2`. Baris kedua juga menambahkan label "bunga" ke legenda.

Lalu menggunakan pengulangan untuk fungsi `y3` hingga `y18`. Untuk setiap fungsi `y`, dibuat plot garis menggunakan nilai x dan y dengan warna tertentu yang ditentukan oleh kode heksadesimal `#4aa0f0`.

5. Mewarnai Area Antar Garis (y):

for y in (y1, y2):
    plt.fill_between(x, y, color='pink')

plt.fill_between(x, y3, y4, color='#ec33e3')
# ... (fill_between serupa untuk fungsi lainnya)

Looping ini mewarnai area antara garis yang dibuat dari `y1` dan `y2` dengan warna pink.

Baris ini menggunakan `plt.fill_between` untuk mewarnai area antara pasangan fungsi tertentu (`y3` dan `y4`, dll.) dengan warna yang ditentukan oleh kode heksadesimal `#ec33e3`.

6. Menambahkan Legenda dan Grid:

plt.legend(loc='upper left')` menambahkan legenda ke plot di sudut kiri atas, berguna untuk mengidentifikasi garis dan bentuk yang berbeda.
plt.grid()` menambahkan garis grid ke plot untuk visualisasi yang lebih baik.

7. Menampilkan Gambar

plt.show()

Baris ini menampilkan plot final dengan semua elemen yang dibuat.
"""
