from .node import Node

class Edge(object):
    def __init__(self, edge:tuple[Node, Node]):
        self.node1 = edge[0]
        self.node2 = edge[1]

    def __repr__(self):
        return f"Edge({self.node1}, {self.node2})"
    
    def get_nodes(self):
        return self.node1, self.node2
    
    def __hash__(self):
        # Cung cấp hàm hash để sử dụng đối tượng Edge làm khóa trong các cấu trúc dữ liệu như set, dict
        return hash(frozenset([self.node1, self.node2]))

    def __eq__(self, other):
        # Kiểm tra xem hai edge có giống nhau không (dựa trên node1 và node2)
        return (self.node1 == other.node1 and self.node2 == other.node2) or \
               (self.node1 == other.node2 and self.node2 == other.node1)