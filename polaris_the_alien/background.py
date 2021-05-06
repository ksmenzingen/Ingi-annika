import pygame

class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((self.width, self.height))

    def draw_self(self,alien):
        x0 = 0
        y0 = 0
        cellSize = self.width/20
        columns = 20
        rows = columns
        self.surface.fill((8, 0, 70))
        self.surface.blit(alien.figure, (alien.coord_x, alien.coord_y))
        height = 100
        color = (200,0,0)
        pygame.draw.rect(self.surface, (color), pygame.Rect(0, self.height - height, self.height, height))
        pygame.draw.rect(self.surface, (color), pygame.Rect(0, 0, self.height, height))
        #pygame.draw.polygon(self.surface,(color),((25,75),(67,125),(250,250)))
        pygame.display.update()

