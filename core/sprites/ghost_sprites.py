from .spritesheet import Spritesheet
from config import *
# from ..entities.entity import Entity

class GhostSprites(Spritesheet):
    def __init__(self, entity):
        # Spritesheet.__init__(self)
        super().__init__()
        self.x = {BLINKY:0, PINKY:2, INKY:4, CLYDE:6}
        self.entity = entity
        self.entity.image = self.getStartImage()
               
    def getStartImage(self):
        return self.getImage(self.x[self.entity.name], 4)

    def getImage(self, x, y):
        return Spritesheet.getImage(self, x, y, 2*TILESIZE, 2*TILESIZE)
