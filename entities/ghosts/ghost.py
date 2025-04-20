import pygame
from pygame.locals import *
from utils.math.vector import Vector2
from config import *
from ..entity import Entity
from ui.sprites.ghost_sprites import GhostSprites
from mazes.node import MazeNode
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
        # self.recontructPath()

    def update(self, dt):
        if not self.visible or not self.moveable: return
        self.sprites.update(dt)

        self.position += self.directions[self.direction] * self.speed * dt

        if self.targetLost():
            self.reconstructPath()

        if self.overshotTarget():
            # if self.currentNode.neighbors[PORTAL] is not None:
            #     if not self.disablePortal:
            #         self.currentNode = self.targetNode = self.currentNode.neighbors[PORTAL]
            #         self.targetIdx += 1
            # else:
            #     # Khi ghost không đứng yên
            #     self.currentNode = self.targetNode

            self.currentNode = self.targetNode
            self.stepForward()
            self.setPosition()
        
    def render(self, screen):
        super().render(screen=screen)

        # adjust = Vector2(TILESIZE, TILESIZE)/2
        # for i in range(len(self.path) - 1):
        #     if self.path[i] is self.currentNode:
        #         break
        #     if self.path[i] is self.path[i + 1].neighbors[PORTAL]:
        #         continue
        #     line_start = (self.path[i].position+adjust).asTuple()
        #     line_end = (self.path[i + 1].position+adjust).asTuple()
        #     pygame.draw.line(screen, self.color, line_start, line_end, PATHSIZE)

        # line_start = (self.currentNode.position+adjust).asTuple()
        # line_end = (self.position+adjust).asTuple()
        # pygame.draw.line(screen, self.color, line_start, line_end, PATHSIZE)

    def targetLost(self):
        if self.pacman.currentNode is not self.pacman.targetNode: # pacman di chuyển
            if self.goalNode is not self.pacman.targetNode:
                return True
        return False
    
    def reconstructPath(self):
        if not self.pacman: return
        self.recalculatePath()
        self.goalNode = self.pacman.targetNode
        if self.currentNode is self.targetNode:
            self.targetIdx = -1  # new target = path[1]
        else:
            self.targetIdx = 0 # new target = path[0]
        
        self.stepForward()

    def stepForward(self):
        if not self.disablePortal:
            portalNode = self.currentNode.neighbors[PORTAL]
            if portalNode is not None and portalNode in self.path:
                self.targetIdx += 1
                self.currentNode = self.targetNode = self.currentNode.neighbors[PORTAL]

        newTarget = self.peekNextNode()
        if newTarget:
            self.targetIdx += 1
            self.targetNode = newTarget

            direction = self.getDirection()
            if direction is not PORTAL:
                self.direction = direction
        else:
            self.direction = STOP
    
    # def tele(self):

    def peekNextNode(self) -> MazeNode | None:
        """Trả về node kế tiếp nếu có"""
        if self.targetIdx + 1 < len(self.path):
            return self.path[self.targetIdx + 1]
        return None

    def getDirection(self):
        for key, node in self.currentNode.neighbors.items():
            if node is self.targetNode:
                return key
        return STOP
    #
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

    def reset(self):
        super().reset()
        self.path.clear()
