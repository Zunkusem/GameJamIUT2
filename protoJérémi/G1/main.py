import pygame
GRAVITY = 0.2  # Pretty low gravity.
XS = .1

from player import *
from block import *

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1270, 670))
    pygame.display.set_caption("Scrolling Camera")
    clock = pygame.time.Clock()
    running = True
    circles = pygame.sprite.Group(Player((600, 0), screen))
    blocks = pygame.sprite.Group(Block((600,600), screen))
    blocks.add(Block((690,600), screen))
    blocks.add(Block((690,200), screen))
    blocks.add(Block((780,620), screen))
    blocks.add(Block((510,620), screen))

    while running:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                circles.add(Player(event.pos, screen))
        pass
        if pressed[pygame.K_d]:
            for i in circles:
                i.movex()
            pass
        if pressed[pygame.K_a]:
            for i in circles:
                i.movexmin()
            pass
        if pressed[pygame.K_w]:
            for i in circles:
                i.movey()
            pass

        circles.update(blocks)

        screen.fill((10, 10, 30))
        circles.draw(screen)
        blocks.draw(screen)

        pygame.display.flip()
        clock.tick(60)


run_game()
pygame.quit()
