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

nb_sprite_x = 15
nb_sprite_y = 15
nb_case = [
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

def cadre_jeu()
    mur = pygame.image.load(os.path.join('data', 'mur.png')).convert()
    mur = 30
    for ligne in nb_case:
        ligne = nb_case[0]
        x = mur * len(nb_case[0][0])
        y = mur * len(nb_case[0])
        for sprite in ligne:
            sprite = '\n'
            if sprite == nb_case[0][m]:
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



main()