from utils.math.vector import Vector2
from config import *
from typing import Optional

class Node:
    def __init__(self,x=0,y=0):
        self.position = Vector2(x,y)
        self.neighbors: dict[int, Optional[Node]] = {dir:None for dir in [UP, DOWN, LEFT, RIGHT, PORTAL]} # type: ignore
        # self.occupied = None

    def getKey(self, position:Vector2):
        for key, neighbor in self.neighbors.items():
            if neighbor.position == position:
                return key
        return None
    
    def __lt__(self, other):
        return id(self) < id(other)

    def distanceTo(self, other:'Node') -> float:
        if self.neighbors[PORTAL] == other:
            return 0.
        return (self.position - other.position).magnitude()

    def distanceSquaredTo(self, other:'Node') -> float:
        if self.neighbors[PORTAL] == other:
            return 0.
        return (self.position - other.position).magnitudeSquared()
    
    # def occupy(self, entityName):
    #     self.occupied = entityName

    # def release(self):
    #     self.occupied = None