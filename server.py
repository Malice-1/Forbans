import socket

HOST="localhost"
PORT=5000

server_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

while True:
    message,address=server_socket.recvfrom(1024)
    print(f"MESSAGE : {message} FROM {address}")
