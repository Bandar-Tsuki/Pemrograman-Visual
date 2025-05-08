from tkinter import *

master = Tk()
w = Canvas(master, width=75, height=100)
w.pack()

canvas_heights=100
canvas_width=75

y = int(canvas_heights/2)
w.create_line(0, y, canvas_width, y)
mainloop()