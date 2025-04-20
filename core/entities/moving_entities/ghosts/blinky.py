from config import *
from core.entities.moving_entities.moving_entity import MovingEntity
from core.ui.sprites.ghost_sprites import GhostSprites
from core.mazes.graph import MazeGraph
from utils.algos.a_star import astar_path
from .ghost import Ghost

class Blinky(Ghost): # Red ghost
    def __init__(self, node, pacman:MovingEntity=None):
        super().__init__(node,pacman)
        self.name = BLINKY
        self.color = RED
        self.sprites = GhostSprites(self)
        pass

    def recalculatePath(self):
        self.path.clear()
        self.peakMem = 0
        self.numExpandNode = 0
        self.path, peakMem, searchTime, cameFrom = astar_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.goalNode,
            nextGoal=self.nextGoalNode
        )
        self.searchTree = MazeGraph(cameFrom=cameFrom, searchTime=searchTime, peakMem=peakMem)
