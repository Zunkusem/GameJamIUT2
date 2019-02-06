import pygame
from Bloc import *
from Player import *

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # How far this world has been scrolled left/right
        self.world_shiftx = 0
        self.world_shifty = 0

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BLUE)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_worldx(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shiftx += shift_x


        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    def shift_worldy(self, shift_y, player):
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

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

# Create platforms for the level
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
                 [50, 30, 1000, 250],
                 [50, 30, 1300, 250],
                 [50, 30, 1600, 250],
                 [50, 30, 1900, 450],
                 [50, 30, 2100, 350],
                 [50, 30, 2050, 220],
                 [50, 618, 2200, 150],
                 [50, 900, 2350 , 100],
                 #blocs 2eme partie en haut
                 [100, 30, 2500, -700],
                 [100, 30, 2700, -650],
                 [10, 150, 2900, -680],
                 [100, 30, 3000, -650],
                 [10, 150, 3200, -680],
                 [100, 30, 3300, -650],
                 [200, 250, 3500, -758],
                 [50, 900, 3800, -778],
                 ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


# reate platforms for the level
#"
