# Case 1
print("Case 1")
# Data bertipe Boolean yang Kita Deklarasikan (Cara Standar)
f = bool(True)
g = bool(False)
print(f)
print(g)
print("===================================")

# Case 2
print("Case 2")
# Data Bertipe Boolean Dalam Berbagai Konteks
# Tercatat Dengan Sendirinya oleh Komputer tanpa Deklarasi.
print(3 > 2)
print(3 + 2 == 5)
print(3 < 2)
print("===================================")

# Case 3
print("Case 3")
# Data Bertipe Boolean Dalam Berbagai Konteks
# Tercatat Dengan Sendirinya oleh Komputer tanpa Deklarasi.
Penghasilan = 2000000
PenghasilanTanpaPajak = 4000000
PajakYangHarusDibayar = 0  # Nilai default

if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan

print("Pajak yang harus Anda bayar: Rp", PajakYangHarusDibayar)
if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan
print("Pajak yang harus Anda bayar: Rp ", PajakYangHarusDibayar)

# PART 2
# Case 4
print("Case 4")
# Semua data yang tidak nol (kosong) memiliki nilai Boolean True

a = 3  # integer
b = "Ini data string."  # string
c = ("laptop", "buku", "ballpen")  # tuple
d = ["laptop", "buku", "ballpen"]  # list
e = {"laptop": "asus", "buku": "buku_teks", "ballpen": "arrow"}  # dictionary
f = {1, 2, 3, 4, 5}  # set

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("===================================")

# PART 3
# Case 5
print("Case 5")
# Variabel yang kosong memiliki nilai Boolean False

a = 0  # integer null
b = ""  # string kosong
c = ()  # tuple kosong
d = []  # list kosong
e = {}  # dictionary/set kosong

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("===================================")

# Case 6
print("Case 6")
# Variabel yang panjangnya nol memiliki nilai Boolean False

class myClass():
    def __len__(self):
        return 0

print(bool(myClass()))
print("===================================")
