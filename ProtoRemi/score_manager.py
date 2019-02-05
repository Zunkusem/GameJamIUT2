import pygame
from pygame import *
import score.py


scoreAMettre = 1500


def changeScore(score):
    f = open('score.txt', 'r')
    txt = f.read()
    f.close()
    if f == null
        f = open('score.txt', 'a')
        f.write(score)
        f.close
    else
        txt += score
        txtList = txt.split(' ')
        triTxt = sorted(txtList)
        f = open('score.txt', 'w')
        f.write(triTxt)
        f.close()
