import pygame
from Param import *
from Player import *
from Projectile import *
from math import *

def calculDeLaVitesseProjectile(x1,y1,x2,y2):# (x,y) position du tireur (x1,y1) position de la cible
    x= x2-x1
    y= y2-y1
    if x!=0:
        angle=atan(y/x)
    else:
        print("division par zero")

    angleEnDegree=degrees(angle)
    vitesseX=cos(angle)
    vitesseY=sin(angle)
    #print(vitesseX)
    #print(vitesseY)
    #print("norme")
    #print(sqrt(vitesseX*vitesseX+vitesseY*vitesseY))
    #print(degrees(angle))
    if x>0:
        return (vitesseX,vitesseY)
    else:
        return (-vitesseX,-vitesseY)

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

        if self.hp <=0:
            self.kill()

    def update(self,bullets,player):
        self.countdonw -= 1
        if self.countdonw == 0:
            vitesseX,vitesseY=calculDeLaVitesseProjectile(self.rect.right,self.rect.centery,player.rect.x,player.rect.y)
            bullets.add(EnnemyBullet(self.rect.right, self.rect.centery, vitesseX, vitesseY))
            self.countdonw = 60
