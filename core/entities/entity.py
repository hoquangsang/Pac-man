from utils.math.vector import Vector2
from core.mazes.node import MazeNode
from core.ui.sprites.spritesheet import Spritesheet
from config import *

class Entity(object):
    def __init__(self):
        super().__init__()
        self.position = Vector2()
        self.name = None
        self.color = None
        self.image = None
        self.sprites: Spritesheet = None
        self.visible: bool = True
    
    def update(self, dt):
        pass

    def render(self, screen):
        pass

    def reset(self):
        pass

    def show(self):
        self.visible = True
    
    def hide(self):
        self.visible = False