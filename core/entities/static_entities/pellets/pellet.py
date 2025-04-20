import pygame
from utils.math.vector import Vector2
from config import *
from core.entities.static_entities.static_entity import StaticEntity

class Pellet(StaticEntity):
    def __init__(self, row, column):
        super().__init__()
        self.name = PELLET
        self.position = Vector2(column*TILESIZE, row*TILESIZE)
        self.color = WHITE
        self.radius = int(2 * TILESIZE / 16)
        self.collideRadius = int(TILESIZE / 16)
        self.points = 10
        
    def render(self, screen):
        if self.visible:
            adjust = Vector2(TILESIZE, TILESIZE) / 2
            p = self.position + adjust
            pygame.draw.circle(screen, self.color, p.asInt(), self.radius)

    def reset(self):
        self.show()
        # self.points = 10