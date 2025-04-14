from config import *
import pygame
from pygame.locals import *
import sys
import os
from core.mazes.nodes.graph import Graph
from .entities.moving_entities.player.pacman import Pacman
from .entities.moving_entities.ghosts.ghost import Ghost
from .entities.moving_entities.ghosts.ghost_group import GhostGroup
from .entities.static_entities.pellets import *
from .entities.moving_entities.ghosts.inky import Inky
from .entities.moving_entities.ghosts.pinky import Pinky
from .entities.moving_entities.ghosts.clyde import Clyde
from .entities.moving_entities.ghosts.blinky import Blinky
from .ui.sprites.maze_sprite import MazeSprites 

class GameController(object): 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pacman")
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, COLOR_DEPTH)
        self.clock = pygame.time.Clock()
        self.background = None
        self.ghosts = []
        self.pacman = None
        self.nodes = None #Graph("res/mazes/maze1.txt")
        self.mode = MODE_PLAY# mode
        self.running = True
        self.pellets = None
        self.level = 0
        self.lives = 5
        self.options = [
            "Blue Ghost",
            "Pink Ghost",
            "Orange Ghost",
            "Red Ghost",
            "All Ghosts",
            "Play"
        ]
        self._initData()

    def update(self):
        dt = self.clock.tick(FPS) / 1000.0
        if self.mode == MODE_PLAY:
            self.pacman.update(dt)
            self.pellets.update(dt)
            self.checkPelletEvents()
        # self.ghost.update(dt)

        self.ghosts.update(dt)
        self.checkGhostEvents()
        self.checkEvents()
        self.render()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        if self.mode == MODE_PLAY:
            self.pellets.render(self.screen)
        self.ghosts.render(self.screen)
        self.pacman.render(self.screen)
        pygame.display.update()

    def startGame(self):
        self.running = True
        self.setBackground()
        self.mazesprites = MazeSprites("res/mazes/maze1.txt","res/mazes/maze1_rotation.txt")
        self.background = self.mazesprites.constructBackground(self.background, self.level%5)

        self.pacman.reset()
        self.setMode()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)
    
    #####
    def _initData(self):
        self.nodes = Graph("res/mazes/maze1.txt")
        self.nodes.setPortalPair((0,17), (27,17))
        homekey = self.nodes.createHomeNodes(11.5, 14)
        self.nodes.connectHomeNodes(homekey, (12,14), LEFT)
        self.nodes.connectHomeNodes(homekey, (15,14), RIGHT)

        self.pacman = Pacman(self.nodes.getNodeFromTiles(15, 26))
        self.pellets = PelletGroup("res/mazes/maze1.txt")
        self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)
        self.ghosts.blinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 0+14))
        self.ghosts.pinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))
        self.ghosts.inky.setStartNode(self.nodes.getNodeFromTiles(0+11.5, 3+14))
        self.ghosts.clyde.setStartNode(self.nodes.getNodeFromTiles(4+11.5, 3+14))
        
        self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))

        self.nodes.denyHomeAccess(self.pacman)
        self.nodes.denyHomeAccessList(self.ghosts)
        self.nodes.denyAccessList(2+11.5, 3+14, LEFT, self.ghosts)
        self.nodes.denyAccessList(2+11.5, 3+14, RIGHT, self.ghosts)
        self.ghosts.inky.startNode.denyAccess(RIGHT, self.ghosts.inky)
        self.ghosts.clyde.startNode.denyAccess(LEFT, self.ghosts.clyde)
        self.nodes.denyAccessList(12, 14, UP, self.ghosts)
        self.nodes.denyAccessList(15, 14, UP, self.ghosts)
        self.nodes.denyAccessList(12, 26, UP, self.ghosts)
        self.nodes.denyAccessList(15, 26, UP, self.ghosts)

    ##############
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
        pellet: Pellet = self.pacman.eatPellets(self.pellets.pelletList)
        if pellet:
            pellet.hide()
            self.pellets.numEaten += 1
            if pellet.name == POWERPELLET:
                self.ghosts.startFreight()

    def checkGhostEvents(self):
       for ghost in self.ghosts:
            if self.pacman.collideGhost(ghost):
                if ghost.mode.current is FREIGHT:
                    ghost.startSpawn()
                    self.nodes.allowHomeAccess(ghost)
                elif ghost.mode.current is not SPAWN:
                    self.running = False
                    return
    #                  if self.pacman.alive:
    #                      self.lives -=  1
    #                      self.pacman.die()
    #                      self.ghosts.hide()
    #                      if self.lives <= 0:
    #                          self.pause.setPause(pauseTime=3, func=self.restartGame)
    #                      else:
    #                          self.pause.setPause(pauseTime=3, func=self.resetLevel)
    
    def showMenu(self):
        bg_path = os.path.join("res", "images", "menubg.jpg")
        self.background = pygame.image.load(bg_path).convert()
        self.background = pygame.transform.scale(self.background, SCREENSIZE)

        while True:
            self.drawMenu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.mode = (self.mode - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.mode = (self.mode + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return  # Thoát menu
            self.clock.tick(30)
    
    def drawMenu(self):
        self.screen.blit(self.background, (0, 0))

        title = TITLE_FONT.render("Pacman", True, ORANGE)
        title_x = SCREENWIDTH // 2 - title.get_width() // 2
        self.screen.blit(title, (title_x, 20))

        # Vẽ từng option
        for i, option in enumerate(self.options):
            is_selected = (i == self.mode)
            box_width = 280
            box_height = 40
            x = SCREENWIDTH // 2 - box_width // 2
            y = 140 + i * 55
            rect = pygame.Rect(x, y, box_width, box_height)

            # Viền bo góc
            border_color = LIGHT_BLUE if is_selected else WHITE
            pygame.draw.rect(self.screen, border_color, rect, width=3, border_radius=10)

            # Text màu
            text_color = LIGHT_BLUE if is_selected else WHITE
            text_surface = OPTION_FONT.render(option, True, text_color)
            text_x = x + (box_width - text_surface.get_width()) // 2
            text_y = y + (box_height - text_surface.get_height()) // 2
            self.screen.blit(text_surface, (text_x, text_y))

        pygame.display.flip()

    def setMode(self):
        if self.mode == MODE_BLUE_GHOST:
            self.pellets.hide()
            self.ghosts.hide()
            self.ghosts.inky.reset()
        elif self.mode == MODE_PINK_GHOST:
            self.pellets.hide()
            self.ghosts.hide()
            self.ghosts.pinky.reset()
        elif self.mode == MODE_ORANGE_GHOST:
            self.pellets.hide()
            self.ghosts.hide()
            self.ghosts.clyde.reset()
        elif self.mode == MODE_RED_GHOST:
            self.pellets.hide()
            self.ghosts.hide()
            self.ghosts.blinky.reset()
        elif self.mode == MODE_ALL_GHOST:
            self.pellets.hide()
            self.ghosts.reset()
        elif self.mode == MODE_PLAY:
            self.ghosts.reset()
            self.pellets.reset()
    
    def run(self):
        while True:
            self.showMenu()
            # self.setMode()
            self.startGame()
            while self.running:
                self.update()
    
    
    def showEntities(self):
        self.pacman.visible = True
        self.ghosts.show()
        self.pellets.show()

    def hideEntities(self):
        self.pacman.visible = False
        self.ghosts.hide()
        self.pellets.hide()
    pass