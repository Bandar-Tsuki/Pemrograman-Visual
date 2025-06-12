import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator Sederhana")
        master.geometry("300x400") # Mengatur ukuran jendela
        master.resizable(0, 0) # Mencegah perubahan ukuran jendela

        self.expression = ""
        self.input_text = tk.StringVar()

        # Input field/Display
        self.input_frame = self.create_input_frame()
        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'),
                                    textvariable=self.input_text, width=20, bg="#eee",
                                    bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0, ipady=10)
        self.input_field.pack(expand=True, fill='both')

        # Buttons frame
        self.buttons_frame = self.create_buttons_frame()

        # Layout untuk tombol
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',
        ]
        self.row = 0
        self.col = 0
        for button in self.buttons:
            self.create_button(button)

        self.create_equals_button()

    def create_input_frame(self):
        frame = tk.Frame(self.master, bd=0, relief=tk.RIDGE, bg="lightblue")
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.master, bg="lightgray")
        frame.pack(expand=True, fill='both')
        return frame

    def create_button(self, char):
        if char == 'C':
            button = tk.Button(self.buttons_frame, text=char, font=('arial', 14, 'bold'),
                               relief=tk.RIDGE, bd=1, padx=20, pady=20,
                               command=lambda: self.clear_input())
        elif char in ['/', '*', '-', '+']:
            button = tk.Button(self.buttons_frame, text=char, font=('arial', 14, 'bold'),
                               relief=tk.RIDGE, bd=1, padx=20, pady=20, fg="blue",
                               command=lambda: self.button_click(char))
        else:
            button = tk.Button(self.buttons_frame, text=char, font=('arial', 14, 'bold'),
                               relief=tk.RIDGE, bd=1, padx=20, pady=20,
                               command=lambda: self.button_click(char))

        button.grid(row=self.row, column=self.col, sticky="nsew", padx=1, pady=1)
        self.col += 1
        if self.col > 3:
            self.col = 0
            self.row += 1

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', font=('arial', 14, 'bold'),
                           relief=tk.RIDGE, bd=1, padx=20, pady=20, bg="lightgreen",
                           command=lambda: self.calculate_result())
        button.grid(row=self.row, column=self.col, columnspan=4, sticky="nsew", padx=1, pady=1)

    def button_click(self, char):
        self.expression += str(char)
        self.input_text.set(self.expression)

    def clear_input(self):
        self.expression = ""
        self.input_text.set("")

    def calculate_result(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            messagebox.showerror("Error", "Tidak bisa membagi dengan nol!")
            self.expression = ""
            self.input_text.set("")
        except SyntaxError:
            messagebox.showerror("Error", "Input tidak valid!")
            self.expression = ""
            self.input_text.set("")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
            self.expression = ""
            self.input_text.set("")

if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()