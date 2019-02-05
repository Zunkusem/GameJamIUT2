import pygame
from block import *

class Map():
    def creeMap(screenx,screeny,blocks):
        screen = (screenx,screeny)
        #bordure gauche
        blocks.add(Block2((0,0), screen))
        blocks.add(Block2((0,90), screen))
        blocks.add(Block2((0,180), screen))
        blocks.add(Block2((0,270), screen))
        blocks.add(Block2((0,360), screen))
        blocks.add(Block2((0,450), screen))
        blocks.add(Block2((0,540), screen))
        blocks.add(Block2((0,630), screen))
        blocks.add(Block2((0,720), screen))
        #bordure basse
        blocks.add(Block((0,650), screen))
        blocks.add(Block((90,650), screen))
        blocks.add(Block((180,650), screen))
        blocks.add(Block((270,650), screen))
        blocks.add(Block((360,650), screen))
        blocks.add(Block((450,650), screen))
        blocks.add(Block((540,650), screen))
        blocks.add(Block((630,650), screen))
        blocks.add(Block((720,650), screen))
        blocks.add(Block((810,650), screen))
        blocks.add(Block((900,650), screen))
        blocks.add(Block((990,650), screen))
        blocks.add(Block((1080,650), screen))
        blocks.add(Block((1170,650), screen))
