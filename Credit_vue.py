import pygame
from pygame import *

pygame.init()

screen=pygame.display.set_mode([1280, 720])
screen.fill([255, 255, 255])
left=500
top=600
screen_width = (1280/2)-(left/2)
screen_height = (720/2)+200

retour = pygame.draw.rect(screen, [255, 0, 0], [0, 0, 125, 50], 0)
credit = pygame.draw.rect(screen, [255, 255, 255], [screen_width, screen_height, left, top], 0)

font.init()
font_a = pygame.font.SysFont('arial', 50)
font_b = pygame.font.SysFont('arial', 30)
font_titre = font_a.render("CREDITS", 1, (0,0,0))
font_return = font_b.render("RETOUR", 1, (0,0,0))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 50 and event.pos[1] > 0:
            import Accueil_vue.py
    screen.blit(font_return, (0,0))
    screen.blit(font_titre, ((screen_width+screen_width+left-120)/2, screen_height-550))

    pygame.display.flip()
