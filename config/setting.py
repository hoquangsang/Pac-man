# Cấu hình màn hình và tile
TILESIZE = 16
NROWS = 36
NCOLS = 28
SCREENWIDTH = TILESIZE * NCOLS
SCREENHEIGHT = TILESIZE * NROWS
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
COLOR_DEPTH = 32
NODESIZE = 12
PATHSIZE = 4

# Định nghĩa hướng
STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2
PORTAL = 3

# Định nghĩa thực thể game
PACMAN = 0
PELLET = 1
POWERPELLET = 2
GHOST = 3
BLINKY = 4
PINKY = 5
INKY = 6
CLYDE = 7
FRUIT = 8

# Ghost mode
SCATTER = 0     # các bóng ma phân tán đến một trong bốn góc của mê cung
CHASE = 1       # lấy vị trí của Pacman làm mục tiêu
FREIGHT = 2     # khi Pacman ăn Power Pellet, các bóng ma di chuyển ngẫu nhiên và chậm hơn trong mê cung
SPAWN = 3       # sau khi Pacman ăn

# Option
MODE_BLUE_GHOST = 1
MODE_PINK_GHOST = 2
MODE_ORANGE_GHOST = 3
MODE_RED_GHOST = 4
MODE_ALL_GHOST = 5
MODE_PLAY = 6