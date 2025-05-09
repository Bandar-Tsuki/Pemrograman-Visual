import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()
root.title("Contoh Button Lanjut")
root.geometry("400x300")

# Creating a button with specified options
button = tk.Button(root,
                   text="Klik Akuh",
                   command=button_clicked,
                   activebackground="red",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Consolar", 14),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()