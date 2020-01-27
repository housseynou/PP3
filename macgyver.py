#! user/bin/env/ python3
# coding: utf-8

'''A game about helping macgiver to find his way out the labyrinthe
whithout meeting the guardian'''

import os
import random
import pygame
from pygame.locals import *

pygame.init()

ecran = pygame.display.set_mode((450, 450), RESIZABLE)

background = pygame.image.load(os.path.join('data','fond.jpg')).convert()
ecran.blit(background, (0,0))

macgyver = pygame.image.load(os.path.join('data', 'macGyver.png')).convert_alpha()
position = macgyver.get_rect()
ecran.blit(macgyver, position)




class zone:

    MIN_POSITION = 0
    MAX_POSITION = 450
    LONG_MUR = 30
    LARGE_MUR = 30
    NBSPRITE_X = 15
    NBSPRITE_Y = 15

    nb_zone = [
        "oooomomommmommm",
        "ommooomoooooooo",
        "oomommoommomomo",
        "omooooommmomomo",
        "oommmmommomooom",
        "mooommoomommmoo",
        "momommmmooooomm",
        "momomoooommmomo",
        "ooommommomooomo",
        "mommooooomommmo",
        "mooommmmomoooom",
        "mmmomoooommmooo",
        "mooomommmmmmoom",
        "mommmomoooooooo",
        "mooooommmommmma",
    ]

    def __init__(self, long, large):
        self.long = long
        self.large = large

    def generer_zone(self):
        for sprite in range(self.MIN_POSITION, self.MAX_POSITION, self.LARGE_MUR):
            largsprite = self.LARGE_MUR
            for colonne in range(self.MIN_POSITION, self.MAX_POSITION, self.LONG_MUR):
                longsprite = self.LONG_MUR
                posprite = [][]
                zone_in = zone(LONG_MUR, LARGE_MUR)
                self.nb_zone.append(zone_in)

                mur = pygame.image.load(os.path.join('data', 'mur.png')).convert()
                if self.position == nb_case[0][m]:
                    ecran.blit(mur, (x, y))






def deplacer():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_RIGHT:
            macgyver.position.move(3,0)



pygame.display.flip()





continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0



def main():
    ecran.blit(background, (0, 0))
    ecran.blit(macgyver, position)
    pygame.display.flip()
    self.macgyver()
    ecran.blit(mur, (x, y))


main()