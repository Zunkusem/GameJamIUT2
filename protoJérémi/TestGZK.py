import pygame

GRAVITY = 0  # Pretty low gravity.
XS = .1
listeB = []

class Circle(pygame.sprite.Sprite):

    def __init__(self, pos, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (30, 90, 150), (40, 40), 40)
        self.rect = self.image.get_rect(center=pos)
        self.pos_y = pos[1]
        self.pos_x = pos[0]
        self.speed_x = 0
        self.speed_y = 0
        self.xs = 0
        listeB.append(self)

    def update(self):
        self.speed_y += GRAVITY
        self.pos_y += self.speed_y
        self.rect.y = self.pos_y
        self.pos_x += self.speed_x
        self.rect.x = self.pos_x
        if self.speed_x > 0:
            self.speed_x -= XS
        elif self.speed_x < 0:
            self.speed_x += XS

        if self.speed_y > 0:
            self.speed_y -= XS
        elif self.speed_y < 0:
            self.speed_y += XS

        if self.pos_y > self.screen.get_height():
            self.kill()  # Remove off-screen circles.

    def moveymin(self):
        self.speed_y = 5

    def movey(self):
        self.speed_y = -5

    def movex(self):
        self.speed_x = 5

    def movexmin(self):
        self.speed_x = -5



def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1270, 670))
    clock = pygame.time.Clock()
    running = True
    circles = pygame.sprite.Group(Circle((600, 0), screen))

    while running:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                circles.add(Circle(event.pos, screen))
            elif pressed[pygame.K_d]:
                for i in range(0,len(listeB)):
                    listeB[i].movex()
                pass
            elif pressed[pygame.K_a]:
                for i in range(0,len(listeB)):
                    listeB[i].movexmin()
                pass
            elif pressed[pygame.K_w]:
                for i in range(0,len(listeB)):
                    listeB[i].movey()
                pass
            elif pressed[pygame.K_s]:
                for i in range(0,len(listeB)):
                    listeB[i].moveymin()
                pass

        circles.update()

        screen.fill((10, 10, 30))
        circles.draw(screen)

        pygame.display.flip()
        clock.tick(60)


run_game()
pygame.quit()
