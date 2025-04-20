import pygame
from pygame.locals import *
from utils.math.vector import Vector2
from config import *
from core.entities.moving_entities.moving_entity import MovingEntity
from core.ui.sprites.ghost_sprites import GhostSprites
from core.mazes.node import MazeNode
from .modes.mode_controller import ModeController

class Ghost(MovingEntity):
    def __init__(self, node, pacman:MovingEntity=None):
        super().__init__(node)
        self.name = GHOST
        self.points = 200
        self.color = WHITE
        self.sprites: GhostSprites = None
        self.path: list[MazeNode] = []
        self.targetIdx: int = 0
        self.pacman = pacman
        self.spawnNode: MazeNode = None
        self.scatterNode: MazeNode = None
        self.goalNode: MazeNode = self.pacman.currentNode if self.pacman else None
        self.nextGoalNode: MazeNode = self.pacman.targetNode if self.pacman else None
        self.peakMem = 0
        self.disablePortal = False
        self.mode = ModeController(self)
        self.homeNode: MazeNode = node
        # self.recontructPath()

    def update(self, dt):
        if not self.visible or not self.moveable: return

        self.sprites.update(dt)

        self.mode.update(dt)
        if self.mode.current is CHASE:
            self.chase()
        elif self.mode.current is SCATTER:
            self.scatter()

        self.position += self.directions[self.direction] * self.speed * dt

        if self.targetLost():
            self.reconstructPath()

        if self.overshotTarget():
            self.currentNode = self.targetNode
            self.stepForward()
            self.setPosition()

    def targetLost(self):
        if self.mode.current == CHASE:
            if self.pacman.currentNode is not self.pacman.targetNode: # pacman di chuyển
                if self.goalNode is not self.pacman.targetNode:
                    return True
        return False
    
    def reconstructPath(self):
        # if not self.pacman: return
        # self.goalNode = self.pacman.targetNode
        self.recalculatePath()

        if self.targetNode is self.path[0]:
            self.targetIdx = -1
        elif self.currentNode is self.path[0]:
            self.targetIdx = 0
        # if self.currentNode is self.targetNode:
        #     self.targetIdx = -1  # new target = path[1]
        # else:
        #     self.targetIdx = 0 # new target = path[0]
        
        self.stepForward()

    def stepForward(self):
        if not self.disablePortal:
            portalNode = self.currentNode.neighbors[PORTAL]
            if portalNode and portalNode in self.path:
                self.targetIdx += 1
                self.currentNode = self.targetNode = self.currentNode.neighbors[PORTAL]
        # else:
            # self.reconstructPath()
            # return

        newTarget = self.peekNextNode()
        if newTarget:
            self.targetIdx += 1
            self.targetNode = newTarget

            direction = self.getDirection()
            if direction is not PORTAL:
                self.direction = direction
        else:
            self.direction = STOP
    
    def peekNextNode(self) -> MazeNode | None:
        """Trả về node kế tiếp nếu có"""
        if self.targetIdx + 1 < len(self.path):
            return self.path[self.targetIdx + 1]
        return None

    def getDirection(self):
        # for key, node in self.currentNode.neighbors.items():
        #     if node is self.targetNode:
        #         return key
        for direction, node in self.currentNode.neighbors.items():
            if direction == PORTAL:
                continue
            if node is self.targetNode and self.validDirection(direction):
                return direction
        return STOP
    #
    def recalculatePath(self):
        pass

    def scatter(self):
        self.goalNode = self.nextGoalNode = self.scatterNode
        # self.goal = Vector2()

    def chase(self):
        self.goalNode = self.pacman.currentNode
        self.nextGoalNode = self.pacman.targetNode
        # self.goal = self.pacman.position

    def spawn(self):
        self.goalNode = self.nextGoalNode = self.spawnNode
        # self.goal = self.spawnNode.position

    def freight(self):
        self.goalNode = self.nextGoalNode = self.scatterNode
        pass

    def setSpawnNode(self, node:MazeNode):
        self.spawnNode = node
    
    def setScatterNode(self, node:MazeNode):
        self.scatterNode = node
    
    def startSpawn(self):
        self.mode.setSpawnMode()
        if self.mode.current == SPAWN:
            self.setSpeed(150)
            self.spawn()
            self.reconstructPath()
            # self.directionMethod = self.goalDirection

    def startFreight(self):
        self.mode.setFreightMode()
        if self.mode.current == FREIGHT:
            self.setSpeed(50)
            self.freight()
            self.reconstructPath()
            # self.directionMethod = self.randomDirection         

    def normalMode(self):
        self.setSpeed(100)
        self.goalNode = self.pacman.currentNode if self.pacman else None
        self.nextGoalNode = self.pacman.targetNode if self.pacman else None
        self.reconstructPath()

    def reset(self):
        super().reset()
        self.points = 200
        self.path.clear()
        self.goalNode = self.pacman.currentNode if self.pacman else None
        self.nextGoalNode = self.pacman.targetNode if self.pacman else None
