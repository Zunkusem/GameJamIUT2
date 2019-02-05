import self as self
import math
class Objet:
    def __init__(self, nom):
        self.forme=nom

    def getForme(self):
        return self.forme

class Rectangle(Objet):
    def __init__(self, x=0, y=0, larg=0, hauteur=0):
        super().__init__("Rectangle")
        self.x = x
        self.y = y
        self.largeur = larg
        self.hauteur=hauteur

    def setPosition(self, x=0, y=0):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getLargeur(self):
        return self.largeur

    def getHauteur(self):
        return self.hauteur





class Personnage(Rectangle):

    def __init__(self):
                super().__init__()
                self.x = 10
                self.y = 10
                self.largeur = 10
                self.hauteur = 10

    def affiche(self):
        print("x=",self.x," y=",self.y)


class Cercle(Objet):
    def __init__(self, x=0, y=0, rayon=0):
            super().__init__("Cercle")
            self.x = x
            self.y = y
            self.rayon=rayon

    def setPosition(self, x=0, y=0):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRayon(self):
        return self.rayon

class Triangle(Objet):
    def __init__(self,x=0,y=0,z=0):
        super().__init__("Triangle")
        self.x=x
        self.y=y
        self.z=z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z


def intersection(cercle, rect):
    cercleDistanceX= abs(cercle.getX() - rect.getX())
    cercleDistanceY= abs(cercle.getY() - rect.getY())

    if (cercleDistanceX > (rect.getLargeur()/2 + cercle.getRayon())):
        print("pas collision cercle rect")
        return False
    if (cercleDistanceY > (rect.getHauteur()/2 + cercle.getRayon())):
        print("pas collision cercle rect")
        return False
    if (cercleDistanceX <= (rect.getLargeur()/2)):
        print("collision cercle rect")
        return True
    if (cercleDistanceY <= (rect.getHauteur()/2)):
        print("collision cercle rect")
        return True

    cornerDistance = math.sqrt(cercleDistanceX - rect.getLargeur()/2) + math.sqrt(cercleDistanceY - rect.getHauteur()/2)
    return (cornerDistance <= math.sqrt(cercle.getRayon()))

def Collision(a, b):
    if a.getForme() == "Rectangle" and b.getForme() == "Rectangle":
        if ((b.getX() >= a.getX()+a.getLargeur())or(b.getX()+b.getLargeur() <= a.getX())or((b.getY() >= a.getY() + a.getHauteur())or (b.getY() + b.getHauteur() <= a.getY()))) :
            print("pas collision entre Rectangle")
        else:
            print("collision entre Rectangle")
    elif a.getForme() == "Cercle" and b.getForme() == "Cercle":
        d2 = (a.getX()-b.getX())*(a.getX()-b.getX()) + (a.getY()-b.getY())*(a.getY()-b.getY())
        if (d2 > ((a.getRayon() + b.getRayon())*(a.getRayon() + b.getRayon()))):
            print("Pas collision Cercle")
        else:
            print("collision cercle")
    elif a.getForme() == "Cercle" and b.getForme() == "Rectangle":
        intersection(a, b)
    elif a.getForme() == "Rectangle" and b.getForme() == "Cercle":
        intersection(b, a)
    else:
        print("erreur")


running = True

perso = Personnage()
Rec1 = Rectangle(1,1,1,1)
Rec2 = Rectangle(1,1,1,1)
Rec3 = Rectangle(10,10,1,1)

cer1 = Cercle(1,1,1)
cer2 = Cercle(1,1,1)
#cer2 = Cercle(10,10,1)
while running:
    #Collision(Rec1,Rec2)
    #Collision(cer1,cer2)
    #Collision(cer1, Rec1)
    #Collision(Rec1,cer1)
    #Collision(cer1,Rec3)
    continue
