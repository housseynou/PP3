#! user/bin/env/ python3
# coding: utf-8

"""A game about helping macgiver to find his way out the labyrinthe
whithout meeting the guardian"""

import pygame
from pygame.locals import *

pygame.init()
ecran = pygame.display.set_mode((450, 450))
background = pygame.image.load("data/fond.jpg").convert()
nbsprite = 15
taille_mur = 30
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

class Surface:
    def __init__(self):

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
        mur = pygame.image.load("data/mur.png").convert()
        arrive = pygame.image.load("data/arrive.png").convert()
        ligne = 0
        for piste in self.cadrejeux:
            zone = 0
            for sprite in piste:
                y = ligne * taille_mur
                x = zone * taille_mur
                if sprite == 'm':
                    ecran.blit(mur, (x, y))
                elif sprite == 'a':
                    ecran.blit(arrive, (x,y))
                zone += 1
            ligne += 1


surface = Surface()


class Macgyver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite().__init__()
        self.player = pygame.image.load("data/macGyver.png").convert_alpha()
        self.position = self.player.get_rect()
        self.speed = 10

        self.piste_y = 0
        self.zone_x = 0
        self.all_zone_x = 15
        self.surface = Surface()



    def move_right(self):
        if event.type == KEYDOWN and event.key == K_RIGHT:
            if macgyver.position.x < 430:
                if self.surface.cadrejeux[self.position.y][self.position.x + 10] != 'm':
                    self.position.x += self.speed




    def move_left(self):
        if event.type == KEYDOWN and event.key == K_LEFT:
            if self.surface.cadrejeux[self.piste_y][self.zone_x - 1] != 'm':
                self.zone_x -= 1
                macgyver.position.x = self.zone_x * taille_mur

    def move_up(self):
        if event.type == KEYDOWN and event.key == K_UP:
            if self.surface.cadrejeux[self.piste_y - 1][self.zone_x] != 'm':
                self.piste_y -= 1
                macgyver.position.y = self.piste_y * taille_mur

    def move_down(self):
        if event.type == KEYDOWN and event.key == K_DOWN:
            if self.surface.cadrejeux[self.piste_y + 1][self.zone_x] != 'm':
                self.piste_y += 1
                macgyver.position.y = self.piste_y * taille_mur
                macgyver.position.y += self.speed


macgyver = Macgyver()

class toucher:
    def __init__(self):
        self.gard = pygame.image.load("data/Gard.png").convert()
        self.ether = pygame.image.load("data/etherM.png").convert
        self.tube = pygame.image.load("data/tubeplastique.png").convert()


    def objet(self):
        pass


continuer = 1

while continuer:
    ecran.blit(background, (0, 0))
    surface.afficher_zone()
    ecran.blit(macgyver.player, macgyver.position)


    # chargement de la page
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT]:
        macgyver.move_right()
    elif key[pygame.K_LEFT]:
        macgyver.move_left()
    elif key[pygame.K_UP]:
        macgyver.move_up()
    elif key[pygame.K_DOWN]:
        macgyver.move_down()




    print(macgyver.position)








