from config.sound import *
import pygame

class Music:
    def __init__(self):
        pygame.mixer.init()
        self.channel = pygame.mixer.Channel(0)
        self.sounds = {}
        self.addSound(SOUND_EATPELLET, "res/musics/eat_pellet.wav")
        self.addSound(SOUND_EATPOWERPELLET, "res/musics/eat_powerpellet.wav")
        self.addSound(SOUND_EATGHOST, "res/musics/eat_ghost.wav")
        self.addSound(SOUND_EATFRUIT, "res/musics/eat_fruit.wav")
        self.addSound(SOUND_PACMANDEATH, "res/musics/pacman_death.wav")
        self.addSound(SOUND_STARTGAME, "res/musics/start_game.wav")
        self.addSound(SOUND_INTERMISSION, "res/musics/intermission.wav")
        self.addSound(SOUND_GHOSTFREIGHT, "res/musics/freight.wav")
        self.addSound(SOUND_MENU, "res/musics/menu.wav")

    def play(self, sound_id: int):
        """Phát âm thanh theo ID"""
        if sound_id in self.sounds:
            self.stop()
            self.channel.play(self.sounds[sound_id])

    def stop(self):
        """Dừng phát âm thanh hiện tại"""
        self.channel.stop()

    def addSound(self, id, path):
        """"""
        self.sounds[id] = pygame.mixer.Sound(path)

    def get_busy(self):
        return self.channel.get_busy()
