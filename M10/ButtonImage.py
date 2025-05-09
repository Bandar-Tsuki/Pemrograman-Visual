from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()
root.title("Button Dengan Image")
root.geometry("600x600")

# Adding widgets to the root window
Label(root, text='GAS LOGIN', font=('Consolas', 15)).pack(side=TOP, pady=10)

# Creating a photoimage object to use image
photo = PhotoImage(file=r"C:\Users\fillo\OneDrive\Pictures\plogin.png")

# here, image option is used to
# set image on button
Button(root, text='KLIK AKU!', image=photo).pack(side=TOP)

mainloop()
