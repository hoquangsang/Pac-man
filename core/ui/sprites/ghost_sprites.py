from .spritesheet import Spritesheet
from config import *
# from ..entities.entity import Entity

class GhostSprites(Spritesheet):
    def __init__(self, ghost):
        # Spritesheet.__init__(self)
        super().__init__()
        self.x = {BLINKY:0, PINKY:2, INKY:4, CLYDE:6}
        self.ghost = ghost
        self.ghost.image = self.getStartImage()

    def getStartImage(self):
        return self.getImage(self.x[self.ghost.name], 4)

    def getImage(self, x, y):
        return Spritesheet.getImage(self, x, y, 2*TILESIZE, 2*TILESIZE)

    def update(self, dt):
        x = self.x[self.ghost.name]
        if self.ghost.mode.current in [SCATTER, CHASE]:
            if self.ghost.direction == LEFT:
                self.ghost.image = self.getImage(x, 8)
            elif self.ghost.direction == RIGHT:
                self.ghost.image = self.getImage(x, 10)
            elif self.ghost.direction == DOWN:
                self.ghost.image = self.getImage(x, 6)
            elif self.ghost.direction == UP:
                self.ghost.image = self.getImage(x, 4)
        elif self.ghost.mode.current == FREIGHT:
            self.ghost.image = self.getImage(10, 4)
        elif self.ghost.mode.current == SPAWN:
            if self.ghost.direction == LEFT:
                self.ghost.image = self.getImage(8, 8)
            elif self.ghost.direction == RIGHT:
                self.ghost.image = self.getImage(8, 10)
            elif self.ghost.direction == DOWN:
                self.ghost.image = self.getImage(8, 6)
            elif self.ghost.direction == UP:
               self.ghost.image = self.getImage(8, 4)