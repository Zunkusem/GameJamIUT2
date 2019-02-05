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
        f = open(fichier, 'w')
        f.write(score + "\n")
        f.close()

    def getScoreFromTexte(fichier):
f = open('score', 'r')
if f == null:
    print("pas de score")
    f.close()
else:
    for i in f:
        a = f.readlines()
        print(a)
    f.close()
