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
        hoehe = random.randint(100, 500)  # höhe
        #self.li_top.append([breite, hoehe])
        #self.li_bottom.append([breite,hoehe])
        self.li_top.append([0,random.randint(0,100),random.randint(50,100)])


    def border(self):
        #border
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, self.background.height - self.height, self.background.height, self.height))
        pygame.draw.rect(self.background.surface, (self.color),
                         pygame.Rect(0, 0, self.background.height, self.height))

    #def draw_self(self):
    #    for i in range (len(self.li_top)):
    #        numbers = self.li_top[i]
    #        height = numbers[1]
    #        width = numbers[0]
    #        pygame.draw.polygon(self.background.surface,self.color,((width,height),(self.li_top[i][0],self.height),(self.li_top[i][0]-height,self.height)))
    #        self.li_top[i][0] += 5
    #        if self.li_top[i][0] >= self.background.width:
    #            self.li_top.pop(0)
    #            self.li_top.insert(0,[random.randint(70, 125),random.randint(100, 300)])

    #    for i in range(len(self.li_bottom)):
    #        numbers = self.li_bottom[i]
    #        height = numbers[1]
    #        width = numbers[0]-400
    #        pygame.draw.polygon(self.background.surface, self.color, (
    #        (width, self.background.height - (self.height + self.li_bottom[i][1])),
    #        (width, self.background.height - self.height),
    #        (width - height, self.background.height - self.height)))
    #        self.li_bottom[i][0] += 5
    #        if self.li_bottom[i][0] >= self.background.width:
    #            self.li_bottom.insert(0, [random.randint(70, 125), random.randint(100, 300)])
    #            self.li_bottom.pop()

    def draw(self):
        pos_x = 0
        for i in range(len(self.li_top)):

            pygame.draw.rect(self.background.surface, self.color,
                             pygame.Rect(self.li_top[i][0],self.height,self.li_top[i][2],self.height + self.li_top[i][1]))

            pygame.draw.rect(self.background.surface, self.color,
                             pygame.Rect(self.li_top[i][0],self.height+self.li_top[i][1]+300,self.li_top[i][2],self.background.height-self.height))

            self.li_top[i][0] += 3

            if self.li_top[i][0] == 399:
                self.li_top.append([0,random.randint(0,530),random.randint(50,100)])

            #if self.li_top[i][0] >= 800:
            #    self.li_top.pop(i)


        pygame.display.update()


