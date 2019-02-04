import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1270, 670))
    clock = pygame.time.Clock()
    running = True
    circles = pygame.sprite.Group(Circle((600, 0), screen))

    while running:
        
        circles.update()

        screen.fill((10, 10, 30))
        circles.draw(screen)

        pygame.display.flip()
        clock.tick(60)


run_game()
pygame.quit()
