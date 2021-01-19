# -*- coding: utf-8 -*-
import socket
import os

print("Opening socket...")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind("/tmp/python_unix_sockets_example")

print("Listening...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    else:
        print("-" * 20)
        print(datagram.decode('utf-8'))
        if "DONE" == datagram.decode('utf-8'):
            break
print("-" * 20)
print("Shutting down...")
server.close()
print("Done")