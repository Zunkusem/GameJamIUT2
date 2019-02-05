import pygame
GRAVITY = 0.2  # Pretty low gravity.
XS = .2
class Player(pygame.sprite.Sprite):

    def __init__(self, pos, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (30, 90, 150), pygame.rect.Rect((0, 0, 25, 25)))
        self.rect = self.image.get_rect(center=pos)
        self.pos_y = pos[1]
        self.pos_x = pos[0]
        self.speed_x = 0
        self.speed_y = 0
        self.xs = 0

    def update(self,block):
        self.speed_y += GRAVITY
        self.pos_y += self.speed_y
        self.rect.y = self.pos_y
        self.pos_x += self.speed_x
        self.rect.x = self.pos_x
        if self.speed_x > 0:
            self.speed_x -= XS
        elif self.speed_x < 0:
            self.speed_x += XS

        # if self.speed_y > 0:
        #     self.speed_y -= XS
        # elif self.speed_y < 0:
        #     self.speed_y += XS

        if self.pos_y > 600:
            self.speed_y = 0
            self.speed_y -= 0.2

        for bloc in block:
            if self.pos_x > bloc.hittop[0]+2 and self.pos_x < bloc.hittop[2]-2.5 and self.pos_y > bloc.hittop[1]-5 and self.pos_y < bloc.hitbottom[1]-5 :
                if self.pos_y >= bloc.hittop[1]+2:
                    self.speed_y = 0
                    self.speed_y -= 5
                else:
                    self.speed_y = 0
                    self.speed_y -= 0.2

            if self.pos_x > bloc.hitleft[0] and self.pos_x < bloc.hitleft[2]+5 and self.pos_y > bloc.hittop[1] and self.pos_y < bloc.hitbottom[1]-5 :
                if self.pos_x < bloc.hitleft[0]-1.2:
                    self.speed_x = 0
                    self.speed_x -= 5
                else:
                    self.speed_x = 0
                    self.speed_x -= 0.5

            if self.pos_x < bloc.hitright[0] and self.pos_x > bloc.hitright[2]-5 and self.pos_y > bloc.hittop[1] and self.pos_y < bloc.hitbottom[1]-5:
                if self.pos_x < bloc.hitright[0]-1.2:
                    self.speed_x = 0
                    self.speed_x += 5
                else:
                    self.speed_x = 0
                    self.speed_x += 0.5
            if self.pos_x > bloc.hitbottom[0]+2 and self.pos_x < bloc.hitbottom[2]-2.5 and self.pos_y > bloc.hittop[1]+5 and self.pos_y < bloc.hitbottom[1]-5:
                if self.pos_x > bloc.hitbottom[0]+1.2:
                    self.speed_y = +0.5
                else:
                    self.speed_y = 0
                    self.speed_y += 0.2
        pass

        if self.speed_x>6:
            self.speed_x= 6
        elif self.speed_x< -6:
            self.speed_x= -6
        pass

        if self.speed_x<0.2 and self.speed_x>-0.2:
            self.speed_x = 0

        if self.pos_y > self.screen.get_height():
            self.kill()  # Remove off-screen circles.
        if self.pos_y > self.screen.get_width():
            self.kill()  # Remove off-screen circles.

    def moveymin(self):
        self.speed_y += 0.5
    def movey(self):
        self.speed_y = -5
    def movex(self):
        self.speed_x += 0.5
    def movexmin(self):
        self.speed_x -= 0.5
