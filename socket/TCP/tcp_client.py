from socket import *

message = []
f = open("input.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    message.append(line)
f.close()

server_name = "192.168.242.143"
server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
modified_message = []
f = open("output.txt", "w")
client_socket.connect((server_name, server_port))
for m in message:
    client_socket.send(m.encode())
    recvm = client_socket.recv(1024)
    f.write(recvm.decode())
f.close()
client_socket.close()