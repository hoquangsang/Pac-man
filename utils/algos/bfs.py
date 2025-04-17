from utils.math.distance import euclidean_distance
from utils.math.vector import Vector2
from utils.datastructure.node import Node
from utils.datastructure.graph import Graph
from collections import deque
import tracemalloc

# def bfs_path(start_node, goal_node): ...
def bfs_tree(start: Node, goal: Node) -> Graph:
    queue = deque([start])
    came_from: dict[Node, Node] = {start: None}

    while queue:
        current: Node = queue.popleft()

        if current == goal:
            break
        
        for neighbor in current.neighbors.values():
            if neighbor is not None and neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current
    
    return came_from

def bfs_path(start: Node, goal: Node) -> list[Node]:
    search_tree = bfs_tree(start, goal)
    # if search_tree:pass
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = search_tree[current]
    
    path.reverse()
    return path
