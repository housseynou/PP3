#! user/bin/env/ python3
# coding: utf-8

"""A game about helping macgiver to find his way out the labyrinthe
whithout meeting the guardian"""

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




class Macgyver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = pygame.image.load("data/macGyver.png").convert_alpha()
        self.position = self.player.get_rect()
        self.mobility = 5
        self.npiste = 0
        self.nsprite = 0
        self.taille_mur = 30
        self.x = 0
        self.y = 0
        self.surface = surface
        self.fast = {}

    def move_right(self):
        if event.type == KEYDOWN and event.key == K_RIGHT:
            if self.surface.cadrejeux[self.nsprite][self.npiste] != 'm':
                self.position.x += self.mobility
                self.x = self.npiste * self.taille_mur

    def move_left(self):
        if event.type == KEYDOWN and event.key == K_LEFT:
            if self.surface.cadrejeux[self.nsprite][self.npiste] != 'm':
                self.position.x -= self.mobility
    def move_up(self):
        if event.type == KEYDOWN and event.key == K_UP:
            if self.surface.cadrejeux[self.nsprite][self.npiste] != 'm':
                self.position.y -= self.mobility
    def move_down(self):
        if event.type == KEYDOWN and event.key == K_DOWN:
            if self.surface.cadrejeux[self.nsprite][self.npiste] != 'm':
                self.position.y += self.mobility


surface = Surface()
macgyver = Macgyver()
surface.generer_zone()


continuer = 1

while continuer:
    ecran.blit(background, (0, 0))
    surface.afficher_zone()
    ecran.blit(macgyver.player, macgyver.position)


    print(macgyver.position)
    # chargement de la page
    pygame.display.flip()

    if macgyver.position == 'm'
        print("BRAVO! VOUS AVEZ GAGNÉ")
        continuer = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

        elif event.type == KEYDOWN:
            macgyver.fast[event.key] = True
        elif event.type == KEYUP:
            macgyver.fast[event.key] = False

# fludifier les mouvements du joueur et eviter qu'il sorte du cadre
    if macgyver.fast.get(pygame.K_RIGHT) and macgyver.position.x < 430:
        macgyver.move_right()
    elif macgyver.fast.get(pygame.K_LEFT) and macgyver.position.x > 0:
        macgyver.move_left()
    elif macgyver.fast.get(pygame.K_UP) and macgyver.position.y > 0:
        macgyver.move_up()
    elif macgyver.fast.get(pygame.K_DOWN) and macgyver.position.y < 420:
        macgyver.move_down()







