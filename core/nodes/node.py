from config import *
from utils.math.vector import Vector2

class Node:
    def __init__(self,x,y):
        self.position = Vector2(x,y)
        self.neighbors = {dir: None for dir in [UP, DOWN, LEFT, RIGHT, PORTAL]} # type: ignore
    
    def render(self, screen):       
        for neighbor in self.neighbors.values():
            if neighbor:
                line_start = self.position.asTuple()
                line_end = neighbor.position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, PATHSIZE)
            pygame.draw.circle(screen, RED, self.position.asInt(), NODESIZE)