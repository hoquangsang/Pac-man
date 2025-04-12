from .ghost import Ghost
from config import *
from utils.algos.a_star import astar_path


class Blinky(Ghost): # Red ghost
    def __init__(self, node, pacman=None):
        super().__init__(node,pacman)
        self.name = BLINKY
        self.color = RED
        pass

    # def goalDirection(self, directions):
    #     pass
