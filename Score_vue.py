import pygame
from pygame import *


pygame.init()

score=pygame.display.set_mode([1280, 720])
score.fill([255, 255, 255])
background = pygame.draw.rect(score, [25, 6, 45], [0, 0, 1280, 720], 0)
left_s=500
top_s=600
score_width = (1280/2)-(left_s/2)
score_height = (720/2)+200

retour = pygame.draw.rect(score, [255, 0, 0], [0, 670, 125, 50], 0)

font.init()
font_a = pygame.font.SysFont('arial', 50)
font_b = pygame.font.SysFont('arial', 30)
font_titre = font_a.render("Meilleurs Scores", 1, (255,255,255))
font_return = font_b.render("RETOUR", 1, (0,0,0))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 720 and event.pos[1] > 670:
            running=False
            #run=True
            #import Accueil_vue.py
            from Accueil_vue.py import *

    score.blit(font_return, (10,680))
    score.blit(font_titre, ((score_width+score_width+left_s-175)/2, score_height-550))
    pygame.display.flip()
pygame.quit()