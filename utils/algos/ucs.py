from utils.math.distance import euclidean_distance
from utils.math.vector import Vector2
from utils.datastructure.node import Node
from utils.datastructure.graph import Graph
import tracemalloc
import heapq

def ucs_tree(start: Node, goal: Node) -> tuple[dict[Node, Node], int, int]:
    tracemalloc.start()
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from: dict[Node, Node] = {start: None}
    cost_so_far: dict[Node, int] = {start: 0}

    init_mem, _ = tracemalloc.get_traced_memory()

    while frontier:
        current_cost, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor in current.neighbors.values():
            step_cost = (current.position - neighbor.position).magnitudeSquared()
            new_cost = cost_so_far[current] + step_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(frontier, (new_cost, neighbor))


    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return came_from, peak_mem

def ucs_path(start: Node, goal: Node) -> list[Node]:
    search_tree, _, _ = dfs_tree(start, goal)
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = search_tree[current]

    path.reverse()
    return path
