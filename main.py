#! /usr/bin/python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from classes import *
import random
import math

def main():

    pygame.init()

    fps = 40

    window = pygame.display.set_mode((1000, 400))
    font = pygame.font.Font(None,90)
    back = pygame.image.load("Back.png").convert()

    game = 1

    jump = 0
    clock = pygame.time.Clock()
    space = 0

    elements = pygame.sprite.Group()
    jack = pygame.sprite.GroupSingle(Jack())

    while game:

        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus

            if event.type == QUIT:

                game = 0

            if event.type == KEYDOWN and event.key == K_SPACE :

                jump = 1
                space = 1 #la touche espace est activée

            if event.type == KEYUP and event.key == K_SPACE:
                space = 0

        if jump == 0 and space == 1:
            jump = 1

        clock.tick(fps)

        if add_rock():

            elements.add(Element())

        window.blit(back, (0,0))

        elements.update()

        elements.draw(window)

        print space


        if len(pygame.sprite.groupcollide(elements,jack,0,0)) != 0:
            print "perdu"
            game = 0


        jack.update(space)
        jack.draw(window)


        pygame.display.flip()


def add_rock():

    i = random.randint(0,100)

    if i == 100:

        return 1

    else:

        return 0

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()







if __name__ == "__main__":
    main()