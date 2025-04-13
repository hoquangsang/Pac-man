from ..entity import Entity
from utils.math.vector import Vector2
from config import *

class MovingEntity(Entity):
    def __init__(self, node):
        super().__init__()
        self.directions = {STOP:Vector2(), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}
        self.direction = STOP
        self.radius = 10
        self.collideRadius = 5
        # self.node = node
        # self.startNode = None
        # self.target = node
        self.disablePortal = False
        self.speed = 0
        self.setSpeed(100)
        # self.setPosition()
        self.setStartNode(node)
    
    def update(self, dt):
        pass

    def render(self, screen):
        if self.visible:
            if self.image is not None:
                adjust = Vector2(TILESIZE, TILESIZE) / 2
                p = self.position - adjust
                screen.blit(self.image, p.asTuple())
            else:
                p = self.position.asInt()
                pygame.draw.circle(screen, self.color, p, self.radius)

    def setStartNode(self, node):
        self.node = node
        self.startNode = node
        self.target = node
        self.setPosition()

    def setPosition(self):
        self.position = self.node.position.copy()

    # Movement
    def setSpeed(self, speed):
        self.speed = speed * TILESIZE / 16

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
    
