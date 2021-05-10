import pygame
import random

class Obstacles:
    def __init__(self,background,color,height,rand1,rand2):
        self.background = background
        self.color = color
        self.height = height
        self.rand1 = rand1
        self.rand2 = rand2

    def generate(self):
        #border
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, self.background.height - self.height, self.background.height, self.height))
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, 0, self.background.height, self.height))
        #random generated
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, self.background.height - 2 * self.height, self.rand1, self.rand2))
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, self.height, self.rand1, self.rand2))