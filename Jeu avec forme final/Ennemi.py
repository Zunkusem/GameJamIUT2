import pygame
from Param import *
from Player import *
from Projectile import *
from math import *
import Map



class Cible(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self,carte):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        width = 25
        height = 25
        self.hp = 1
        self.image = pygame.transform.scale(pygame.image.load('Ennemypic/Cible.png'),[30,30])
        self.rect = self.image.get_rect()
        self.map=carte

    def bulletHit(self):
        self.hp -= 1

        if self.hp <=0:
            mobs = pygame.mixer.Sound('music/mobs.wav')
            pygame.mixer.Sound.play(mobs)
            self.map.score.incrementeScoreDeUn()
            self.map.score.incrementemultiplicateurDeUn()
            self.kill()



class Tourelle(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, carte):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        width = 30
        height = 30
        self.hp = 5
        self.image = pygame.transform.scale(pygame.image.load('Ennemypic/Tourelle.png'),[30,30])
        self.rect = self.image.get_rect()
        self.hitzone = [self.rect.x-width*2.5,self.rect.y-height*2.5,self.rect.y+height*2.5,self.rect.y+height*2.5]
        self.countdonw = 60
        self.map=carte

    def bulletHit(self):
        self.hp -= 1

        if self.hp <=0:
            mobs = pygame.mixer.Sound('music/mobs.wav')
            pygame.mixer.Sound.play(mobs)
            self.map.score.incrementeScoreDeUn()
            self.map.score.incrementeScoreDeUn()
            self.map.score.incrementemultiplicateurDeUn()
            self.kill()

    def update(self,bullets,player):
        self.countdonw -= 1
        if self.countdonw == 0:
            vitesseX,vitesseY=calculDeLaVitesseProjectile(self.rect.centerx,self.rect.centery,player.rect.centerx,player.rect.centery)
            bullets.add(EnnemyBullet(self.rect.centerx, self.rect.centery, vitesseX, vitesseY))
            self.countdonw = 60


class Piece(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        width = 25
        height = 25
        self.countdonw = 10
        self.index = 0
        self.images = []
        self.images.append(pygame.image.load('Ennemypic/energy0000.png'))
        self.images.append(pygame.image.load('Ennemypic/energy0001.png'))
        self.images.append(pygame.image.load('Ennemypic/energy0002.png'))
        self.images.append(pygame.image.load('Ennemypic/energy0003.png'))

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.modindex = 1

    def update(self,screen):
        self.countdonw -= 1
        BLACK = (0, 0, 0)
        if self.countdonw == 0:
            self.index += self.modindex
            screen.fill(BLACK)
            if self.index >= len(self.images)-1 or self.index == 0:
                self.modindex = self.modindex*-1
            self.image = self.images[self.index]
            self.countdonw =10




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
