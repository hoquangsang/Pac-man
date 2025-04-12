from .ghost import Ghost
from utils.algos.dfs import dfs_path
from config import *

class Pinky(Ghost): # Pink ghost
    def __init__(self, node, pacman=None):
        super().__init__(node)
        self.name = PINKY
        self.color = PINK
        pass

    # def goalDirection(self, directions):
    #     pass