"""A game about helping macgiver to find his way out the labyrinthe
 whithout meeting the guardian"""

import os
import pygame
from pygame.locals import *
from moving import *


class objet:
    def __init__(self):
        self.gard = pygame.image.load("data/Gard.png").convert()
        self.ether = pygame.image.load("data/etherM.png").convert
        self.tube = pygame.image.load("data/tubeplastique.png").convert()


    def recueil(self):
        for piste in Surface.cadrejeux:
            for sprite in piste:
                if sprite != "m":
                    ecran.blit(self.Gard, (0, 0))
                    ecran.blit(self.ether,(0, 0))
                    ecran.blit(self.tube, (0, 0))


        if event.type == KEYDOWN and event.key == K_RIGHT:
            for y in range(len(nb_zone)):
                for x in range(len(nb_zone[y])):
                    self.zone = nb_zone[y][x]
                    self.zone_x = nb_zone.index(self.zone) * taille_mur
                    self.piste_y = nb_zone.index(self.zone) * taille_mur
                    if self.zone_x == 'm':
                        self.wall.append((self.zone_x, self.piste_y))

                    elif self.zone_x == 'o':
                        self.way.append((self.zone_x, self.piste_y))
                        if macgyver.position.x + 1 in self.way:
                            macgyver.position.x += self.speed
