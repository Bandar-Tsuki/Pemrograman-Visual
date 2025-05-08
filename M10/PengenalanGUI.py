# CREATING GUI USING TKINTER
import tkinter as tk

# Jalankan code untuk tiap topik bergantian. Komentari bagian yang tidak digunakan

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Latihan GUI Tkinter")
root.geometry("800x600")  # Ukuran default

# ========================================================================
# ------------------------ Latihan-2: Membuat Canvas ------------------------
# ========================================================================
canvas_utama = tk.Canvas(root, height=300, width=600, bg='lightgray')
canvas_utama.pack(pady=10)

# ========================================================================
# ------------------------ Latihan-3: Membuat Frame ------------------------
# ========================================================================
frame_utama = tk.Frame(root, bg='blue')
frame_utama.place(relwidth=0.9, relheight=0.5, relx=0.05, rely=0.4)

# ========================================================================
# ------------------------ Latihan-4a: Membuat Button Di Root ------------------------
# ========================================================================
tombol_di_root = tk.Button(root, text="Tombol di Root", bg='gray', fg='red')
tombol_di_root.pack(pady=5)

# ========================================================================
# ------------------------ Latihan-4b: Membuat Button Di Frame ------------------------
# ========================================================================
tombol_di_frame = tk.Button(frame_utama, text="Tombol di Frame", bg='gray', fg='red')
tombol_di_frame.pack(pady=10)

# ========================================================================
# ------------------------ Latihan-5: Membuat Entry ------------------------
# ========================================================================
entry_di_frame = tk.Entry(frame_utama, bg='green')
entry_di_frame.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
