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
obstacles = Obstacles(background,(200,0,0),100)


while not game_over:
    for event in pygame.event.get():

        while event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:

                alien.coord_y += 0.5
                background.draw_self(alien,obstacles)
                alien.move(6)
                alien.figure = pygame.transform.scale(pygame.image.load('./data/alien_drawing2.png').convert_alpha(),(115,100))
                background.draw_self(alien,obstacles)


            if event.key == pygame.K_UP:
                alien.move(-6)
                alien.figure = pygame.transform.scale(pygame.image.load('./data/alien_image_combustion2.png').convert_alpha(),(115,150))
                background.draw_self(alien,obstacles)

            if event.key == pygame.K_ESCAPE:
                game_over = True

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    break

            for i in range(len(obstacles.li_top)):
                if alien.coord_y <= obstacles.li_top[i][1] + 95 and obstacles.li_top[i][0] >= 350:
                    game_over = True
                    break

                if alien.coord_y >= obstacles.li_top[i][1] + 200 and obstacles.li_top[i][0] >= 350:
                    game_over = True
                    break
        if event.type == pygame.QUIT:
            game_over = True
            break



    for i in range(len(obstacles.li_top)):
        if alien.coord_y <= obstacles.li_top[i][1]+95 and obstacles.li_top[i][0] >= 350:
            game_over = True
            break

        if alien.coord_y >= obstacles.li_top[i][1]+200 and obstacles.li_top[i][0] >= 350:
            game_over = True
            break

    background.draw_self(alien,obstacles)
    pygame.display.update()

pygame.time.delay(delay)