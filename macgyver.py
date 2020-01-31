#! user/bin/env/ python3
# coding: utf-8

'''A game about helping macgiver to find his way out the labyrinthe
whithout meeting the guardian'''

import os
import pygame
from pygame.locals import *

pygame.init()

ecran = pygame.display.set_mode((450, 450), RESIZABLE)

background = pygame.image.load(os.path.join('data', 'fond.jpg')).convert()




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


class Surface(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.mur = pygame.image.load(os.path.join('data', 'mur.png')).convert()
        self.long_mur = 30
        self.large_mur = 30

    def generer_zone(self):
        self.fenetre = nb_zone
        for ligne in nb_zone:
            self.zone = []
            for sprite in ligne:
                self.zone.append(sprite)
            self.fenetre.append(ligne)


    def afficher_zone(self):

        num_ligne = 0
        for ligne in nb_zone:
            num_zone = 0
            for sprite in ligne:
                x = num_ligne * self.large_mur
                y = num_zone * self.long_mur

                if sprite == 'm':
                    ecran.blit(mur, (x, y))
                elif sprite == 'a':
                    ecran.blit(arrive, (x,y))
                num_zone += 1
            num_ligne += 1

surface = Surface()


class Macgyver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = pygame.image.load(os.path.join('data', 'macGyver.png')).convert_alpha()
        self.position = self.player.get_rect()
        self.mobility = 5
        self.fast = {}

    def move_right(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RIGHT:
                self.position.x += self.mobility
    def move_left(self):
        if event.type == KEYDOWN and event.key == K_LEFT:
            self.position.x -= self.mobility
    def move_up(self):
        if event.type == KEYDOWN and event.key == K_UP:
            self.position.y -= self.mobility
    def move_down(self):
        if event.type == KEYDOWN and event.key == K_DOWN:
            self.position.y += self.mobility



macgyver = Macgyver()


continuer = 1

while continuer:
    ecran.blit(background, (0, 0))
    ecran.blit(macgyver.player, macgyver.position)

# fludifier les mouvements du joueur et eviter qu'il sorte du cadre

    if macgyver.fast.get(pygame.K_RIGHT) and macgyver.position.x < 450:
        macgyver.move_right()
    elif macgyver.fast.get(pygame.K_LEFT) and macgyver.position.x > 0:
        macgyver.move_left()
    elif macgyver.fast.get(pygame.K_UP) and macgyver.position.y > 0:
        macgyver.move_up()
    elif macgyver.fast.get(pygame.K_DOWN) and macgyver.position.y < 450:
        macgyver.move_down()


    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        elif event.type == KEYDOWN:
            macgyver.fast[event.key] = True
        elif event.type == KEYUP:
            macgyver.fast[event.key] = False
        print(macgyver.fast)
# chargement de la page

        pygame.display.flip()
