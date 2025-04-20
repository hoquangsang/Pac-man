from config import *
from utils.math.vector import Vector2
from core.mazes.node import MazeNode
from core.ui.sprites.spritesheet import Spritesheet
from core.entities.entity import Entity

class MovingEntity(Entity):
    def __init__(self, node):
        super().__init__()
        self.directions: dict[int, Vector2] = {STOP:Vector2(), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0), PORTAL:Vector2()}
        self.direction: int = STOP
        self.radius: int = 10
        self.collideRadius: int = 5
        self.disablePortal: bool = False
        self.speed: float = 0
        self.setSpeed(100)
        self.moveable: bool = True

        self.currentNode: MazeNode = None
        self.startNode: MazeNode = None
        self.targetNode: MazeNode = None
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

    def reset(self):
        self.setStartNode(self.startNode)
        self.direction = STOP
        self.speed = 100
        self.visible = True
        self.moveable = True
        # self.active = True

    def setStartNode(self, node: MazeNode):
        self.currentNode = node
        self.startNode = node
        self.targetNode = node
        self.setPosition()

    def setPosition(self):
        self.position = self.currentNode.position.copy()
    
    # Movement
    def setSpeed(self, speed):
        self.speed = speed * TILESIZE / 16

    def validDirection(self, direction):
        if direction is not STOP:
            if self.name in self.currentNode.access[direction]:
                if self.currentNode.neighbors[direction] is not None:
                    return True
        return False

    def getNewTarget(self, direction):
        if self.validDirection(direction):
            return self.currentNode.neighbors[direction]
        return self.currentNode
    
    def overshotTarget(self):
        if self.targetNode is not None:
            vec1 = self.targetNode.position - self.currentNode.position
            vec2 = self.position - self.currentNode.position
            node2Target = vec1.magnitudeSquared()
            node2Self = vec2.magnitudeSquared()
            return node2Self >= node2Target
        return False
    
    def reverseDirection(self):
        self.direction *= -1
        self.currentNode, self.targetNode = self.targetNode, self.currentNode

    def oppositeDirection(self, direction):
        if direction is not STOP:
            return direction == -self.direction
        return False
    
    #
    def enableMovement(self):
        self.moveable = True
        
    def disableMovement(self):
        self.moveable = False