import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1280,720),RESIZABLE)

fond = pygame.image.load("start.jpg").convert()
fenetre.blit(fond, (0,0))

pygame.display.flip

continuer = 1
while continuer:
    continuer = int(input())
