#! user/bin/env/ python3
# coding: utf-8

"""A game about helping macgiver to find his way out the labyrinthe
whithout meeting the guardian"""

import pygame
from pygame.locals import *
from macg import *
from laby import *

pygame.init()
ecran = pygame.display.set_mode((450, 450))
background = pygame.image.load("data/fond.jpg").convert()



continuer = 1

while continuer:
    ecran.blit(background, (0, 0))
    surface.generate_zone()
    surface.rand_object()
    surface.display_zone(ecran)
    ecran.blit(macgyver.player, macgyver.position)


    # chargement de la page
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

        elif event.type == KEYDOWN:

            if event.key == K_RIGHT:
                macgyver.move_right()
            elif event.key == K_LEFT:
                macgyver.move_left()
            elif event.key == K_UP:
                macgyver.move_up()
            elif event.key == K_DOWN:
                macgyver.move_down()