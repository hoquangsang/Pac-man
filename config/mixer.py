import pygame

pygame.mixer.init()

# Đặt các âm thanh trong game
chomp = pygame.mixer.Sound("res/musics/chomp.wav")
death = pygame.mixer.Sound("res/musics/death.wav")
start = pygame.mixer.Sound("res/musics/start.wav")