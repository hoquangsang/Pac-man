from utils.math.distance import euclidean_distance
from utils.math.vector import Vector2
from utils.datastructure.node import Node
from utils.datastructure.graph import Graph
from collections import deque
import tracemalloc

def dfs_tree(start: Node, goal: Node) -> tuple[dict[Node, Node], int]:
    tracemalloc.start()
    stack = deque([start])  # dùng deque như stack, chi phí là O(1) thay vì list O(1), O(n)
    came_from: dict[Node, Node] = {start: None}

    init_mem, _ = tracemalloc.get_traced_memory()
    while stack:
        current: Node = stack.pop()

        if current == goal:
            break

        for neighbor in current.neighbors.values():
            if neighbor is not None and neighbor not in came_from:
                stack.append(neighbor)
                came_from[neighbor] = current

    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return came_from, peak_mem

def dfs_path(start: Node, goal: Node) -> list[Node]:
    search_tree, _ = dfs_tree(start, goal)
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = search_tree[current]

    path.reverse()
    return path
