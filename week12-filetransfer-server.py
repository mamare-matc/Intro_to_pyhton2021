#!/env/bin/env python3
import socket

#create a socket (TCP/IP)
myServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define an IP and Port
serverIp = '172.20.1.1'
serverPort = 5000
myServerInfo = (serverIp, serverPort)
BUFFER_SIZE = 4096
separator = "<separator>"

#binding the server info
s = socket.socket()
s.bind(myServerInfo)

#tell out server to listen for the incoming connections
s.listen(5)

print(f"{serverIp}:{serverPort}")

#accept connection if there is any
client_socket, address = s.accept()

#if below code is excuted that me sender is connected 
print(f"{address} is connected")


#recive the file infos using client socket, not server socket
received = client_socket.rcv(BUFFER_SIZE).decode()
filename, filesize = received.split(separator)

#start receiving from the socket and write to the file stream
with open(filename, "wb") as file:
    while True:
        data = client_socket.revc(BUFFER_SIZE)
        if not data:
            break
    file.write(data)
        
client_socket.close()
s.close()