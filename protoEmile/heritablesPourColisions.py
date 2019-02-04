import self as self

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

    def getHauteurX(self):
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


def Collision(a, b):
    if a.getForme == "Rectangle" and b.getForme == "Rectangle":
        if ((b.getX() >= a.getX()+a.getLargeur())or(b.getX()+b.getLargeur() <= a.getX())or((b.getY() >= a.getY() + a.getHauteur())or (b.getY() + b.h <= a.getY)) :
            print("collision")
        else:








running = True

perso = Personnage()

while running:
    print(perso.getForme())
    continue

