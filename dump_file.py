import pygame
import random
from Tree_class import Tree
from Floor_class import Floor

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
clock = pygame.time.Clock()

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

# ignore this for now



def objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


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

    TextSurf, TextRect = objects("WORKING" , big)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(TextSurf, TextRect)


# random number between 5 for spawning

list_of_numbers = [1, 2, 3, 4, 5]
spawn_location = []
spawn_location.append(random.choice(list_of_numbers))


# for spawn location number between 5
"""while close:
    for a in range(5):
        if foo == 1:
            one = random.choice(list_of_number)"""



    button(100,100,20,20,GREEN,BROWN,None)
    pygame.display.flip()
