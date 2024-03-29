import pygame
from Player import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, sx, sy):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Ennemypic/bullet.png'),[10,10])
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = sy
        self.speedx = sx

    def update(self,player):
        self.rect.y += self.speedy*20
        self.rect.x += self.speedx*20
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, player.level.platform_list, False)
        enemy_hit_list = pygame.sprite.spritecollide(self, player.level.enemy_list, False)
        enemy2_hit_list = pygame.sprite.spritecollide(self, player.level.ennemy_tourelle_liste, False)
        self.rect.y -= 2
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
        if self.rect.y >= SCREEN_HEIGHT or self.rect.x >= SCREEN_WIDTH or self.rect.y < 0 or self.rect.x < 0:
            self.kill()
        if len(enemy_hit_list) > 0:
            for ennemy in enemy_hit_list:
                ennemy.bulletHit()
            pass
            self.kill()
        if len(enemy2_hit_list) > 0:
            for ennemy in enemy2_hit_list:
                ennemy.bulletHit()
            pass
            self.kill()

    def shiftx(self,shift_x):
        self.rect.x += shift_x

class EnnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, sx, sy):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Ennemypic/Ennemybullet.png'),[10,10])
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = sy
        self.speedx = sx

    def update(self,player):
        self.rect.y += self.speedy*10
        self.rect.x += self.speedx*10
        self.rect.y += 2
        self.player_liste = pygame.sprite.Group(player)
        platform_hit_list = pygame.sprite.spritecollide(self, player.level.platform_list, False)
        hit_player = pygame.sprite.spritecollide(self, self.player_liste, False)
        self.rect.y -= 2
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
        if self.rect.y >= SCREEN_HEIGHT or self.rect.x >= SCREEN_WIDTH or self.rect.y < 0 or self.rect.x < 0:
            self.kill()
        if len(hit_player) > 0:
            for player in hit_player:
                player.bulletHit()
                #print("#")
                # ennemy.bulletHit()
            pass

            self.kill()

    def shiftx(self,shift_x):
        self.rect.x += shift_x
