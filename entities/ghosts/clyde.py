from .ghost import Ghost
from utils.algos.ucs import ucs_path
from config import *
from ui.sprites.ghost_sprites import GhostSprites
from utils.math.vector import Vector2

class Clyde(Ghost): # Orange ghost
    def __init__(self, node, pacman=None):
        super().__init__(node, pacman)
        self.name = CLYDE
        self.color = ORANGE
        self.sprites = GhostSprites(self)
        pass

    def recalculatePath(self):
        self.path.clear()
        self.peakMem = 0
        self.numExpandNode = 0
        self.tree = {}
        self.path, self.peakMem, self.numExpandNode, self.tree = ucs_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.pacman.currentNode,
            nextGoal=self.pacman.targetNode
        )
