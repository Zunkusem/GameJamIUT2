class score: # Définition de notre classe Personne

    def __init__(self): # Notre méthode constructeur
        self.valeur = 0
        self.multiplicateur = 0


    def resetMultiplicateur(self):
        self.multiplicateur =0

    def incrementerMultiplicateur(self):
        self.multiplicateur += 1

    def getScore(self):
        return self.valeur

    def getMultiplicateur(self):
        return self.multiplicateur

    def addScore(score, fichier):
        f = open(fichier, 'a')
        f.write(score + "\n")
        f.close()

    def getScoreFromTexte(fichier):
         f = open(fichier,'r')
             a = f.readline()
         f.close()
         return a
