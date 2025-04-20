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
        self.nextGoalNode = None
        self.goalNode = None
        self.peakMem = 0
        self.disablePortal = True
        self.mode = ModeController(self)
        self.homeNode = node
        # self.recontructPath()

    def update(self, dt):
        if not self.visible or not self.moveable: return

        self.mode.update(dt)
        if self.mode.current is CHASE:
            self.chase()
        elif self.mode.current is SCATTER:
            self.scatter()

        self.sprites.update(dt)

        self.position += self.directions[self.direction] * self.speed * dt

        if self.targetLost():
            self.reconstructPath()

        if self.overshotTarget():
            self.currentNode = self.targetNode
            self.stepForward()
            self.setPosition()

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
        pass

    def scatter(self):
        self.goal = Vector2()
        # self.goal = self.pacman.position

    def chase(self):
        self.goal = self.pacman.position  

    def spawn(self):
        self.goal = self.spawnNode.position

    def setSpawnNode(self, node):
        self.spawnNode = node
    
    def startSpawn(self):
        self.mode.setSpawnMode()
        if self.mode.current == SPAWN:
            self.setSpeed(150)
            # self.directionMethod = self.goalDirection
            self.spawn()

    def startFreight(self):
        self.mode.setFreightMode()
        if self.mode.current == FREIGHT:
            self.setSpeed(50)
            # self.directionMethod = self.randomDirection         

    def normalMode(self):
        self.setSpeed(100)
        # self.directionMethod = self.goalDirection
        self.homeNode.denyAccess(DOWN, self)

    def reset(self):
        super().reset()
        self.points = 200
        self.path.clear()
