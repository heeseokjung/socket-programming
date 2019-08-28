from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(100)
print("server: ready to receive")

connection_socket, address = server_socket.accept()
while True:
    recvm = connection_socket.recv(1024).decode().upper()
    connection_socket.send(recvm.encode())
connection_socket.close()