from .ghost import Ghost
from config import *
from utils.algos.bfs import bfs_path
from utils.math.vector import Vector2
from core.ui.sprites.ghost_sprites import GhostSprites

class Inky(Ghost): # Blue ghost
    def __init__(self, node, pacman=None):
        super().__init__(node,pacman)
        self.name = INKY
        self.color = BLUE
        self.sprites = GhostSprites(self)
        pass

    # def goalDirection(self, directions):
    #     pass

    def scatter(self):
        self.goal = Vector2(TILESIZE*NCOLS, TILESIZE*NROWS)

    # def chase(self):
    #     vec1 = self.pacman.position + self.pacman.directions[self.pacman.direction] * TILESIZE * 2
    #     vec2 = (vec1 - self.blinky.position) * 2
    #     self.goal = self.blinky.position + vec2