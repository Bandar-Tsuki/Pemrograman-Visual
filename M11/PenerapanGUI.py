from tkinter import StringVar, Frame, Canvas, Scrollbar, VERTICAL, RIGHT, LEFT, Y, BOTH, NW
from ttkbootstrap import Window, ttk


class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Multi Operasi")
        self.root.geometry("500x500")

        self.input_vars = []
        self.hasil = StringVar()
        self.operasi = StringVar(value="Penjumlahan")

        # ==== FRAME DENGAN SCROLLBAR ====
        container = ttk.Frame(self.root)
        container.pack(fill=BOTH, expand=True)

        canvas = Canvas(container)
        scrollbar = Scrollbar(container, orient=VERTICAL, command=canvas.yview)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Frame tengah (centered content)
        self.center_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=self.center_frame, anchor="n", width=480)

        self.center_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # ==== INPUT BILANGAN ====
        self.tambah_input_field()
        self.tambah_input_field()
        ttk.Button(self.center_frame, text="Tambah Input Lagi", command=self.tambah_input_field).pack(pady=5)

        # ==== PILIHAN OPERASI ====
        ttk.Label(self.center_frame, text="Pilih Operasi:").pack()
        operasi_menu = ttk.Combobox(self.center_frame, textvariable=self.operasi, values=[
            "Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"
        ], state="readonly")
        operasi_menu.pack(pady=5)

        # ==== TOMBOL AKSI ====
        btn_frame = ttk.Frame(self.center_frame)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Hitung", style="success", command=self.hitung).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Reset", style="warning", command=self.reset).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Keluar", style="danger", command=self.root.quit).pack(side="left", padx=5)

        # ==== OUTPUT ====
        ttk.Label(self.center_frame, text="Hasil:").pack(pady=5)
        ttk.Entry(self.center_frame, textvariable=self.hasil, state="readonly").pack()

    def tambah_input_field(self):
        var = StringVar()
        self.input_vars.append(var)
        index = len(self.input_vars)
        ttk.Label(self.center_frame, text=f"Masukkan bilangan ke-{index}").pack()
        ttk.Entry(self.center_frame, textvariable=var).pack(pady=2)

    def hitung(self):
        try:
            angka = [float(var.get()) for var in self.input_vars if var.get() != ""]
            if not angka:
                self.hasil.set("Semua input kosong")
                return

            operasi = self.operasi.get()
            if operasi == "Penjumlahan":
                hasil = sum(angka)
            elif operasi == "Pengurangan":
                hasil = angka[0]
                for n in angka[1:]:
                    hasil -= n
            elif operasi == "Perkalian":
                hasil = 1
                for n in angka:
                    hasil *= n
            elif operasi == "Pembagian":
                hasil = angka[0]
                for n in angka[1:]:
                    if n == 0:
                        self.hasil.set("Error: pembagian dengan nol")
                        return
                    hasil /= n
            else:
                hasil = "Operasi tidak dikenali"

            self.hasil.set(hasil)
        except ValueError:
            self.hasil.set("Input tidak valid")

    def reset(self):
        for var in self.input_vars:
            var.set("")
        self.hasil.set("")
        self.operasi.set("Penjumlahan")


if __name__ == '__main__':
    app = Window(themename="cosmo")
    Kalkulator(app)
    app.mainloop()
