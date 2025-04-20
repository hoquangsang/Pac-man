from utils.math.vector import Vector2
from utils.datastructure.node import Node
from collections import deque
import tracemalloc
import time

def bfs_path(start:Node, nextStart:Node, goal:Node, nextGoal:Node=None):
    start_time = time.time()
    tracemalloc.start()

    queue = deque([nextStart])
    came_from: dict[Node, Node] = {nextStart: None}
    path: list[Node] = []

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
    end_time = time.time()
    search_time = end_time - start_time

    return path, peakMem, search_time*1000, came_from