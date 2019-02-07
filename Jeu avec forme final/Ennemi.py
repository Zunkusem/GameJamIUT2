import pygame
from Param import *
from Player import *
from Projectile import *
from math import *



class Cible(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        width = 25
        height = 25
        self.hp = 2
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def bulletHit(self):
        self.hp -= 1

        if self.hp <=0:
            self.kill()

class Tourelle(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        width = 100
        height = 100
        self.hp = 5
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.hitzone = [self.rect.x-width*2.5,self.rect.y-height*2.5,self.rect.y+height*2.5,self.rect.y+height*2.5]
        self.countdonw = 60

    def bulletHit(self):
        self.hp -= 1

        if self.hp <0:
            self.kill()

    def update(self,bullets,player):
        self.countdonw -= 1
        if self.countdonw == 0:
            vitesseX,vitesseY=calculDeLaVitesseProjectileAvecRamdom(self.rect.right,self.rect.centery,player.rect.centerx,player.rect.centery)
            bullets.add(Bullet(self.rect.right, self.rect.centery, vitesseX, vitesseY))
            self.countdonw = 60



            

class EnnemiDetecteur(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        width = 100
        height = 100
        self.hp = 5
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.hitzone = [self.rect.x-width*2.5,self.rect.y-height*2.5,self.rect.y+height*2.5,self.rect.y+height*2.5]
        self.countdonw = 60

    def bulletHit(self):
        self.hp -= 1

        if self.hp <0:
            self.kill()

    def update(self,bullets,player):
        self.countdonw -= 1
        if self.countdonw == 0:
            vitesseX,vitesseY=calculDeLaVitesseProjectile(self.rect.right,self.rect.centery,player.rect.x,player.rect.y)
            bullets.add(Bullet(self.rect.right, self.rect.centery, vitesseX, vitesseY))
            self.countdonw = 60
