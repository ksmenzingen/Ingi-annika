import pygame


class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((self.width, self.height))

    def draw_self(self):
        self.surface.fill((0, 0, 139))
        pygame.display.update()
