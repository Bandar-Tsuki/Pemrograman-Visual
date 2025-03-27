# Memasukkan nilai a dan b dari pengguna
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

# Cek dengan boolean apakah a lebih besar dari b
print("Apakah a lebih besar dari b?", a > b)

# Cek dengan boolean apakah b lebih besar dari a
print("Apakah b lebih besar dari a?", b > a)

# Cek dengan boolean apakah a sama dengan b
print("Apakah a sama dengan b?", a == b)

# Hitung PPN untuk a jika lebih dari 10000
ppn_a = 0
if a > 10000:
    ppn_a = 0.12 * a

# Hitung PPN untuk b jika lebih dari 50000
ppn_b = 0
if b > 50000:
    ppn_b = 0.12 * b

# Cetak PPN masing-masing
print("PPN a:", ppn_a)
print("PPN b:", ppn_b)

# Tambahkan kedua PPN a dan b
total_ppn = ppn_a + ppn_b

# Cek total PPN dengan boolean -> True jika ada nilai
print("Apakah total PPN lebih dari 0?", bool(total_ppn))

# Hapus a dan b
del a
del b

# Cek apakah a dan b masih ada dengan try-except
try:
    print(bool(a))
except NameError:
    print("Variabel a sudah dihapus, nilainya False.")

try:
    print(bool(b))
except NameError:
    print("Variabel b sudah dihapus, nilainya False.")
