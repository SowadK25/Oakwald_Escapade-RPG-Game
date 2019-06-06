import pygame  # imports
import random
from Player_class import Player
from Shooting_class import Shoot
from Enemy_class import Enemy
from Floor_class import Floor

pygame.init()

# Dimensions of the screen
height = 675
width = 675

# Player score and lives variables
score = 0
hp = 100


screen = pygame.display.set_mode((height, width))  # screen display size
screen_rect = screen.get_rect()
pygame.display.set_caption('Oakwald Escapade')  # screen caption

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
GREY = (104, 109, 105)
YELLOW = (252, 252, 25)
ORANGE = (242, 141, 19)

enemy_speeds = [-2, -1, 1, 2]

clock = pygame.time.Clock()  # clock


# for sentences

def sentence(font, word, color, x, y):
    """Sentence making function"""
    text = font.render(word, True, color)
    screen.blit(text, (x, y))
    pygame.display.update()


#def sound_effects(sound):
    """Plays sound effects requested"""
   # noise = pygame.mixer.Sound(sound)
    #noise.play(0)


def scoreboard(statement, value, x, y1, y2, color):
    """Contains the scoreboard for the player"""
    box = small.render(statement + str(value), True, color)  # Rendering font for the scoreboard
    screen.fill(GREY, rect=box.get_rect(bottomleft=(x, y1)))  # Filling the background of the scoreboard with grey
    screen.blit(box, (x, y2))  # Putting the scoreboard in the bottom corner of the screen
    pygame.display.update()  # Updating the screen


def win_function():
    """Will be called when the player wins"""
    pass


# sizes for sentences
small = pygame.font.SysFont("TimesNewRoman", 35)
big = pygame.font.SysFont("TimesNewRoman", 50)

# Max and min speeds of player
max_s = 10
min_s = -5

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

# Creating sprite groups
all_sprites_list = pygame.sprite.Group()
shooting_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

# Instance variables
player = Player()

all_sprites_list.add(player)


def game():

    global score
    global hp
    for i in range(20):  # 20 enemies will spawn
        enemy = Enemy()
        enemy.rect.x = random.randrange(width)  # Enemies will randomly spawn within the screen
        enemy.rect.y = random.randrange(height)

        enemy.speed_x = random.choice(enemy_speeds)  # Enemies will have a speed within these values
        enemy.speed_y = random.choice(enemy_speeds)

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

    while close:  # While the game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit pygame if event is quit
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
                    #sound_effects("Shooting.wav")  # Sound effects function called

                    # Adding shooting to both sprite lists
                    all_sprites_list.add(shoot)
                    shooting_list.add(shoot)

            if event.type == pygame.KEYUP:  # When the key is released
                if event.key == pygame.K_ESCAPE:  # Press escape to quit
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

        kills = pygame.sprite.groupcollide(enemy_list, shooting_list, True, True)  # Checking for enemy hit by shooting

        for hit in kills:
            enemy = Enemy()
            score += 1  # Add 1 to score each time enemy is shot

            # Remove enemies from sprite lists
            all_sprites_list.remove(enemy)
            enemy_list.remove(enemy)
            enemy.kill()  # Enemy taken off the screen

        die = pygame.sprite.spritecollide(player, enemy_list, False)  # Check if player is hit by an enemy
        if die:  # If they player is hit
            hp -= 1  # Subtract 1 from their lives
            if hp <= 0:
                hp = 0

        screen.fill(WHITE)
        for row in range(15):
            for column in range(15):
                screen.blit(image_library[map1[row][column]], (column * size_of_tile, row * size_of_tile))
        all_sprites_list.update()  # Updating the all sprites list
        all_sprites_list.draw(screen)  # Drawing all sprites created on the screen

        # Scoreboard function called to show player lives and current score
        scoreboard("Score: ", score, 50, 625, 600, WHITE)

        if hp <= 100:
            scoreboard("HP: ", hp, 550, 625, 600, GREEN)
        elif hp <= 75:
            scoreboard("HP: ", hp, 550, 625, 600, ORANGE)
        if hp <= 50:
            scoreboard("HP: ", hp, 550, 625, 600, YELLOW)
        if hp <= 25:
            scoreboard("HP: ", hp, 550, 625, 600, RED)

        if hp == 0:
           myfont=big  
           textsurface= myfont.render('YOU LOSE' , False, RED)
           screen.blit(textsurface, (75,300))
           pygame.display.update()
           

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


game()
