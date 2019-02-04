import pygame

GRAVITY = .5  # Pretty low gravity.

class Rectangle(pygame.sprite.sprite):

	def _init_(self, pos, screen):
		super()._init_();
		self.screen = screen
		self.image = pygale.Surface((100, 100), pygame.SRCALPHA)
		pygame.draw.rect(self.image, [50,50,50], [40, 40, 100, 100], 0)
		self.rect = self.image.get.get_rect(center=pos)
		self.pos_y = pos[1]
		self.speed_y = 0

	def update(self):
		self.speed_y += GRAVITY
		sel.pos_y += self.speed_y
		self.rect.y = self.pos_y

		if self.pos_y>self.screen.get_height():
			self.kill()

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1270,670))
	clock = pygame.time.clock()
	running = True;
	rectangles = pygame.sprite.Group(Rectangle((600,0), screen))

	while running:
		for(event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:
				rectangles.add(Rectangle(event.pos, screen))

		rectangles.update()

		screen.fill((10,10,30))
		rectangles.draw(screen)
		pygame.display.flip()
		clock.tick(60)
run_game()
pygame.quit()
