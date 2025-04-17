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