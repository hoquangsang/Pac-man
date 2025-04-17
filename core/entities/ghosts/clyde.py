from .ghost import Ghost
from utils.algos.ucs import ucs_path
from config import CLYDE, ORANGE, TILESIZE, NROWS
from core.ui.sprites.ghost_sprites import GhostSprites
from utils.math.vector import Vector2

class Clyde(Ghost): # Orange ghost
    def __init__(self, node, pacman=None):
        super().__init__(node, pacman)
        self.name = CLYDE
        self.color = ORANGE
        self.sprites = GhostSprites(self)
        pass
