import pygame
from alien import *
from background import *

pygame.init()

delay = 200

game_over = False
background = Background(800, 800)
alien = Alien(100,background,"alien_drawing.png")

#start game
while not game_over:
    #background.draw_self()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
    background.draw_self(alien)

pygame.time.delay(delay)