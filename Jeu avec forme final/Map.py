from Projectile import *
from Bloc import *
from Ennemi import *

class Map():
    def __init__(self, jeu):
        self.gravitePartieHaute= -9  #changer les variables gravite
        self.gravitePartieMilieu=0
        self.gravitePartieBasse=9
        self.jeu=jeu
        self.groupeEnnemi= pygame.sprite.Group() #Compléter
        self.groupeBloc= pygame.sprite.Group() #Compléter
        self.groupeProjectile= pygame.sprite.Group()#compléter
