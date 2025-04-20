from utils.datastructure.node import Node
from utils.datastructure.edge import Edge
from utils.datastructure.graph import Graph
from .edge import MazeEdge
from .node import MazeNode
from typing import Optional

class MazeGraph(Graph):
    def __init__(self, cameFrom: dict['Node', Optional['Node']] = None,peakMem=0,searchTime=0):
        super().__init__()
        if cameFrom:
            for node, parent in cameFrom.items():
                if parent is not None:
                    self.addEdge(MazeEdge((node, parent)))
        self.numExpandNode = len(cameFrom)
        self.searchTime = searchTime
        self.peakMem = peakMem

    def render(self, screen):
        # Render tất cả các đỉnh (nodes)
        for vertex in self.vertexList:
            if isinstance(vertex, MazeNode):
                vertex.render(screen)
        
        # Render tất cả các cạnh (edges)
        for edge in self.edgeList:
            if isinstance(edge, MazeEdge):
                edge.render(screen)