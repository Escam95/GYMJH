import pygame
import random
icon = pygame.image.load('Ryze.png')
screen_width = 1360
screen_height = 840
rect_width = 250
rect_height = 500
i = 0
j = 0
chess_size = 64

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Window')
pygame.display.set_icon(icon)
#  pygame.draw.ellipse(window, (200, 120, 30), (680, 500, 250, 300))
#  pygame.draw.rect(window, (120, 200, 255), ((screen_width - rect_width)/2, (screen_height - rect_height)/2, 250, 500))
#  pygame.draw.rect(window, (120, 200, 255), ((screen_width - 500)/2, (screen_height - 250)/2, 500, 250))

while j < 8:
    while i < 8:
        if i % 2 == 0 and j % 2 != 0:
            color = (0, 222, 222)
        else:
            color = (222, 222, 222)
        pygame.draw.rect(window, color, (0 + i * chess_size, 0 + j * chess_size, chess_size, chess_size))
        i += 1
    j += 1


pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()