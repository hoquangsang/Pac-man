from config import *
import pygame
from pygame.locals import *
import sys
import os
from mazes.maze import Maze, MazeNode
from mazes.graph import MazeGraph
from entities.pacmans.pacman import Pacman
from entities.ghosts.ghost import Ghost
from entities.ghosts.ghost_group import GhostGroup
from entities.ghosts.inky import Inky
from entities.ghosts.pinky import Pinky
from entities.ghosts.clyde import Clyde
from entities.ghosts.blinky import Blinky
from ui.sprites.maze_sprite import MazeSprites 
from ui.pauser.pause import Pause
from ui.text.text import Text
from ui.text.text_group import TextGroup

class GameController(object): 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pacman")
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, COLOR_DEPTH)
        self.clock = pygame.time.Clock()
        self.background = None
        self.ghosts: GhostGroup
        self.pacman = None
        self.maze = None #Graph("res/mazes/maze1.txt")
        self.mode = MODEPLAY-5# mode
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
        self.pause = Pause(True)
        self.score = 0
        self.timer = 0.0
        self.textgroup = TextGroup()
        # self.searchTree: MazeGraph = None

    def update(self):
        dt = self.clock.tick(FPS) / 1000.0
        self.textgroup.update(dt)

        if not self.pause.paused:
            self.pacman.update(dt)
            self.ghosts.update(dt)
            self.checkGhostEvents()
            self.timer += dt
            self.textgroup.updateTime(self.timer)
        
        if not self.pacman.alive:
            self.pacman.sprites.update(dt)
        
        afterPauseMethod = self.pause.update(dt)
        if afterPauseMethod is not None:
            afterPauseMethod()
            
        self.checkEvents()
        self.render()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.ghosts.render(self.screen)
        self.pacman.render(self.screen)

        if self.mode < MODEALL:
            self.maze.render(self.screen)
            if self.searchTree:
                self.searchTree.render(self.screen)
                self.textgroup.updateExpands(self.searchTree.numExpandNode)
                self.textgroup.updatePeekMem(self.searchTree.peekMem)

        self.textgroup.render(self.screen)
        pygame.display.update()

    def startLevel(self):
        self.running = True
        self.pause.paused = True
        self.setBackground()
        self.mazesprites = MazeSprites("res/mazes/maze1.txt","res/mazes/maze1_rotation.txt")
        self.background = self.mazesprites.constructBackground(self.background, self.level%5)

        self.score = 0
        self.textgroup.updateScore(self.score)
        self.textgroup.showNotify(READYTXT)
        self.timer = 0
        self.textgroup.updateTime(self.timer)

        self.setMode()

    def endGame(self):
        self.running = False
        pass

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)
    
    #####
    def _startgame(self):
        self.maze = Maze("res/mazes/maze1.txt")
        self.maze.setPortalPair((0,17), (27,17))
        homekey = self.maze.createHomeNodes(11.5, 14)
        self.maze.connectHomeNodes(homekey, (12,14), LEFT)
        self.maze.connectHomeNodes(homekey, (15,14), RIGHT)

        # self.pacman = Pacman(self.maze.getNodeFromTiles(26, 32))
        self.pacman = Pacman(self.maze.getNodeFromTiles(15, 26))
        self.ghosts = GhostGroup(self.maze.getStartTempNode(), self.pacman)
        self.ghosts.blinky.setStartNode(self.maze.getNodeFromTiles(2+11.5, 0+14))
        self.ghosts.pinky.setStartNode(self.maze.getNodeFromTiles(2+11.5, 3+14))
        self.ghosts.inky.setStartNode(self.maze.getNodeFromTiles(0+11.5, 3+14))
        self.ghosts.clyde.setStartNode(self.maze.getNodeFromTiles(4+11.5, 3+14))
        
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                self.pause.paused = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.pacman.alive:
                        # self.pacman.moveable = not self.pacman.moveable
                        self.pause.setPause(playerPaused=True)
                        if not self.pause.paused:
                            self.textgroup.hideAllText()
                        else: 
                            self.textgroup.showNotify(PAUSETXT)
                elif event.key == pygame.K_ESCAPE:
                    if not self.pause.paused and self.pacman.alive:
                        self.running = False
                        # self.pause.setPause(pauseTime=1,playerPaused=True, func=self.endGame)

    def checkGhostEvents(self):
       for ghost in self.ghosts:
            if self.pacman.collideGhost(ghost):
                ghost.hide()
                if self.pacman.alive:
                    self.pacman.die()
                    self.textgroup.showNotify(GAMEOVERTXT)
                    self.pause.setPause(pauseTime=3, func=self.endGame)
    
    def updateScore(self, points):
        self.score += points
        self.textgroup.updateScore(self.score)

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
        self.pacman.reset()
        self.ghosts.reset()

        if self.mode == MODEPLAY:
            self.textgroup.showText(SCORETXT)
            self.textgroup.hideText(MEMORYTXT)
            self.textgroup.hideText(EXPANDEDTXT)
        elif self.mode == MODEALL:
            self.textgroup.hideText(SCORETXT)
            self.textgroup.hideText(MEMORYTXT)
            self.textgroup.hideText(EXPANDEDTXT)
            self.pacman.disableMovement()
        else:
            self.textgroup.hideText(SCORETXT)
            self.textgroup.showText(MEMORYTXT)
            self.textgroup.showText(EXPANDEDTXT)
            self.pacman.disableMovement()
            self.ghosts.hide()
            if self.mode == MODEINKY:
                ghost = self.ghosts.inky
            elif self.mode == MODEPINKY:
                ghost = self.ghosts.pinky
            elif self.mode == MODECLYDE:
                ghost = self.ghosts.clyde
            elif self.mode == MODEBLINKY:
                ghost = self.ghosts.blinky

            if ghost:
                ghost.reset()

        self.ghosts.recontructPath()

        if self.mode < MODEALL:
            if ghost:
                self.searchTree = ghost.searchTree
            else: 
                self.searchTree = None

    def run(self):
        self._startgame()
        while True:
            self.showMenu()
            # self.setMode()
            self.startLevel()
                
            while self.running:
                self.update()

