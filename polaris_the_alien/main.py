import pygame
from alien import *
from background import *
from obstacles import *
import random

pygame.init()

delay = 200

game_over = False
background = Background(800, 800)
alien = Alien(100,"alien_drawing2.png",(background.height*0.5-50),100)
obstacles = Obstacles(background,(200,0,0),100,random.randint(50,125),random.randint(100,300))

#start game
while not game_over:
    #background.draw_self()
    for event in pygame.event.get():
          while event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                alien.coord_y += 0.5
                background.draw_self(alien,obstacles)
                if event.type == pygame.KEYUP:
                    break

            if event.key == pygame.K_UP:
                alien.coord_y -= 5
                background.draw_self(alien,obstacles)

          if event.type == pygame.QUIT:
            game_over = True
            break
    #obstacles.generate()
    background.draw_self(alien,obstacles)
    pygame.display.update()

pygame.time.delay(delay)