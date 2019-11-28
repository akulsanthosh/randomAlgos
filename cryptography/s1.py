import socket
import threading

s = socket.socket()
port = 4488
s.bind(("", port))
s.listen(5)


def createClient(c):
    print("here also")
    c.sendall("Welcome".encode())
    print(c.recv(1024).decode())


while True:
    c, a = s.accept()
    print("here")
    threading.Thread(target=createClient, args=(c,))
