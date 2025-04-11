from config import *
import pygame

class MainGame(object): 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pacman")
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, COLOR_DEPTH)
        self.clock = pygame.time.Clock()
        self.background = None
        self.ghosts = []
        self.pacman = None
        self.nodes = []
        self.mode = 1

    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.render()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()

    def startGame(self):
        self.setBackground()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def setMode(self, option):
        self.mode = option

    def run(self):
        self.startGame()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Quay lại menu
            self.update()
