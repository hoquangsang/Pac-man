from .ghost import Ghost
from utils.algos.ucs import ucs_path
from config import CLYDE, ORANGE

class Clyde(Ghost): # Orange ghost
    def __init__(self, node, pacman=None):
        super().__init__(node)
        self.name = CLYDE
        self.color = ORANGE
        pass

    # def goalDirection(self, directions):
    #     pass