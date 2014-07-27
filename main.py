#! /usr/bin/python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from classes import *
import random
import math

def main():

    fps = 40

    pygame.init()
    window = pygame.display.set_mode((1000, 400))
    font = pygame.font.Font(None,90)
    back = pygame.image.load("back.png").convert()
    pngJack = pygame.image.load("Jack.png").convert()
    rock = pygame.image.load("Rock.png").convert()

    game = 1

    jump = 0
    clock = pygame.time.Clock()
    space = 0

    elements = []
    jack = Jack()

    while game:

        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus

            if event.type == QUIT:

                game = 0

            if event.type == KEYDOWN and event.key == K_SPACE and jump == 0:

                jump = 1
                space = 1 #la touche espace est activée

            if event.type == KEYUP and event.key == K_SPACE:
                space = 0

        if jump == 0 and space == 1:
            jump = 1

        clock.tick(fps)

        if add_rock():

            elements.append(Element())

        window.blit(back, (0,0))

        for el in elements:

            if el.pos >= 100 and el.pos <= 150 and jack.pos >= 250:

                game = 0


            el.move()

            window.blit(rock, (el.pos,350))

            if el.pos < 0:

                elements.remove(el)
                del el



        if jump != 0 and jump < 40 :

            jump += 1

            jack.jump(jump,fps)

        else:

            jump = 0


        window.blit(pngJack, (100,jack.pos))


        pygame.display.flip()


def add_rock():

    i = random.randint(0,100)

    if i == 100:

        return 1

    else:

        return 0







if __name__ == "__main__":
    main()