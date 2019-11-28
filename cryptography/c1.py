import socket
import time
import sys

s = socket.socket()
port = 4488
s.connect(("", port))

print("going good")
print(s.recv(1024).decode())
s.sendall("Thank you".encode())
