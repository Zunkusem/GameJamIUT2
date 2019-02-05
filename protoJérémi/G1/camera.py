import pygame
GRAVITY = 0.2  # Pretty low gravity.
XS = .1

class Cam:
    def __init__(self):
        super().__init__()
        self.pos_x = 200
        self.pos_y = 200
        
