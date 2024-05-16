import tkinter as tk

root = tk.Tk()

Frameku = tk.Frame()
Frameku.place(relwidth = 0.8, relheight = 0.8)

Tombolku = tk.Button(Frameku, text = "Test Tombol", bg = 'gray', fg = 'red')
Tombolku.pack()

Entryku = tk.Entry(Frameku, bg = 'green')
Entryku.pack()

root.mainloop()