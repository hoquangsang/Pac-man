import pygame
from pygame.locals import *
from utils.math.vector import Vector2
from config import *
from core.entities.moving_entities.moving_entity import MovingEntity
from core.ui.sprites.pacman_sprites import PacmanSprites
from core.entities.static_entities.pellets.pellet import Pellet

class Pacman(MovingEntity):
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
            self.currentNode = self.targetNode
            if self.currentNode.neighbors[PORTAL] is not None:
                self.currentNode = self.currentNode.neighbors[PORTAL]
            self.targetNode = self.getNewTarget(direction)
            if self.targetNode is not self.currentNode:
                self.direction = direction
            else:
                self.targetNode = self.getNewTarget(self.direction)
                if self.targetNode is self.currentNode:
                    self.direction = STOP
            self.setPosition()
        else: 
            if self.oppositeDirection(direction):
                self.reverseDirection()
        
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
    def eatPellets(self, pelletList:list[Pellet]):
        for pellet in pelletList:
            if pellet.visible:
                if self.collideCheck(pellet):
                    return pellet
        return None
    
    def collideGhost(self, ghost: MovingEntity):
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
        MovingEntity.reset(self)
        self.direction = LEFT
        self.image = self.sprites.getStartImage()
        self.sprites.reset()
        self.alive = True

    def die(self):
        self.alive = False
        self.direction = STOP
    pass