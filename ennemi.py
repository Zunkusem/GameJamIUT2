class ennemi: # Définition de notre classe Personne

    def __init__(self, vie, poids, x, y): # Notre méthode constructeur
        self.vie= vie
        self.mort = False
        self.poids = poids
        self.positionX = x
        self.positionY = y
        self.largeur = 10
        self.hauteur = 10
        self.vecteurVitesse = array.array('b',[0,0])
        self.frottement = 3

    def getEnVie(self):
        return self.vie

    def setPosition(self,x=0,y=0):
		self.positionX=x
        self.positionY=y

    def gauche(self):
        self.vecteurVitesse -= 1

    def droite(self):
        self.vecteurVitesse += 1

    def sautRessort(int):

    def tirer(posXTir, posYTir):

    def touche():

    def setVecVitesse(x,y):
        self.vecteurVitesse= array.array('b',[x,y])

    def afficher():