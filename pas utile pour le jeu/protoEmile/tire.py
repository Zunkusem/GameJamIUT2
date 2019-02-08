#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
listeProjectile = []

# Before you can do much with pygame, you will need to initialize it
pygame.init()
# Init de clock
clock = pygame.time.Clock()

CIEL = 0, 200, 255  # parenthèses inutiles, l'interpréteur reconnaît un tuple
POSITIONCERCLE= [60, 250]

class Projectile():
    def __init__(self, pos,trajectoire, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (30, 90, 150), pygame.rect.Rect((0, 0, 25, 25)))
        self.rect = self.image.get_rect(center=pos)
        self.pos_y = pos[1]
        self.pos_x = pos[0]
        self.speed_x = 0
        self.speed_y = 0
        self.trajectoireX=trajectoire[0]
        self.trajectoireY=trajectoire[1]
        self.xs = 0
        listeProjectile.append(self)

    def update(self):
        if(self.x<=selfself.trajectoireX):
            self.incPosX()
        if(self.y<=selfself.trajectoireY):
            self.incPosY()
        

    def incPosX(self):
        x+=1

    def incPosY(self):
        y+=1

def CalculTrajectoireProjectile(x1,y1,x2,y2):
    #donne la trajectoire du projectectile depuis le point (x1,y1) jusqu'au point (x2,y2)
    x=x2-x1
    y=y2-y1
    return(x,y)

def main():
    fenetre = pygame.display.set_mode((1280, 720))

    # loop
    loop = True
    # Création d'une image de la taille de la fenêtre
    background = pygame.Surface(fenetre.get_size())
    pro = pygame.sprite.Group()
    
    
    while loop:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("x:",event.pos[0]," y:",event.pos[1])
                xSouris=event.pos[0]
                ySouris=event.pos[1]
                xTrajectoire,yTrajectoire=CalculTrajectoireProjectile(POSITIONCERCLE[0],POSITIONCERCLE[1],xSouris,ySouris)
                print("xTrajectoire",xTrajectoire," yTrajectoire",yTrajectoire)
                pro.add(Projectile(POSITIONCERCLE,[xTrajectoire,yTrajectoire],fenetre))
                print("test")
                
            if pressed[pygame.K_d]:
                circles.movex()
            if pressed[pygame.K_a]:
                circles.movexmin()
            if pressed[pygame.K_w]:
                circles.movey()
            if pressed[pygame.K_s]:
                circles.moveymin()


        # Superposition du fond ciel
        background.fill(CIEL)
        fenetre.blit(background, (0, 0))
        pygame.draw.circle(fenetre, (  0,   0,   0), POSITIONCERCLE, 2)
        for i in range(0,len(listeProjectile)):
                listeProjectile[i].update()
        pass
        pro.draw(fenetre)
        pygame.display.flip()
        # Rafraîchissement de l'écran
        pygame.display.flip()
        # By calling Clock.tick(10) once per frame, the program will never run
        # at more than 10 frames per second
        clock.tick(10)

if __name__ == '__main__':
    main()
