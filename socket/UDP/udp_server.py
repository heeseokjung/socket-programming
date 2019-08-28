from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print("server: ready to receive")

while True:
    m, cliend_address = server_socket.recvfrom(2048)
    mm = m.decode().upper()
    server_socket.sendto(mm.encode(), cliend_address)