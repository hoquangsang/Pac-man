from config import *
from .spritesheet import Spritesheet
from core.entities.entity import Entity

class GhostSprites(Spritesheet):
    def __init__(self, entity:Entity):
        # Spritesheet.__init__(self)
        super().__init__()
        self.x = {BLINKY:0, PINKY:2, INKY:4, CLYDE:6}
        self.entity = entity
        self.entity.image = self.getStartImage()

    def getStartImage(self):
        return self.getImage(self.x[self.entity.name], 4)

    def getImage(self, x, y):
        return Spritesheet.getImage(self, x, y, 2*TILESIZE, 2*TILESIZE)

    def update(self, dt):
        x = self.x[self.entity.name]
        if self.entity.mode.current in [SCATTER, CHASE]:
            if self.entity.direction == LEFT:
                self.entity.image = self.getImage(x, 8)
            elif self.entity.direction == RIGHT:
                self.entity.image = self.getImage(x, 10)
            elif self.entity.direction == DOWN:
                self.entity.image = self.getImage(x, 6)
            elif self.entity.direction == UP:
                self.entity.image = self.getImage(x, 4)
        elif self.entity.mode.current == FREIGHT:
            self.entity.image = self.getImage(10, 4)
        elif self.entity.mode.current == SPAWN:
            if self.entity.direction == LEFT:
                self.entity.image = self.getImage(8, 8)
            elif self.entity.direction == RIGHT:
                self.entity.image = self.getImage(8, 10)
            elif self.entity.direction == DOWN:
                self.entity.image = self.getImage(8, 6)
            elif self.entity.direction == UP:
                self.entity.image = self.getImage(8, 4)
        # x = self.x[self.entity.name]
        # if self.entity.direction == LEFT:
        #     self.entity.image = self.getImage(x, 8)
        # elif self.entity.direction == RIGHT:
        #     self.entity.image = self.getImage(x, 10)
        # elif self.entity.direction == DOWN:
        #     self.entity.image = self.getImage(x, 6)
        # elif self.entity.direction == UP:
        #     self.entity.image = self.getImage(x, 4)