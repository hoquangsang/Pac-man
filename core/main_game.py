from config import *
import pygame
from pygame.locals import *
from .nodes.graph import Graph
from .entities.moving_entities.player.pacman import Pacman
from .entities.moving_entities.ghosts.ghost import Ghost
from .entities.static_entities.pellets import *
from .entities import Ghost, GhostGroup, Inky, Pinky, Clyde, Blinky

class GameController(object): 
    def __init__(self, mode=1):
        pygame.init()
        pygame.display.set_caption("Pacman")
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, COLOR_DEPTH)
        self.clock = pygame.time.Clock()
        self.background = None
        self.ghosts = []
        self.pacman = None
        self.nodes = None #NodeGroup("res/mazes/maze1.txt")
        # self.nodes.setPortalPair((0,17), (27,17))
        self.mode = mode
        self.running = True
        self.pellets = None
        # self.setMode(mode)

    def update(self):
        dt = self.clock.tick(FPS) / 1000.0
        self.pacman.update(dt)
        # self.ghost.update(dt)
        self.ghosts.update(dt)
        self.pellets.update(dt)
        self.checkPelletEvents()
        # self.checkGhostEvents()
        self.checkEvents()
        self.render()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.nodes.render(self.screen)
        self.pellets.render(self.screen)
        # self.ghost.render(self.screen)
        self.ghosts.render(self.screen)
        self.pacman.render(self.screen)
        pygame.display.update()

    def startGame(self):
        self.setBackground()
        self.nodes = Graph("res/mazes/maze1.txt")
        self.nodes.setPortalPair((0,17), (27,17))

        homekey = self.nodes.createHomeNodes(11.5, 14)
        self.nodes.connectHomeNodes(homekey, (12,14), LEFT)
        self.nodes.connectHomeNodes(homekey, (15,14), RIGHT)

        # self.pacman = Pacman(self.nodes.getStartTempNode())
        self.pacman = Pacman(self.nodes.getNodeFromTiles(15, 26))

        self.pellets = PelletGroup("res/mazes/maze1.txt")
        # self.ghost = Blinky(self.nodes.getStartTempNode(),self.pacman)
        self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)
        self.ghosts.blinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 0+14))
        self.ghosts.pinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))
        self.ghosts.inky.setStartNode(self.nodes.getNodeFromTiles(0+11.5, 3+14))
        self.ghosts.clyde.setStartNode(self.nodes.getNodeFromTiles(4+11.5, 3+14))
        # self.ghost.setSpawnNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))
        self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def setMode(self, option):
        self.mode = option

    def run(self):
        self.startGame()
        while self.running:
            self.update()
    
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == pygame.K_SPACE:
                pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def checkPelletEvents(self):
        pellet = self.pacman.eatPellets(self.pellets.pelletList)
        if pellet:
            self.pellets.numEaten += 1
            self.pellets.pelletList.remove(pellet)
            # if pellet.name == POWERPELLET:
            #     self.ghosts.startFreight()

    # def checkGhostEvents(self):
    #     for ghost in self.ghosts:
    #         # if self.pacman.collideGhost(self.ghost):
    #         if self.pacman.collideGhost(ghost):
    #             # if self.ghost.mode.current is FREIGHT:
    #             if ghost.mode.current is FREIGHT:
    #                 # self.ghost.startSpawn()
    #                 ghost.startSpawn()
    
    pass