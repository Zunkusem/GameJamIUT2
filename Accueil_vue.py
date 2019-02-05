import pygame
from pygame import *

def accueil():
pygame.init()

screen=pygame.display.set_mode([1280, 720])
screen.fill([255, 255, 255])
background = pygame.draw.rect(screen, [59, 55, 55], [0, 0, 1280, 720], 0)
left=400
top=100
screen_width = (1280/2)-(left/2)
screen_height = (720/2)+200

start = pygame.draw.rect(screen, [255, 0, 0], [screen_width, screen_height, left, top], 0)
score = pygame.draw.rect(screen, [255, 125, 0], [screen_width, screen_height-125, left, top], 0)
credit = pygame.draw.rect(screen, [0, 255, 125], [screen_width, screen_height-250, left, top], 0)
quit = pygame.draw.rect(screen, [125, 0, 255], [screen_width, screen_height-375, left, top], 0)

font.init()
font_a = pygame.font.SysFont('arial', 40)
font_b = pygame.font.SysFont('arial', 70)
font_titre = font_b.render("OCTOGONE SANS REGLE", 1, (0,0,0))
font_start = font_a.render("START", 1, (255,255,255))
font_score = font_a.render("SCORE", 1, (255,255,255))
font_credit = font_a.render("CREDITS", 1, (255,255,255))
font_quit = font_a.render("QUITTER", 1, (255,255,255))

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top and event.pos[1] > screen_height:
            run=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top-125 and event.pos[1] > screen_height-125:
            import Credit_vue.py
            from Credit_vue.py import *
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top-250 and event.pos[1] > screen_height-250:
            pygame.display.flip()
            #run=False
            #import Score_vue.py
            from Score_vue.py import *
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top-375 and event.pos[1] > screen_height-375:
            import Start_vue.py
            from Start_vue.py import *

    screen.blit(font_titre, ((screen_width+screen_width-275)/2, screen_height-500))
    screen.blit(font_start, ((screen_width+screen_width+left-120)/2, screen_height-350))
    screen.blit(font_score, ((screen_width+screen_width+left-125)/2, screen_height-225))
    screen.blit(font_credit, ((screen_width+screen_width+left-135)/2, screen_height-100))
    screen.blit(font_quit, ((screen_width+screen_width+left-135)/2, screen_height+25))
    pygame.display.flip()
pygame.quit()
