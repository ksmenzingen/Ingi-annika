import pygame

class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((self.width, self.height))

    def draw_self(self,alien,obstacles):
        asteroid = pygame.transform.scale(pygame.image.load('./data/asteroid.png').convert_alpha(), (90, 60))
        planet1 = pygame.transform.scale(pygame.image.load('./data/planet2.png').convert_alpha(),(70,70))
        comet1 = pygame.transform.scale(pygame.image.load('./data/comet1.png').convert_alpha(),(120,100))
        stars = pygame.transform.scale(pygame.image.load('./data/stars.png').convert_alpha(),(400,400))
        columns = 20
        rows = columns
        self.surface.fill((8, 0, 70))
        #background
        self.surface.blit(stars, (0, 0))
        self.surface.blit(stars, (0, 400))
        self.surface.blit(stars, (400, 0))
        self.surface.blit(stars, (400, 400))
        self.surface.blit(asteroid, (100,200))
        self.surface.blit(planet1, (600,500))
        self.surface.blit(comet1,(220,550))
        #player
        self.surface.blit(alien.figure, (alien.coord_x, alien.coord_y))
        obstacles.border()
        obstacles.draw_self()
        #height = 100
        #pygame.draw.polygon(self.surface,(color),((25,75),(67,125),(250,250)))
        pygame.display.update()


