import pygame
from pygame import *
from ClassGestionFichierScore import *

pygame.init()

score=pygame.display.set_mode([1024, 768])
#score.fill([255, 255, 255])
img_background = pygame.image.load("score.png").convert()
img_gold = pygame.image.load("or.png").convert()
img_silver= pygame.image.load("argent.png").convert()
img_bronze = pygame.image.load("bronze.png").convert()

gold = pygame.transform.scale(img_gold, (100,100))
silver = pygame.transform.scale(img_silver, (100,100))
bronze = pygame.transform.scale(img_bronze, (100,100))
background = pygame.transform.scale(img_background, (1024,768))
#background = pygame.draw.rect(score, [25, 6, 45], [0, 0, 1024, 768], 0)
left=500
top=600
score_width = (1024/2)-(left/2)
score_height = (768/2)+200

retour = pygame.draw.rect(score, [255, 0, 0], [0, 720, 125, 50], 0)

mid_x = pygame.draw.rect(score, [255, 0, 0], [1024/2, 0, 2, 768], 0)
mid_y = pygame.draw.rect(score, [255, 0, 0], [0, 768/2, 1024, 2], 0)

font.init()
#police titre
font_a = pygame.font.SysFont('arial', 70, bold=True)
#police retour
font_b = pygame.font.SysFont('arial', 30, bold=True)
#police 1er
font_c = pygame.font.SysFont('arial', 60, bold=True)
#police 2eme et 3eme
font_d = pygame.font.SysFont('arial', 45, bold=True)
#police reste du classement
font_e = pygame.font.SysFont('arial', 35)

titre = font_a.render("Meilleurs Scores", 1, (255,255,255))
font_return = font_b.render("RETOUR", 1, (134,210,48))

score_titre = font_c.render("PLACE           NOM         SCORE", 1,(255, 0, 255))
nom_un = font_c.render(result[0][0] , 1,(255, 0, 0))
nom_deux = font_d.render(result[0][1], 1,(255, 108, 0))
nom_trois = font_d.render(result[0][2], 1,(255, 229, 0))
nom_quatre = font_e.render(result[0][3], 1,(255, 255, 255))
nom_cinque = font_e.render(result[0][4], 1,(255, 255, 255))
nom_six = font_e.render(result[0][5], 1,(255, 255, 255))
nom_sept = font_e.render(result[0][6], 1,(255, 255, 255))
nom_huit = font_e.render(result[0][7], 1,(255, 255, 255))
nom_neuf = font_e.render(result[0][8], 1,(255, 255, 255))
nom_dix = font_e.render(result[0][9], 1,(255, 255, 255))


score_un = font_c.render(result[1][0], 1,(255, 0, 0))
score_deux = font_d.render(result[1][1], 1,(255, 108, 0))
score_trois = font_d.render(result[1][2], 1,(255, 229, 0))
score_quatre = font_e.render(result[1][3], 1,(255, 255, 255))
score_cinque = font_e.render(result[1][4], 1,(255, 255, 255))
score_six = font_e.render(result[1][5], 1,(255, 255, 255))
score_sept = font_e.render(result[1][6], 1,(255, 255, 255))
score_huit = font_e.render(result[1][7], 1,(255, 255, 255))
score_neuf = font_e.render(result[1][8], 1,(255, 255, 255))
score_dix = font_e.render(result[1][9], 1,(255, 255, 255))

place_un = font_c.render("1er:", 1, (255, 0, 0))
place_deux = font_d.render("2ème:", 1, (255, 108, 0))
place_trois = font_d.render("3ème:", 1, (255, 229, 0))
place_quatre = font_e.render("4ème:", 1, (255, 255, 255))
place_cinque = font_e.render("5ème:", 1, (255, 255, 255))
place_six = font_e.render("6ème:", 1, (255, 255, 255))
place_sept = font_e.render("7ème:", 1, (255, 255, 255))
place_huit = font_e.render("8ème:", 1, (255, 255, 255))
place_neuf = font_e.render("9ème:", 1, (255, 255, 255))
place_dix = font_e.render("10ème:", 1, (255, 255, 255))

#f.close()

running=True
while running:
    score.blit(background, (0,0))
    #score.blit(gold, 262,110)
    #score.blit(silver, 262,198)
    #score.blit(bronze, 262,276)
    score.blit(font_return, (10,720))
    score.blit(titre, (312, 0))
    score.blit(score_titre,(160, 80))
    score.blit(place_un, (190,160))
    score.blit(nom_un, (490,160))
    score.blit(score_un, (730,160))
    score.blit(place_deux, (190,228))
    score.blit(nom_deux, (490,228))
    score.blit(score_deux, (730,228))
    score.blit(place_trois, (190,286))
    score.blit(nom_trois, (490,286))
    score.blit(score_trois, (730,286))
    score.blit(place_quatre, (190,354))
    score.blit(nom_quatre, (490,354))
    score.blit(score_quatre, (730,354))
    score.blit(place_cinque, (190,412))
    score.blit(nom_cinque, (490,412))
    score.blit(score_cinque, (730,412))
    score.blit(place_six, (190,470))
    score.blit(nom_six, (490,470))
    score.blit(score_six, (730,470))
    score.blit(place_sept, (190,528))
    score.blit(nom_sept, (490,528))
    score.blit(score_sept, (730,528))
    score.blit(place_huit, (190,586))
    score.blit(nom_huit, (490,586))
    score.blit(score_huit, (730,586))
    score.blit(place_neuf, (190,644))
    score.blit(nom_neuf, (490,644))
    score.blit(score_neuf, (730,644))
    score.blit(place_dix, (190,702))
    score.blit(nom_dix, (490,702))
    score.blit(score_dix, (730,702))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 768 and event.pos[1] > 720:
            running = False
            import Accueil_vue
