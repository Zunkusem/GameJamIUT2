import pygame
from pygame import *

pygame.init()

score=pygame.display.set_mode([1280, 720])
score.fill([255, 255, 255])
background = pygame.draw.rect(score, [25, 6, 45], [0, 0, 1280, 720], 0)
left=500
top=600
score_width = (1280/2)-(left/2)
score_height = (720/2)+200

retour = pygame.draw.rect(score, [255, 0, 0], [0, 670, 125, 50], 0)

font.init()
font_a = pygame.font.SysFont('arial', 50)
font_b = pygame.font.SysFont('arial', 30)
font_c = pygame.font.SysFont('arial', 30)
font_d = pygame.font.SysFont('arial', 30)
font_e = pygame.font.SysFont('arial', 30)
font_titre = font_a.render("Meilleurs Scores", 1, (255,255,255))
font_return = font_b.render("RETOUR", 1, (134,210,48))
font_premier = font_c.render("1er : ", 1, (255, 255, 255))
font_premier = font_c.render("1er : ", 1, (255, 255, 255))
font_scnd = font_d.render("2ème : ", 1, (255, 255, 255))
font_trsm = font_e.render("3ème : ", 1, (255, 255, 255))




running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 720 and event.pos[1] > 670:
            import Accueil_vue.py
    score.blit(font_return, (10,680))
    score.blit(font_titre, ((score_width+score_width+left-175)/2, score_height-550))
    score.blit(font_trsm, (640,360))
    score.blit(font_scnd, (640,260))
    score.blit(font_premier, (640,160))
    pygame.display.flip()
pygame.quit()
