class Score():
    def __init__(self,nomDuFichier):  #le mettre avec l'extension
        self.nom=nomDuFichier

    def getNom(self):
        return self.nom

    def recupèreLesScores(self):
        #return tupes de deux listes avec nom et score en string
        listeBrute=self.recupereLaListe(self.getNom())
        nom,score=self.separeScoreDuNom(listeBrute)
        return (nom,score)

    def EnregistreScore(self, nomJoueur,scoreJoueur):#nomJoueur en string et score en int meme si le score n'est pas dans le top 10, faire cette methode, elle gerera ca
        nom,score=self.recupèreLesScores()
        score=self.transformeListeStringEnListeInteger(score)
        nom,score=self.ajouteScore(nomJoueur,scoreJoueur,nom,score)
        self.enregistrerNouvelleListe(nom,self.transformeListeIntEnListeString(score),self.getNom())

    def estPair(self, i):
        if i%2 == 0:
            return True
        else:
            return False

    def separeScoreDuNom(self, liste):                #separe les noms des scores
        #peut permettre a recuperer les scores pour les afficher dans le jeu
        nom=[]
        score=[]
        for i in range(0,len(liste)):
            if(self.estPair(i)):
                nom.append(liste[i])
            else:
                score.append(liste[i])
        return (nom,score)

    def transformeListeStringEnListeInteger(self, liste): #transforme la liste score en integer
        nouvListe= []
        for i in liste:
            nouvListe.append(int(i))
        return nouvListe

    def transformeListeIntEnListeString(self, liste):
        nouvListe= []
        for i in liste:
            nouvListe.append(str(i))
        return nouvListe

    def ajouteScore(self, nom,score,listeNom,listeScore): #ajoute les scores si ils sont suffisants
        nouvListeScore= []
        nouvListeNom=[]
        for i in range(0,len(listeScore)):
            if(listeScore[i]>score):
                nouvListeScore.append(listeScore[i])
                nouvListeNom.append(listeNom[i])
            else:
                nouvListeScore.append(score)
                nouvListeNom.append(nom)
                score=0
                nouvListeScore.append(listeScore[i])
                nouvListeNom.append(listeNom[i])
        if len(nouvListeScore)>10:
            nouvListeScore.pop()
            nouvListeNom.pop()
        return (nouvListeNom,nouvListeScore)

    def enregistrerNouvelleListe(self, nom,score,nomFichier):     #ecrit le resultat dans le fichier desiré
        fichier=open(nomFichier,'w')#pour un fichier texte, sinon, mettre 'wb' au lieu de "w"
        #le fichier a été vidé ci-dessus
        for i in range(0,len(score)):
            fichier.write(nom[i]+":"+score[i]+",")#on peut maintenant écrire

        fichier.close()#ne pas oublier pour libérer l'accès.


    def recupereLaListe(self, fichier):   #recupere la liste brute des scores dans le ficher desire
        f = open(fichier,'r') #ouvre le fichier
        text = str(f.readlines())      #recupere
        text=text.replace("'","")       #eleve les caractere en trop
        text=text.replace("[","")
        text=text.replace("]","")
        #text[2:(len(text)-2)]
        textSplit=text.split(',')       #decoupe suivant les virugule
        a=[]
        for i in textSplit:
            i=i.split(':')
            a+=i
        f.close()
        return a


sc = Score("score.txt")
result = sc.recupèreLesScores()
