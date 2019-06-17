# Group Members: Sowad Khan, Constantinos Boyatiz, Ciara Manle, Liban Nur, Maryam Rasheed
# ICS 3UI Final Summative Project
# Create a RPG Game: Oakwald Escapade
# All commits and modifications can be seen on Github
# Game finished on Monday, June 10th, 2019

# Notes:

# Game backgound music link: https://www.bensound.com
# Shooting sound effect link: https://youtu.be/FuvmTL1nPDs
# Home page background image link (just the background, not text or special affects): https://www.google.com/url?sa=i&
# source=images&cd=&ved=2ahUKEwjToPTPuN_iAhUIVN8KHa8ADwQQjRx6BAgBEAU&url=https%3A%2F%2Fwww.videoblocks.com%2Fvideo%2F
# magical-forest-background-loop-h0c0xdonfjg93mzlu&psig=AOvVaw1pFxs4M5CRTDucJsfOMWKH&ust=1560274237764799
# Enemy image link: https://www.google.com/search?q=pixelated+ghost&safe=strict&rlz=1C1CHBD_enCA775CA776&source=lnms&tbm=
# isch&sa=X&ved=0ahUKEwjkyLHvgOfiAhWIY98KHXqyDiUQ_AUIECgB&biw=1280&bih=864#imgdii=PpQXn2BsacYhoM:&imgrc=46WxeTcp2UG9tM:
# Player image link: https://www.google.com/imgres?imgurl=https%3A%2F%2Fopengameart.org%2Fsites%2Fdefault%2Ffiles%2F
# preview_idle.gif&imgrefurl=https%3A%2F%2Fopengameart.org%2Fcontent%2Fanimated-top-down-survivor-player&docid=GL07EFfbH
# j1rSM&tbnid=T5QI3yCr6dWPNM%3A&vet=10ahUKEwja38nUud_iAhUJPK0KHa9jBkIQMwhWKAEwAQ..i&w=253&h=216&safe=strict&bih=754&biw
# =1536&q=top%20view%20player%20&ved=0ahUKEwja38nUud_iAhUJPK0KHa9jBkIQMwhWKAEwAQ&iact=mrc&uact=8


# imports
import pygame
import random
import os
from Player_class import Player
from Shooting_class import Shoot
from Enemy_class import Enemy
from Button_class import Button
from Clock_class import Clock

# Computer screen size cords, will vary for different computers/PC's
cord1 = 675
cord2 = 50

os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % (cord1, cord2)  # Trying to center pygame window on screen
pygame.init()

# Dimensions of the screen
height = 675
width = 675

# Player score, wave number, and player HP variables
score_1 = 0
score_2 = 0
hp = 100
wave_number = 1


screen = pygame.display.set_mode((height, width))  # screen display size
screen_rect = screen.get_rect()
pygame.display.set_caption('Oakwald Escapade')  # screen caption

main_page = pygame.transform.scale(pygame.image.load("Images/homepage.png"), [675, 675])  # Main page for game
screen.blit(main_page, (0, 0))

# Background music for game (non copyright, link above)
pygame.mixer.music.load("Music/Battle_music.mp3")
pygame.mixer.music.play(-1)

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (29, 173, 10)
LIGHT_GREEN = (57, 229, 34)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
GREY = (104, 109, 105)
YELLOW = (252, 252, 25)
ORANGE = (242, 141, 19)

enemy_speeds = [-7, -5, -2, -1, 1, 2, 5, 7]  # Enemy speeds

clock = pygame.time.Clock()  # clock
# for instruction screen.


def instructions():
    """Loads instructions page"""
    instruction_picture = pygame.transform.scale(pygame.image.load('Images/instructions.png'), [675, 675])
    screen.blit(instruction_picture, (0, 0))


def map_screen():
    """Buttons for map will be loaded here"""
    maps = pygame.transform.scale(pygame.image.load("Images/homepage.png"), [675, 675])
    screen.blit(maps, (0, 0))


# for sentences
def sentence(font, word, color, x, y):
    """Sentence making function"""
    text = font.render(word, True, color)
    screen.blit(text, (x, y))
    pygame.display.update()


def sound_effects(sound):
    """Plays sound effects requested"""
    noise = pygame.mixer.Sound(sound)
    noise.play(0)


def scoreboard(statement, value, x, y1, y2, color):
    """Contains the scoreboard for the player"""
    box = small.render(statement + str(value), True, color)  # Rendering font for the scoreboard
    screen.fill(GREY, rect=box.get_rect(bottomleft=(x, y1)))  # Filling the background of the scoreboard with grey
    screen.blit(box, (x, y2))  # Putting the scoreboard in the bottom corner of the screen
    pygame.display.update()  # Updating the screen


def enemy_spawn(number, x, y):
    """Function to spawn enemies"""
    for i in range(number):  # enemies will spawn
        enemy = Enemy()
        enemy.rect.x = random.randrange(x[0], x[1])  # Enemies will randomly spawn within the screen
        enemy.rect.y = random.randrange(y[0], y[1])

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


# sizes for sentences
small = pygame.font.SysFont("TimesNewRoman", 25)
big = pygame.font.SysFont("TimesNewRoman", 50)

# Max and min speeds of player
max_s = 10
min_s = -5

# for the map
floor = 0
tree = 1

image_library = {
    tree: pygame.transform.scale(pygame.image.load('Images/tree.png'), [45, 45]),
    floor: pygame.transform.scale(pygame.image.load('Images/floor.png'), [45, 45])
}

# 4 different maps, can all be used based on player's choice
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

close = True
wave = True


def game(score, layout):
    """Main program for game"""

    # Variables declared global
    global event
    global score_1, score_2
    global wave_number
    global hp
    global close
    global kills
    global wave

    if wave_number == 1:
        enemy_spawn(20, (275, 400), (0, 2))
    if wave_number == 2:
        enemy_spawn(25, (275, 400), (0, 2))
    if wave_number == 3:
        enemy_spawn(30, (275, 400), (0, 2))

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

    while close and wave:  # While the game is running
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
                    player.angle_speed -= 5
                # Player moves right if d is hit
                if event.key == pygame.K_d:
                    player.angle_speed += 5

                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:  # Player can boost by holding shift
                    player.speed = 12  # Increase player speed to 12

                if event.key == pygame.K_SPACE:  # If player hits spacebar
                    shoot = Shoot(player.rect.center, player.direction)  # Bullets start where player is at
                    sound_effects("Music/Shooting.wav")  # Sound effects function called

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
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    player.speed = 0

        kills = pygame.sprite.groupcollide(enemy_list, shooting_list, True, True)  # Checking for enemy hit by shooting
        for kills in kills:
            enemy = Enemy()
            score += 1  # Add 1 to score each time enemy is shot
            # Remove enemies from sprite lists
            all_sprites_list.remove(enemy)
            enemy_list.remove(enemy)
            enemy.kill()  # Enemy taken off the screen

        die = pygame.sprite.spritecollide(player, enemy_list, False)  # Check if player is hit by an enemy
        if die:  # If they player is hit
            hp -= 1  # Subtract 1 from their lives
            if hp <= 0:  # If HP goes lower than 0
                hp = 0  # Set HP equal to 0 so it doesn't go to negatives

        if hp == 0:  # When player loses all HP
            # Sentences to show that player has lost, kill player
            sentence(big, "YOU DIED", RED, 200, 300)
            sentence(big, "YOU REACHED WAVE: " + str(wave_number), RED, 50, 350)
            player.kill()
            pygame.time.delay(5000)
            pygame.quit()
            quit()

        if score == 20 and wave_number == 1:  # If player kills all 20 enemies on screen
            wave_number += 1  # Increase wave number
            game(score_2, layout)  # Call game function for new wave
        if score == 25 and wave_number == 2:
            wave_number += 1  # Increase wave number
            game(score_2, layout)
        if score == 30 and wave_number == 3:
            wave_number += 1  # Increase wave number
            game(score_2, layout)

        if wave_number == 4:  # If the player reaches wave 4
            # Sentences to show the player has beat all waves and has won the game
            sentence(big, "OAKWALD ESCAPADE", DARK_GREEN, 100, 250)
            sentence(big, "SMILES UPON YOU", DARK_GREEN, 120, 300)
            sentence(big, "(YOU WIN!)", DARK_GREEN, 200, 350)
            pygame.time.delay(5000)  # Delay pygame for 3 seconds
            pygame.quit()  # Quit pygame
            quit()

        screen.fill(WHITE)
        for row in range(15):
            for column in range(15):
                screen.blit(image_library[layout[row][column]], (column * size_of_tile, row * size_of_tile))
        all_sprites_list.update()  # Updating the all sprites list
        all_sprites_list.draw(screen)  # Drawing all sprites created on the screen

        # Scoreboard function called to show player lives and current score
        scoreboard("Score: ", score, 50, 625, 600, WHITE)
        scoreboard("Wave: ", wave_number, 50, 75, 50, WHITE)

        # Color changes depending on players HP level
        if hp <= 100:
            scoreboard("HP: ", hp, 550, 625, 600, DARK_GREEN)
        if hp <= 75:
            scoreboard("HP: ", hp, 550, 625, 600, ORANGE)
        if hp <= 50:
            scoreboard("HP: ", hp, 550, 625, 600, YELLOW)
        if hp <= 25:
            scoreboard("HP: ", hp, 550, 625, 600, RED)

        clock.tick(60)  # 60 fps
        pygame.display.flip()


# Create two buttons by calling Button class
instructions_button = Button("Instructions", (338, 200), instructions, DARK_GREEN, WHITE)

# Map buttons
map_one = Button("Play Map 1", (75, 350), game, DARK_GREEN, WHITE)
map_two = Button("Play Map 2", (75, 500), game, DARK_GREEN, WHITE)
map_three = Button("Play Map 3", (600, 350), game, DARK_GREEN, WHITE)
map_four = Button("Play Map 4", (600, 500), game, DARK_GREEN, WHITE)

timer = Clock("Time: ", RED, 0, 0)

button_list = [instructions_button, map_one, map_two, map_three, map_four]  # Button list
home_screen = True

while home_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # If player preses the mouse
            position = pygame.mouse.get_pos()  # Gets the mouse position on screen
            if instructions_button.rect.collidepoint(position):  # Checks if it is within the button dimensions
                button_list.remove(instructions_button)  # Removes the instructions button from the list
                instructions_button.call()  # Calls instructions function

            # Map buttons, check for press with mouse, will load the corresponding map for the game
            if map_one.rect.collidepoint(position):
                map_one.call(score_1, map1)
            if map_two.rect.collidepoint(position):
                map_two.call(score_1, map2)
            if map_three.rect.collidepoint(position):
                map_three.call(score_1, map3)
            if map_four.rect.collidepoint(position):
                map_four.call(score_1, map4)

    for button in button_list:
        button.draw()  # Draws buttons on screen from the button list
    pygame.display.update()
