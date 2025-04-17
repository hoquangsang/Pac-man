from .ghost import Ghost
from ..pacmans.pacman import Pacman
from config import PINKY, PINK, TILESIZE, NCOLS
from utils.algos.dfs import dfs_path, dfs_tree
from utils.math.vector import Vector2
from core.ui.sprites.ghost_sprites import GhostSprites

class Pinky(Ghost): # Pink ghost
    def __init__(self, node, pacman:Pacman=None):
        super().__init__(node,pacman)
        self.name = PINKY
        self.color = PINK
        self.sprites = GhostSprites(self)
        pass