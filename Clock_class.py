import pygame

height = 675
width = 675

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (29, 173, 10)
LIGHT_GREEN = (57, 229, 34)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
GREY = (104, 109, 105)
YELLOW = (252, 252, 25)
ORANGE = (242, 141, 19)

screen = pygame.display.set_mode((height, width))  # screen display size
screen_rect = screen.get_rect()

small = pygame.font.SysFont("TimesNewRoman", 25)
big = pygame.font.SysFont("TimesNewRoman", 50)


class Clock:
    def __init__(self, message, color, x, y, clock=None):
        super().__init__()

        self.clock = clock
        self.color = color
        self.x = x
        self.y = y
        self.time = pygame.time.get_ticks()
        self.message = message

    def draw(self):
        self.time = pygame.time.get_ticks()
        screen.blit(small.render(self.message, True, WHITE), (self.x, self.y))

