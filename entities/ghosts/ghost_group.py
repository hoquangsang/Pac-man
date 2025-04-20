from mazes.node import MazeNode
from entities.entity import Entity
from .ghost import Ghost
from .inky import Inky
from .pinky import Pinky
from .blinky import Blinky
from .clyde import Clyde

class GhostGroup(object):
    def __init__(self, node:MazeNode, pacman:Entity):
        self.blinky = Blinky(node, pacman)
        self.pinky = Pinky(node, pacman)
        self.inky = Inky(node, pacman)
        self.clyde = Clyde(node, pacman)
        self.ghosts: list[Ghost] = [self.inky, self.pinky, self.clyde, self.blinky] # đây cũng là thứ tự ưu tiên luôn
        
    def __iter__(self):
        return iter(self.ghosts)

    def update(self, dt):
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
              
    
    def render(self, screen):
        for ghost in self:
            if ghost.visible:
                ghost.render(screen)
                
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

    pass