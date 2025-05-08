from tkinter import *

main = Tk()
ourMessage = 'ini pesan saya'
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='pink')
messageVar.pack()
main.mainloop()