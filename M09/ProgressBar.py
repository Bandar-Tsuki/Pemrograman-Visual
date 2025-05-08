import tkinter as tk
from tkinter import ttk

def start_progress():
    progress['value'] = 0  # Reset nilai
    increment_progress(0)

def increment_progress(value):
    if value <= 100:
        progress['value'] = value
        root.after(50, increment_progress, value + 1)  # Delay 50ms per step

# Membuat window utama
root = tk.Tk()
root.title("Contoh Progressbar")
root.geometry("400x150")

# Membuat Progressbar
progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress.pack(pady=20)

# Membuat Tombol untuk Memulai Progress
btn_mulai = tk.Button(root, text="Mulai", command=start_progress)
btn_mulai.pack()

# Menjalankan aplikasi
root.mainloop()
