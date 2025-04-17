from .ghost import Ghost
from ..pacmans.pacman import Pacman
from config import *
from utils.algos.bfs import bfs_path, bfs_tree
from utils.math.vector import Vector2
from core.ui.sprites.ghost_sprites import GhostSprites

class Inky(Ghost): # Blue ghost
    def __init__(self, node, pacman:Pacman=None):
        super().__init__(node,pacman)
        self.name = INKY
        self.color = BLUE
        self.sprites = GhostSprites(self)
        pass

    # def goalDirection(self, directions):
    #     if self.pacman is None:
    #         return self.randomDirection(directions)

    #     path = bfs_path(self.node, self.pacman.node)

    #     if path is not None and len(path) > 1:
    #         next_node = path[1]
    #         for direction in directions:
    #             if self.node.neighbors.get(direction) == next_node:
    #                 return direction
                
    #     return STOP