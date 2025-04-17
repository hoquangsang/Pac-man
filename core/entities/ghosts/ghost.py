import pygame
from pygame.locals import *
from utils.math.vector import Vector2
from config import *
from ..entity import Entity
from core.ui.sprites.ghost_sprites import GhostSprites

class Ghost(Entity):
    def __init__(self, node, pacman=None):
        super().__init__(node)
        self.name = GHOST
        self.points = 200
        self.color = WHITE
        self.goal = pacman.position #Vector2()
        self.directionMethod: function = self.goalDirection
        self.pacman = pacman
        self.sprites: GhostSprites = None
        self.homeNode = node

    def update(self, dt):
        if not self.visible: return

        self.sprites.update(dt)

        if not self.moveable: return

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
        Entity.reset(self)
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
    
    def goalDirection(self, directions):
        distances = []
        for direction in directions:
            vec = self.node.position  + self.directions[direction]*TILESIZE - self.goal
            distances.append(vec.magnitudeSquared())
        index = distances.index(min(distances))
        return directions[index]
