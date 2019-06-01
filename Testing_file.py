import pygame
from pygame.math import Vector2

pygame.init()

height = 750
width = 750
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Oakwald Escapade')

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

max_s = 10
min_s = -5

image = pygame.image.load("grass.png")
screen.blit(image, (0, 0))
pygame.display.flip()


class Player(pygame.sprite.Sprite):
    """Class that contains player movement and spawning"""

    # Initializing the class
    def __init__(self):
        super().__init__()

        # Loading player image and putting it in a surface and rectangle
        self.image = pygame.Surface([750, 750])
        self.image = pygame.image.load("pawn.png")
        self.org_image = self.image
        self.rect = self.image.get_rect()
        self.pos = (200, 200)  # Start position of player
        self.position = Vector2(self.pos)  # Position set as a vector quantity
        self.direction = Vector2(0, -1)  # Vector points upwards

        # Setting player speed, angle speed, and angle size
        self.speed = 0
        self.angle_speed = 0
        self.angle = 0

    def update(self):



class Shoot(pygame.sprite.Sprite):
    """Contains how the player will shoot"""

    def __init__(self, pos, direction):
        super().__init__()
        # Class is being initialized

        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.position = Vector2(pos)
        self.vel = direction * 10

    def update(self):
        """Allow bullets to be moved"""
        self.position += self.vel
        self.rect.center = self.position


clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
shooting_list = pygame.sprite.Group()

player = Player()

all_sprites_list.add(player)


running = True  # While the game is running, the following actions will be done
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Stops running if the program quits
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player.speed > min_s:
                player.speed += 2
            if event.key == pygame.K_s and player.speed < max_s:
                player.speed -= 2
            if event.key == pygame.K_a:
                player.angle_speed -= 2
            if event.key == pygame.K_d:
                player.angle_speed += 2

            if event.key == pygame.K_SPACE:
                shoot = Shoot(player.rect.center, player.direction)
                all_sprites_list.add(shoot)
                shooting_list.add(shoot)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.angle_speed = 0
            if event.key == pygame.K_d:
                player.angle_speed = 0

    pygame.display.flip()
    all_sprites_list.clear(screen, image)  # Clearing all sprites from the screen

    all_sprites_list.update()  # Updating the all sprites list
    all_sprites_list.draw(screen)  # Drawing all sprites created on the screen

    clock.tick(60)

pygame.quit()
