import pygame
from Bloc import *
from Player import *
from Ennemi import *
from Projectile import *
from Jeu import *
from Score import *

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
        self.piece_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.ennemy_tourelle_liste = pygame.sprite.Group()
        self.score = Score()
        self.player = player
        self.bullets_liste = pygame.sprite.Group()
        font.init()
        self.font_a = pygame.font.SysFont('arial', 40)
        self.font_b = pygame.font.SysFont('arial', 70)
        self.font_score = self.font_a.render(self.score.getScore(), 1, (YELLOW))
        self.font_multiplicateur = self.font_a.render("x "+self.score.getMultiplicateur(), 1, (ORANGE))


        # How far this world has been scrolled left/right
        self.world_shiftx = 0
        self.world_shifty = 0

    def getScore():
        return self.score.getScore()


    # Update everythign on this level
    def update(self,player):
        #print(len(self.bullets_liste))
        """ Update everything in this level."""
        self.platform_list.update()
        self.piece_list.update() #
        self.enemy_list.update()
        self.bullets_liste.update(player)
        self.ennemy_tourelle_liste.update(self.bullets_liste,player)
        self.font_score = self.font_a.render(self.score.getScore(), 1, (YELLOW))
        self.font_multiplicateur = self.font_a.render("x "+self.score.getMultiplicateur(), 1, (ORANGE))



    def draw(self, screen):
        """ Draw everything on this level. """

        screen.fill(BLUE)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.piece_list.draw(screen)
        self.enemy_list.draw(screen)
        self.bumper_list.draw(screen)
        self.platformRetourArriere_list.draw(screen)
        self.ennemy_tourelle_liste.draw(screen)
        self.bullets_liste.draw(screen)
        self.platformRetourAvant_list.draw(screen)
        screen.blit(self.font_score, (750,10))
        screen.blit(self.font_multiplicateur, (900,10))

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

        for platform in self.piece_list:
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

        for platform in self.piece_list:
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

class Tuto(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create Tuto. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -8000

        # Array with width, height, x, and y of platform
        level = [#bords de la map
                 [150, 968, -140, -100],
                 [8000, 100, 0, 758],
                 [150, 968, -140, -988],
                 [8000, 100, 0, -858],
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
                 [50, 620, 2200, 150],
                 [50, 1050, 2350, -50],
                 #blocs 2eme partie en haut
                 [150, 200, 1950, -768],
                 [100, 30, 2500, -680],
                 [100, 30, 2700, -650],
                 [10, 150, 2900, -680],
                 [100, 30, 3000, -650],
                 [10, 150, 3200, -680],
                 [100, 30, 3300, -650],
                 [200, 250, 3500, -758],
                 [50, 700, 3800, -778],
                 #blocs 3eme partie en bas et en haut
                 [500, 200, 2900, 568],
                 [50, 800, 4100, -800],
                 [50, 1000, 4500, -200],
                 [50, 1100, 5250, -778],
                 [50, 900, 4900, -100],
                 [50, 1000, 5950, -200],
                 #blocs 4eme partie fin tuto
                 [50, 100, 6200, -778],
                 [50, 200, 6350, -778],
                 [50, 300, 6500, -778],
                 [50, 400, 6650, -778],
                 [50, 500, 6800, -778],
                 [50, 600, 6950, -778],
                 [50, 600, 7100, 200],
                 [600, 200, 7400, -778]
                 ]


        Bump = [[102, 41, 2249, 757],#bloc passage 2eme niveau
                [102, 41, 3699, -798],#bloc passage 3eme niveau
                [102, 41, 3850, -798],#rattrapage 1 niveau 3
                [100, 41, 4050, 757],#1er bloc niveau 3
                [102, 41, 4799, -798],#2eme bloc niveau 3
                [102, 41, 4549, 757],#rattrapage 2 niveau 3
                [100, 60, 5500, 757],#3eme bloc niveau 3
                #blocs de rattage épisode 4
                [102, 41, 6249, -798],#1
                [102, 41, 6399, -798],#2
                [102, 41, 6549, -798],#3
                [102, 41, 6699, -798],#4
                [102, 41, 6849, -798],#5
                [48, 20, 6951, -197],#dernier bloc de saut
                [102, 41, 5999, 757],#gestion de nullité 1 niveau 4
                [102, 41, 7000, -798],#gestion de grugeur 2 niveau 4 A CORRIGER CA MARCHE PAS SA MERE CA ME CASSE LES COUILLES
                ]

        levelPlatformRetourArriere = [[1400, 40, 800, 758],#rattrapage niveau 1
                                      [750, 40, 2750, -798],#rattrapage niveau 2
                                      [150, 41, 3950, -798],#rattrapage 1 niveau 3
                                      [250, 40, 4650, 758],#rattrapage 2 niveau 3
                                      [700, 40, 6100, 758],#rattrapage 1 niveau 4
                                      [300, 41, 7100, -797],#rattrapage 2 niveau 4  A CORRIGER CA MARCHE PAS SA MERE CA ME CASSE LES COUILLES
                                      ]

        levelPlatformRetourAvant =  [[150, 40, 3900, 758],#1er accélérateur niveau 3
                                     [150, 40, 4650, -798],#2eme accélérateur niveau 3
                                     [150, 40, 5350, 758],#3eme accélérateur niveau 3
                                     [700, 40, 5300, -798],#aide accélérateur pour arriver niveau 4
                                     ]


        pieces=[[100,600],[200,700],[240,700],[280,700],[320,700],[360,700],
                [500,600],[540,600],
                [850,450],
                [1200,100],
                [1400,50],
                [2000,250]
                ]



        i=25
        Ennemy= [[10,100,0],
                 [500,500,1],
                 [1200,700,1],
                 [10+i*1,500,0],

                 [10+i*8,500,0],


                 ]
        for piece in pieces:
            block = Piece()
            block.rect.x = piece[0]
            block.rect.y = piece[1]
            block.player = self.player
            self.piece_list.add(block)

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
                block = Tourelle(self)
                block.rect.x = ennemy[0]
                block.rect.y = ennemy[1]
                block.player = self.player
                self.ennemy_tourelle_liste.add(block)

class Level_01(Level):

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -8000

        level = [#bords de la map
                 [150, 968, -140, -100],
                 [8000, 100, 0, 758],
                 [150, 968, -140, -988],
                 [7400, 100, 0, -858],
                 #1ere partie
                 [1300, 100, 500, 658],
                 [1300, 100, 500, -758],
                 #pleins de petits blocs
                 [50, 50, 500 , 500],
                 [50, 50, 500 , -450],
                 [50, 50, 500 , -200],
                 [50, 50, 500 , 50],
                 [50, 50, 500, 300],
                 [50, 50, 600, 200],
                 [50, 50, 600, -300],
                 [50, 50, 600, -500],
                 [50, 50, 700, -600],
                 [50, 50, 700, -480],
                 [50, 50, 700, -160],
                 [50, 50, 700, 20],
                 [50, 50, 700, 156],
                 [50, 50, 700, 500],
                 [50, 50, 800, 400],
                 [50, 50, 800, 100],
                 [50, 50, 800, -350],
                 [50, 50, 900, -470],
                 [50, 50, 900, 20],
                 [50, 50, 900, 600],
                 [50, 50, 1200, 500],
                 [50, 50, 1200 , -450],
                 [50, 50, 1200 , -200],
                 [50, 50, 1200 , 50],
                 [50, 50, 1200, 300],
                 [50, 50, 1300, 200],
                 [50, 50, 1300, -300],
                 [50, 50, 1300, -500],
                 [50, 50, 1400, -600],
                 [50, 50, 1400, -480],
                 [50, 50, 1400, -160],
                 [50, 50, 1400, 20],
                 [50, 50, 1400, 156],
                 [50, 50, 1400, 500],
                 [50, 50, 1500, 400],
                 [50, 50, 1500, 100],
                 [50, 50, 1500, -350],
                 [50, 50, 1600, -470],
                 [50, 50, 1600, 20],
                 [50, 50, 1600, 600],
                 [40, 500, 1800, -768],
                 [40, 700, 1800, 100],
                 [1000, 100, 2000, -150],
                 [1000, 600, 2000, -650],
                 [100, 700, 2900, 123],
                 [40, 90, 2000, 677],
                 [40, 40, 2100, 527],
                 [40, 40, 2100, 377],
                 [40, 40, 2100, 227],
                 [40, 40, 2650, 527],
                 [40, 40, 2650, 377],
                 [40, 40, 2650, 227],
                 [400, 40, 2700, 123],
                 [500,820, 3100, -651],
                 [600, 800, 3000, 162],
                 [300, 600, 3700, -758],
                 [100, 500, 4000, -658],
                 [2000, 900, 3600, -58],
                 [400, 600, 5200, -758],
                 [150, 40 , 4200, -158],
                 [150, 40 , 4500, -258],
                 [150, 40, 4800, -358],
                 [150, 40, 5100, -458],
                 [20, 20, 4800, -575],
                 [20, 20, 4500, -575],
                 [20, 20, 4200, -575],
                 [50, 500, 5900, -758],#premier bras
                 [150, 20, 5850, -658],
                 [150, 20, 5850, -558],
                 [150, 20, 5850, -458],
                 [150, 20, 5850, -358],

                 ]

        Bump = [[1300, 41, 500, 657],
                [1300, 41, 500, -698],
                [100, 41, 1840, -798],
                [100, 41, 1840, 757],
                [100, 41, 3000, 122],
                [100, 41, 3600, -798],
                [100, 41, 4500, -798],
                [100, 41, 5500, -59]
                ]
        levelPlatformRetourArriere = [[860, 40, 2040, 757]
                                      ]

        levelPlatformRetourAvant = []
        Ennemy = [[1100, -658, 0],
                  [1100, -558, 0],
                  [1100, -458, 0],
                  [1100, -358, 0],
                  [1100, -258, 0],
                  [1100, -158, 0],
                  [1100, -58, 0],
                  [1100, 42, 0],
                  [1100, 142, 0],
                  [1100, 242, 0],
                  [1100, 342, 0],
                  [1100, 442, 0],
                  [1100, 542, 0],
                  [1100, 627, 0],
                  ]


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
