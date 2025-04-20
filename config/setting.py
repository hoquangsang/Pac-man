# Cấu hình màn hình và tile
FPS = 30

TILESIZE = 16
NROWS = 36
NCOLS = 28
SCREENWIDTH = TILESIZE * NCOLS
SCREENHEIGHT = TILESIZE * NROWS
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
COLOR_DEPTH = 32
NODESIZE = 6#12
PATHSIZE = 3#4

# Định nghĩa hướng
STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2
PORTAL = 3
DEATH = 5

# Định nghĩa thực thể game
PACMAN = 0
PELLET = 1
POWERPELLET = 2
GHOST = 3
CLYDE = 4
INKY = 5
PINKY = 6
BLINKY = 7
FRUIT = 8

# Ghost mode
SCATTER = 0     # các bóng ma phân tán đến một trong bốn góc của mê cung
SCATTER = 1     # Thực tế là vậy, nhưng game chúng ta không cần tới chế độ này. Nếu muốn, chỉ cần đổi lại thành 0 là được
CHASE = 1       # lấy vị trí của Pacman làm mục tiêu
FREIGHT = 2     # khi Pacman ăn Power Pellet, các bóng ma di chuyển ngẫu nhiên và chậm hơn trong mê cung
SPAWN = 3       # sau khi Pacman ăn

# Option
MODEINKY = 0
MODEPINKY = 1
MODECLYDE = 2
MODEBLINKY = 3
MODEALL = 4
MODEPLAY = 5

# 
SCORETXT = 0
TIMERTXT = 1
READYTXT = 2
PAUSETXT = 3
GAMEOVERTXT = 4
MEMORYTXT = 5
EXPANDEDTXT = 6
