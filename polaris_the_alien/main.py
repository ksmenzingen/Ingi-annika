import pygame
from alien import *
from background import *

pygame.init()


game_over = False
background = Background(100, 100)

#start game
while not game_over:
    background.draw_self()
