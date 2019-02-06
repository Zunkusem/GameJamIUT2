import pygame
from pygame import *


pygame.init()

screen=pygame.display.set_mode([1024, 768])
#screen.fill([255, 255, 255])
img = pygame.image.load("start.jpg").convert()
background = pygame.transform.scale(img, (1024,768))
#background = pygame.draw.rect(screen, [59, 55, 55], [0, 0, 1024, 768], 0)
left=400
top=100
screen_width = (1024/2)-(left/2)
screen_height = (768/2)+200

#mid_x = pygame.draw.rect(screen, [255, 0, 0], [1024/2, 0, 2, 768], 0)
#mid_y = pygame.draw.rect(screen, [255, 0, 0], [0, 768/2, 1024, 2], 0)

start = pygame.draw.rect(screen, [255, 0, 0], [screen_width, screen_height, left, top], 0)
score = pygame.draw.rect(screen, [255, 125, 0], [screen_width, screen_height-125, left, top], 0)
credit = pygame.draw.rect(screen, [0, 255, 125], [screen_width, screen_height-250, left, top], 0)
quit = pygame.draw.rect(screen, [125, 0, 255], [screen_width, screen_height-375, left, top], 0)

font.init()
font_a = pygame.font.SysFont('arial', 40)
font_b = pygame.font.SysFont('arial', 70)
#font_titre = font_b.render("CybeRush180 by KotProd", 1, (0,0,0))
font_start = font_a.render("START", 1, (255,255,255))
font_score = font_a.render("SCORE", 1, (255,255,255))
font_credit = font_a.render("CREDITS", 1, (255,255,255))
font_quit = font_a.render("QUITTER", 1, (255,255,255))

run=True
while run:
    screen.blit(background, (0,0))
    #screen.blit(font_titre, ((screen_width+screen_width-275)/2, screen_height-500))
    screen.blit(font_start, ((screen_width+screen_width+left-120)/2, screen_height-350))
    screen.blit(font_score, ((screen_width+screen_width+left-125)/2, screen_height-225))
    screen.blit(font_credit, ((screen_width+screen_width+left-135)/2, screen_height-100))
    screen.blit(font_quit, ((screen_width+screen_width+left-135)/2, screen_height+25))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top and event.pos[1] > screen_height:
            run=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top-125 and event.pos[1] > screen_height-125:
            import Credit_vue
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top-250 and event.pos[1] > screen_height-250:
            import Score_vue
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top-375 and event.pos[1] > screen_height-375:
            import Start_vue
