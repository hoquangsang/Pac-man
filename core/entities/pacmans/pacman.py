import pygame
from pygame.locals import *
from utils.math.vector import Vector2
from config import *
from ..entity import Entity
from core.ui.sprites.pacman_sprites import PacmanSprites
from ..ghosts.ghost import Ghost

class Pacman(Entity):
    def __init__(self, node):
        super().__init__(node)
        self.name = PACMAN
        self.color = YELLOW
        self.direction = LEFT
        self.sprites = PacmanSprites(self)
        self.alive = True

    def update(self, dt):
        if not self.visible: return
        if not self.moveable: return
        
        self.sprites.update(dt)

        self.position += self.directions[self.direction]*self.speed*dt
        direction = self.getValidKey()
        if self.overshotTarget():
            self.node = self.target
            if self.node.neighbors[PORTAL] is not None:
                self.node = self.node.neighbors[PORTAL]
            self.target = self.getNewTarget(direction)
            if self.target is not self.node:
                self.direction = direction
            else:
                self.target = self.getNewTarget(self.direction)
                if self.target is self.node:
                    self.direction = STOP
            self.setPosition()
        else: 
            if self.oppositeDirection(direction):
                self.reverseDirection()
        
           
    def reverseDirection(self):
        self.direction *= -1
        self.node, self.target = self.target, self.node

    def oppositeDirection(self, direction):
        if direction is not STOP:
            return direction == -self.direction
        return False

    # movement
    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return STOP

    # action
    def collideGhost(self, ghost: Ghost):
        if ghost.visible:
            return self.collideCheck(ghost)
        return False
    
    def collideCheck(self, other):
        d = self.position - other.position
        dSquared = d.magnitudeSquared()
        rSquared = (self.collideRadius + other.collideRadius)**2
        if dSquared <= rSquared:
            return True
        return False
    
    def reset(self):
        Entity.reset(self)
        self.direction = LEFT
        self.image = self.sprites.getStartImage()
        self.sprites.reset()
        self.alive = True

    def die(self):
        self.alive = False
        self.direction = STOP
    pass