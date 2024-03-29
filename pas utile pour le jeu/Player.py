import pygame
from Param import *
from Map import *
from Projectile import *
from Ennemi import *

class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)



        # Set a referance to the image rect.
        self.rect = self.image.get_rect()


        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.Gstate = 1
        self.Gmult =1
        self.level = None
        self.G = 0.35
        self.Gstat = 1
        self.J1 = 2
        self.J2 = -10
        # self.BZone = -150
        # self.TZone = -800
        self.posP = 0

    def invG(self):
        self.G = self.G*(-1)
        self.Gstat = self.Gstat*(-1)
        self.J1 = self.J1*(-1)
        self.J2 = self.J2*(-1)

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()


        # Move left/right
        self.rect.x += self.change_x

        # See if we hit PlateformPic
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platformRetourArriere_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.Gmult == 1
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.Gmult == 1
                self.rect.left = block.rect.right
            else:
                self.Gmult == 0

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platformRetourAvant_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.Gmult == 1
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.Gmult == 1
                self.rect.left = block.rect.right
            else:
                self.Gmult == 0

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.Gmult == 1
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.Gmult == 1
                self.rect.left = block.rect.right
            else:
                self.Gmult == 0


        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platformRetourArriere_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0
            self.change_x= -15

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platformRetourAvant_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0
            self.change_x= 15



        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

        block_hit_list = pygame.sprite.spritecollide(self, self.level.bumper_list, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.change_y = -10;
            elif self.change_y < 0:
                self.change_y = 10;
            self.invG();

        self.posP += self.change_y





    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = self.Gstat*self.Gmult
        else:
            self.change_y += self.G*self.Gmult

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        self.rect.y += self.J1
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= self.J1

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = self.J2


    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def shoot(self, xSouris, ySouris):
        self.level.bullets_liste.add(Bullet(self.rect.centerx, self.rect.top, xSouris, ySouris))
