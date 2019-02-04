import pygame


screen=pygame.display.set_mode([1280, 720])
screen.fill([255, 255, 255])
left=400
top=100
screen_width = (1280/2)-(left/2)
screen_height = (720/2)+200

start = pygame.draw.rect(screen, [255, 0, 0], [screen_width, screen_height, left, top], 0)
score = pygame.draw.rect(screen, [255, 125, 0], [screen_width, screen_height-125, left, top], 0)
credit = pygame.draw.rect(screen, [0, 255, 125], [screen_width, screen_height-250, left, top], 0)
quit = pygame.draw.rect(screen, [125, 0, 255], [screen_width, screen_height-375, left, top], 0)

mouse_xy = pygame.mouse.get_pos()
over_quit = quit.collidepoint(mouse_xy)

pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top and event.pos[1] > screen_height:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top-125 and event.pos[1] > screen_height-125:
            print("Crédit")
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top-250 and event.pos[1] > screen_height-250:
            print("Score")
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > screen_width and event.pos[0] < screen_width+left and event.pos[1] < screen_height+top-375 and event.pos[1] > screen_height-375:
            print("Jouer")
pygame.quit()
