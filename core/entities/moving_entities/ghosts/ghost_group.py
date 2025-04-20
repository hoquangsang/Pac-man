from core.mazes.node import MazeNode
from core.entities.moving_entities.moving_entity import MovingEntity
from .ghost import Ghost
from .inky import Inky
from .pinky import Pinky
from .blinky import Blinky
from .clyde import Clyde

class GhostGroup(object):
    def __init__(self, node:MazeNode, pacman:MovingEntity):
        self.blinky = Blinky(node, pacman)
        self.pinky = Pinky(node, pacman)
        self.inky = Inky(node, pacman)
        self.clyde = Clyde(node, pacman)
        self.ghosts: list[Ghost] = [self.blinky,self.pinky,self.clyde,self.inky]
        
    def __iter__(self):
        return iter(self.ghosts)

    def update(self, dt):
        # 1. Reset trạng thái moveable
        for ghost in self:
            ghost.enableMovement()

        # 2. Duyệt theo thứ tự ưu tiên cao -> thấp (name càng lớn càng ưu tiên)
        nextMoves = {}       # key: (fromNode, toNode), value: ghost.name
        occupiedNodes = {}   # key: toNode, value: ghost.name

        for ghost in self:#sorted(self, key=lambda g: g.name, reverse=True):  # name lớn → ưu tiên cao
            if not ghost.visible:
                continue

            currentNode = ghost.currentNode
            nextNode = ghost.peekNextNode()

            if currentNode is None or nextNode is None:
                continue

            move = (currentNode, nextNode)
            reverseMove = (nextNode, currentNode)

            # 1. Tránh ghost khác đã đi tới node này
            if nextNode in occupiedNodes:
                otherName = occupiedNodes[nextNode]
                if ghost.name < otherName:  # ghost này ưu tiên thấp hơn → phải đứng lại
                    ghost.disableMovement()
                    continue

            # 2. Tránh ghost đối đầu
            if reverseMove in nextMoves:
                otherName = nextMoves[reverseMove]
                if ghost.name < otherName:  # ghost này ưu tiên thấp hơn
                    ghost.disableMovement()
                    continue

            # 3. Không bị block, thì ghi lại hành động
            nextMoves[move] = ghost.name
            occupiedNodes[nextNode] = ghost.name

        # 3. Cập nhật từng ghost
        for ghost in self:
            if ghost.visible:
                ghost.update(dt)

    def render(self, screen):
        for ghost in self:
            if ghost.visible:
                ghost.render(screen)

    ### mode
    def startFreight(self):
        for ghost in self:
            if ghost.visible:
                ghost.startFreight()
        self.resetPoints()

    def startSpawn(self):
        for ghost in self:
            if ghost.visible:
                ghost.startSpawn()

    def setSpawnNode(self, node):
        for ghost in self:
            if ghost.visible:
                ghost.setSpawnNode(node)

    def updatePoints(self):
        for ghost in self:
            ghost.points *= 2

    def resetPoints(self):
        for ghost in self:
            ghost.points = 200

    ### data    
    def recontructPath(self):
        for ghost in self:
            if ghost.visible:
                ghost.reconstructPath()

    def reset(self):
        for ghost in self:
            ghost.reset()

    def hide(self):
        for ghost in self:
            ghost.hide()
    
    def show(self):
        for ghost in self:
            ghost.show()

"""    def update(self, dt):
        # 1. Reset trạng thái moveable
        for ghost in self:
            ghost.enableMovement()

        # 2. Lưu vị trí hiện tại của từng ghost
        currentOccupied = {}  # key: node, value: ghost.name
        for ghost in self:
            if ghost.currentNode is not None:
                currentOccupied[ghost.currentNode] = ghost.name

        # 3. Duyệt theo thứ tự ưu tiên cao -> thấp
        nextMoves = {}
        occupiedNodes = {}

        for ghost in sorted(self, key=lambda g: g.name, reverse=True):
            if not ghost.visible:
                continue

            currentNode = ghost.currentNode
            nextNode = ghost.peekNextNode()

            if currentNode is None or nextNode is None:
                continue

            move = (currentNode, nextNode)
            reverseMove = (nextNode, currentNode)

            # Trường hợp node kế tiếp đang bị 1 ghost khác đứng trên đó
            if nextNode in currentOccupied:
                otherName = currentOccupied[nextNode]
                if ghost.name < otherName:
                    ghost.disableMovement()
                    continue

            # Tránh va chạm cùng hướng
            if nextNode in occupiedNodes:
                otherName = occupiedNodes[nextNode]
                if ghost.name < otherName:
                    ghost.disableMovement()
                    continue

            # Tránh va chạm đối đầu
            if reverseMove in nextMoves:
                otherName = nextMoves[reverseMove]
                if ghost.name < otherName:
                    ghost.disableMovement()
                    continue

            # OK, được quyền đi
            nextMoves[move] = ghost.name
            occupiedNodes[nextNode] = ghost.name

        # 4. Cập nhật từng ghost
        for ghost in self:
            if ghost.visible:
                ghost.update(dt)
"""


    ### ui
"""    def update(self, dt):
        # 1. Reset trạng thái moveable
        for ghost in self:
            ghost.enableMovement()

        # 2. Duyệt theo thứ tự độ ưu tiên (đã có sẵn trong self.ghosts)
        nextPositions = {}  # key: node, value: ghost.name
        for ghost in self:
            if not ghost.visible:
                continue

            nextNode = ghost.peekNextNode()
            if nextNode is None:
                continue

            if nextNode in nextPositions:
                # Có ghost khác đi tới node này trước đó
                otherName = nextPositions[nextNode]
                if ghost.name > otherName:  # ghost này ưu tiên thấp hơn
                    ghost.disableMovement()
            else:
                nextPositions[nextNode] = ghost.name  # đăng ký bước tới

        # 3. Cập nhật từng ghost (chỉ ghost.moveable mới update)
        for ghost in self:
            if ghost.visible:
                ghost.update(dt)
"""
