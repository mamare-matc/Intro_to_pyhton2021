#!/usr/bin/env python3
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((socket.gethostname(), 5000))

msg = clientSocket.recv(1024)
print(msg.decode("utf-8"))

