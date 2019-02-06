from pygame.locals import *
import pygame, os, sys

from Player import *
from Map import *


class Jeu(pygame.sprite.Sprite):
    """Classe <Jeu>"""
    def __init__(self, menu, screen):
        """Constructeur de la classe:
        - Créer une fenêtre
        - Affiche des images

        """
        pygame.sprite.Sprite.__init__(self)
        pygame.init()

        #Variables

       self.horloge = pygame.time.Clock()


        #Screen + titre
        self.screen=pygame.display.set_mode((1270, 670))
        pygame.display.set_caption("CybeRush180")

        self.player = Player()
        self.map = Map()
        self.menu = menu   #jeu connait menu car il faut pouvoir retourner au menu

        #On crée un groupe avec les instances self.player/map
        self.groupe = pygame.sprite.Group(self.player, self.map)


    def mainloop(self):
        """Mainloop du jeu
        - Gestion des événements clavier
        - Blitage"""
        continuer = True
        self.m = "D"
        while continuer :  #Remplacer par tant que temps<=180000 millisecondes (=3mn)



            #On blit tout le groupe d'un coup + flip + fill
            self.groupe.draw(self.screen)
            pygame.display.flip()
            self.screen.fill((0, 0, 0), self.perso.rect)
