import pygame

class Alien:
    def __init__(self,speed,background,image_name):
        self.speed = speed
        self.background = background
        self.figure = pygame.transform.scale(pygame.image.load('./data/'+image_name).convert(),(300,300))
    #def draw_self(self,surface):
        #surface.blit(self.figure,(0,0))


