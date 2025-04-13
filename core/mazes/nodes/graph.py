from utils.math.vector import Vector2
from .node import Node
from config import TILESIZE, UP, DOWN, LEFT, RIGHT, PORTAL, WHITE, RED, PATHSIZE, NODESIZE
import numpy as np
import heapq


class Graph:
    def __init__(self, level):
        self.level = level
        self.nodesLUT = {}  # Look-up table cho các node
        self.nodeSymbols = ['+', 'P', 'n']
        self.pathSymbols = ['.', '-', '|', 'p']
        self.loadDataFromFile(level)
        self.homekey = None

    def render(self, screen):
        for node in self.nodesLUT.values():
            node.render(screen)

    def loadDataFromFile(self, textfile):
        data = np.loadtxt(textfile, dtype='<U1')
        if data is None:
            return
        
        self.createNodeTable(data)
        self.connectHorizontally(data)
        self.connectVertically(data)        
        
    def createNodeTable(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):
            for col in list(range(data.shape[1])):
                if data[row][col] in self.nodeSymbols:
                    x, y = self.constructKey(col+xoffset, row+yoffset)
                    self.nodesLUT[(x, y)] = Node(x, y)

    def createHomeNodes(self, xoffset, yoffset):
        homedata = np.array([['X','X','+','X','X'], # homekey = '+'
                             ['X','X','.','X','X'],
                             ['+','X','.','X','+'],
                             ['+','.','+','.','+'],
                             ['+','X','X','X','+']])

        self.createNodeTable(homedata, xoffset, yoffset)
        self.connectHorizontally(homedata, xoffset, yoffset)
        self.connectVertically(homedata, xoffset, yoffset)
        self.homekey = self.constructKey(xoffset+2, yoffset)
        return self.homekey
        
    def connectHorizontally(self, data, xoffset=0, yoffset=0):
        for row in range(data.shape[0]):
            key = None
            for col in range(data.shape[1]):
                if data[row][col] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col+xoffset, row+yoffset)
                    else:
                        otherkey = self.constructKey(col+xoffset, row+yoffset)
                        self.nodesLUT[key].neighbors[RIGHT] = self.nodesLUT[otherkey]
                        self.nodesLUT[otherkey].neighbors[LEFT] = self.nodesLUT[key]
                        key = otherkey
                elif data[row][col] not in self.pathSymbols:
                    key = None

    def connectVertically(self, data, xoffset=0, yoffset=0):
        dataT = data.transpose()
        for col in range(dataT.shape[0]):
            key = None
            for row in range(dataT.shape[1]):
                if dataT[col][row] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col+xoffset, row+yoffset)
                    else:
                        otherkey = self.constructKey(col+xoffset, row+yoffset)
                        self.nodesLUT[key].neighbors[DOWN] = self.nodesLUT[otherkey]
                        self.nodesLUT[otherkey].neighbors[UP] = self.nodesLUT[key]
                        key = otherkey
                elif dataT[col][row] not in self.pathSymbols:
                    key = None

    def constructKey(self, x, y):
        return x * TILESIZE, y * TILESIZE
    
    def getNodeFromPixels(self, xpixel, ypixel):
        if (xpixel, ypixel) in self.nodesLUT.keys():
            return self.nodesLUT[(xpixel, ypixel)]
        return None

    def getNodeFromTiles(self, col, row):
        x, y = self.constructKey(col, row)
        if (x, y) in self.nodesLUT.keys():
            return self.nodesLUT[(x, y)]
        return None
    
    def getStartTempNode(self):
        nodes = list(self.nodesLUT.values())
        return nodes[0]
    
    def setPortalPair(self, pair1, pair2):
        key1 = self.constructKey(*pair1)
        key2 = self.constructKey(*pair2)
        if key1 in self.nodesLUT.keys() and key2 in self.nodesLUT.keys():
            self.nodesLUT[key1].neighbors[PORTAL] = self.nodesLUT[key2]
            self.nodesLUT[key2].neighbors[PORTAL] = self.nodesLUT[key1]

    def connectHomeNodes(self, homekey, otherkey, direction):     
        key = self.constructKey(*otherkey)
        self.nodesLUT[homekey].neighbors[direction] = self.nodesLUT[key]
        self.nodesLUT[key].neighbors[direction*-1] = self.nodesLUT[homekey]



#####
def getNearestNodeByDistance(nodes, target_position):
    min_node = None
    min_distance = float('inf')
    for node in nodes:
        distance = (node.position - target_position).magnitudeSquared()
        if distance < min_distance:
            min_distance = distance
            min_node = node
    return min_node

def getNearestNodeByPath(start_node: Node, target_position: Vector2):
    visited = set()
    heap = []
    heapq.heappush(heap, (0, start_node))
    nearest_node = start_node
    min_distance = float('inf')

    while heap:
        cost, current = heapq.heappop(heap)

        if current in visited:
            continue
        visited.add(current)

        # Tính khoảng cách từ current đến target_position
        distance = (current.position - target_position).magnitudeSquared()
        if distance < min_distance:
            min_distance = distance
            nearest_node = current

        for neighbor in current.neighbors.values():
            if neighbor is not None and neighbor not in visited:
                step_cost = (neighbor.position - current.position).magnitudeSquared()  # cost thực tế đến neighbor
                heapq.heappush(heap, (cost + step_cost, neighbor))

    return nearest_node