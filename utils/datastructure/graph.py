from utils.math.vector import Vector2
from utils.datastructure.node import Node
from config import *
import sys

class Graph(dict[Node, Node]):
    def __init__(self):
        super().__init__()

    def num_expanded(self):
        return len(self) - 1
    
    def memory_used(self):
        return sys.getsizeof(self)