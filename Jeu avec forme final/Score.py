class Score():

    def __init__(self):
        self.nombre=0
        self.multiplicateur=1

    def incrementeScoreDeUn(self):
        self.nombre=self.nombre+1*self.multiplicateur

    def incrementemultiplicateurDeUn(self):
        self.multiplicateur=self.multiplicateur+1

    def resetMultiplicateur(self):
        self.multiplicateur=1

    def getScore(self):
        return str(self.nombre)

    def getMultiplicateur(self):
        return str(self.multiplicateur)

    def setScore(self, score):
        self.nombre=score

    def setMultiplicateur(self, multipli):
        self.multiplicateur=multipli
    
""" Exemple Code
sc=Score()
sc.incrementeScoreDeUn()
print("score:",sc.getScore())
print(sc.getMultiplicateur())

sc.incrementeScoreDeUn()
print("score:",sc.getScore())
print(sc.getMultiplicateur())

sc.incrementeScoreDeUn()
print("score:",sc.getScore())
print(sc.getMultiplicateur())

sc.incrementeScoreDeUn()
print("score:",sc.getScore())
print(sc.getMultiplicateur())

sc.incrementemultiplicateurDeUn()
print("score:",sc.getScore())
print(sc.getMultiplicateur())

sc.incrementemultiplicateurDeUn()
print("score:",sc.getScore())
print(sc.getMultiplicateur())

sc.incrementemultiplicateurDeUn()
print("score:",sc.getScore())
print(sc.getMultiplicateur())

sc.incrementemultiplicateurDeUn()
print("score:",sc.getScore())
print(sc.getMultiplicateur())

sc.incrementeScoreDeUn()
print("score:",sc.getScore())
print(sc.getMultiplicateur())

sc.resetMultiplicateur()
print("score:",sc.getScore())
print(sc.getMultiplicateur())
"""
