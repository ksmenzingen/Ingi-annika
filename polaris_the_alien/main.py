import pygame
from alien import *
from background import *

pygame.init()

delay = 200

game_over = False
background = Background(800, 800)
alien = Alien(100,background,"alien_drawing2.png",(background.height*0.5-50),100)

#start game
while not game_over:
    #background.draw_self()
    for event in pygame.event.get():
          while event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                alien.coord_y += 0.5
                background.draw_self(alien)
                if event.type == pygame.KEYUP:
                    break

            if event.key == pygame.K_UP:
                alien.coord_y -= 5
                background.draw_self(alien)

          if event.type == pygame.QUIT:
            game_over = True
            break
    background.draw_self(alien)

pygame.time.delay(delay)