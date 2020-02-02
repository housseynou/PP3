#! user/bin/env/ python3
# coding: utf-8

'''A game about helping macgiver to find his way out the labyrinthe
whithout meeting the guardian'''

import os
import pygame
from pygame.locals import *

pygame.init()

ecran = pygame.display.set_mode((450, 450))

background = pygame.image.load("data/fond.jpg").convert()




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
        self.taille_mur = 30
        self.nbsprite = 15
        self.cadrejeux = nb_zone

    def generer_zone(self):
        fenetre = []
        for piste in nb_zone:
            num_piste = []
            for zone in num_piste:
                num_piste.append(zone)
            fenetre.append(piste)
        self.cadrejeux = fenetre





    def afficher_zone(self):

        ligne = 0
        for piste in self.cadrejeux:
            zone = 0
            for sprite in piste:
                mur = pygame.image.load("data/mur.png").convert()
                arrive = pygame.image.load("data/arrive.png").convert()
                x = ligne * self.taille_mur
                y = zone * self.taille_mur

                if sprite == 'm':
                    ecran.blit(mur, (x, y))
                elif sprite == 'a':
                    ecran.blit(arrive, (x,y))
                zone += 1
            ligne += 1

surface = Surface()


class Macgyver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = pygame.image.load("data/macGyver.png").convert_alpha()
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
    surface.afficher_zone()

    # chargement de la page
    pygame.display.flip()

# fludifier les mouvements du joueur et eviter qu'il sorte du cadre
    if macgyver.fast.get(pygame.K_RIGHT):
        macgyver.move_right()
    elif macgyver.fast.get(pygame.K_LEFT):
        macgyver.move_left()
    elif macgyver.fast.get(pygame.K_UP):
        macgyver.move_up()
    elif macgyver.fast.get(pygame.K_DOWN):
        macgyver.move_down()


    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        elif event.type == KEYDOWN:
            macgyver.fast[event.key] = True
        elif event.type == KEYUP:
            macgyver.fast[event.key] = False


