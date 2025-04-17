import pygame
from pygame.locals import *
from utils.math.vector import Vector2
from config import *
from ..moving_entity import MovingEntity
from random import randint
from .modes.mode_controller import ModeController
from core.ui.sprites.ghost_sprites import GhostSprites

class Ghost(MovingEntity):
    def __init__(self, node, pacman=None):
        super().__init__(node)
        self.name = GHOST
        self.points = 200
        self.color = WHITE
        self.goal = Vector2() #pacman.position
        self.directionMethod: function = self.goalDirection
        self.pacman = pacman
        self.mode = ModeController(self)
        self.sprites: GhostSprites = None
        self.homeNode = node

    def update(self, dt):
        if not self.visible: return
        self.mode.update(dt)
        if self.mode.current is CHASE:
            self.chase()
        elif self.mode.current is SCATTER:
            self.scatter()

        self.sprites.update(dt)

        self.position += self.directions[self.direction]*self.speed*dt
        if self.overshotTarget():
            self.node = self.target
            directions = self.validDirections()
            direction = self.directionMethod(directions)
            if not self.disablePortal:
                if self.node.neighbors[PORTAL] is not None:
                    self.node = self.node.neighbors[PORTAL]
            self.target = self.getNewTarget(direction)
            if self.target is not self.node:
                self.direction = direction
            else:
                self.target = self.getNewTarget(self.direction)
            self.setPosition()
    
    def reset(self):
        MovingEntity.reset(self)
        self.points = 200
        self.directionMethod = self.goalDirection

    #
    def validDirections(self):
        directions = []
        for key in [UP, DOWN, LEFT, RIGHT]:
            if self.validDirection(key):
                if key != self.direction * -1:
                    directions.append(key)
        if len(directions) == 0:
            directions.append(self.direction * -1)
        return directions
    
    def randomDirection(self, directions):
        return directions[randint(0, len(directions)-1)]
    
    def goalDirection(self, directions):
        distances = []
        for direction in directions:
            vec = self.node.position  + self.directions[direction]*TILESIZE - self.goal
            distances.append(vec.magnitudeSquared())
        index = distances.index(min(distances))
        return directions[index]
    
    ###
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
            self.directionMethod = self.goalDirection
            self.spawn()

    def startFreight(self):
        self.mode.setFreightMode()
        if self.mode.current == FREIGHT:
            self.setSpeed(50)
            self.directionMethod = self.randomDirection         

    def normalMode(self):
        self.setSpeed(100)
        self.directionMethod = self.goalDirection
        self.homeNode.denyAccess(DOWN, self)
