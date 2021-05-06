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
        for i in range(0,columns):
            pygame.draw.line(self.surface,(200,200,200),(x0,self.height),(x0,0))
            x0 += cellSize
        for i in range(0,rows):
            pygame.draw.line(self.surface,(200,200,200),(self.width,y0),(0,y0))
            y0 += cellSize
        self.surface.blit(alien.figure, (self.height*0.5, self.height*0.5))
        height = 100
        color = (200,0,0)
        pygame.draw.rect(self.surface, (color), pygame.Rect(0, self.height - height, self.height, height))
        pygame.draw.rect(self.surface, (color), pygame.Rect(0, 0, self.height, height))
        pygame.display.update()

