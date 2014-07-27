
import math

class Element:

    speed = 10

    def __init__(self,pos=1000,typ=0):

        self.pos = pos
        self.typ = typ

    def __str__(self):

        return 'pos =' + str(self.pos)

    def move(self):

        self.pos -= self.speed

class Jack:

    def __init__(self,pos=300):
        self.pos = pos

    def jump(self,f,fps):
        self.pos = 300 - math.sin((math.pi*f)/fps)*300

