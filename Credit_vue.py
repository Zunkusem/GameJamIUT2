import pygame
from pygame import *

pygame.init()

credit=pygame.display.set_mode([1024, 768])
#credit.fill([255, 255, 255])
img = pygame.image.load("start.jpg").convert()
#background = pygame.transform.scale(img, (1024,768))
background = pygame.draw.rect(credit, [25, 6, 45], [0, 0, 1024, 768], 0)
left=500
top=600
credit_width = (1024/2)-(left/2)
credit_height = (768/2)+200

mid_x = pygame.draw.rect(credit, [255, 0, 0], [1024/2, 0, 2, 768], 0)
mid_y = pygame.draw.rect(credit, [255, 0, 0], [0, 768/2, 1024, 2], 0)

retour = pygame.draw.rect(credit, [255, 0, 0], [0, 720, 125, 50], 0)

font.init()
font_a = pygame.font.SysFont('arial', 50)
font_b = pygame.font.SysFont('arial', 30)
font_c = pygame.font.SysFont('arial', 25)

titre = font_a.render("KOTPROD", 1, (255,255,255))
retour = font_b.render("RETOUR", 1, (255,255,255))

credit_un= font_c.render("GAME DESIGN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
credit_deux = font_c.render("ANIMATIONS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
credit_trois = font_c.render("LEVEL DESIGN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
credit_quatre = font_c.render("CARACTERE DESIGN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
credit_cinque = font_c.render("MUSIC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
credit_six = font_c.render("CONTROL DESIGN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
credit_sept = font_c.render("TEXTURE ENVIRONEMENT. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
credit_huit = font_c.render("IMAGE MENU. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
credit_neuf = font_c.render("POCHETTE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
credit_dix = font_c.render("MENUS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", 1, (255,255,255))
bravo = font_c.render("Bravo à toute l'équipe du projet pour cette performance !", 1, (255,255,255))

running=True
while running:
    #credit.blit(background,(0,0))
    credit.blit(retour, (10,725))
    credit.blit(titre, (420, 0))
    credit.blit(credit_un, (100, 80))
    credit.blit(credit_deux, (100, 120))
    credit.blit(credit_trois, (100, 160))
    credit.blit(credit_quatre, (100, 200))
    credit.blit(credit_cinque, (100, 240))
    credit.blit(credit_six, (100, 280))
    credit.blit(credit_sept, (100, 320))
    credit.blit(credit_huit, (100, 360))
    credit.blit(credit_neuf, (100, 400))
    credit.blit(credit_dix, (100, 440))
    credit.blit(bravo, (250, 550))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 0 and event.pos[0] < 125 and event.pos[1] < 770 and event.pos[1] > 720:
            import Accueil_vue
            running=False
