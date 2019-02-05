def estPair(i):
    if i%2 == 0:
        return True
    else:    
        return False

def separeScoreDuNom(liste):
    #peut permettre a recuperer les scores pour les afficher dans le jeu
    nom=[]
    score=[]
    for i in range(0,len(liste)):
        if(estPair(i)):
            nom.append(liste[i])
        else:
            score.append(liste[i])
    return (nom,score)

def transformeListeStringEnListeInteger(liste):
    nouvListe= []
    for i in liste:
        nouvListe.append(int(i))
    return nouvListe

def transformeListeIntEnListeString(liste):
    nouvListe= []
    for i in liste:
        nouvListe.append(str(i))
    return nouvListe

def ajouteScore(nom,score,listeNom,listeScore):
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
    
def enregistrerNouvelleListe(nom,score,nomFichier):
    fichier=open(nomFichier,'w')#pour un fichier texte, sinon, mettre 'wb' au lieu de "w"
    #le fichier a été vidé ci-dessus
    for i in range(0,len(score)):
        fichier.write(nom[i]+":"+score[i]+",")#on peut maintenant écrire
    
    fichier.close()#ne pas oublier pour libérer l'accès.
    

def recupereLaListe(fichier):
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


listeBrute=recupereLaListe("score.txt")                                         #recupere la liste brute des scores dans le ficher desire
nom,score=separeScoreDuNom(listeBrute)                                          #separe les noms des scores
score=transformeListeStringEnListeInteger(score)                                #transforme la liste score en integer
nom,score=ajouteScore("Premier",39888888888888,nom,score)                       #ajoute les scores si ils sont suffisants
print("nouvelle liste:")
print(nom)
print(score)
enregistrerNouvelleListe(nom,transformeListeIntEnListeString(score),"score.txt")#ecrit le resultat dans le fichier desiré



    
    

    
    
    
