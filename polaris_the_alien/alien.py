import pygame

class Alien:
    def __init__(self,speed,image_name,coord_x,coord_y):
        self.speed = speed
        self.image_name = image_name
        self.figure = pygame.transform.scale(pygame.image.load('./data/'+self.image_name).convert_alpha(),(115,100))
        self.coord_x = coord_x
        self.coord_y = coord_y

    def move(self,change):
        self.coord_y += change



