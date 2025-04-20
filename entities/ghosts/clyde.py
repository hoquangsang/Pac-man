from .ghost import Ghost
from config import *
from ui.sprites.ghost_sprites import GhostSprites
from entities.entity import Entity
from mazes.graph import MazeGraph
from utils.algos.ucs import ucs_path

class Clyde(Ghost): # Orange ghost
    def __init__(self, node, pacman:Entity=None):
        super().__init__(node, pacman)
        self.name = CLYDE
        self.color = ORANGE
        self.sprites = GhostSprites(self)
        pass

    def recalculatePath(self):
        self.path.clear()
        self.peakMem = 0
        self.numExpandNode = 0
        self.path, peakMem, numExpandNode, cameFrom = ucs_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.pacman.currentNode,
            nextGoal=self.pacman.targetNode
        )
        self.searchTree = MazeGraph(cameFrom=cameFrom, expands=numExpandNode,peekMem=peakMem)
