import pygame
from pygame import *

f = open("score.txt",'r')
text = str(f.readlines())
for line in f:
    text = text + str(f.read())

print(text)
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
font_c = pygame.font.SysFont('arial', 45)
font_d = pygame.font.SysFont('arial', 35)
font_e = pygame.font.SysFont('arial', 25)

font_titre = font_a.render("Meilleurs Scores", 1, (255,255,255))
font_return = font_b.render("RETOUR", 1, (134,210,48))

font_un = font_c.render("1er : ", 1, (255, 255, 255))
score_un = font_c.render(text[3], 1,(255, 255, 255))
font_deux = font_d.render("2ème : ", 1, (255, 255, 255))
font_trois = font_d.render("3ème : ", 1, (255, 255, 255))
font_quatre = font_e.render("4ème : ", 1, (255, 255, 255))
font_cinque = font_e.render("5ème : ", 1, (255, 255, 255))
font_six = font_e.render("6ème : ", 1, (255, 255, 255))
font_sept = font_e.render("7ème : ", 1, (255, 255, 255))
font_huit = font_e.render("8ème : ", 1, (255, 255, 255))
font_neuf = font_e.render("9ème : ", 1, (255, 255, 255))
font_dix = font_e.render("10ème : ", 1, (255, 255, 255))

f.close()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 720 and event.pos[1] > 670:
            import Accueil_vue.py
    score.blit(font_return, (10,680))
    score.blit(font_titre, ((score_width+score_width+left-175)/2, score_height-550))
    score.blit(font_un, ((score_width+score_width+left-325)/2,100))
    score.blit(score_un, ((score_width+score_width+left-250)/2,100))
    score.blit(font_deux, ((score_width+score_width+left-350)/2,165))
    score.blit(font_trois, ((score_width+score_width+left-350)/2,230))
    score.blit(font_quatre, ((score_width+score_width+left-300)/2,295))
    score.blit(font_cinque, ((score_width+score_width+left-300)/2,360))
    score.blit(font_six, ((score_width+score_width+left-300)/2,425))
    score.blit(font_sept, ((score_width+score_width+left-300)/2,490))
    score.blit(font_huit, ((score_width+score_width+left-300)/2,555))
    score.blit(font_neuf, ((score_width+score_width+left-300)/2,620))
    score.blit(font_dix, ((score_width+score_width+left-325)/2,685))
    pygame.display.flip()
pygame.quit()
