import pygame
from alien import *
from background import *

pygame.init()

delay = 200

game_over = False
background = Background(1000, 1000)
#start game
while not game_over:
    background.draw_self()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break

pygame.time.delay(delay)