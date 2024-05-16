import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
data = [
   ["Arle",500,19200],
   ["Chino",310,25000],
   ["Nadine",180,29000],
   ["Eleine",220,39500],
]
index=0
def read_data():
   for index, line in enumerate(data):
      tree.insert('', tk.END, iid = index,
         text = line[0], values = line[1:])
columns = ("age", "salary")

tree= ttk.Treeview(root, columns=columns ,height = 20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text='Name')
tree.heading('age', text='Age')
tree.heading('salary', text='Salary')

read_data()
root.mainloop()