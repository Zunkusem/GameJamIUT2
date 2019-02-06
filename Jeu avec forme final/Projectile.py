import pygame
from Player import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, sx, sy):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(BLACK)
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
        self.rect.y -= 2
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
        if self.rect.y >= SCREEN_HEIGHT or self.rect.x >= SCREEN_WIDTH or self.rect.y < 0 or self.rect.x < 0:
            self.kill()
