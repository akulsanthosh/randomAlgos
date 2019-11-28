import socket as soc

s = soc.socket()  # socket object

port = 12348  # port address
s.connect(('', port))
# connection to server ip
# recv fn to get stuff atmost 1024 bytes data can be recieved
while(True):
    i = input("Enter something : ")
    s.sendall(i.encode())
    print(s.recv(1024).decode())
s.close()
