import pygame
import socket

HOST="localhost"
PORT=5000


client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
message=b'test'
client_socket.sendto(message, (HOST, PORT))

try:
    data,server=client_socket.recvfrom(1024)
    print(f"{data} - {server}")
except socket.timeout:
    print("REQUEST TIMED OUT")
