import pygame
import random

class Obstacles:
    def __init__(self,background,color,height):
        self.background = background
        self.color = color
        self.height = height
        self.li_top = []
        self.li_top.append([0,random.randint(0,1),random.randint(50,100)])
        self.score = 0

    def border(self):
        #border
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, self.background.height - self.height, self.background.height, self.height))
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, 0, self.background.height, self.height))


    def draw(self):
        for i in range(len(self.li_top)):

            pygame.draw.rect(self.background.surface, self.color,
                             pygame.Rect(self.li_top[i][0],self.height,self.li_top[i][2], self.li_top[i][1]))

            pygame.draw.rect(self.background.surface, self.color,
                             pygame.Rect(self.li_top[i][0],self.height+self.li_top[i][1]+200,self.li_top[i][2],self.background.height-self.height))

            self.li_top[i][0] += 3

            if self.li_top[i][0] == 399:
                self.li_top.append([0,random.randint(0,530),random.randint(50,100)])
                self.li_top.pop(i)
                self.score += 1
        pygame.display.update()


