import pygame
import sys
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
        self.imagesflipR = []
        self.imagesflipL = []
        self.imagesL = []
        self.imagesR = []
        self.imagesflipR.append( pygame.image.load('Playerpic/AnimationFlipR0000.png'))
        self.imagesflipR.append( pygame.image.load('Playerpic/AnimationFlipR0001.png'))
        self.imagesflipR.append( pygame.image.load('Playerpic/AnimationFlipR0002.png'))
        self.imagesflipR.append( pygame.image.load('Playerpic/AnimationFlipR0003.png'))
        self.imagesflipR.append( pygame.image.load('Playerpic/AnimationFlipR0004.png'))
        self.imagesflipR.append( pygame.image.load('Playerpic/AnimationFlipR0005.png'))
        self.imagesflipR.append( pygame.image.load('Playerpic/AnimationFlipR0006.png'))
        self.imagesflipR.append( pygame.image.load('Playerpic/AnimationFlipR0007.png'))

        self.imagesflipL.append( pygame.image.load('Playerpic/AnimationFlipL0000.png'))
        self.imagesflipL.append( pygame.image.load('Playerpic/AnimationFlipL0001.png'))
        self.imagesflipL.append( pygame.image.load('Playerpic/AnimationFlipL0002.png'))
        self.imagesflipL.append( pygame.image.load('Playerpic/AnimationFlipL0003.png'))
        self.imagesflipL.append( pygame.image.load('Playerpic/AnimationFlipL0004.png'))
        self.imagesflipL.append( pygame.image.load('Playerpic/AnimationFlipL0005.png'))
        self.imagesflipL.append( pygame.image.load('Playerpic/AnimationFlipL0006.png'))
        self.imagesflipL.append( pygame.image.load('Playerpic/AnimationFlipL0007.png'))

        self.imagesR.append( pygame.image.load('Playerpic/AnimationR0000.png'))
        self.imagesR.append( pygame.image.load('Playerpic/AnimationR0001.png'))
        self.imagesR.append( pygame.image.load('Playerpic/AnimationR0002.png'))
        self.imagesR.append( pygame.image.load('Playerpic/AnimationR0003.png'))
        self.imagesR.append( pygame.image.load('Playerpic/AnimationR0004.png'))
        self.imagesR.append( pygame.image.load('Playerpic/AnimationR0005.png'))
        self.imagesR.append( pygame.image.load('Playerpic/AnimationR0006.png'))
        self.imagesR.append( pygame.image.load('Playerpic/AnimationR0007.png'))

        self.imagesL.append( pygame.image.load('Playerpic/AnimationL0000.png'))
        self.imagesL.append( pygame.image.load('Playerpic/AnimationL0001.png'))
        self.imagesL.append( pygame.image.load('Playerpic/AnimationL0002.png'))
        self.imagesL.append( pygame.image.load('Playerpic/AnimationL0003.png'))
        self.imagesL.append( pygame.image.load('Playerpic/AnimationL0004.png'))
        self.imagesL.append( pygame.image.load('Playerpic/AnimationL0005.png'))
        self.imagesL.append( pygame.image.load('Playerpic/AnimationL0006.png'))
        self.imagesL.append( pygame.image.load('Playerpic/AnimationL0007.png'))


        self.index = 0
        self.image = self.imagesR[self.index]



        # Set a referance to the image rect.
        self.rect = self.imagesR[0].get_rect()


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
        self.J3 = -5
        # self.BZone = -150
        # self.TZone = -800
        self.posP = 0
        self.countdonw = 10

    def invG(self):
        self.G = self.G*(-1)
        self.Gstat = self.Gstat*(-1)
        self.J1 = self.J1*(-1)
        self.J2 = self.J2*(-1)
        self.J3 = self.J3*(-1)

    def update(self,screen):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        BLACK = (0, 0, 0)
        self.countdonw -= 1
        if self.change_x > 0 :
            if self.countdonw <=0 and self.Gstat==1:
                self.index += 1
                screen.fill(BLACK)
                if self.index >= len(self.imagesR):
                    self.index = 0
                self.image = self.imagesR[self.index]
                self.countdonw = 10

            if self.countdonw <=0 and self.Gstat==-1:
                self.index += 1
                screen.fill(BLACK)
                if self.index >= len(self.imagesflipR):
                    self.index = 0
                self.image = self.imagesflipR[self.index]
                self.countdonw = 10

        elif self.change_x < 0:
            if self.countdonw <=0 and self.Gstat==1:
                self.index += 1
                screen.fill(BLACK)
                if self.index >= len(self.imagesL):
                    self.index = 0
                self.image = self.imagesL[self.index]
                self.countdonw = 10

            if self.countdonw <=0 and self.Gstat==-1:
                self.index += 1
                screen.fill(BLACK)
                if self.index >= len(self.imagesflipL):
                    self.index = 0
                self.image = self.imagesflipL[self.index]
                self.countdonw = 10


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

        block_hit_list = pygame.sprite.spritecollide(self, self.level.piece_list, False)
        for block in block_hit_list:
            orbe = pygame.mixer.Sound('music/orbe.wav')
            pygame.mixer.Sound.play(orbe)
            block.kill()
            self.level.score.incrementeScoreDeUn()

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right



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
                self.rect.bottom = block.rect.top
                self.change_y = -10;
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                self.change_y = 10;
            self.invG();

        # self.posP += self.change_y

        # Ennemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        # for ennemy in Ennemy_hit_list:
        #
        #     # Reset our position based on the top/bottom of the object.
        #     if self.change_y > 0 :
        #         self.rect.bottom = ennemy.rect.top
        #     elif self.change_y < 0 :
        #         self.rect.top = ennemy.rect.bottom
        #
        #     # Stop our vertical movement
        #     self.change_y = 0
        #     print("BRUUUU")
        #
        # Ennemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        # for ennemy in Ennemy_hit_list:
        #     if self.change_x > 0 and self.rect.bottom != ennemy.rect.top and self.rect.top != ennemy.rect.bottom:
        #         self.rect.right = ennemy.rect.left
        #     elif self.change_x < 0 and self.rect.bottom != ennemy.rect.top and self.rect.top != ennemy.rect.bottom:
        #         self.rect.left = ennemy.rect.right


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
        ennemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        self.rect.y -= self.J1

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = self.J2

        if len(ennemy_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
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
        self.level.bullets_liste.add(Bullet(self.rect.centerx, self.rect.centery, xSouris, ySouris))

    def bulletHit(self):
        hit = pygame.mixer.Sound('music/hit.wav')
        pygame.mixer.Sound.play(hit)
        self.level.score.resetMultiplicateur()
        self.change_y = self.J3
        self.change_x = 0
        #print("GGGGGGGGGGGGGGGGGGG")
