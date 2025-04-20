from config import TILESIZE
from .spritesheet import Spritesheet
from core.entities.entity import Entity

class FruitSprites(Spritesheet):
    def __init__(self, entity, level):
        Spritesheet.__init__(self)
        self.entity = entity
        self.fruits = {0:(16,8), 1:(18,8), 2:(20,8), 3:(16,10), 4:(18,10), 5:(20,10)}
        self.entity.image = self.getStartImage(level % len(self.fruits))

    def getStartImage(self, key):
        return self.getImage(*self.fruits[key])

    def getImage(self, x, y):
        return Spritesheet.getImage(self, x, y, 2*TILESIZE, 2*TILESIZE)