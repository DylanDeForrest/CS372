import socket

s = socket.socket()

server = (("localhost", 4200))

s.connect(server)

while(True):
    data = s.recv(100)

    str = data.decode()

    print(str, end='')