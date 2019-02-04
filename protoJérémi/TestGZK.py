import pygame

GRAVITY = 0.2  # Pretty low gravity.
XS = .1
listeB = []

class Block(pygame.sprite.Sprite):

    def __init__(self, pos, screen):
        super().__init__()
        lenght = 100
        height = 50
        self.screen = screen
        self.image = self.image = pygame.Surface((lenght, 50), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (255, 255, 255), pygame.rect.Rect((0, 0, lenght, height)))
        self.rect = self.image.get_rect(center=pos)
        self.hittop = [pos[0]-(lenght/2)-30,pos[1]-(lenght/2),(pos[0]+lenght)-(lenght/2),pos[1]]



class Circle(pygame.sprite.Sprite):

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
        listeB.append(self)

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
            if self.pos_x > bloc.hittop[0] and self.pos_x < bloc.hittop[2] and self.pos_y > bloc.hittop[1]-5:
                if self.pos_y >= bloc.hittop[1]+5:
                    self.speed_y = 0
                    self.speed_y -= 5
                else:
                    self.speed_y = 0
                    self.speed_y -= 0.2

        pass

        if self.pos_y > self.screen.get_height():
            self.kill()  # Remove off-screen circles.
        if self.pos_y > self.screen.get_width():
            self.kill()  # Remove off-screen circles.

    def moveymin(self):
        self.speed_y = 5

    def movey(self):
        self.speed_y = -5

    def movex(self):
        self.speed_x = 2

    def movexmin(self):
        self.speed_x = -2

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1270, 670))
    clock = pygame.time.Clock()
    running = True
    circles = pygame.sprite.Group(Circle((600, 0), screen))
    blocks = pygame.sprite.Group(Block((600,600), screen))

    while running:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                circles.add(Circle(event.pos, screen))
            if pressed[pygame.K_d]:
                for i in range(0,len(listeB)):
                    listeB[i].movex()
                pass
            if pressed[pygame.K_a]:
                for i in range(0,len(listeB)):
                    listeB[i].movexmin()
                pass
            if pressed[pygame.K_w]:
                for i in range(0,len(listeB)):
                    listeB[i].movey()
                pass
            if pressed[pygame.K_s]:
                for i in range(0,len(listeB)):
                    listeB[i].moveymin()
                pass

        circles.update(blocks)

        screen.fill((10, 10, 30))
        circles.draw(screen)
        blocks.draw(screen)

        pygame.display.flip()
        clock.tick(60)


run_game()
pygame.quit()
