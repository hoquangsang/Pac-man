from ..entity import Entity
from utils.math.vector import Vector2
from config import *
from random import randint

class MovingEntity(Entity):
    def __init__(self, node):
        super().__init__()
        self.directions = {STOP:Vector2(), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}
        self.direction = STOP
        self.radius = 10
        self.collideRadius = 5
        self.node = node
        self.target = node
        self.disablePortal = False
        self.speed = 0
        self.setSpeed(100)
        self.setPosition()

    def render(self, screen):
        if self.visible:
            p = self.position.asInt()
            pygame.draw.circle(screen, self.color, p, self.radius)

    def update(self, dt):
        self.position += self.directions[self.direction]*self.speed*dt
         
        if self.overshotTarget():
            self.node = self.target
            directions = self.validDirections()
            direction = self.randomDirection(directions)   
            if not self.disablePortal:
                if self.node.neighbors[PORTAL] is not None:
                    self.node = self.node.neighbors[PORTAL]
            self.target = self.getNewTarget(direction)
            if self.target is not self.node:
                self.direction = direction
            else:
                self.target = self.getNewTarget(self.direction)
            self.setPosition()
    
    #
    def setPosition(self):
        self.position = self.node.position.copy()

    # Movement
    def setSpeed(self, speed):
        self.speed = speed * TILESIZE / 16

    # - 
    def validDirection(self, direction):
        if direction is not STOP:
            if self.node.neighbors[direction] is not None:
                return True
        return False
       
    def reverseDirection(self):
        self.direction *= -1
        self.node, self.target = self.target, self.node

    def oppositeDirection(self, direction):
        if direction is not STOP:
            return direction == -self.direction
        return False
    
    def getNewTarget(self, direction):
        if self.validDirection(direction):
            return self.node.neighbors[direction]
        return self.node
    
    def overshotTarget(self):
        if self.target is not None:
            vec1 = self.target.position - self.node.position
            vec2 = self.position - self.node.position
            node2Target = vec1.magnitudeSquared()
            node2Self = vec2.magnitudeSquared()
            return node2Self >= node2Target
        return False
    
    #
    def randomDirection(self, directions):
        return directions[randint(0, len(directions)-1)]

