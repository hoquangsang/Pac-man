from collections import defaultdict
import heapq
import tracemalloc
from itertools import count
from utils.math.vector import Vector2
from utils.datastructure.node import Node
from config import PORTAL
import time

def astar_path(start: Node, nextStart: Node, goal: Node, nextGoal: Node = None):
    start_time = time.time()
    tracemalloc.start()
    frontier = []
    counter = count()  # Đếm để tie-break nếu f-cost bằng nhau

    def heuristic(a: Node, b: Node):
        delta = a.position - b.position
        return delta.magnitudeSquared()

    heapq.heappush(frontier, (0, next(counter), nextStart))
    came_from: dict[Node, Node] = {nextStart: None}
    cost_so_far: dict[Node, float] = {nextStart: 0}
    path: list[Node] = []

    while frontier:
        _, _, current = heapq.heappop(frontier)

        if current is goal:
            while current is not None:
                path.append(current)
                current = came_from[current]
            if start and start is not nextStart:
                path.append(start)
            path.reverse()
            break

        for neighbor in current.neighbors.values():
            if neighbor is not None:
                if neighbor is current.neighbors[PORTAL]:
                    new_cost = cost_so_far[current]
                else:
                    new_cost = cost_so_far[current] + (neighbor.position - current.position).magnitudeSquared()

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(frontier, (priority, next(counter), neighbor))
                    came_from[neighbor] = current

    if path and nextGoal and nextGoal is not goal:
        path.append(nextGoal)

    _, peakMem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    search_time = end_time - start_time

    return path, peakMem, search_time*1000, came_from