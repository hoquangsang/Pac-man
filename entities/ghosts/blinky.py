from .ghost import Ghost
from config import *
from ui.sprites.ghost_sprites import GhostSprites
from entities.entity import Entity
from mazes.graph import MazeGraph
from utils.algos.a_star import astar_path

class Blinky(Ghost): # Red ghost
    def __init__(self, node, pacman:Entity=None):
        super().__init__(node,pacman)
        self.name = BLINKY
        self.color = RED
        self.sprites = GhostSprites(self)
        pass

    def recalculatePath(self):
        self.path.clear()
        self.peakMem = 0
        self.numExpandNode = 0
        self.path, peakMem, numExpandNode, cameFrom = astar_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.pacman.currentNode,
            nextGoal=self.pacman.targetNode
        )
        self.searchTree = MazeGraph(cameFrom=cameFrom, expands=numExpandNode,peekMem=peakMem)
