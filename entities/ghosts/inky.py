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

    def calculatePath(self):
        self.path.clear()
        self.path, self.peakMem, self.numExpandNode, self.tree = bfs_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.goalNode,
            nextGoal=self.pacman.targetNode
        )

    # def renderTree(self, screen):
    #     self.path, self.peakMem, self.numExpandNode, self.tree = bfs_path(
    #         start=None,
    #         nextStart=self.startNode,
    #         goal=self.goalNode,
    #         nextGoal=None
    #     )

    #     # if self.tree is None: return
    #     adjust = Vector2(TILESIZE, TILESIZE) / 2 + Vector2((self.name-GHOST+1) * TILESIZE/8)

        
    #     for cur in self.tree:
    #         nbr = self.tree[cur]
    #         if cur.neighbors[PORTAL] is not nbr:
    #             line_start = (cur.position+adjust).asTuple()
    #             line_end = (nbr.position+adjust).asTuple()
    #             pygame.draw.line(screen, self.color, line_start, line_end, PATHSIZE//2)