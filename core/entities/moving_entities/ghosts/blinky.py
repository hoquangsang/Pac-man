from .ghost import Ghost
from config import *
from utils.algos.a_star import astar_path
from core.sprites.ghost_sprites import GhostSprites


class Blinky(Ghost): # Red ghost
    def __init__(self, node, pacman=None):
        super().__init__(node,pacman)
        self.name = BLINKY
        self.color = RED
        self.sprites = GhostSprites(self)
        pass

    # def goalDirection(self, directions):
    #     pass
