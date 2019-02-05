import pygame

pygame.init()

clock = pygame.time.Clock()

CIEL = 0, 200, 255

def main():
    fenetre = pygame.display.set_mode((640, 480))

    loop = True

    background = pygame.Surface(fenetre.get_size())

    while loop:
      for event in pygame.event.get():
          if pygame.event==pygame.QUIT():
              loop = False
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
              print("x:",event.pos[0]," y:",event.pos[1])
              pygame.draw.line(fenetre, WHITE, (0,0), (event.pos[0],event.pos[1]))

    background.fill(CIEL)
    fenetre.blit(background, (0, 0))

    pygame.display.flip()
    clock.tick(10)

if __name__ == '__main__':
    main()
