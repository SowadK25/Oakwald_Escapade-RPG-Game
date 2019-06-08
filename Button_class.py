import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREEN = (29, 173, 10)
LIGHT_GREEN = (57, 229, 34)
small = pygame.font.SysFont("TimesNewRoman", 25)

height = 675
width = 675

screen = pygame.display.set_mode((height, width))  # screen display size
screen_rect = screen.get_rect()


class Button:
    def __init__(self, text, pos, action, color1, color2, size=(125, 40)):
        super().__init__()

        self.color = color1
        self.color1 = color1
        self.color2 = color2
        self.size = size
        self.text = text
        self.font = pygame.font.SysFont("TimesNewRoman", 25)
        self.textbox = self.font.render(self.text, 3, self.color2)
        self.textrect = self.textbox.get_rect(center=[i/2 for i in self.size])
        self.surface = pygame.surface.Surface(self.size)
        self.rect = self.surface.get_rect(center=pos)
        self.call = action

    def draw(self):
        self.mouse_hit()
        self.surface.fill(self.color1)
        self.surface.blit(self.textbox, self.textrect)
        screen.blit(self.surface, self.rect)

    def mouse_hit(self):
        self.color1 = self.color
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            self.color1 = LIGHT_GREEN

    def call(self):
        self.call()
