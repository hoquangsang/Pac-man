import pygame
from config import *
import numpy as np

class Spritesheet(object):
    def __init__(self):
        self.sheet = pygame.image.load("res/images/spritesheet.png").convert()
        transcolor = self.sheet.get_at((0,0))
        self.sheet.set_colorkey(transcolor)
        width = int(self.sheet.get_width())
        height = int(self.sheet.get_height())
        self.sheet = pygame.transform.scale(self.sheet, (width, height))
        
    def getImage(self, x, y, width, height):
        x *= TILESIZE
        y *= TILESIZE
        self.sheet.set_clip(pygame.Rect(x, y, width, height))
        return self.sheet.subsurface(self.sheet.get_clip())

    def reset(self):
        pass

    def getStartImage(self):
        pass
