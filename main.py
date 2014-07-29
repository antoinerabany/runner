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
    font = pygame.font.Font(None,80)
    back = pygame.image.load("Back.png").convert()

    game = 1
    go = 1

    jump = 0
    clock = pygame.time.Clock()
    space = 0
    score = Score()

    elements = pygame.sprite.Group()
    jack = pygame.sprite.GroupSingle(Jack())

    while go:

        while game:

            for event in pygame.event.get():   #On parcours la liste de tous les événements reçus

                if event.type == QUIT:

                    game = 0
                    end = 0
                    go = 0

                if event.type == KEYDOWN and event.key == K_SPACE :

                    space = 1 #la touche espace est activée

                if event.type == KEYUP and event.key == K_SPACE:
                    space = 0

            clock.tick(fps)

            if add_rock():

                elements.add(Element())

            window.blit(back, (0,0))

            elements.update()

            elements.draw(window)

            score.update()

            window.blit(font.render(str(score), 1, (255,255,255)), (600,330))

            if len(pygame.sprite.groupcollide(elements,jack,0,0)) != 0:
                game = 0
                end = 1
                score.save()


            jack.update(space,fps)
            jack.draw(window)


            pygame.display.flip()

        while end:

            for event in pygame.event.get():   #On parcours la liste de tous les événements reçus

                if event.type == QUIT:

                    game = 0
                    end = 0
                    go = 0

                if event.type == KEYDOWN :

                    if event.key == K_ESCAPE:

                        game = 0
                        end = 0
                        go = 0

                    if event.key == K_RETURN:

                        game = 1
                        end = 0
                        elements.empty()
                        score.clear()


            clock.tick(40)

            window.blit(font.render('Jack est gravement blesse', 1, (255,255,255)), (100,100))

            #window.blit(font.render(str(score), 1, (255,255,255)), (500,330))

            window.blit(font.render('Best score : ' + str(score.best_score), 1, (255,255,255)), (500,200))

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