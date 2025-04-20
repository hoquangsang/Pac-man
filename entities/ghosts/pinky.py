from .ghost import Ghost
from ..pacmans.pacman import Pacman
from config import *
from utils.algos.dfs import dfs_path
from utils.math.vector import Vector2
from ui.sprites.ghost_sprites import GhostSprites

class Pinky(Ghost): # Pink ghost
    def __init__(self, node, pacman:Pacman=None):
        super().__init__(node,pacman)
        self.name = PINKY
        self.color = PINK
        self.sprites = GhostSprites(self)
        pass

    def recalculatePath(self):
        self.path.clear()
        self.peakMem = 0
        self.numExpandNode = 0
        self.tree = {}
        self.path, self.peakMem, self.numExpandNode, self.tree = dfs_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.pacman.currentNode,
            nextGoal=self.pacman.targetNode
        )
