import pygame
screen=pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
red=255
blue=0
green=0
left=50
top=50
width=90
height=90
filled=0
pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
pygame.draw.rect(screen, [50, 50, 50], [0, 430, 200, 50], 0)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()
