from tkinter import *

top = Tk ()
mb = Menubutton(top, text = "Menu")
mb.grid()
mb.menu = Menu (mb, tearoff = 0)
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
oVar = IntVar()
mb.menu.add_checkbutton(label='Contract', variable=cVar)
mb.menu.add_checkbutton(label='About', variable=aVar)
mb.menu.add_checkbutton(label='Close', variable=oVar)
mb.pack()
top.mainloop()