import tkinter as tk

def on_key_press(event):
    status_label.config(text=f"Tombol ditekan: {event.keysym}")
    print(f"Key pressed: {event.keysym}")

def on_left_click(event):
    status_label.config(text=f"Klik kiri di ({event.x}, {event.y})")
    print(f"Left click at ({event.x}, {event.y})")

def on_right_click(event):
    status_label.config(text=f"Klik kanan di ({event.x}, {event.y})")
    print(f"Right click at ({event.x}, {event.y})")

def on_mouse_motion(event):
    status_label.config(text=f"Mouse di ({event.x}, {event.y})")
    print(f"Mouse moved to ({event.x}, {event.y})")

root = tk.Tk()
root.title("Contoh Event Handling Lanjut")
root.geometry("400x300")

status_label = tk.Label(root, text="Arahkan mouse atau tekan tombol...", anchor="w")
status_label.pack(side=tk.BOTTOM, fill=tk.X)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<KeyPress>", on_key_press)
canvas.bind("<Button-1>", on_left_click)
canvas.bind("<Button-3>", on_right_click)
canvas.bind("<Motion>", on_mouse_motion)

canvas.focus_set()

root.mainloop()
