import socket as soc

s = soc.socket()  # object creation
port = 12348  # port defination

s.bind(('', port))  # port and ip bind 127.0.0.1

s.listen(5)  # listening mode
c, addr = s.accept()
while(True):
    # client request -> connection object and address of client
    print(c.recv(1024).decode())
    i = input("Enter something : ")
    c.send(i.encode())
    # send fn to comm with client
c.close()  # to close the function
