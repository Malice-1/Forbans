import pygame
import socket
from models.player import Player
from models.ship import Ship

s1=Ship(10, 1, 1, 1, 50)
p1=Player(0, 0, 0, s1)

s2=Ship(10, 1, 1, 1, 50)
p2=Player(0, 10, 10, s2)



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


pygame.init()
WIDTH,HEIGHT=800,600
window=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Forbans")

BLACK=(0,0,0)
BLUE=(0,0,255)


running=True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    window.fill(BLACK)
    pygame.draw.rect(window, BLUE, (p1.pos_x, p1.pos_y, p1.active_ship.size, p1.active_ship.size))
    pygame.draw.rect(window, BLUE, (p2.pos_x, p2.pos_y, p2.active_ship.size, p2.active_ship.size))

    pygame.display.update()

pygame.quit()

