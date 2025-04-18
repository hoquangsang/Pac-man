from .ghost import Ghost
from config import *
from utils.algos.bfs import bfs_path, bfs_search_tree
from utils.math.vector import Vector2
from core.ui.sprites.ghost_sprites import GhostSprites
from core.mazes.node import MazeNode
from core.entities.entity import Entity


class Inky(Ghost): # Blue ghost
    def __init__(self, node, pacman:Entity=None):
        super().__init__(node,pacman)
        self.name = INKY
        self.color = BLUE
        self.sprites = GhostSprites(self)
        pass

    def calculatePath(self):
        self.path.clear()
        self.path, self.peakMem, self.numExpandNode = bfs_path(
            self.currentNode,
            self.goalNode,
            self.pacman.targetNode
        )
        print(f"{self.targetNode.position}; {self.pacman.currentNode.position},{self.pacman.position},{self.pacman.targetNode.position}")
        for i in self.path: print(i.position)
        print("=====================")

    # def update(self, dt):
    #     if not self.visible or not self.moveable: return
    #     self.sprites.update(dt)
    #     # Nếu pacman thay đổi current;target
    #     if self.pacman.currentNode != self.goalNode:
    #         self.goalNode = self.pacman.currentNode
    #         self.contructPath()

    #     self.position += self.directions[self.direction] * self.speed * dt
        
    #     if self.overshotTarget():
    #         self.currentNode = self.targetNode
    #         if self.currentNode.neighbors[PORTAL] is not None:
    #             self.currentNode = self.targetNode = self.currentNode.neighbors[PORTAL]
    #             self.targetIdx += 1
    #         self.nextStep()
    #         self.setPosition()
            
