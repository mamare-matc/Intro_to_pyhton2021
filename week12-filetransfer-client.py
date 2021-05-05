#!/usr/bin/env python3
import socket

myHost = '172.20.1.1'
port = 5000
filename = 'data.txt'

s = socket.socket()
s.connect((myHost, port))

s.send(f"{filename}".encode())
progress = (f"sending{filename}", s.recv(1024))

with open(filename, 'r') as file:
    while True:
        data = file.read()
        if not data:
            break
        s.sendall(data)
        progress.update(len(data))
        
s.close()


