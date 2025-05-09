import tkinter as tk

root = tk.Tk()
root.title("contoh place")

label = tk.Label(root, text="Label")
label.place(x=50, y=50)
root.mainloop()