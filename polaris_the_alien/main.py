import pygame

class Alien:
    def __init__(self,speed,surface):
        self.speed = speed
        self.surface = surface

    def draw_self(self):
        alien = pygame.image.load('./data/alien_drawing.png')
        return alien