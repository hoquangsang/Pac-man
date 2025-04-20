from utils.math.vector import Vector2
from utils.datastructure.node import Node
import tracemalloc
import random #dfs có thể khiến ghost xảy ra hành vi lạ do pacman di chuyển liên tục

def dfs_path(start:Node, nextStart:Node, goal: Node, nextGoal:Node=None):
    tracemalloc.start()

    stack = [nextStart]
    came_from: dict[Node, Node] = {nextStart: None}
    path: list[Node] = []

    current: Node = None
    while stack:
        current: Node = stack.pop()

        if current is goal:
            while current is not None:
                path.append(current)
                current = came_from[current]
            if start and start is not nextStart:
                path.append(start)
            path.reverse()
            break
        
        neighbors = [n for n in current.neighbors.values() if n is not None and n not in came_from]
        random.shuffle(neighbors)

        for neighbor in neighbors:
            stack.append(neighbor)
            came_from[neighbor] = current

    if nextGoal and nextGoal is not goal: # Trường hợp Pacman k nằm trên node
        path.append(nextGoal)
    
    _, peakMem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return path, peakMem, len(came_from), came_from