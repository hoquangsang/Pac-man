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

    def calculatePath(self):
        self.path.clear()
        self.path, self.peakMem, self.numExpandNode, self.tree = ucs_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.goalNode,
            nextGoal=self.pacman.targetNode
        )

    # def renderTree(self, screen):
    #     self.path, self.peakMem, self.numExpandNode, self.tree = ucs_path(
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