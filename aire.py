import pygame
from pygame.locals import *
from main import *

class Surface:
    def __init__(self):
        self.taille_mur = 30

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








