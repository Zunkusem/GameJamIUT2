import pygame
from block import *

class Map:
    def creeMap(screenx,screeny,blocks):
        screen = (screenx,screeny)
        for i in range(0,10):
            blocks.add(Block2((0,i*80), screen))

        for j in range(0,20):
            blocks.add(Block((j*80,650), screen))

        blocks.add(Platform((300,550), screen))
        blocks.add(Platform((550,450), screen))
        blocks.add(Platform((800,350), screen))
        blocks.add(Platform((1050,250), screen))
