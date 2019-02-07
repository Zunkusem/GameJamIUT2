import pygame
from Param import *

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height,x,y,screen):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        self.image = pygame.Surface([width, height])
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.screen = screen
        # self.texture = pygame.image.load("index.jpg")

    def graph(self):

        if self.width < self.height:
            texture = pygame.transform.scale(self.texture, [self.width,225])
            texture_rect=texture.get_rect()
            texture_rect.x = self.x
            texture_rect.y = self.y
            mult = (self.width+225)/225
            for i in range (0,int(mult)) :
                tmp_image=texture.copy()
                tmp_rect = tmp_image.get_rect()
                tmp_rect.x = self.width*i
                tmp_rect.y = self.y
            pass
        elif self.height <= self.width:
            texture = pygame.transform.scale(self.texture, [self.height,225])
            texture_rect=texture.get_rect()
            texture_rect.x = self.x
            texture_rect.y = self.y
            mult = (self.height+225)/225
            for i in range (0,int(mult)):
                tmp_image=texture.copy()
                tmp_rect = tmp_image.get_rect()
                tmp_rect.x = self.width*i
                tmp_rect.y = self.y
                self.screen.blit(tmp_image,tmp_rect)
            pass

        self.screen.blit(texture,texture_rect)
        pygame.display.flip()






class Bumper(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(CYAN)

        self.rect = self.image.get_rect()


class PlatformRetourAvant(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()


class PlatformRetourArriere(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
