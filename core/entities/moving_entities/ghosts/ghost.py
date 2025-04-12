import pygame
from pygame.locals import *
from utils.math.vector import Vector2
from config import *
from ..moving_entity import MovingEntity
from random import randint
# from .modes.mode_controller import ModeController

class Ghost(MovingEntity):
    def __init__(self, node, pacman=None):
        super().__init__(node)
        self.name = GHOST
        self.points = 200
        self.color = WHITE
        self.goal = Vector2()
        # self.directionMethod = self.randomDirection
        self.directionMethod = self.goalDirection
        self.pacman = pacman
        # self.mode = ModeController(self)

    def update(self, dt):
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

    def render(self, screen):
        if self.visible:
            p = self.position.asInt()
            pygame.draw.circle(screen, self.color, p, self.radius)

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
        # pass
        distances = []
        for direction in directions:
            vec = self.node.position  + self.directions[direction]*TILESIZE - self.goal
            distances.append(vec.magnitudeSquared())
        index = distances.index(min(distances))
        return directions[index]
    
    ###
    def spawn(self):
        self.goal = self.spawnNode.position

    def setSpawnNode(self, node):
        self.spawnNode = node