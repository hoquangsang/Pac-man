from utils.math.vector import Vector2
from utils.datastructure.node import Node
from collections import deque
import tracemalloc

# def bfs_path(start_node, goal_node): ...
def bfs_search_tree(start: Node, goal: Node):
    queue = deque([start])
    came_from: dict[Node, Node] = {start: None}

    while queue:
        current: Node = queue.popleft()

        if current == goal:
            return came_from
        
        for neighbor in current.neighbors.values():
            if neighbor is not None and neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current


def bfs_path(start: Node, goal: Node, nextGoal:Node=None):
    tracemalloc.start()
    queue = deque([start])
    came_from: dict[Node, Node] = {start: None}
    path: list[Node] = []

    current: Node = None
    while queue:
        current: Node = queue.popleft()

        if current is goal:
            while current is not None:
                path.append(current)
                current = came_from[current]
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

    return path, peakMem, len(came_from)