import pygame
import random
from Player_class import Player
from Shooting_class import Shoot
from Enemy_class import Enemy

pygame.init()

height = 675
width = 675
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Oakwald Escapade')

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Max and min speeds of player
max_s = 10
min_s = -5

image = pygame.image.load("grass.png")
screen.blit(image, (0, 0))
pygame.display.flip()


clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
shooting_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

player = Player()
enemy = Enemy()

all_sprites_list.add(player)

for i in range(25):
    enemy = Enemy()
    enemy.rect.x = random.randrange(width)
    enemy.rect.y = random.randrange(height)

    enemy.speed_x = random.randrange(-2, 2)
    enemy.speed_y = random.randrange(-2, 2)
    enemy.left = 0
    enemy.top = 0
    enemy.right = width
    enemy.bottom = height

    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

running = True  # While the game is running, the following actions will be done
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Stops running if the program quits
            running = False

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

        if event.type == pygame.KEYUP:  # If the key is let go
            # Angle is reset back to 0 if let go for left and right movement
            if event.key == pygame.K_a:
                player.angle_speed = 0
            if event.key == pygame.K_d:
                player.angle_speed = 0
            if event.key == pygame.K_w:
                player.speed = 0
            if event.key == pygame.K_s:
                player.speed = 0

    pygame.display.flip()
    all_sprites_list.clear(screen, image)  # Clearing all sprites from the screen

    all_sprites_list.update()  # Updating the all sprites list
    all_sprites_list.draw(screen)  # Drawing all sprites created on the screen

    clock.tick(60)

pygame.quit()
