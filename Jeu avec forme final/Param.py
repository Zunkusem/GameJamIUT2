from math import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (249, 249, 6)
CYAN = (0, 255, 255)
ELEC_BLUE=(13, 13, 242)
ORANGE=(249, 152, 6)

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768


def calculNorme(x1,y1,x2,y2): #calcule la longueur entre deux points
    x=x2-x1
    y=y2-y1
    return sqrt(x*x+y*y)

def calculDeLaVitesseProjectile(x1,y1,x2,y2):# (x1,y1) position du tireur (x2,y2) position de la cible
    x= x2-x1
    y= y2-y1
    if x!=0:
        angle=atan(y/x)
        print(angle)
    else:
        angle=0.7036137827794523
        print("div par zero !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
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
    else :
        return (-vitesseX,-vitesseY)
