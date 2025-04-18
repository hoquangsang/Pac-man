from utils.math.vector import Vector2
from utils.datastructure.node import Node
from config import PORTAL
import heapq
import tracemalloc

def ucs_path(start: Node, nextStart: Node, goal: Node, nextGoal: Node = None):
    tracemalloc.start()
    
    frontier = []
    heapq.heappush(frontier, (0, nextStart))
    came_from: dict[Node, Node] = {nextStart: None}
    cost_so_far: dict[Node, float] = {nextStart: 0}
    path: list[Node] = []

    current: Node = None
    while frontier:
        current_cost, current = heapq.heappop(frontier)

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
                # Tính chi phí từ current đến neighbor
                if neighbor is current.neighbors[PORTAL]:
                    new_cost = cost_so_far[current]
                else:
                    new_cost = cost_so_far[current] + (neighbor.position - current.position).magnitudeSquared()
                
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(frontier, (new_cost, neighbor))
                    came_from[neighbor] = current

    if path and nextGoal and nextGoal is not goal:
        path.append(nextGoal)

    _, peakMem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return path, peakMem, len(came_from), came_from
