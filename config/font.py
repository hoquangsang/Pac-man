import pygame

pygame.font.init()
#
FONT_NAME = "Arial"

# Font tiêu đề
TITLE_FONT      = pygame.font.SysFont(FONT_NAME, 60, bold=True)
SUBTITLE_FONT   = pygame.font.SysFont(FONT_NAME, 36, bold=True)

# Font cho các option
OPTION_FONT     = pygame.font.SysFont(FONT_NAME, 24, bold=False)
OPTION_FONT_B   = pygame.font.SysFont(FONT_NAME, 24, bold=True)

# Font nhỏ hơn
SMALL_FONT      = pygame.font.SysFont(FONT_NAME, 20)
SMALL_FONT_B    = pygame.font.SysFont(FONT_NAME, 20, bold=True)

# Font lớn hơn
LARGE_FONT      = pygame.font.SysFont(FONT_NAME, 60, bold=True)
XL_FONT         = pygame.font.SysFont(FONT_NAME, 72, bold=True)

# Bạn có thể thêm các font khác nếu cần
# e.g., FONT_VERDANA = pygame.font.SysFont("Verdana", 30)
