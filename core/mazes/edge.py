# trong maze
from utils.datastructure.edge import Edge
from utils.datastructure.node import Node
from utils.math.vector import Vector2
from config import *

class MazeEdge(Edge):
    def __init__(self, edge:tuple[Node, Node]):
        super().__init__(edge)
    
    def render(self, screen, color=LIGHT_GRAY, adjust = Vector2(TILESIZE, TILESIZE) / 2):
        if self.node1.neighbors[PORTAL] is not self.node2:
            line_start = (self.node1.position + adjust).asTuple()
            line_end = (self.node2.position + adjust).asTuple()
            pygame.draw.line(screen, color, line_start, line_end, PATHSIZE)  # Vẽ đường nối