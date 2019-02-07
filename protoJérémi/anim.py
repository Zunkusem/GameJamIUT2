import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('Animation0000.png'))
        self.images.append(load_image('Animation0001.png'))
        self.images.append(load_image('Animation0002.png'))
        self.images.append(load_image('Animation0003.png'))
        self.images.append(load_image('Animation0004.png'))
        self.images.append(load_image('Animation0005.png'))
        self.images.append(load_image('Animation0006.png'))
        self.images.append(load_image('Animation0007.png'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)
        self.countdonw = 1000


    def update(self,screen):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        BLACK = (0, 0, 0)
        self.countdonw -= 1
        if self.countdonw <=0:
            self.index += 1
            screen.fill(BLACK)
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.countdonw = 1000


def main():
    pygame.init()
    screen = pygame.display.set_mode((250, 250))
    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)


    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.

        my_group.update(screen)
        my_group.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
