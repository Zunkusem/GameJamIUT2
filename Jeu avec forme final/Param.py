from math import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (249, 249, 6)
CYAN = (0, 255, 255)
ELEC_BLUE=(13, 13, 242)
ORANGE=(249, 152, 6)

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768


def calculNorme(x1,y1,x2,y2): #calcule la longueur entre deux points
    x=x2-x1
    y=y2-y1
    return sqrt(x*x+y*y)
