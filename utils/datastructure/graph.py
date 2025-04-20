from .edge import Edge
from .node import Node

class Graph(object):
    def __init__(self):
        self.edgeList: list[Edge] = [] #Danh sách kề
        self.vertexList: list[Node] = []
        
    def clear(self):
        self.edgeList.clear()
        self.vertexList.clear()

    def addEdge(self, edge: Edge):
        self.edgeList.append(edge)
        # Thêm các node vào vertexList nếu chưa tồn tại
        if edge.node1 not in self.vertexList:
            self.vertexList.append(edge.node1)
        if edge.node2 not in self.vertexList:
            self.vertexList.append(edge.node2)
            
    def addVertex(self, vertex: Node):
        if vertex not in self.vertexList:
            self.vertexList.append(vertex)