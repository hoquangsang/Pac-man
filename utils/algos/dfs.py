from utils.math.vector import Vector2
from utils.datastructure.node import Node
# from collections import deque
import tracemalloc
from config import PORTAL

def dfs_path(start: Node, goal: Node, nextGoal:Node=None):
    tracemalloc.start()

    stack = [start]
    came_from: dict[Node, Node] = {start: None}
    path: list[Node] = []

    current: Node = None
    while stack:
        current: Node = stack.pop()

        if current is goal:
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            break
        
        for neighbor in current.neighbors.values():
            if neighbor is not None and neighbor not in came_from:
                stack.append(neighbor)
                came_from[neighbor] = current

    if nextGoal and nextGoal is not goal: # Trường hợp Pacman k nằm trên node
        path.append(nextGoal)
    
    _, peakMem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return path, peakMem, len(came_from)