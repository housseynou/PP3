import pygame
from random import randint
from laby import *

class Surface:
    def __init__(self):
        self.cadrejeux = nb_zone

    def generate_zone(self):
        fenetre = []
        for piste in nb_zone:
            num_piste = []
            for zone in num_piste:
                num_piste.append(zone)
            fenetre.append(piste)
        self.cadrejeux = fenetre


    def rand_object(self):
        objects = {"ether": [], "tube": [], "seringue": [], "aiguille": []}

        for key in objects:
            num_obj = 0
            while num_obj < len(objects[key]):
                rand_zone = randint(0, nbsprite - 1)
                rand_piste = randint(0, nbsprite - 1)
                if self.cadrejeux[rand_piste][rand_zone] == 'o':
                    self.cadrejeux[rand_piste][rand_zone] = objects[key]
                    num_obj += 1



    def display_zone(self, ecran):
        mur = pygame.image.load("data/mur.png").convert()
        arrive = pygame.image.load("data/arrive.png").convert()
        gard = pygame.image.load("data/Gard.png").convert_alpha()
        ether = pygame.image.load("data/etherM.png").convert_alpha()
        tube = pygame.image.load("data/tubeplastique.png").convert_alpha()
        seringue = pygame.image.load("data/seringue.png").convert_alpha()
        aiguille = pygame.image.load("data/aiguille.png").convert_alpha()
        ligne = 0
        for piste in self.cadrejeux:
            zone = 0
            for sprite in piste:
                y = ligne * taille_mur
                x = zone * taille_mur
                if sprite == 'm':
                    ecran.blit(mur, (x, y))
                elif sprite == 'a':
                    ecran.blit(arrive, (x, y))
                    ecran.blit(gard, (x, y))
                elif sprite == "ether":
                    ecran.blit(ether, (x, y))
                elif sprite == "tube":
                    ecran.blit(tube, (x, y))
                elif sprite == "seringue":
                    ecran.blit(seringue, (x, y))
                elif sprite == "aiguille":
                    ecran.blit(aiguille, (x, y))
                zone += 1
            ligne += 1

            print(seringue, (x, y))



class Macgyver:
    def __init__(self):
        self.player = pygame.image.load("data/macGyver1.png")
        self.position = self.player.get_rect()

        self.speed = 10
        self.piste_y = 0
        self.zone_x = 0
        self.all_zone_x = 15
        self.surface = Surface()

    def collect_obj(self):
        object = 0
        if macgyver.position.x == self.rand_pos_x and macgyver.position.y == self.rand_pos_y:
            object += 1
            pass

    def move_right(self):
        if self.zone_x < (self.all_zone_x - 1):
            if surface.cadrejeux[self.piste_y][self.zone_x + 1] != 'm':
                    self.zone_x += 1
                    self.position.x = self.zone_x * taille_mur

    def move_left(self):
        if self.zone_x > 0:
            if surface.cadrejeux[self.piste_y][self.zone_x - 1] != 'm':
                self.zone_x -= 1
                self.position.x = self.zone_x * taille_mur

    def move_up(self):
        if self.piste_y > 0:
            if surface.cadrejeux[self.piste_y - 1][self.zone_x] != 'm':
                self.piste_y -= 1
                self.position.y = self.piste_y * taille_mur

    def move_down(self):
        if self.piste_y < (self.all_zone_x - 1):
            if surface.cadrejeux[self.piste_y + 1][self.zone_x] != 'm':
                self.piste_y += 1
                self.position.y = self.piste_y * taille_mur


surface = Surface()
macgyver = Macgyver()


