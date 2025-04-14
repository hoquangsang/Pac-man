from .ghost import Ghost
from .inky import Inky
from .pinky import Pinky
from .blinky import Blinky
from .clyde import Clyde

class GhostGroup(object):
    def __init__(self, node, pacman):
        self.blinky = Blinky(node, pacman)
        self.pinky = Pinky(node, pacman)
        self.inky = Inky(node, pacman)
        self.clyde = Clyde(node, pacman)
        # self.blinky = None
        # self.pinky = None
        # self.inky = None
        # self.clyde = None
        self.ghosts: list[Ghost] = [self.blinky, self.pinky, self.inky, self.clyde]

    def __iter__(self):
        return iter(self.ghosts)

    def update(self, dt):
        for ghost in self:
            if ghost.visible:
                ghost.update(dt)
    
    def render(self, screen):
        for ghost in self:
            if ghost.visible:
                ghost.render(screen)

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
    # def addBlinky(self, node, pacman):
    #     self.blinky = Blinky(node, pacman)
    #     self.ghosts.append(self.blinky)
        
    # def addPinky(self, node, pacman):
    #     self.pinky = Pinky(node, pacman)
    #     self.ghosts.append(self.pinky)
    
    # def addInky(self, node, pacman):
    #     self.inky = Inky(node, pacman)
    #     self.ghosts.append(self.inky)

    # def addClyde(self, node, pacman):
    #     self.clyde = Clyde(node, pacman)
    #     self.ghosts.append(self.clyde)

    # def clear(self):
    #     self.ghosts.clear()