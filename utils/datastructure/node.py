from utils.math.vector import Vector2
from config import *

class Node:
    def __init__(self,x=0,y=0):
        self.position = Vector2(x,y)
        self.neighbors: dict[int, Node|None] = {dir:None for dir in [UP, DOWN, LEFT, RIGHT, PORTAL]} # type: ignore
        self.isOccupied = False

    def getKey(self, position:Vector2):
        for key, neighbor in self.neighbors.items():
            if neighbor.position == position:
                return key
        return None
    
    def __lt__(self, other):
        return id(self) < id(other)


#####
# def getNearestNodeByDistance(nodes, target_position):
#     min_node = None
#     min_distance = float('inf')
#     for node in nodes:
#         distance = (node.position - target_position).magnitudeSquared()
#         if distance < min_distance:
#             min_distance = distance
#             min_node = node
#     return min_node

# def getNearestNodeByPath(start_node: Node, target_position: Vector2):
#     visited = set()
#     heap = []
#     heapq.heappush(heap, (0, start_node))
#     nearest_node = start_node
#     min_distance = float('inf')

#     while heap:
#         cost, current = heapq.heappop(heap)

#         if current in visited:
#             continue
#         visited.add(current)

#         # Tính khoảng cách từ current đến target_position
#         distance = (current.position - target_position).magnitudeSquared()
#         if distance < min_distance:
#             min_distance = distance
#             nearest_node = current

#         for neighbor in current.neighbors.values():
#             if neighbor is not None and neighbor not in visited:
#                 step_cost = (neighbor.position - current.position).magnitudeSquared()  # cost thực tế đến neighbor
#                 heapq.heappush(heap, (cost + step_cost, neighbor))

#     return nearest_node