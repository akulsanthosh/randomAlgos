import socket
s = socket.socket()
port = 12344
s.connect(("", port))

print(s.recv(1024).decode())
s.sendall("Thank you".encode())
s.close()
