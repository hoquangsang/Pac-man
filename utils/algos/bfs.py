from utils.math.vector import Vector2
from utils.datastructure.node import Node
from collections import deque
import tracemalloc

def bfs_path(start:Node, nextStart:Node, goal:Node, nextGoal:Node=None):
    tracemalloc.start()
    queue = deque([nextStart])
    came_from: dict[Node, Node] = {nextStart: None}
    path: list[Node] = []

    current: Node = None
    while queue:
        current: Node = queue.popleft()

        if current is goal:
            while current is not None:
                path.append(current)
                current = came_from[current]
            if start and start is not nextStart:
                path.append(start)
            path.reverse()
            break
        
        for neighbor in current.neighbors.values():
            if neighbor is not None and neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current

    if path and nextGoal and nextGoal is not goal: # Trường hợp Pacman k nằm trên node
        path.append(nextGoal)
    
    
    _, peakMem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return path, peakMem, len(came_from), came_from