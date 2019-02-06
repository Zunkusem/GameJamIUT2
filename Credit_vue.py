import pygame
from pygame import *

pygame.init()

credit=pygame.display.set_mode([1280, 720])
credit.fill([255, 255, 255])
background = pygame.draw.rect(credit, [25, 6, 45], [0, 0, 1280, 720], 0)
left=500
top=600
credit_width = (1280/2)-(left/2)
credit_height = (720/2)+200

mid_x = pygame.draw.rect(score, [255, 0, 0], [1280/2, 0, 2, 720], 0)
mid_y = pygame.draw.rect(score, [255, 0, 0], [0, 720/2, 1280, 2], 0)

retour = pygame.draw.rect(credit, [255, 0, 0], [0, 670, 125, 50], 0)

font.init()
font_a = pygame.font.SysFont('arial', 50)
font_b = pygame.font.SysFont('arial', 30)
font_titre = font_a.render("CREDITS", 1, (255,255,255))
font_return = font_b.render("RETOUR", 1, (0,0,0))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 720 and event.pos[1] > 680:
            import Accueil_vue.py
            running=False

    credit.blit(font_return, (10,680))
    credit.blit(font_titre, ((credit_width+credit_width+left-120)/2, credit_height-550))

    pygame.display.flip()
pygame.quit()
