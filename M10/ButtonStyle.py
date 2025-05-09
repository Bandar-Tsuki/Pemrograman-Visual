from tkinter import *
from tkinter.ttk import *

def klik_aku():
    print("Tombol 'Klik Aku' ditekan!")

# Buat jendela utama
root = Tk()
root.title("Button Dengan Style")
root.geometry("200x200")

# Buat style tombol khusus
style = Style()
style.configure('W.TButton',
                font=('Consolas', 12, 'bold', 'underline'),
                foreground='red')

# Tombol Quit
btn1 = Button(root, text='Quit!',
              style='W.TButton',
              command=root.destroy)
btn1.grid(row=0, column=0, padx=50, pady=20)

# Tombol Klik Aku
btn2 = Button(root, text='Klik Aku',
              style='W.TButton',
              command=klik_aku)
btn2.grid(row=1, column=0, padx=50, pady=10)

root.mainloop()
