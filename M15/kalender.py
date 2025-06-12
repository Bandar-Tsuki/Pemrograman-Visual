from tkinter import *
import calendar
from tkinter import messagebox


def showcal():
    new_gui = Tk()
    new_gui.config(background="white")
    new_gui.title("Calendar")
    new_gui.geometry("600x600")

    try:
        fetch_year = int(year_field.get())
        cal_content = calendar.calendar(fetch_year)

        cal_year = Label(new_gui, text=cal_content, font=("Courier New", 12), justify=LEFT)
        cal_year.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        new_gui.grid_rowconfigure(0, weight=1)
        new_gui.grid_columnconfigure(0, weight=1)

    except ValueError:
        messagebox.showerror("Error Input", "Tahun harus berupa angka!")
        new_gui.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        new_gui.destroy()

    new_gui.mainloop()


if __name__ == '__main__':
    gui = Tk()

    gui.config(background="white")
    gui.title("KALENDER")
    gui.geometry("250x250")
    gui.resizable(False, False)

    cal = Label(gui, text="KALENDER", bg="dark gray", font=("times", 28, "bold"))
    year = Label(gui, text="Enter Year", bg="light green")

    year_field = Entry(gui)

    Show = Button(gui, text="Tampilkan", fg="white", bg="green", command=showcal)

    Exit = Button(gui, text="Keluar", fg="white", bg="red", command=gui.destroy)

    cal.grid(row=0, column=0, columnspan=2, pady=10)
    year.grid(row=1, column=0, pady=5, sticky=E)
    year_field.grid(row=1, column=1, pady=5, sticky=W)
    Show.grid(row=2, column=0, columnspan=2, pady=10)
    Exit.grid(row=3, column=0, columnspan=2, pady=5)

    gui.grid_rowconfigure(0, weight=1)
    gui.grid_rowconfigure(1, weight=1)
    gui.grid_rowconfigure(2, weight=1)
    gui.grid_rowconfigure(3, weight=1)
    gui.grid_columnconfigure(0, weight=1)
    gui.grid_columnconfigure(1, weight=1)

    gui.mainloop()