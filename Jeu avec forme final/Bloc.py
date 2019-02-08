import pygame
from Param import *

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        self.image = pygame.Surface([width, height])
        BLUE = (3,50,68)
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        # self.texture = pygame.image.load("index.jpg")








class Bumper(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        ORANGE = (255,102,66)
        self.image = pygame.Surface([width, height])
        self.image.fill(ORANGE)

        self.rect = self.image.get_rect()


class PlatformRetourAvant(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()

        VERT = (17,158,82)
        self.image = pygame.Surface([width, height])
        self.image.fill(VERT)

        self.rect = self.image.get_rect()


class PlatformRetourArriere(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        VERT = (17,158,82)
        self.image = pygame.Surface([width, height])
        self.image.fill(VERT)

        self.rect = self.image.get_rect()
