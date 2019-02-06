import pygame
from Param import *

class Cible(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self,hp):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        width = 25
        height = 25
        self.hp = 500
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def bulletHit(self,deg):
        self.hp =- deg

        if self.hp <0:
            self.kill()
