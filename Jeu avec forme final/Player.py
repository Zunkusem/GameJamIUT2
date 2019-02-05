class Player():
    def __init__(self, pos, jeu):
        height
        width
        self.jeu= jeu
        self.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (30, 90, 150), pygame.rect.Rect((0, 0, 25, 25)))
        self.pos_y = pos[1]
        self.pos_x = pos[0]
        self.speed_x = 0
        self.speed_y = 0
        self.hitbottom = self.pos_x
