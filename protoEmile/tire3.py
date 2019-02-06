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
    return (vitesseX,vitesseY)

    


vx1,vy1=calculDeLaVitesseProjectile(2, 1, 5, 3)

vx2,vy2=calculDeLaVitesseProjectile(2, 1, 3, 5)

vx3,vy3=calculDeLaVitesseProjectile(2, 1, 4, 8)

import pygame
 
screen = pygame.display.set_mode((640, 480))
running = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 255), (0, 0), ((5-2)*100, (3-1)*100))
    pygame.draw.line(screen, (0, 0, 255), (0, 0), (vx1*100, 0*100))
    pygame.draw.line(screen, (0, 0, 255), (vx1*100, 0*100), (vx1*100, vy1*100))

    pygame.draw.line(screen, (0, 255, 0), (0, 0), ((3-2)*100, (5-1)*100))
    pygame.draw.line(screen, (0, 255, 0), (0, 0), (vx2*100, 0*100))
    pygame.draw.line(screen, (0, 255, 0), (vx2*100, 0*100), (vx2*100, vy2*100))

    pygame.draw.line(screen, (255, 0, 0), (0, 0), ((4-2)*100, (8-1)*100))
    pygame.draw.line(screen, (255, 0, 0), (0, 0), (vx3*100, 0*100))
    pygame.draw.line(screen, (255, 0, 0), (vx3*100, 0*100), (vx3*100, vy3*100))
    
    pygame.display.flip()


