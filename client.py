import socket
from socket import AF_INET, SOCK_STREAM
from threading import Thread
from tkinter import *

class ChatIO:
    def __init__(self, root):
        self.client_socket = None
        self.root = root
        self.root.title("ChatIO")
        self.firstclick = True

        self.messages_frame = Frame(self.root)
        self.my_msg = StringVar()
        self.my_msg.set("Type your messages here.")
        self.scrollbar = Scrollbar(self.messages_frame)
        self.msg_list = Listbox(self.messages_frame, height=15, width=50, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.msg_list.pack(side=LEFT, fill=BOTH)
        self.messages_frame.pack()

        self.entry_field = Entry(self.root, textvariable=self.my_msg)
        self.entry_field.bind('<FocusIn>', self.on_entry_click)
        self.entry_field.bind("<Return>", self.send)
        self.entry_field.pack()
        self.send_button = Button(self.root, text="Send", command=self.send)
        self.send_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_entry_click(self, event):
        if self.firstclick:
            self.firstclick = False
            self.entry_field.delete(0, "end")

    def receive(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode("utf8")
                self.msg_list.insert(END, msg)
            except OSError:
                break

    def send(self, event=None):
        msg = self.my_msg.get()
        self.my_msg.set("")
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.client_socket.close()
            self.root.quit()

    def on_closing(self, event=None):
        self.my_msg.set("{quit}")
        self.send()

if __name__ == "__main__":
    HOST = input('Enter host: ')
    PORT = input('Enter port: ')
    if not PORT:
        PORT = 33002
    else:
        PORT = int(PORT)

    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    try:
        client_socket = socket.socket(AF_INET, SOCK_STREAM)
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client_socket.connect(ADDR)
    except socket.gaierror:
        print("Error: Unable to resolve hostname or IP address.")
        exit(1)

    root = Tk()
    chat_io = ChatIO(root)
    chat_io.client_socket = client_socket
    receive_thread = Thread(target=chat_io.receive)
    receive_thread.start()
    root.mainloop()