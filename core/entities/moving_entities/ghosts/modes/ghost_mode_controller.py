from .main_mode import MainMode
from core.entities import MovingEntity
from config import *

class GhostModeController(object):
    def __init__(self, entity: MovingEntity):
        self.timer = 0
        self.time = None
        self.mainmode = MainMode()
        self.current = self.mainmode.mode
        self.entity = entity 

    def update(self, dt):
        self.mainmode.update(dt)
        if self.current is FREIGHT:
            self.timer += dt
            if self.timer >= self.time:
                self.time = None
                self.entity.normalMode()
                self.current = self.mainmode.mode
        elif self.current in [SCATTER, CHASE]:
            self.current = self.mainmode.mode
        if self.current is SPAWN:
            if self.entity.node == self.entity.spawnNode:
                self.entity.normalMode()
                self.current = self.mainmode.mode
                
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

