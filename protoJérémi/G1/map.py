import pygame
from block import *

class Map():
    def creeMap(screenx,screeny,blocks):
        screen = (screenx,screeny)
        blocks.add(Block((690,600), screen))
        blocks.add(Block((690,200), screen))
        blocks.add(Block((780,620), screen))
        blocks.add(Block((510,620), screen))
        blocks.add(Block2((510,620), screen))
