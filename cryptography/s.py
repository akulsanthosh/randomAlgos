import socket

s = socket.socket()
port = 12344
s.bind(("", port))
s.listen(5)

while True:
    c, a = s.accept()
    c.sendall("Welcome".encode())
    print(c.recv(1024).decode())
    c.close()
