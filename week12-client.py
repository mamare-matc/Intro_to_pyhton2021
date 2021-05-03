#!/usr/bin/env python3
import socket

serverAddress = '172.20.1.1'
serverPort = 5000
myServerInfo = (serverAddress, serverPort)
dataFormUser = ''

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(myServerInfo)

while dataFormUser != 'EOF':
   dataFormUser = input('Hello Class')
   dataToSend = dataFormUser.encode()
   print(f'sending {dataToSend}')
   clientSocket.send(dataToSend)
   dataReceived = clientSocket.recv(1024)
   print('we recieved data'.dataReceived.decode())
   
print(f'closing the connection to {serverAddress}:{serverPort}')
clientSocket.close()

