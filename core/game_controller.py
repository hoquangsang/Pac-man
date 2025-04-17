from config import *
import pygame
from pygame.locals import *
import sys
import os
from core.mazes.maze import Maze, MazeNode
from .entities.pacmans.pacman import Pacman
from .entities.ghosts.ghost import Ghost
from .entities.ghosts.ghost_group import GhostGroup
from .entities.ghosts.inky import Inky
from .entities.ghosts.pinky import Pinky
from .entities.ghosts.clyde import Clyde
from .entities.ghosts.blinky import Blinky
from .ui.sprites.maze_sprite import MazeSprites 
from .ui.pauser.pause import Pause

class GameController(object): 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pacman")
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, COLOR_DEPTH)
        self.clock = pygame.time.Clock()
        self.background = None
        self.ghosts = []
        self.pacman = None
        self.maze = None #Graph("res/mazes/maze1.txt")
        self.mode = MODE_PLAY-5# mode
        self.running = True
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
        self._config()
        self.pause = Pause(False)
        

    def update(self):
        dt = self.clock.tick(FPS) / 1000.0

        if not self.pause.paused:
            self.ghosts.update(dt)
            self.checkGhostEvents()

            self.pacman.update(dt)
        
        if not self.pacman.alive:
            self.pacman.sprites.update(dt)
        
        # if self.pacman.alive:

        afterPauseMethod = self.pause.update(dt)
        if afterPauseMethod is not None:
            afterPauseMethod()
            
        self.checkEvents()
        self.render()

    def render(self):
        self.screen.blit(self.background, (0, 0))

        self.ghosts.render(self.screen)
        self.pacman.render(self.screen)
        self.maze.render(self.screen)
        pygame.display.update()


    def startGame(self):
        self.running = True
        self.setBackground()
        self.mazesprites = MazeSprites("res/mazes/maze1.txt","res/mazes/maze1_rotation.txt")
        self.background = self.mazesprites.constructBackground(self.background, self.level%5)

        self.pacman.reset()
        self.setMode()

    def endGame(self):
        self.running = False
        self.pacman.die()
        # self.pause.paused = True
    # def resetLevel(self):
    #     self.pause.paused = True
    #     # self.pacman.reset()
    #     # self.ghosts.reset()
    #     self.fruit = None
    #     self.setMode()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)
    
    #####
    def _config(self):
        self.maze = Maze("res/mazes/maze1.txt")
        self.maze.setPortalPair((0,17), (27,17))
        homekey = self.maze.createHomeNodes(11.5, 14)
        self.maze.connectHomeNodes(homekey, (12,14), LEFT)
        self.maze.connectHomeNodes(homekey, (15,14), RIGHT)

        self.pacman = Pacman(self.maze.getNodeFromTiles(15, 26))
        self.ghosts = GhostGroup(self.maze.getStartTempNode(), self.pacman)
        self.ghosts.blinky.setStartNode(self.maze.getNodeFromTiles(2+11.5, 0+14))
        self.ghosts.pinky.setStartNode(self.maze.getNodeFromTiles(2+11.5, 3+14))
        self.ghosts.inky.setStartNode(self.maze.getNodeFromTiles(0+11.5, 3+14))
        self.ghosts.clyde.setStartNode(self.maze.getNodeFromTiles(4+11.5, 3+14))
        
        self.maze.denyHomeAccess(self.pacman)
        self.maze.denyHomeAccessList(self.ghosts)
        self.maze.denyAccessList(2+11.5, 3+14, LEFT, self.ghosts)
        self.maze.denyAccessList(2+11.5, 3+14, RIGHT, self.ghosts)
        # if self.mode == MODE_PLAY:
        # self.ghosts.inky.startNode.denyAccess(RIGHT, self.ghosts.inky)
        # self.ghosts.clyde.startNode.denyAccess(LEFT, self.ghosts.clyde)
        self.maze.denyAccessList(12, 14, UP, self.ghosts)
        self.maze.denyAccessList(15, 14, UP, self.ghosts)
        self.maze.denyAccessList(12, 26, UP, self.ghosts)
        self.maze.denyAccessList(15, 26, UP, self.ghosts)

    ##############
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                self.pause.paused = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.pacman.alive:
                        self.pause.setPause(playerPaused=True)
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.pause.paused = False


    def checkGhostEvents(self):
       for ghost in self.ghosts:
            if self.pacman.collideGhost(ghost):
                ghost.hide()
                if self.pacman.alive:
                    self.pause.setPause(pauseTime=3, func=self.endGame())
                    self.running = False
    
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
        if self.mode is MODE_BLUE_GHOST:
            self.ghosts.hide()
            self.ghosts.inky.reset()
            self.pacman.disableMovement()
        elif self.mode is MODE_PINK_GHOST:
            self.ghosts.hide()
            self.ghosts.pinky.reset()
            self.pacman.disableMovement()
        elif self.mode is MODE_ORANGE_GHOST:
            self.ghosts.hide()
            self.ghosts.clyde.reset()
            self.pacman.disableMovement()
        elif self.mode is MODE_RED_GHOST:
            self.ghosts.hide()
            self.ghosts.blinky.reset()
            self.pacman.disableMovement()
        elif self.mode is MODE_ALL_GHOST:
            self.ghosts.reset()
            self.pacman.disableMovement()
        else:
            self.ghosts.reset()
            self.pacman.enableMovement()
            # self.ghosts.inky.startNode.denyAccess(RIGHT, self.ghosts.inky)
            # self.ghosts.clyde.startNode.denyAccess(LEFT, self.ghosts.clyde)
    
    def run(self):
        while True:
            self.showMenu()
            # self.setMode()
            self.startGame()
            while self.running or self.pause.paused:
                self.update()
    
    # def showEntities(self):
    #     self.pacman.show()
    #     self.ghosts.show()

    # def hideEntities(self):
    #     self.pacman.hide()
    #     self.ghosts.hide()
    pass