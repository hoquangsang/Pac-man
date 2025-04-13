from .ghost import Ghost
from utils.algos.dfs import dfs_path
from config import PINKY, PINK, TILESIZE, NCOLS
from core.ui.sprites.ghost_sprites import GhostSprites
from utils.math.vector import Vector2

class Pinky(Ghost): # Pink ghost
    def __init__(self, node, pacman=None):
        super().__init__(node,pacman)
        self.name = PINKY
        self.color = PINK
        self.sprites = GhostSprites(self)
        pass

    # def goalDirection(self, directions):
    #     pass

    def scatter(self):
        self.goal = Vector2(TILESIZE*NCOLS, 0)

    # def chase(self):
    #     self.goal = self.pacman.position + self.pacman.directions[self.pacman.direction] * TILESIZE * 4
