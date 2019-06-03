import pygame  # imports
import random

# Class imports
from Player_class import Player
from Shooting_class import Shoot
from Enemy_class import Enemy
# from Tree_class import Tree
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

# For main loop
screen.fill(WHITE)

# Max and min speeds of player
max_s = 10
min_s = -5

close = True

# for the map
floor = 0
tree = 1


class LoadImage:
    def __init__(self, image, name):
        self.image = pygame.transform.scale(pygame.image.load(image), [45, 45])
        self.rect = self.image.get_rect()
        self.name = name


image_library = {
    tree: LoadImage("tree.png", "tree"),
    floor: LoadImage('floor.png', "floor")
}
'''
image_library = {
    tree: pygame.transform.scale(pygame.image.load('tree.png'), [45, 45]),
    floor: pygame.transform.scale(pygame.image.load('floor.png'), [45, 45])
}
'''
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

all_sprites_list = pygame.sprite.Group()
shooting_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

player = Player()
enemy = Enemy()

all_sprites_list.add(player)


for i in range(20):  # 20 enemies will spawn
    enemy = Enemy()
    enemy.rect.x = random.randrange(width)  # Enemies will randomly spawn within the screen
    enemy.rect.y = random.randrange(height)

    enemy.speed_x = random.randrange(-2, 2)  # Enemies will have a speed within these values
    enemy.speed_y = random.randrange(-2, 2)

    # Boundaries set for the enemy on screen
    enemy.left = 0
    enemy.top = 0
    enemy.right = width
    enemy.bottom = height

    # Adding enemies to both sprite lists created
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

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

print(final_level)
while close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:  # If player hits a key
            # Player moves up if w is entered and bigger than minimum speed
            if event.key == pygame.K_w and player.speed > min_s:
                player.speed += 5
            # Player moves down if s is entered and speed is smaller than maximum
            if event.key == pygame.K_s and player.speed < max_s:
                player.speed -= 5
            # Player moves left if a is hit
            if event.key == pygame.K_a:
                player.angle_speed -= 3
            # Player moves right if d is hit
            if event.key == pygame.K_d:
                player.angle_speed += 3

            if event.key == pygame.K_SPACE:  # If player hits spacebar
                shoot = Shoot(player.rect.center, player.direction)  # Bullets start where player is at

                # Adding shooting to both sprite lists
                all_sprites_list.add(shoot)
                shooting_list.add(shoot)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            # Angle is reset back to 0 if let go for left and right movement
            if event.key == pygame.K_a:
                player.angle_speed = 0
            if event.key == pygame.K_d:
                player.angle_speed = 0
            if event.key == pygame.K_w:
                player.speed = 0
            if event.key == pygame.K_s:
                player.speed = 0
    screen.fill((255, 255, 255))
    for row in range(15):
        for column in range(15):
            screen.blit(image_library[map1[row][column]].image, (column * size_of_tile, row * size_of_tile))
    #all_sprites_list.clear(screen, )  # Clearing all sprites from the screen

    all_sprites_list.update()  # Updating the all sprites list
    all_sprites_list.draw(screen)  # Drawing all sprites created on the screen
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
