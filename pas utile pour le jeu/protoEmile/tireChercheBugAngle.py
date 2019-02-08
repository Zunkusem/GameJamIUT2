from math import *


def calculDeLaVitesseProjectile(x1,y1,x2,y2):# (x1,y1) position du tireur (x2,y2) position de la cible
    x= x2-x1
    y= y2-y1
    if x!=0:
        angle=atan(y/x)
        print(angle)
    else:
        angle=0.7036137827794523
    
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




calc=0
for x in range(0,200):
    for y in range(0,200):
        calc=calc+1
        print(calc," ",x," ",y," ",calculDeLaVitesseProjectile(100,100,x,y))
        
