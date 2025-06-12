import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


class TemperatureConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Konverter Suhu Inovatif")
        self.master.geometry("450x380")
        self.master.resizable(False, False)
        # Baris ini dihapus karena tidak lagi diperlukan atau menyebabkan AttributeError
        # self.master.tk.call("source", ttk.utility.ThemeManager.get_style_path())
        self.master.config(bg="#2c3e50")  # Latar belakang gelap, mungkin tidak terlalu terlihat dengan tema gelap

        # Variabel kontrol
        self.temperature_input = tk.StringVar()
        self.converted_temperature = tk.StringVar()
        self.conversion_type = tk.StringVar(value="C_to_F")  # Default: Celsius ke Fahrenheit

        self.create_widgets()

    def create_widgets(self):
        # Frame utama
        # Menggunakan 'secondary' atau 'dark' untuk frame agar kontras dengan tema 'darkly'
        main_frame = ttk.Frame(self.master, padding=20, style="secondary")
        main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

        # Judul Aplikasi
        ttk.Label(main_frame, text="Konverter Suhu", font=("Helvetica Neue", 24, "bold"),
                  style="primary").pack(pady=(0, 20))

        # Pilihan Konversi (Radiobuttons)
        conversion_frame = ttk.Frame(main_frame)
        conversion_frame.pack(pady=10)

        ttk.Radiobutton(conversion_frame, text="Celsius ke Fahrenheit",
                        variable=self.conversion_type, value="C_to_F",
                        style="info-round-toggle", command=self.reset_fields).pack(side=LEFT, padx=10)
        ttk.Radiobutton(conversion_frame, text="Fahrenheit ke Celsius",
                        variable=self.conversion_type, value="F_to_C",
                        style="info-round-toggle", command=self.reset_fields).pack(side=LEFT, padx=10)

        # Input Suhu
        ttk.Label(main_frame, text="Masukkan Suhu:", font=("Helvetica", 14),
                  style="inverse-secondary").pack(pady=(10, 5))  # Ubah style agar lebih terlihat

        # Entry dengan validasi angka
        self.temp_entry = ttk.Entry(main_frame, textvariable=self.temperature_input,
                                    width=25, font=("Helvetica", 16), justify="center",
                                    style="info")
        self.temp_entry.pack(pady=5)
        self.temp_entry.bind("<KeyRelease>", self.validate_input)

        # Tombol Konversi
        ttk.Button(main_frame, text="Konversi", command=self.convert_temperature,
                   style="success-outline", width=15).pack(pady=15)

        # Hasil Konversi
        ttk.Label(main_frame, text="Hasil Konversi:", font=("Helvetica", 14),
                  style="inverse-secondary").pack(pady=(10, 5))  # Ubah style agar lebih terlihat

        self.result_label = ttk.Label(main_frame, textvariable=self.converted_temperature,
                                      font=("Helvetica", 22, "bold"), style="primary")
        self.result_label.pack(pady=5)

        # Tombol Reset
        ttk.Button(main_frame, text="Reset", command=self.reset_fields,
                   style="danger-outline", width=10).pack(pady=(15, 0))

    def validate_input(self, event=None):
        current_text = self.temperature_input.get()
        new_text = ""
        has_decimal = False

        for char in current_text:
            if char.isdigit():
                new_text += char
            elif char == '.' and not has_decimal:
                new_text += char
                has_decimal = True
            elif char == '-' and not new_text and len(
                    current_text) > 1:  # Izinkan minus di awal, tapi tidak jika hanya '-'
                new_text += char
            elif char == '-' and not new_text and len(current_text) == 1:  # Izinkan minus sebagai input tunggal awal
                new_text += char

        # Perbaikan: jika input hanya '-' atau '.', tidak valid untuk konversi
        if new_text == '-' or new_text == '.':
            self.temperature_input.set(new_text)
            return

        self.temperature_input.set(new_text)

    def convert_temperature(self):
        try:
            temp_str = self.temperature_input.get()
            if not temp_str or temp_str == '-' or temp_str == '.':  # Tambahkan kondisi untuk '-' atau '.' saja
                messagebox.showwarning("Input Kosong/Invalid", "Mohon masukkan nilai suhu yang valid.")
                return

            temperature = float(temp_str)
            result = 0.0
            unit = ""

            if self.conversion_type.get() == "C_to_F":
                result = (temperature * 9 / 5) + 32
                unit = "°F"
            else:  # F_to_C
                result = (temperature - 32) * 5 / 9
                unit = "°C"

            self.converted_temperature.set(f"{result:.2f} {unit}")
            self.update_result_style(result)
        except ValueError:
            messagebox.showerror("Input Invalid", "Mohon masukkan angka yang valid.")
            self.reset_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
            self.reset_fields()

    def update_result_style(self, temperature):
        if self.conversion_type.get() == "C_to_F":
            # Untuk Fahrenheit
            if temperature <= 32:
                self.result_label.config(style="info")
            elif temperature >= 212:
                self.result_label.config(style="danger")
            else:
                self.result_label.config(style="success")
        else:
            # Untuk Celsius
            if temperature <= 0:
                self.result_label.config(style="info")
            elif temperature >= 100:
                self.result_label.config(style="danger")
            else:
                self.result_label.config(style="success")

    def reset_fields(self):
        self.temperature_input.set("")
        self.converted_temperature.set("")
        self.result_label.config(style="primary")
        self.temp_entry.focus_set()


if __name__ == "__main__":
    app_window = ttk.Window(themename="darkly")  # Menggunakan tema 'darkly' yang elegan
    TemperatureConverterApp(app_window)
    app_window.mainloop()