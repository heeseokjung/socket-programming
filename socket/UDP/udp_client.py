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
client_socket = socket(AF_INET, SOCK_DGRAM) 
modified_message = []
f = open("output.txt", "w")
for m in message:
    client_socket.sendto(m.encode(), (server_name, server_port))
    recvm, server_address = client_socket.recvfrom(2048)
    f.write(recvm.decode())
f.close()
client_socket.close()
