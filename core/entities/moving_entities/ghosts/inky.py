from .ghost import Ghost
from config import *
from utils.algos.bfs import bfs_path

class Inky(Ghost): # Blue ghost
    def __init__(self, node, pacman=None):
        super().__init__(node)
        self.name = INKY
        self.color = BLUE
        pass

    # def goalDirection(self, directions):
    #     pass