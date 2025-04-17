from .pellet import Pellet
from config import POWERPELLET, TILESIZE, WHITE, BLACK

class PowerPellet(Pellet):
    def __init__(self, row, column):
        Pellet.__init__(self, row, column)
        self.name = POWERPELLET
        self.radius = int(8 * TILESIZE / 16)
        self.points = 50
        self.flashTime = 0.2
        self.timer= 0
        
    def update(self, dt):
        self.timer += dt
        if self.timer >= self.flashTime:
            self.timer = 0
            self.visible = not self.visible
            # if self.color == WHITE:
            #     self.color = BLACK
            # else:
            #     self.color = WHITE