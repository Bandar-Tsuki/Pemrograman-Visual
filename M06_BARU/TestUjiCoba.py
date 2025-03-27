import tkinter as tk
from tkinter import messagebox

# Harga tiket berdasarkan jenis film
HARGA_TIKET = {
    "Animasi": 25000,
    "Aksi": 35000,
    "Horor": 40000
}

# Batas usia untuk menonton film
BATAS_USIA = {
    "Animasi": 0,
    "Aksi": 13,
    "Horor": 17
}


# Fungsi untuk menambah jumlah tiket
def tambah_tiket():
    jumlah = int(entry_tiket["text"])
    entry_tiket["text"] = str(jumlah + 1)


# Fungsi untuk mengurangi jumlah tiket
def kurang_tiket():
    jumlah = int(entry_tiket["text"])
    if jumlah > 1:
        entry_tiket["text"] = str(jumlah - 1)


# Fungsi pemesanan tiket
def pesan_tiket():
    try:
        usia = int(entry_usia.get())
        film = var_film.get()
        jumlah_tiket = int(entry_tiket["text"])

        if usia < BATAS_USIA[film]:
            messagebox.showerror("Usia Tidak Memenuhi",
                                 f"Anda harus berusia {BATAS_USIA[film]}+ untuk menonton {film}.")
            return

        # Hitung harga tiket
        harga_tiket = HARGA_TIKET[film]
        total_harga = harga_tiket * jumlah_tiket

        # Diskon 10% jika beli lebih dari 3 tiket
        if jumlah_tiket > 3:
            total_harga *= 0.9

        # Tampilkan hasil
        hasil.set(f"Harga per Tiket: Rp {harga_tiket}\nTotal Harga: Rp {int(total_harga)}")

    except ValueError:
        messagebox.showerror("Input Tidak Valid", "Masukkan angka yang valid!")


# GUI Setup
root = tk.Tk()
root.title("Pemesanan Tiket Bioskop")
root.geometry("400x350")

tk.Label(root, text="Usia Anda:").pack(pady=5)
entry_usia = tk.Entry(root)
entry_usia.pack()

tk.Label(root, text="Pilih Jenis Film:").pack(pady=5)
var_film = tk.StringVar(value="Animasi")
tk.OptionMenu(root, var_film, *HARGA_TIKET.keys()).pack()

tk.Label(root, text="Jumlah Tiket:").pack(pady=5)

# Frame untuk counter
frame_counter = tk.Frame(root)
frame_counter.pack()

btn_kurang = tk.Button(frame_counter, text="-", command=kurang_tiket, width=3)
btn_kurang.pack(side=tk.LEFT)

entry_tiket = tk.Label(frame_counter, text="1", width=5)
entry_tiket.pack(side=tk.LEFT)

btn_tambah = tk.Button(frame_counter, text="+", command=tambah_tiket, width=3)
btn_tambah.pack(side=tk.LEFT)

tk.Button(root, text="Pesan Tiket", command=pesan_tiket).pack(pady=10)

hasil = tk.StringVar()
tk.Label(root, textvariable=hasil, fg="blue").pack()

root.mainloop()
