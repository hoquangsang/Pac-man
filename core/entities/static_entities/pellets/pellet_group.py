from .pellet import Pellet
from .powerpellet import PowerPellet
import numpy as np

class PelletGroup(object):
    def __init__(self, pelletfile):
        self.pelletList: list[Pellet] = []
        self.powerpellets: list[PowerPellet] = []
        self.createPelletList(pelletfile)
        self.numEaten = 0

    def update(self, dt):
        for powerpellet in self.powerpellets:
            # if powerpellet.active:
                powerpellet.update(dt)
                
    def createPelletList(self, pelletfile):
        data = self.readPelletfile(pelletfile)        
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                if data[row][col] in ['.', '+']:
                    self.pelletList.append(Pellet(row, col))
                elif data[row][col] in ['P', 'p']:
                    pp = PowerPellet(row, col)
                    self.pelletList.append(pp)
                    self.powerpellets.append(pp)
                    
    def readPelletfile(self, textfile):
        return np.loadtxt(textfile, dtype='<U1')
    
    def isEmpty(self):
        return self.numEaten == len(self.pelletList)
    
    def render(self, screen):
        for pellet in self.pelletList:
            pellet.render(screen)

    def reset(self):
        for pellet in self.pelletList:
            pellet.reset()

    # def enable(self):
    #     for pellet in self.pelletList:
    #         pellet.enable()
    
    # def disable(self):
    #     for pellet in self.pelletList:
    #         pellet.disable()

    def show(self):
        for pellet in self.pelletList:
            pellet.show()
    
    def hide(self):
        for pellet in self.pelletList:
            pellet.hide()