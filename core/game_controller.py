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

    def update(self):
        dt = self.clock.tick(FPS) / 1000.0
        if self.mode == MODE_PLAY:
            self.pacman.update(dt)
        # self.ghost.update(dt)
        self.ghost.update(dt)
        self.pellets.update(dt)
        self.checkPelletEvents()
        self.checkGhostEvents()
        self.checkEvents()
        self.render()
        # if self.ghost.directionMethod == self.ghost.randomDirection: print("random", end=",")
        # elif self.ghost.directionMethod == self.ghost.goalDirection: print("goal", end=",")
        # print(f"{self.ghost.goal}, {self.pacman.position}", end=",")
        # if self.ghost.mode.current == CHASE: print("CHASE")
        # elif self.ghost.mode.current == SCATTER: print("SCATTER")
        # else: print(self.ghost.mode.current)

    def render(self):
        self.screen.blit(self.background, (0, 0))
        # self.nodes.render(self.screen)
        self.pellets.render(self.screen)
        # self.ghost.render(self.screen)
        self.ghost.render(self.screen)
        self.pacman.render(self.screen)
        pygame.display.update()

    def startGame(self):
        self.setBackground()
        self.mazesprites = MazeSprites("res/mazes/maze1.txt","res/mazes/maze1_rotation.txt")
        self.background = self.mazesprites.constructBackground(self.background, self.level%5)
        self.nodes = Graph("res/mazes/maze1.txt")
        self.nodes.setPortalPair((0,17), (27,17))

        homekey = self.nodes.createHomeNodes(11.5, 14)
        self.nodes.connectHomeNodes(homekey, (12,14), LEFT)
        self.nodes.connectHomeNodes(homekey, (15,14), RIGHT)

        # self.pacman = Pacman(self.nodes.getStartTempNode())
        self.pacman = Pacman(self.nodes.getNodeFromTiles(15, 26))
        self.pellets = PelletGroup("res/mazes/maze1.txt")
        
        # self.ghost = Blinky(self.nodes.getStartTempNode(),self.pacman)
        self.setMode()
        # self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)
        # self.ghosts.blinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 0+14))
        # self.ghosts.pinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))
        # self.ghosts.inky.setStartNode(self.nodes.getNodeFromTiles(0+11.5, 3+14))
        # self.ghosts.clyde.setStartNode(self.nodes.getNodeFromTiles(4+11.5, 3+14))
        
        # self.ghost.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 0+14))
        self.ghost.setSpawnNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))
        # self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)
    
    def restartGame(self):
        self.lives = 5
        self.level = 0
        # self.pause.paused = True
        self.fruit = None
        self.running = True
        self.startGame()

    def resetLevel(self):
        self.pause.paused = True
        self.pacman.reset()
        self.ghost.reset()
        self.fruit = None

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
            if pellet.name == POWERPELLET:
                self.ghost.startFreight()

    def checkGhostEvents(self):
    #    # for ghost in self.ghosts:
            if self.pacman.collideGhost(self.ghost):
            # if self.pacman.collideGhost(ghost):
                if self.ghost.mode.current is FREIGHT:
    #             if ghost.mode.current is FREIGHT:
                    self.ghost.startSpawn()
    #                 ghosts.startSpawn()
    #             elif ghost.mode.current is not SPAWN:
    #                  if self.pacman.alive:
    #                      self.lives -=  1
    #                      self.pacman.die()
    #                      self.ghosts.hide()
    #                      if self.lives <= 0:
    #                          self.pause.setPause(pauseTime=3, func=self.restartGame)
    #                      else:
    #                          self.pause.setPause(pauseTime=3, func=self.resetLevel)
    
    def showMenu(self):
        bg_path = os.path.join("res", "images", "menu_bg.jpg")
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
            self.ghost = Inky(self.nodes.getStartTempNode(),self.pacman)
        elif self.mode == MODE_PINK_GHOST:
            self.ghost = Pinky(self.nodes.getStartTempNode(),self.pacman)
        elif self.mode == MODE_ORANGE_GHOST:
            self.ghost = Clyde(self.nodes.getStartTempNode(),self.pacman)
        elif self.mode == MODE_RED_GHOST:
            self.ghost = Blinky(self.nodes.getStartTempNode(),self.pacman)
        elif self.mode == MODE_ALL_GHOST:
            self.ghost = Inky(self.nodes.getStartTempNode(),self.pacman)
        elif self.mode == MODE_PLAY:
            self.ghost = Inky(self.nodes.getStartTempNode(),self.pacman)
    
    def run(self):
        while True:
            self.showMenu()
            # self.setMode()
            self.restartGame()
            while self.running:
                self.update()
    pass