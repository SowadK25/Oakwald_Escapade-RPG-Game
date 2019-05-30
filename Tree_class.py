import pygame

Trees = []

class Tree(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()

        Trees.append(self)
        self.rect = pygame.Rect(position[0], position[1], 50, 50)
        
        
'''import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

pygame.init()

height = 750
width = 750

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Oakwald Escapade")

small = pygame.font.SysFont("TimesNewRoman", 25)
big = pygame.font.SysFont("TimesNewRoman", 50)

screen.fill(WHITE)
pygame.display.flip()


def sentence(font, word, color, x, y):
    text = font.render(word, True, color)
    screen.blit(text, (x, y))
    pygame.display.update()


sentence(big, "Hello", RED, 500, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False'''
