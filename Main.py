import pygame
import random
from Tree_class import Tree
from Floor_class import Floor
pygame.init()
# foo = 1
height = 750
width = 750
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Oakwald Escapade')
# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# function for the word

def sentence(font, word, color, x, y):
    text = font.render(word, True, color)
    screen.blit(text, (x, y))
    pygame.display.update()

small = pygame.font.SysFont("TimesNewRoman", 25)
big = pygame.font.SysFont("TimesNewRoman", 50)


# for the maps
Tree_x = 0
Tree_y = 0
Floor_x = 0
Floor_y = 0

# for button function
def button (text,x,y,w,h,active,inactive,action = None):
    position = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()

    if x+w > position[0] > x and y+h > position[1] > y:
        pygame.draw.rect(screen, active, (x,y,w,h))

        if clicked[0] == 1 and action != None:
            print('working') # what the button is going to do
    else:
        pygame.draw.rect(screen, inactive,(x,y,w,h))

    TextSurf, TextRect = text_objects(text, small)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(TextSurf, TextRect)
# For main loop
close = True

# random number between 5 for spawning

list_of_numbers = [1, 2, 3, 4, 5]
spawn_location = []
spawn_location.append(random.choice(list_of_numbers))


# for spawn location number between 5
"""while close:
    for a in range(5):
        if foo == 1:
            one = random.choice(list_of_number)"""


# this is map 0 is nothing 1 is wall
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
lvl_type = 2
clear = []  # used for clearing the list
final_level = []  # final list for map
while close:
    if lvl_type == 1:
        final_level.append(clear)
        final_level.append(map1)
    if lvl_type == 2:
        final_level.append(clear)
        final_level.append(map2)
    if lvl_type == 3:
        final_level.append(clear)
        final_level.append(map3)
    if lvl_type == 4:
        final_level.append(clear)
        final_level.append(map4)
    else:
        break



for row in final_level:
    for col in row:
        if col == '1':
            Tree((Tree_x, Tree_y))
        if col == '0':
            Floor((Floor_x, Floor_y))
    Tree_y += 50
    Tree_x = 0

while close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    button(100,100,20,20,WHITE,BLACK,print('wokring'))
    pygame.display.flip()
