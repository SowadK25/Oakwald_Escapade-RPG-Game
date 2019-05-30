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


clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()

player = Player()
all_sprites_list.add(player)


running = True  # While the game is running, the following actions will be done
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Stops running if the program quits
            running = False

    pygame.display.flip()
    all_sprites_list.clear(screen, image)  # Clearing all sprites from the screen

    all_sprites_list.update()  # Updating the all sprites list
    all_sprites_list.draw(screen)  # Drawing all sprites created on the screen

    clock.tick(60)

pygame.quit()
