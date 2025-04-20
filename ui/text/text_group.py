import pygame
from utils.math.vector import Vector2
from config import *
from .text import Text

class TextGroup(object):
    def __init__(self):
        self.nextid = 10
        self.alltext = {}
        self.setupText()
        self.showNotify(READYTXT)

    def addText(self, text, color, x, y, size, time=None, id=None):
        self.nextid += 1
        self.alltext[self.nextid] = Text(text, color, x, y, size, time=time, id=id)
        return self.nextid

    def removeText(self, id):
        self.alltext.pop(id)
        
    def setupText(self):
        size = TILESIZE
        self.alltext[READYTXT]      = Text("READY!", YELLOW, 11.25*TILESIZE, 20*TILESIZE, size, visible=False)
        self.alltext[PAUSETXT]      = Text("PAUSED!", YELLOW, 10.625*TILESIZE, 20*TILESIZE, size, visible=False)
        self.alltext[GAMEOVERTXT]   = Text("GAMEOVER!", YELLOW, 10*TILESIZE, 20*TILESIZE, size, visible=False)

        self.alltext[SCORETXT]      = Text("0".zfill(8), WHITE, 0, 1.1*TILESIZE, size)
        self.alltext[MEMORYTXT]     = Text("0MB".zfill(8), WHITE, 0, 1.1*TILESIZE, size)
        self.alltext[TIMERTXT]      = Text("00:00".zfill(5), WHITE, 21*TILESIZE, 1.1*TILESIZE, size)
        self.alltext[EXPANDEDTXT]   = Text("0".zfill(3), WHITE, 12.5*TILESIZE, 34.75*TILESIZE, size)

    def update(self, dt):
        for tkey in list(self.alltext.keys()):
            self.alltext[tkey].update(dt)
            if self.alltext[tkey].destroy:
                self.removeText(tkey)

    def updateText(self, id, value):
        if id in self.alltext.keys():
            self.alltext[id].setText(value)

    def updateScore(self, score):
        self.updateText(SCORETXT, str(score).zfill(8))
    
    def updateTime(self, seconds: float):
        # seconds = miliseconds // 1000
        minutes = int(seconds) // 60
        secs = int(seconds) % 60
        millis = int((seconds - int(seconds)) * 100)
        formatted_time = f"{minutes}:{secs:02}.{millis:02}"
        self.updateText(TIMERTXT, formatted_time)

    def updateExpands(self, value):
        self.updateText(EXPANDEDTXT, str(value).zfill(3))

    def updatePeekMem(self, value):
        format_mem = f"{str(int(value)).zfill(6)}MB"
        self.updateText(MEMORYTXT, format_mem)

    def render(self, screen):
        for tkey in list(self.alltext.keys()):
            self.alltext[tkey].render(screen)

    def showText(self, id):
        self.alltext[id].visible = True

    def hideText(self, id):
        self.alltext[id].visible = False

    def hideAllText(self):
        self.alltext[READYTXT].visible = False
        self.alltext[PAUSETXT].visible = False
        self.alltext[GAMEOVERTXT].visible = False
    
    def showNotify(self, id):
        self.hideAllText()
        self.alltext[id].visible = True
