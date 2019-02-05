from Ressort import *
from BlocDeCollision import *

class Bloc(pygame.sprite.Sprite):
    """Classe <Jeu>"""
    def __init__(self,map):
        self.map=map
        ressort = pygame.sprite.Group()
        blocDeCollision = pygame.sprite.Group()

    def addBlockH(pos,screen):
        blocDeCollision.add(BlocH((pos),screen))

    def addBlockV(pos,screen):
        blocDeCollision.add(BlocV((pos),screen))
