from .ghost import Ghost
from config import *
from utils.algos.bfs import bfs_path
from utils.math.vector import Vector2
from ui.sprites.ghost_sprites import GhostSprites
from mazes.node import MazeNode
from entities.entity import Entity


class Inky(Ghost): # Blue ghost
    def __init__(self, node, pacman:Entity=None):
        super().__init__(node,pacman)
        self.name = INKY
        self.color = LIGHT_BLUE
        self.sprites = GhostSprites(self)
        pass

    def recalculatePath(self):
        self.path.clear()
        self.peakMem = 0
        self.numExpandNode = 0
        self.tree = {}
        self.path, self.peakMem, self.numExpandNode, self.tree = bfs_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.pacman.currentNode,
            nextGoal=self.pacman.targetNode
        )
