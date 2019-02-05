import pygame
GRAVITY = 0.2  # Pretty low gravity.
XS = .1
class Block(pygame.sprite.Sprite):

    def __init__(self, pos, screen):
        super().__init__()
        lenght = 100
        height = 50
        self.screen = screen
        self.image = self.image = pygame.Surface((lenght, 50), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (255, 255, 255), pygame.rect.Rect((0, 0, lenght, height)))
        self.rect = self.image.get_rect(center=pos)
        self.hittop = [pos[0]-(lenght/2)-25,pos[1]-(lenght/2)+5,(pos[0]+lenght)-(lenght/2),pos[1]]
        self.hitleft = [pos[0]-(lenght/2)-25,pos[1]-(lenght/2)+10,pos[0]-(lenght/2)-25,(pos[1]+height)-(height/2)]
        self.hitright = [(pos[0]+lenght)-(lenght/2),pos[1],(pos[0]+lenght)-(lenght/2),(pos[1]+height)-(height/2)]
        self.hitbottom = [pos[0]-(lenght/2)-25,(pos[1]+height)-(height/2),(pos[0]+lenght)-(lenght/2),(pos[1]+height)-(height/2)]

class Block2(pygame.sprite.Sprite):

    def __init__(self, pos, screen):
        super().__init__()
        lenght = 50
        height = 100
        self.screen = screen
        self.image = self.image = pygame.Surface((lenght, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (255, 255, 255), pygame.rect.Rect((0, 0, lenght, height)))
        self.rect = self.image.get_rect(center=pos)
        self.hittop = [pos[0]-(lenght/2)-25,pos[1]-(lenght/2)+5,(pos[0]+lenght)-(lenght/2),pos[1]]
        self.hitleft = [pos[0]-(lenght/2)-25,pos[1]-(lenght/2)+10,pos[0]-(lenght/2)-25,(pos[1]+height)-(height/2)]
        self.hitright = [(pos[0]+lenght)-(lenght/2),pos[1],(pos[0]+lenght)-(lenght/2),(pos[1]+height)-(height/2)]
        self.hitbottom = [pos[0]-(lenght/2)-25,(pos[1]+height)-(height/2),(pos[0]+lenght)-(lenght/2),(pos[1]+height)-(height/2)]
