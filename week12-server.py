#!/usr/bin/env python3
import socket 

myServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

myIp = '192.168.1.246'
myPort = 443
myServerInfo = (myIp, myPort)

print({myIp})
print({myPort})

#bind the server port to the IP address 
myServerSocket.bind(myServerInfo)

#Tell the server to listen incoming connections
myServerSocket.listen(1)

while True:
    clientsocket, address = myServerSocket.accept()
    try:
        print(f'connection from {address} has been established')
        while True:
            incomingData = clientsocket.recv(1024)
            print(f'recieved {incomingData}')
            if incomingData:
                print('sending data back')
                clientsocket.sendall(incomingData)
            else:
                print(f'end of client data{address}')
                clientsocket.close()
    except socket.error as mySocketError:
        print(f'connection state {myPort}:{mySocketError}')
        clientsocket.close()
