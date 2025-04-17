from .ghost import Ghost
from ..pacmans.pacman import Pacman
from config import PINKY, PINK, TILESIZE, NCOLS
from utils.algos.dfs import dfs_path, dfs_tree
from utils.math.vector import Vector2
from core.ui.sprites.ghost_sprites import GhostSprites

class Pinky(Ghost): # Pink ghost
    def __init__(self, node, pacman:Pacman=None):
        super().__init__(node,pacman)
        self.name = PINKY
        self.color = PINK
        self.sprites = GhostSprites(self)
        pass

    # def goalDirection(self, directions):
    #     if self.pacman is None:
    #         return self.randomDirection(directions)

    #     path = dfs_path(self.node, self.pacman.node)

    #     if path is not None and len(path) > 1:
    #         next_node = path[1]
    #         for direction in directions:
    #             if self.node.neighbors.get(direction) == next_node:
    #                 return direction
                
    #     return self.randomDirection(directions)

    def scatter(self):
        self.goal = Vector2(TILESIZE*NCOLS, 0)

    # def chase(self):
    #     self.goal = self.pacman.position + self.pacman.directions[self.pacman.direction] * TILESIZE * 4
