import pygame

pygame.mixer.init()

# Đặt các âm thanh trong game


EATPELLETMIXER = pygame.mixer.Sound("res/musics/eat_pellet.wav")
EATPOWERPELLETMIXER = pygame.mixer.Sound("res/musics/eat_powerpellet.wav")
EATGHOSTMIXER = pygame.mixer.Sound("res/musics/eat_ghost.wav")
EATFRUITMIXER = pygame.mixer.Sound("res/musics/eat_fruit.wav")

PACMANDEATHMIXER = pygame.mixer.Sound("res/musics/pacman_death.wav")
# start = pygame.mixer.Sound("res/musics/start.wav")

BEGINMIXER = pygame.mixer.Sound("res/musics/begin.wav")

INTERMISSIONMIXER = pygame.mixer.Sound("res/musics/intermission.wav")

GHOSTFREIGHTMIXER = pygame.mixer.Sound("res/musics/freight.wav")

