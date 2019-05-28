import pygame
#import random
import Tree_class

pygame.init()

height = 750
width = 750
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Oakwald Escapade')

small = pygame.font.SysFont("TimesNewRoman", 25)
big = pygame.font.SysFont("TimesNewRoman", 50)

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen.fill(WHITE)
pygame.display.flip()

#this is map 0 is nothing 1 is wall
map1 = [
    '111110000011111',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '111111111111111',
]
map2 = [
    '111110000011111',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '111110000011111',
]
map3 = [
    '111110000011111',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '000000000000001',
    '000000000000001',
    '000000000000001',
    '000000000000001',
    '000000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '111110000011111',
]
map4 = [
    '111110000011111',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '000000000000000',
    '000000000000000',
    '000000000000000',
    '000000000000000',
    '000000000000000',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '100000000000001',
    '111110000011111',
]
Trees = []



#for row in #will add:
   # for col in row:
      # if col is == '1':
         #  Tree((x,y)) # tree needs to be made



level = [map1, map2, map3, map4]


def sentence(font, word, color, x, y):
    text = font.render(word, True, color)
    screen.blit(text, (x, y))
    pygame.display.update()


sentence(big, "Hello", RED, 500, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
