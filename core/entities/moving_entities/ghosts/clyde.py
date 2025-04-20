from config import *
from core.ui.sprites.ghost_sprites import GhostSprites
from core.entities.moving_entities.moving_entity import MovingEntity
from core.mazes.graph import MazeGraph
from utils.algos.ucs import ucs_path
from .ghost import Ghost

class Clyde(Ghost): # Orange ghost
    def __init__(self, node, pacman:MovingEntity=None):
        super().__init__(node, pacman)
        self.name = CLYDE
        self.color = ORANGE
        self.sprites = GhostSprites(self)
        pass

    def recalculatePath(self):
        self.path.clear()
        self.peakMem = 0
        self.numExpandNode = 0
        self.path, peakMem, searchTime, cameFrom = ucs_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.goalNode,
            nextGoal=self.nextGoalNode
        )
        self.searchTree = MazeGraph(cameFrom=cameFrom, searchTime=searchTime, peakMem=peakMem)
