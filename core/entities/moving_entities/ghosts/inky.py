from config import *
from core.entities.moving_entities.moving_entity import MovingEntity
from core.mazes.graph import MazeGraph
from core.ui.sprites.ghost_sprites import GhostSprites
from utils.algos.bfs import bfs_path
from .ghost import Ghost

class Inky(Ghost): # Blue ghost
    def __init__(self, node, pacman:MovingEntity=None):
        super().__init__(node,pacman)
        self.name = INKY
        self.color = LIGHT_BLUE
        self.sprites = GhostSprites(self)
        pass

    def recalculatePath(self):
        self.path.clear()
        self.peakMem = 0
        self.numExpandNode = 0
        self.searchTree = {}
        self.path, peakMem, numExpandNode, cameFrom = bfs_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.pacman.currentNode,
            nextGoal=self.pacman.targetNode
        )
        self.searchTree = MazeGraph(cameFrom=cameFrom, expands=numExpandNode,peekMem=peakMem)
