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




def generer_zone():
    fenetre = []
    for ligne in nb_zone:
        zone = []
        for sprite in ligne:
            zone.append(sprite)
        fenetre.append(ligne)

def afficher_zone():
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


class Macgyver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = pygame.image.load(os.path.join('data', 'macGyver.png')).convert_alpha()
        self.position = self.player.get_rect()
        self.mobility = 3

    def move_right(self):
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

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            macgyver.move_right()
        elif event.type == KEYDOWN and event.key == K_LEFT:
            macgyver.move_left()
        elif event.type == KEYDOWN and event.key == K_UP:
            macgyver.move_up()
        elif event.type == KEYDOWN and event.key == K_DOWN:
            macgyver.move_down()

        pygame.display.flip()