import pygame
import random

class Obstacles:
    def __init__(self,background,color,height):
        self.background = background
        self.color = color
        self.height = height
        self.di_bottom = {}
        self.di_top = {}

    def border(self):
        #border
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, self.background.height - self.height, self.background.height, self.height))
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, 0, self.background.height, self.height))


    def generate(self):
        random.randint(50, 125) #breite
        random.randint(100, 300) #höhe

