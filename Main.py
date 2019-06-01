import pygame  # imports
# import random
# from Tree_class import Tree # imports of classes
# from Floor_class import Floor


pygame.init()

# Dimensions of the screen
height = 675
width = 675


screen = pygame.display.set_mode((height, width))  # screen display size
pygame.display.set_caption('Oakwald Escapade')  # screen caption

# colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# clock

clock = pygame.time.Clock()


# for sentences

def sentence(font, word, color, x, y):
    text = font.render(word, True, color)
    screen.blit(text, (x, y))
    pygame.display.update()


# sizes for sentences
small = pygame.font.SysFont("TimesNewRoman", 25)
big = pygame.font.SysFont("TimesNewRoman", 50)

# x and y directions for map
Tree_x = 0
Tree_y = 0
Floor_x = 0
Floor_y = 0
# For main loop
screen.fill(WHITE)

close = True

# for the map
floor = 0
tree = 1
image_library = {
    tree: pygame.transform.scale(pygame.image.load('tree.png'), [45, 45]),
    floor: pygame.transform.scale(pygame.image.load('floor.png'), [45, 45])
}

map1 = [

    [tree, tree, tree, tree, tree, floor, floor, floor, floor, floor, tree, tree, tree, tree, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree],
    [tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree],
]
map2 = [

    [tree, tree, tree, tree, tree, floor, floor, floor, floor, floor, tree, tree, tree, tree, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, tree, tree, tree, tree, floor, floor, floor, floor, floor, tree, tree, tree, tree, tree, ],
]
map3 = [

    [tree, tree, tree, tree, tree, floor, floor, floor, floor, floor, tree, tree, tree, tree, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, tree, tree, tree, tree, floor, floor, floor, floor, floor, tree, tree, tree, tree, tree, ],
]
map4 = [

    [tree, tree, tree, tree, tree, floor, floor, floor, floor, floor, tree, tree, tree, tree, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, ],
    [floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, floor, tree, ],
    [tree, tree, tree, tree, tree, floor, floor, floor, floor, floor, tree, tree, tree, tree, tree, ],
]
size_of_tile = 45

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

print(map1)
while close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    for row in range(15):
        for column in range(15):
            screen.blit(image_library[map1[row][column]], (column * size_of_tile, row * size_of_tile))
    pygame.display.update()
    clock.tick(60)
