import pygame

#adfsfs
class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((self.width, self.height))

    def draw_self(self):
        self.surface.fill((8, 0, 70))
        pygame.display.update()
