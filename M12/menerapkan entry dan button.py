# MEMBUAT GUI MENGGUNAKAN TKINTER

import tkinter as tk
from tkinter import *

# Jalankan code untuk tiap topik bergantian. Beri tanda #
# untuk topik yang #tidak dijalankan.

print('====================Exercise #1====================')
print('===Mencetak data dari Entry Widget dengan Button===')
print('===================================================')

root = tk.Tk()
root.geometry('400x200')

def CetakData():
    teks = entry1.get()
    print(teks)
    return None


entry1 = Entry(root, width=20)
entry1.pack()
Button(root, text="Cetak Data", command=CetakData).pack()

root.mainloop()

print('====================Exercise #2 dan 3==============')
print('======Mengambil Data dan Menampilkan Data==========')
print('===================================================')

import tkinter as tk
from tkinter import messagebox

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('400x200+0+0')
        frame1 = tk.Frame(self.root)
        frame1.grid()
        frame2 = tk.Frame(frame1)
        frame2.grid(row=0, column=0)
        frame3 = tk.Frame(frame1)
        frame3.grid(row=1, column=0)

        self.FirstNum = tk.StringVar()
        self.SecondNum = tk.StringVar()
        self.Hasil = tk.StringVar()

        self.lblFirstNum = tk.Label(frame2, text='Masukkan bilangan pertama')
        self.lblFirstNum.grid(row=0, column=0)

        self.txtFirstNum = tk.Entry(frame2, textvariable=self.FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = tk.Label(frame2, text='Masukkan bilangan kedua')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = tk.Entry(frame2, textvariable=self.SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblHasil = tk.Label(frame2, text='Hasil')
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = tk.Entry(frame2, textvariable=self.Hasil)
        self.txtHasil.grid(row=2, column=1)

        self.btnJumlahkan = tk.Button(frame3, text="Jumlahkan", command=self.Jumlahkan)
        self.btnJumlahkan.grid(row=2, column=0)
        self.btnReset = tk.Button(frame3, text="Reset", command=self.Reset)
        self.btnReset.grid(row=2, column=1)
        self.btnKeluar = tk.Button(frame3, text="Keluar", command=self.root.destroy)
        self.btnKeluar.grid(row=2, column=2)

    def Jumlahkan(self):
        try:
            pertama = float(self.FirstNum.get())
            kedua = float(self.SecondNum.get())
            hasil = pertama + kedua
            self.Hasil.set(str(hasil))
        except ValueError:
            messagebox.showerror('Error', 'Masukkan angka yang valid')

    def Reset(self):
        self.FirstNum.set('')
        self.SecondNum.set('')
        self.Hasil.set('')


if __name__ == '__main__':
    root = tk.Tk()
    application = DataInOut(root)
    root.mainloop()
