from tkinter import *
from tkinter import messagebox

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except ZeroDivisionError:
        messagebox.showerror("Error", "Tidak bisa membagi dengan nol!")
        expression = ""
        equation.set("")
    except SyntaxError:
        messagebox.showerror("Error", "Ekspresi tidak valid!")
        expression = ""
        equation.set("")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        expression = ""
        equation.set("")

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="#34495e")
    gui.title("Simple Calculator")
    gui.geometry("280x300")
    gui.resizable(0, 0)

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation, font=('Arial', 18, 'bold'),
                             bg="#ecf0f1", fg="#2c3e50", bd=0, justify=RIGHT)
    expression_field.grid(row=0, columnspan=4, ipadx=8, ipady=10, padx=10, pady=10, sticky="nsew")

    button_clear = Button(gui, text=' C ', fg='white', bg='#e74c3c',
                          command=clear, height=2, width=8, font=('Arial', 12, 'bold'))
    button_clear.grid(row=1, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")

    button_divide = Button(gui, text=' / ', fg='white', bg='#3498db',
                           command=lambda: press("/"), height=2, width=8, font=('Arial', 12, 'bold'))
    button_divide.grid(row=1, column=2, padx=2, pady=2, sticky="nsew")

    button_multiply = Button(gui, text=' * ', fg='white', bg='#3498db',
                             command=lambda: press("*"), height=2, width=8, font=('Arial', 12, 'bold'))
    button_multiply.grid(row=1, column=3, padx=2, pady=2, sticky="nsew")

    button7 = Button(gui, text=' 7 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(7), height=2, width=8, font=('Arial', 12, 'bold'))
    button7.grid(row=2, column=0, padx=2, pady=2, sticky="nsew")

    button8 = Button(gui, text=' 8 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(8), height=2, width=8, font=('Arial', 12, 'bold'))
    button8.grid(row=2, column=1, padx=2, pady=2, sticky="nsew")

    button9 = Button(gui, text=' 9 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(9), height=2, width=8, font=('Arial', 12, 'bold'))
    button9.grid(row=2, column=2, padx=2, pady=2, sticky="nsew")

    button_minus = Button(gui, text=' - ', fg='white', bg='#3498db',
                          command=lambda: press("-"), height=2, width=8, font=('Arial', 12, 'bold'))
    button_minus.grid(row=2, column=3, padx=2, pady=2, sticky="nsew")

    button4 = Button(gui, text=' 4 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(4), height=2, width=8, font=('Arial', 12, 'bold'))
    button4.grid(row=3, column=0, padx=2, pady=2, sticky="nsew")

    button5 = Button(gui, text=' 5 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(5), height=2, width=8, font=('Arial', 12, 'bold'))
    button5.grid(row=3, column=1, padx=2, pady=2, sticky="nsew")

    button6 = Button(gui, text=' 6 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(6), height=2, width=8, font=('Arial', 12, 'bold'))
    button6.grid(row=3, column=2, padx=2, pady=2, sticky="nsew")

    button_plus = Button(gui, text=' + ', fg='white', bg='#3498db',
                         command=lambda: press("+"), height=2, width=8, font=('Arial', 12, 'bold'))
    button_plus.grid(row=3, column=3, padx=2, pady=2, sticky="nsew")

    button1 = Button(gui, text=' 1 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(1), height=2, width=8, font=('Arial', 12, 'bold'))
    button1.grid(row=4, column=0, padx=2, pady=2, sticky="nsew")

    button2 = Button(gui, text=' 2 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(2), height=2, width=8, font=('Arial', 12, 'bold'))
    button2.grid(row=4, column=1, padx=2, pady=2, sticky="nsew")

    button3 = Button(gui, text=' 3 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(3), height=2, width=8, font=('Arial', 12, 'bold'))
    button3.grid(row=4, column=2, padx=2, pady=2, sticky="nsew")

    button_equal = Button(gui, text=' = ', fg='white', bg='#27ae60',
                          command=equalpress, height=2, width=8, font=('Arial', 12, 'bold'))
    button_equal.grid(row=4, column=3, padx=2, pady=2, sticky="nsew")

    button0 = Button(gui, text=' 0 ', fg='white', bg='#7f8c8d',
                     command=lambda: press(0), height=2, width=8, font=('Arial', 12, 'bold'))
    button0.grid(row=5, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")

    button_decimal = Button(gui, text=' . ', fg='white', bg='#7f8c8d',
                            command=lambda: press("."), height=2, width=8, font=('Arial', 12, 'bold'))
    button_decimal.grid(row=5, column=2, padx=2, pady=2, sticky="nsew")

    for i in range(4):
        gui.grid_columnconfigure(i, weight=1)
    for i in range(6):
        gui.grid_rowconfigure(i, weight=1)

    gui.mainloop()