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
        self.surface.fill((8, 0, 70))
        #background
        self.surface.blit(stars, (0, 0))
        self.surface.blit(stars, (0, 400))
        self.surface.blit(stars, (400, 0))
        self.surface.blit(stars, (400, 400))
        self.surface.blit(asteroid, (100,200))
        self.surface.blit(planet1, (600,500))
        self.surface.blit(comet1,(220,550))
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('score ' + str(obstacles.score), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (690, 150)
        if text != None:
            self.surface.blit(text,textRect)
        #player
        self.surface.blit(alien.figure, (alien.coord_x, alien.coord_y))
        obstacles.border()
        obstacles.draw()
        pygame.display.update()


