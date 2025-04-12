from .ghost import Ghost
from config import *
from utils.algos.bfs import bfs_path
from core.sprites.ghost_sprites import GhostSprites

class Inky(Ghost): # Blue ghost
    def __init__(self, node, pacman=None):
        super().__init__(node)
        self.name = INKY
        self.color = BLUE
        self.sprites = GhostSprites(self)
        pass

    # def goalDirection(self, directions):
    #     pass