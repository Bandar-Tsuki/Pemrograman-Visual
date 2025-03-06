import socket
from socket import AF_INET, SOCK_STREAM
from threading import Thread
import sys

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print(f"{client_address} has connected.")
        client.sendall(b"Greetings from the cave! Now type your name and press enter!")
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = f'Welcome {name}! If you ever want to quit, type {{quit}} to exit.'
    client.sendall(welcome.encode("utf8"))
    msg = f"{name} has joined the chat!"
    broadcast(msg.encode("utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg!= b"{quit}":
            broadcast(msg, f"{name}: ".encode("utf8"))
        else:
            client.sendall(b"{quit}")
            client.close()
            del clients[client]
            if not clients:
                SERVER.close()
                sys.exit(0)
            broadcast(f"{name} has left the chat.".encode("utf8"))
            break


def broadcast(msg, prefix=b""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.sendall(prefix + msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33002
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket.socket(AF_INET, SOCK_STREAM)
SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()