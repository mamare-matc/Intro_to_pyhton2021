#!/usr/bin/env python3
import socket

serverAddress = '192.168.1.246'
serverPort = 443
myServerInfo = (serverAddress, serverPort)
dataFormUser = ''

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(myServerInfo)

while dataFormUser != 'EOF':
   dataFormUser = input('what should we send to the server')
   dataToSend = dataFormUser.encode()
   print(f'sending {dataToSend}')
   clientSocket.send(dataToSend)
   dataReceived = clientSocket.recv(1024)
   print('we recieved data'.dataReceived.decode())
   
print(f'closing the connection to {serverAddress}:{serverPort}')
clientSocket.close()