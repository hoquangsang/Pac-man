from .main_mode import MainMode
from config import *

class ModeController(object):
    def __init__(self, ghost):
        self.timer = 0
        self.time = None
        self.mainmode = MainMode()
        self.current = self.mainmode.mode
        self.ghost = ghost

    def update(self, dt):
        self.mainmode.update(dt)
        if self.current is FREIGHT:
            self.timer += dt
            if self.timer >= self.time:
                self.time = None
                self.current = self.mainmode.mode
                self.ghost.normalMode()
                
        elif self.current in [SCATTER, CHASE]:
            self.current = self.mainmode.mode

        if self.current is SPAWN:
            if self.ghost.currentNode is self.ghost.spawnNode:
                self.current = self.mainmode.mode
                self.ghost.normalMode()
                
    def setSpawnMode(self):
        if self.current is FREIGHT:
           self.current = SPAWN

    def setFreightMode(self):
        if self.current in [SCATTER, CHASE]:
            self.timer = 0
            self.time = 7
            self.current = FREIGHT
        elif self.current is FREIGHT:
            self.timer = 0
