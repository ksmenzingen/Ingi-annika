import pygame
import random

class Obstacles:
    def __init__(self,background,color,height):
        self.background = background
        self.color = color
        self.height = height
        self.li_bottom = []
        self.li_top = []
        breite = random.randint(70, 125)  # breite
        hoehe = random.randint(100, 300)  # höhe
        self.li_top.append([breite, hoehe])
        #self.li_top.append([random.randint(70, 125),random.randint(100, 300)])


    def border(self):
        #border
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, self.background.height - self.height, self.background.height, self.height))
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, 0, self.background.height, self.height))

    def draw_self(self):
        for i in range (len(self.li_top)):
            numbers = self.li_top[i]
            height = numbers[1]
            width = numbers[0]
            pygame.draw.polygon(self.background.surface,self.color,((width,height),(self.li_top[i][0],self.height),(self.li_top[i][0]-height,self.height)))
            self.li_top[i][0] += 5
            pygame.display.update()
            if self.li_top[i][0] >= self.background.width:
                self.li_top.append([random.randint(70, 125),random.randint(100, 300)])
                self.li_top.pop(0)




