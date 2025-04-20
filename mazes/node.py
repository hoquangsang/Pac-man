from config import *
from utils.math.vector import Vector2
from utils.datastructure.node import Node

class MazeNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y)

    def render(self, screen,color=RED,adjust=Vector2(TILESIZE, TILESIZE)/2):       
        for key, neighbor in self.neighbors.items():
                pygame.draw.circle(screen, color, (self.position+adjust).asInt(), NODESIZE)
            # if neighbor and key is not PORTAL:
            #     line_start = (self.position+adjust).asTuple()
            #     line_end = (neighbor.position+adjust).asTuple()
            #     pygame.draw.line(screen, WHITE, line_start, line_end, PATHSIZE)
                # edge = MazeEdge(self, neighbor)
                # edge.render(screen)
