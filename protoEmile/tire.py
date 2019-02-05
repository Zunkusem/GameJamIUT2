#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

# Before you can do much with pygame, you will need to initialize it
pygame.init()
# Init de clock
clock = pygame.time.Clock()

CIEL = 0, 200, 255  # parenthèses inutiles, l'interpréteur reconnaît un tuple

def main():
    fenetre = pygame.display.set_mode((640, 480))

    # loop
    loop = True
    # Création d'une image de la taille de la fenêtre
    background = pygame.Surface(fenetre.get_size())

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("x:",event.pos[0]," y:",event.pos[1])#position en Y


        # Superposition du fond ciel
        background.fill(CIEL)
        fenetre.blit(background, (0, 0))

        # Rafraîchissement de l'écran
        pygame.display.flip()
        # By calling Clock.tick(10) once per frame, the program will never run
        # at more than 10 frames per second
        clock.tick(10)

if __name__ == '__main__':
    main()
