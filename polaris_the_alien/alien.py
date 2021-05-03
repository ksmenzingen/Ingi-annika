import pygame

#slkfjh
class Alien:
    def __init__(self,speed,background,image_name):
        self.speed = speed
        self.background = background
        self.figure = pygame.image.load('./data/'+image_name)

    #def draw_self(self):

        