from .ghost import Ghost
from config import *

class Inky(Ghost): # Blue ghost
    def __init__(self, node):
        self.name = INKY
        self.color = BLUE
        pass