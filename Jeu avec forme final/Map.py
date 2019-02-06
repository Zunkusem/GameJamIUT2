import pygame
from Bloc import *
from Player import *
from Ennemi import *
from Projectile import *
from Jeu import *

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.bumper_list = pygame.sprite.Group()
        self.platformRetourArriere_list = pygame.sprite.Group()
        self.platformRetourAvant_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.ennemy_tourelle_liste = pygame.sprite.Group()
        self.player = player
        self.bullets_liste = pygame.sprite.Group()

        # How far this world has been scrolled left/right
        self.world_shiftx = 0
        self.world_shifty = 0

    # Update everythign on this level
    def update(self,player):
        print(len(self.bullets_liste))
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.bullets_liste.update(player)
        self.ennemy_tourelle_liste.update(self.bullets_liste,player)

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BLUE)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.bumper_list.draw(screen)
        self.platformRetourArriere_list.draw(screen)
        self.ennemy_tourelle_liste.draw(screen)
        self.bullets_liste.draw(screen)
        self.platformRetourAvant_list.draw(screen)

    def shift_worldx(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shiftx += shift_x


        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for platform in self.platformRetourArriere_list:
            platform.rect.x += shift_x

        for platform in self.platformRetourAvant_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for bump in self.bumper_list:
            bump.rect.x += shift_x

        for enemy in self.ennemy_tourelle_liste:
            enemy.rect.x += shift_x

        for bullet in self.bullets_liste:
            bullet.rect.x += shift_x

        # Bullet.shiftx(shift_x)



    def shift_worldy(self, shift_y):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        camspeed = abs(shift_y);

        # for platform in self.platform_list:
        #     platform.rect.y -= shift_y
        # for enemy in self.enemy_list:
        #     enemy.rect.y -= shift_y
        #
        # player.rect.top = 400
        # player.posP += shift_y

        self.world_shiftx += shift_y

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.y += shift_y

        for platform in self.platformRetourArriere_list:
            platform.rect.y += shift_y

        for platform in self.platformRetourAvant_list:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

        for bump in self.bumper_list:
            bump.rect.y += shift_y

        for enemy in self.ennemy_tourelle_liste:
            enemy.rect.y += shift_y

        for bullet in self.bullets_liste:
            bullet.rect.y += shift_y

class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -10000

        # Array with width, height, x, and y of platform
        level = [#bords de la map
                 [150, 968, -140, -100],
                 [10000, 100, 0, 758],
                 [150, 968, -140, -988],
                 [10000, 100, 0, -858],
                 #blocs 1ere partie en bas
                 [160, 30, 500, 630],
                 [160, 30, 800, 500],
                 [160, 30, 600, 380],
                 [90, 30, 980, 300],
                 [70, 30, 1300, 250],
                 [70, 30, 1600, 320],
                 [70, 30, 1900, 450],
                 [70, 30, 2100, 350],
                 [70, 30, 2000, 220],
                 [50, 618, 2200, 150],
                 [50, 1050, 2350, -50],
                 #blocs 2eme partie en haut
                 [150, 200, 1950, -768],
                 [100, 30, 2500, -700],
                 [100, 30, 2700, -650],
                 [10, 150, 2900, -680],
                 [100, 30, 3000, -650],
                 [10, 150, 3200, -680],
                 [100, 30, 3300, -650],
                 [200, 250, 3500, -758],
                 [50, 700, 3800, -778],
                 #blocs 3eme partie en bas et en haut
                 [500,200,2900,568],
                 ]



        Bump = [[100, 60, 2250, 718],
                [100, 60, 3700, -808],
                [100, 60, 4400, 757],
                ]

        levelPlatformRetourArriere = [[1400, 40, 800, 758],
                                      [750, 40, 2750, -798],
                                      [500, 40, 3900, 758],
                                      ]

        levelPlatformRetourAvant = [[100,100,100,100]]#exemple

        Ennemy= [[200,200,0],
                [10,200,1]
                ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for bumper in Bump:
            block = Bumper(bumper[0], bumper[1])
            block.rect.x = bumper[2]
            block.rect.y = bumper[3]
            block.player = self.player
            self.bumper_list.add(block)

        for PlatformRetourArr in levelPlatformRetourArriere:
            block = PlatformRetourArriere(PlatformRetourArr[0], PlatformRetourArr[1])
            block.rect.x = PlatformRetourArr[2]
            block.rect.y = PlatformRetourArr[3]
            block.player = self.player
            self.platformRetourArriere_list.add(block)

        for PlatformRetourAv in levelPlatformRetourAvant:
            block = PlatformRetourAvant(PlatformRetourAv[0], PlatformRetourAv[1])
            block.rect.x = PlatformRetourAv[2]
            block.rect.y = PlatformRetourAv[3]
            block.player = self.player
            self.platformRetourAvant_list.add(block)

        for ennemy in Ennemy:

            if ennemy[2] == 0:
                block = Cible()
                block.rect.x = ennemy[0]
                block.rect.y = ennemy[1]
                block.player = self.player
                self.enemy_list.add(block)

            elif ennemy[2] == 1:
                block = Tourelle()
                block.rect.x = ennemy[0]
                block.rect.y = ennemy[1]
                block.player = self.player
                self.ennemy_tourelle_liste.add(block)




# reate platforms for the level
#"
