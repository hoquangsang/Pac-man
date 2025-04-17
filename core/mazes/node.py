from config import *
from utils.math.vector import Vector2
from utils.datastructure.node import Node

class MazeNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y)
        # self.position = Vector2(x,y)
        self.neighbors: dict[int, Node|None] = {dir:None for dir in [UP, DOWN, LEFT, RIGHT, PORTAL]} # type: ignore

        entities = [PACMAN, BLINKY, PINKY, INKY, CLYDE, FRUIT]
        self.access = {direction: entities[:] for direction in [UP, DOWN, LEFT, RIGHT]}
        
    def render(self, screen):       
        for neighbor in self.neighbors.values():
            if neighbor:
                line_start = self.position.asTuple()
                line_end = neighbor.position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, PATHSIZE)
            pygame.draw.circle(screen, RED, self.position.asInt(), NODESIZE)
        
    def denyAccess(self, direction, entity):
        if entity.name in self.access[direction]:
            self.access[direction].remove(entity.name)

    def allowAccess(self, direction, entity):
        if entity.name not in self.access[direction]:
            self.access[direction].append(entity.name)