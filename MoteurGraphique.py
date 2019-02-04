import pygame

pygame.init()
clock = pygame.time.Clock()

CIEL = 0, 200, 255
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0

def main():
    fenetre = pygame.display.set_mode((640,480),RESIZABLE)
    green_color = GREEN
    white_color = WHITE
    red_color = RED
    loop = True

    while loop:
        #récupération et affichage du fond
    background = pygame.image.load("start.jpg").convert()
    fenetre.blit(background, (0,0))
        #affichage des boutons du jeu
    rect_white = pygame.draw.rect(fenetre, white_color, [75, 10, 100, 50])
    rect_green = pygame.draw.rect(fenetre, green_color, [250, 10, 100, 50])
    rect_red = pygame.draw.rect(fenetre, red_color, [250, 10, 100, 50])

        # retourne 1 si le curseur est au dessus du rectangle
    mouse_xy = pygame.mouse.get_pos()
    over_white = rect_white.collidepoint(mouse_xy)
    over_green = rect_green.collidepoint(mouse_xy)
    over_red = rect_red.collidepoint(mouse_xy)

        # Actualisation de l'affichage
    pygame.display.flip()
        # 10 fps
    clock.tick(10)

if __name__ == '__main__':
    main()
