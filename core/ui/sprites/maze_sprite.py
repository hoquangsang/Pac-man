from .spritesheet import Spritesheet
from config import *
import numpy as np

class MazeSprites(Spritesheet):
    def __init__(self, mazefile="res/mazes/maze1.txt", rotfile="res/mazes/maze1_rotation.txt"):
        Spritesheet.__init__(self)
        self.data = self.readMazeFile(mazefile)
        self.rotdata = self.readMazeFile(rotfile)

    def getImage(self, x, y):
        return Spritesheet.getImage(self, x, y, TILESIZE, TILESIZE)

    def readMazeFile(self, mazefile):
        return np.loadtxt(mazefile, dtype='<U1')

    def constructBackground(self, background, y):
        for row in list(range(self.data.shape[0])):
            for col in list(range(self.data.shape[1])):
                if self.data[row][col].isdigit():
                    x = int(self.data[row][col]) + 12
                    sprite = self.getImage(x, y)
                    rotval = int(self.rotdata[row][col])
                    sprite = self.rotate(sprite, rotval)
                    background.blit(sprite, (col*TILESIZE, row*TILESIZE))
                elif self.data[row][col] == '=':
                    sprite = self.getImage(10, 8)
                    background.blit(sprite, (col*TILESIZE, row*TILESIZE))

        return background
    
    def rotate(self, sprite, value):
       return pygame.transform.rotate(sprite, value*90)

