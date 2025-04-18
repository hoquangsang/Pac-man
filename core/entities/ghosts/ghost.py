import pygame
from pygame.locals import *
from utils.math.vector import Vector2
from config import *
from ..entity import Entity
from core.ui.sprites.ghost_sprites import GhostSprites
from core.mazes.node import MazeNode
from utils.algos.bfs import bfs_path

class Ghost(Entity):
    def __init__(self, node, pacman:Entity=None):
        super().__init__(node)
        self.name = GHOST
        self.color = WHITE
        self.sprites: GhostSprites = None

        self.path: list[MazeNode] = []
        self.targetIdx: int = 0
        self.pacman = pacman
        self.goalNode = pacman.currentNode if pacman else None
        self.peakMem = 0
        # self.disablePortal = True
        self.contructPath()

    def update(self, dt):
        if not self.visible or not self.moveable: return
        self.sprites.update(dt)

        # Nếu pacman thay đổi current;target
        if self.targetLost():
            # print(0)
            self.contructPath()

        self.position += self.directions[self.direction] * self.speed * dt

        if self.overshotTarget():
            self.currentNode = self.targetNode
            if not self.disablePortal: # Tạm thời ??
                if self.currentNode.neighbors[PORTAL] is not None: # Quá nhanh nên target ?
                    self.currentNode = self.targetNode = self.currentNode.neighbors[PORTAL]
                    self.targetIdx += 1
                    # print(1)
            self.setNewTarget()
            self.setPosition()
        
    def render(self, screen):
        super().render(screen=screen)

        adjust = Vector2(TILESIZE, TILESIZE) / 2 + Vector2(self.name)
        for i in range(len(self.path) - 1):
            if self.path[i] is self.currentNode:
                break
            if self.path[i] is self.path[i + 1].neighbors[PORTAL]:
                continue
            line_start = (self.path[i].position+adjust).asTuple()
            line_end = (self.path[i + 1].position+adjust).asTuple()
            pygame.draw.line(screen, self.color, line_start, line_end, PATHSIZE//2)

        line_start = (self.currentNode.position+adjust).asTuple()
        line_end = (self.position+adjust).asTuple()
        pygame.draw.line(screen, self.color, line_start, line_end, PATHSIZE//2)

    def targetLost(self):
        # if self.pacman.currentNode is not self.goalNode:
        #     return True
        if self.pacman.currentNode is not self.pacman.targetNode: # pacman di chuyển
            return True
        return False
    
    def contructPath(self):
        if not self.pacman:
            return
        self.goalNode = self.pacman.currentNode
        self.calculatePath()
        self.targetIdx = 0 if self.currentNode is not self.targetNode else -1
        self.targetNode = self.currentNode
        self.setNewTarget()

    def setNewTarget(self):
        if self.targetIdx + 1 < len(self.path):
            self.targetIdx += 1
            self.targetNode = self.path[self.targetIdx]
            
            direction = self.getDirection()
            if direction is not PORTAL:
                self.direction = direction
            # else:
            #     if self.disablePortal:
            #         self.reverseDirection()
                
            # if self.name == BLINKY:
            #     print("========")
            #     print(f"{self.currentNode.position},{self.position}.{self.targetNode.position}")
            #     print(f"{self.pacman.currentNode.position},{self.pacman.position},{self.pacman.targetNode.position}")
            #     for i in self.path:
            #         print(i.position, end=";")
            # if direction is STOP:
        else:
            self.direction = STOP

    def getDirection(self):
        for key, node in self.currentNode.neighbors.items():
            if node is self.targetNode:
                # if node.neighbors[PORTAL]:
                    # return self.direction
                return key
        return STOP
    #
    def calculatePath(self):
        self.path.clear()
        self.path, self.peakMem, self.numExpandNode, self.tree = bfs_path(
            start=self.currentNode,
            nextStart=self.targetNode,
            goal=self.pacman.currentNode,
            nextGoal=self.pacman.targetNode
        )

    def reset(self):
        super().reset()
        self.contructPath()
