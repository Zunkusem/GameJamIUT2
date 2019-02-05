import pygame
GRAVITY = 0.2  # Pretty low gravity.
XS = .1

from player import *
from block import *
from map import *

def run_game():
    pygame.init()
    world = pygame.Surface((1000,1000))
    screen = pygame.display.set_mode((1270, 670))
    pygame.display.set_caption("Scrolling Camera")
    clock = pygame.time.Clock()
    running = True
    map = Map()
    circles = pygame.sprite.Group(Player((600, 0), screen))
    blocks = pygame.sprite.Group()
    map.creeMap(screen,blocks)

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
        camera_pos = (192,192)
        # screen.blit(world,camera_pos)

        pygame.display.flip()
        clock.tick(60)


run_game()
pygame.quit()
