import pygame

class Alien:
    def __init__(self,speed,background,image_name,coord_x,coord_y):
        self.speed = speed
        #self.background = background
        self.figure = pygame.transform.scale(pygame.image.load('./data/'+image_name).convert_alpha(),(100,100))
        self.coord_x = coord_x
        self.coord_y = coord_y
        #rect = self.figure.get_rect()
        #rect.fill(0,0,0,128)



