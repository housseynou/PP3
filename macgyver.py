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

background = pygame.image.load(os.path.join('data', 'fond.jpg')).convert()
ecran.blit(background, (0,0))

macgyver = pygame.image.load(os.path.join('data', 'macGyver.png')).convert_alpha()
position = macgyver.get_rect()
ecran.blit(macgyver, position)








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

def __init__(self,):

    long_mur = 30
    large_mur = 30


def generer_zone(self):
    fenetre = []
    for ligne in nb_zone:
        zone = []
        for sprite in ligne:
            zone.append(sprite)
        fenetre.append(ligne)

def afficher_zone(self):
    mur = pygame.image.load(os.path.join('data', 'mur.png')).convert()
    num_ligne = 0
    for ligne in nb_zone:
        num_zone = 0
        for sprite in ligne:
            x = num_ligne * large_mur
            y = num_zone * long_mur

            if sprite == 'm':
                ecran.blit(mur, (x, y))
            elif sprite == 'a':
                ecran.blit(arrive, (x,y))
                print(sprite)







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
    aire_jeux.afficher_zone()


main()