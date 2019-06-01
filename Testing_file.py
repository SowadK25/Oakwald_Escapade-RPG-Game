import pygame

pygame.init()

height = 750
width = 750
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Oakwald Escapade')

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

image = pygame.image.load("grass.png")
screen.blit(image, (0, 0))
pygame.display.flip()


class Player(pygame.sprite.Sprite):
    """Class that contains player movement and spawning"""

    # Initializing the class
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([750, 750])
        self.image = pygame.image.load("pawn.png")
        self.rect = self.image.get_rect()

    def move_right(self):
        self.rect.x += 5

        if self.rect.x >= 650:
            self.rect.x = 650

    def move_left(self):
        self.rect.x -= 5

        if self.rect.x <= -50:
            self.rect.x = -50

    def move_up(self):
        self.rect.y -= 5

        if self.rect.y <= -30:
            self.rect.y = -30

    def move_down(self):
        self.rect.y += 5

        if self.rect.y >= 630:
            self.rect.y = 630

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player.move_right()

        if keys[pygame.K_a]:
            player.move_left()

        if keys[pygame.K_w]:
            player.move_up()

        if keys[pygame.K_s]:
            player.move_down()


class Shoot(pygame.sprite.Sprite):
    """Contains how the player will shoot"""

    def __init__(self):
        super().__init__()
        # Class is being initialized

        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        self.speed_x = 8
        self.speed_y = 8

    def update(self):
        if player.move_left():
            self.rect.x -= self.speed_x
        if player.move_right():
            self.rect.x += self.speed_x
        if player.move_up():
            self.rect.y -= self.speed_y



clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
shooting_list = pygame.sprite.Group()

player = Player()
shoot = Shoot()

all_sprites_list.add(player)
all_sprites_list.add(shoot)


running = True  # While the game is running, the following actions will be done
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Stops running if the program quits
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot.rect.x = player.rect.x
                shoot.rect.y = player.rect.y
                all_sprites_list.add(shoot)
                shooting_list.add(shoot)

    pygame.display.flip()
    all_sprites_list.clear(screen, image)  # Clearing all sprites from the screen

    all_sprites_list.update()  # Updating the all sprites list
    all_sprites_list.draw(screen)  # Drawing all sprites created on the screen

    clock.tick(60)

pygame.quit()
