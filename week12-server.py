#!/usr/bin/env python3
import socket 

myServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the server port to the IP address 
myServerSocket.bind((socket.gethostname(), 5000))

#Tell the server to listen incoming connections
myServerSocket.listen(1)

while True:
    clientsocket, address = myServerSocket.accept()
    print(f'connection from {address} has been established')
    clientsocket.send(bytes("welcome to the server", "utf-8"))
