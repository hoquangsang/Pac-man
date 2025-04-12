from .ghost import Ghost
from utils.algos.ucs import ucs_path
from config import CLYDE, ORANGE
from core.sprites.ghost_sprites import GhostSprites

class Clyde(Ghost): # Orange ghost
    def __init__(self, node, pacman=None):
        super().__init__(node)
        self.name = CLYDE
        self.color = ORANGE
        self.sprite = GhostSprites(self)
        pass

    # def goalDirection(self, directions):
    #     pass