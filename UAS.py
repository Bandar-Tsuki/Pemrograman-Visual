import os
import random
import tkinter as tk
from tkinter import filedialog


class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title
        self.title("Aplikasi Chat Desktop")

        # Create message area
        self.message_area = tk.Text(
            self,
            font=("Helvetica", 12),
            bg="white",
            fg="black"
        )
        self.message_area.pack(fill=tk.BOTH, expand=True)

        # Create input frame
        input_frame = tk.Frame(self, bg="lightgray")
        input_frame.pack(pady=10)

        # Create entry for message
        self.entry = tk.Entry(
            input_frame,
            font=("Helvetica", 12),
            bg="white",
            fg="black"
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Create send button
        send_button = tk.Button(
            input_frame,
            text="Kirim",
            command=self.send_message,
            font=("Helvetica", 12),
            bg="dodgerblue",
            fg="white"
        )
        send_button.pack(side=tk.LEFT)

        # Create user list
        self.user_list = tk.Listbox(
            self,
            font=("Helvetica", 12),
            bg="white",
            fg="black"
        )
        self.user_list.insert(tk.END, "User 1")
        self.user_list.insert(tk.END, "User 2")
        self.user_list.insert(tk.END, "User 3")
        self.user_list.pack(pady=10)

        # Create file selection button
        self.select_file_button = tk.Button(
            input_frame,
            text="Pilih File",
            command=self.select_file,
            font=("Helvetica", 12),
            bg="lightgray",
            fg="black"
        )
        self.select_file_button.pack(side=tk.LEFT)

        # Initialize file path
        self.file_path = None

    def send_message(self):
        message = self.entry.get()

        if message:
            if self.user_list.curselection():  # Check if a user is selected
                selected_user = self.user_list.get(self.user_list.curselection()[0])
                self.message_area.insert(tk.END, f"Saya -> {selected_user}: {message}\n", ("user",))
                self.entry.delete(0, tk.END)

                if random.random() < 0.5:  # 50% chance of a response
                    response = f"{selected_user}: Terima kasih atas pesan Anda!"
                    self.message_area.insert(tk.END, f"{response}\n", ("response",))

                if self.file_path:
                    self.message_area.insert(tk.END, f"Saya -> {selected_user}: File {os.path.basename(self.file_path)}\n", ("file",))
                    self.file_path = None  # Clear file selection
            else:
                print("Please select a user to send the message to.")

    def select_file(self):
        self.file_path = filedialog.askopenfilename()


if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()