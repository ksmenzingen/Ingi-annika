import pygame

class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((self.width, self.height))

    def draw_self(self,alien,obstacles):
        columns = 20
        rows = columns
        self.surface.fill((8, 0, 70))
        self.surface.blit(alien.figure, (alien.coord_x, alien.coord_y))
        obstacles.generate()
        #height = 100
        #pygame.draw.polygon(self.surface,(color),((25,75),(67,125),(250,250)))
        pygame.display.update()

