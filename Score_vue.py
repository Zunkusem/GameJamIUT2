import pygame
from pygame import *
from ClassGestionFichierScore import *

pygame.init()

score=pygame.display.set_mode([1280, 720])
score.fill([255, 255, 255])
background = pygame.draw.rect(score, [25, 6, 45], [0, 0, 1280, 720], 0)
left=500
top=600
score_width = (1280/2)-(left/2)
score_height = (720/2)+200

retour = pygame.draw.rect(score, [255, 0, 0], [0, 670, 125, 50], 0)

mid_x = pygame.draw.rect(score, [255, 0, 0], [1280/2, 0, 2, 720], 0)
mid_y = pygame.draw.rect(score, [255, 0, 0], [0, 720/2, 1280, 2], 0)

font.init()
font_a = pygame.font.SysFont('arial', 70)
font_b = pygame.font.SysFont('arial', 30)
font_c = pygame.font.SysFont('arial', 35)
font_d = pygame.font.SysFont('arial', 35)
font_e = pygame.font.SysFont('arial', 25)

font_titre = font_a.render("Meilleurs Scores", 1, (255,255,255))
font_return = font_b.render("RETOUR", 1, (134,210,48))


score_un = font_c.render(result[0][0] + " : " + result[1][0], 1,(255, 255, 255))
score_deux = font_c.render(result[0][1] + " : " + result[1][1], 1,(255, 255, 255))
score_trois = font_c.render(result[0][2] + " : " + result[1][2], 1,(255, 255, 255))
score_quatre = font_c.render(result[0][3] + " : " + result[1][3], 1,(255, 255, 255))
score_cinque = font_c.render(result[0][4] + " : " + result[1][4], 1,(255, 255, 255))
score_six = font_c.render(result[0][5] + " : " + result[1][5], 1,(255, 255, 255))
score_sept = font_c.render(result[0][6] + " : " + result[1][6], 1,(255, 255, 255))
score_huit = font_c.render(result[0][7] + " : " + result[1][7], 1,(255, 255, 255))
score_neuf = font_c.render(result[0][8] + " : " + result[1][8], 1,(255, 255, 255))
score_dix = font_c.render(result[0][9] + " : " + result[1][9], 1,(255, 255, 255))

font_un = font_c.render("1er : ", 1, (255, 255, 255))
font_deux = font_d.render("2ème : ", 1, (255, 255, 255))
font_trois = font_d.render("3ème : ", 1, (255, 255, 255))
font_quatre = font_e.render("4ème : ", 1, (255, 255, 255))
font_cinque = font_e.render("5ème : ", 1, (255, 255, 255))
font_six = font_e.render("6ème : ", 1, (255, 255, 255))
font_sept = font_e.render("7ème : ", 1, (255, 255, 255))
font_huit = font_e.render("8ème : ", 1, (255, 255, 255))
font_neuf = font_e.render("9ème : ", 1, (255, 255, 255))
font_dix = font_e.render("10ème : ", 1, (255, 255, 255))

#f.close()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 720 and event.pos[1] > 670:
            import Accueil_vue.py
    score.blit(font_return, (10,680))
    score.blit(font_titre, ((score_width+score_width+left-425)/2, score_height-550))
    score.blit(font_un, ((score_width+score_width+left-250)/2,110))
    score.blit(score_un, ((score_width+score_width+left-100)/2,110))
    score.blit(font_deux, ((score_width+score_width+left-300)/2,168))
    score.blit(score_deux, ((score_width+score_width+left-100)/2,168))
    score.blit(font_trois, ((score_width+score_width+left-300)/2,226))
    score.blit(score_trois, ((score_width+score_width+left-100)/2,226))
    score.blit(font_quatre, ((score_width+score_width+left-250)/2,284))
    score.blit(score_quatre, ((score_width+score_width+left-100)/2,274))
    score.blit(font_cinque, ((score_width+score_width+left-250)/2,342))
    score.blit(score_cinque, ((score_width+score_width+left-100)/2,332))
    score.blit(font_six, ((score_width+score_width+left-250)/2,400))
    score.blit(score_six, ((score_width+score_width+left-100)/2,390))
    score.blit(font_sept, ((score_width+score_width+left-250)/2,458))
    score.blit(score_sept, ((score_width+score_width+left-100)/2,448))
    score.blit(font_huit, ((score_width+score_width+left-250)/2,516))
    score.blit(score_huit, ((score_width+score_width+left-100)/2,506))
    score.blit(font_neuf, ((score_width+score_width+left-250)/2,574))
    score.blit(score_neuf, ((score_width+score_width+left-100)/2,564))
    score.blit(font_dix, ((score_width+score_width+left-275)/2,632))
    score.blit(score_dix, ((score_width+score_width+left-100)/2,622))
    pygame.display.flip()
pygame.quit()
