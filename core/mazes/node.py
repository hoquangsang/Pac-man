from config import *
from utils.math.vector import Vector2
from utils.datastructure.node import Node

class MazeNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y)
        
        entities = [PACMAN, BLINKY, PINKY, INKY, CLYDE, FRUIT]
        self.access = {direction: entities[:] for direction in [UP, DOWN, LEFT, RIGHT]}

    def render(self, screen,color=RED,adjust=Vector2(TILESIZE, TILESIZE)/2):       
        for key, neighbor in self.neighbors.items():
                pygame.draw.circle(screen, color, (self.position+adjust).asInt(), NODESIZE)

    def denyAccess(self, direction, entity):
        if entity.name in self.access[direction]:
            self.access[direction].remove(entity.name)

    def allowAccess(self, direction, entity):
        if entity.name not in self.access[direction]:
            self.access[direction].append(entity.name)