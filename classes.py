
import math

import pygame
from pygame.locals import *

class Element(pygame.sprite.Sprite):

    speed = 10
    x = 269

    def __init__(self,pos=1000,typ=0):

        pygame.sprite.Sprite.__init__(self)

        self.typ = typ
        self.image = pygame.image.load("Rock.png").convert_alpha()
        self.rect = self.image.get_rect(left=pos,bottom=319)

    def update(self):

        self.rect = self.rect.move(-self.speed,0)

        if self.rect.left < 0:
            self.kill()

class Jack(pygame.sprite.Sprite):

    default_pos = 219
    #img = 

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.rect_sheet= pygame.Rect((0,0),(100,100))
        self.sheet = pygame.image.load("Sprites/Jack.png").convert_alpha()
        self.sheet.set_clip(self.rect_sheet)

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect(left=100,bottom=319)

        self.count = 1

        self.jump = 0

    def jump(self,f,fps):
        self.pos = self.default_pos - math.sin((math.pi*f)/fps)*self.default_pos

    def update(self,space,fps=40):

        self.count += 0.375

        if self.count >= 6:

            self.count = 0

        self.rect_sheet.left = int(self.count)*100

        self.sheet.set_clip(self.rect_sheet)
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        if space == 1 and self.jump == 0:
            self.jump = 1

        if self.jump != 0 :

            self.rect.top = self.default_pos - math.sin((math.pi*self.jump)/fps)*self.default_pos

            self.jump += 1

        if self.jump > fps:

            self.jump = 0

        # if self.jump == 0 and space == 1:
        #     self.jump = 1
        # if self.rect.top >= 50:
        #     self.jump = -1
        # elif self.rect.top == 219 and self.jump == -1:
        #     self.jump = 0
        # else:
        #     pass

        # if self.jump == 1 and self.rect.top > 50:
        #     self.rect = self.rect.move(0,-10)
        # elif self.jump == -1:
        #     self.rect = self.rect.move(0,10)

        # print self.rect.top



        #self.pos = 300 - math.sin((math.pi*(self.pos/300))/fps)*300

