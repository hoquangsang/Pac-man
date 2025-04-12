from .spritesheet import Spritesheet
from config import *

class FruitSprites(Spritesheet):
    def __init__(self, entity):
        super.__init__()
        self.entity = entity
        self.entity.image = self.getStartImage()

    def getStartImage(self):
        return self.getImage(16, 8)

    def getImage(self, x, y):
        return Spritesheet.getImage(self, x, y, 2*TILESIZE, 2*TILESIZE)

