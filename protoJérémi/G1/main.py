import pygame
GRAVITY = 0.2  # Pretty low gravity.
XS = .1

from player import *
from block import *
from map import *

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1270, 670))
    pygame.display.set_caption("Scrolling Camera")
    clock = pygame.time.Clock()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(1)
    running = True
    map = Map()
    players = pygame.sprite.Group(Player((600, 0), screen))
    blocks = pygame.sprite.Group()
    map.creeMap(screen,blocks)

    while running:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            if event.type == pygame.MOUSEBUTTONDOWN:
                players.add(Player(event.pos, screen))
                #if pygame.mixer.get_busy == true:
                   # pygame.mixer.music.paused()
               # else:
                   # pygame.mixer.music.unpaused()
                
        pass
        if pressed[pygame.K_d]:
            for i in players:
                i.movex()
            pass
        if pressed[pygame.K_a]:
            for i in players:
                i.movexmin()
            pass
        if pressed[pygame.K_w]:
            for i in players:
                i.movey()
            pass



        players.update(blocks)

        screen.fill((10, 10, 30))
        players.draw(screen)
        blocks.draw(screen)
        camera_pos = (192,192)

        pygame.display.flip()
        world = pygame.Surface((1000,1000))
        clock.tick(60)


run_game()
pygame.quit()
