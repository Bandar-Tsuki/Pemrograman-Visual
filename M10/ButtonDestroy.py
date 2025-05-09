from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Contoh Button Destroy")
root.geometry("400x300")

btn = Button(root, text='JANGAN KLIK AKU!',
             command=root.destroy)

btn.pack(side='bottom')

root.mainloop()
