import pygame
from utils.math.vector import Vector2
from config import *
from ..static_entity import StaticEntity

class Pellet(StaticEntity):
    def __init__(self, row, column):
        self.name = PELLET
        self.position = Vector2(column*TILESIZE, row*TILESIZE)
        self.color = WHITE
        # self.radius = int(4 * TILESIZE / 16)
        # self.collideRadius = self.radius
        self.radius = int(2 * TILESIZE / 16)
        self.collideRadius = int(2 * TILESIZE / 16)
        self.points = 10
        self.visible = True
        
    def render(self, screen):
        if self.visible:
            adjust = Vector2(TILESIZE, TILESIZE) / 2
            p = self.position + adjust
            pygame.draw.circle(screen, self.color, p.asInt(), self.radius)