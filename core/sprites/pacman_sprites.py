from .spritesheet import Spritesheet
from config import *
# from ..entities.entity import Entity

class PacmanSprites(Spritesheet):
    def __init__(self, entity):
        super().__init__()
        self.entity = entity
        self.entity.image = self.getStartImage()       

    def getStartImage(self):
        return self.getImage(8, 0)

    def getImage(self, x, y):
        return Spritesheet.getImage(self, x, y, 2*TILESIZE, 2*TILESIZE)
