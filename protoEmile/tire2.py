from pygame.locals import *
import pygame, os, sys
 
 
 
#-*-*- <Les Classes> || Début de <Jeu> -*-*-#
 
class Jeu(pygame.sprite.Sprite):
    """Classe <Jeu>"""
    def __init__(self, width = 480, height = 240):
        """Constructeur de la classe:
        - Créer une fenêtre
        - Affiche des images
 
        """
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
 
        #Variables
        self.horloge = pygame.time.Clock()
        self.width = width
        self.height = height
 
        #Screen + titre
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mon titre")
 
        #self.projectile = Projectile(self)
        self.perso = Perso(10,10,10,10,self.screen)
        self.projectile=Projectile([20,20],[40,40], self.screen)
 
        #On crée un groupe avec les instances self.bombe/perso/mur
        self.groupe = pygame.sprite.Group(self.projectile, self.perso)
 
 
    def mainloop(self):
        """Mainloop du jeu
        - Gestion des événements clavier
        - Blitage"""
        continuer = True
        
        while continuer:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print("x:",event.pos[0]," y:",event.pos[1])
                    xSouris=event.pos[0]
                    ySouris=event.pos[1]
                    xTrajectoire,yTrajectoire=CalculTrajectoireProjectile(POSITIONCERCLE[0],POSITIONCERCLE[1],xSouris,ySouris)
                    print("xTrajectoire",xTrajectoire," yTrajectoire",yTrajectoire)
                    pro.add(Projectile(POSITIONCERCLE,[xTrajectoire,yTrajectoire],fenetre))
                    print("test")


            #On blit tout le groupe d'un coup + flip + fill
            self.groupe.draw(self.screen)
            pygame.display.flip()
            self.screen.fill((0, 0, 0), self.perso.rect)
             
 
#-*-*- <Les Classes> || Début de <Perso> -*-*-#
 
class Perso(pygame.sprite.Sprite):
    """Perso"""
    def __init__(self,x,y,hauteur,largeur,screen):
        """Constructeur"""
        pygame.sprite.Sprite.__init__(self)
        self.bloc=pygame.draw.rect(screen, (0,0,0), (x,y,largeur,hauteur), 0)
        
        
 
        
 
        
 

 
#-*-*- <Les Classes> || Début de <Jeu> -*-*-#
 
class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos,trajectoire, screen):
        """Constructeur"""
        pygame.sprite.Sprite.__init__(self)
        self.bloc = pygame.draw.rect(screen, (0,0,0), (pos[0],pos[1],20,20), 0)
        
 
 
if __name__ == "__main__":
    partie = Jeu()
    partie.mainloop()
