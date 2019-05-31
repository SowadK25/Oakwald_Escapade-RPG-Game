import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


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

    def right(self):
        self.rect.x += self.speed_x

    def left(self):
        self.rect.x -= self.speed_x

    def up(self):
        self.rect.y -= self.speed_y

    def down(self):
        self.rect.y += self.speed_y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed_x

        if keys[pygame.K_a]:
            self.rect.x -= self.speed_x

        if keys[pygame.K_w]:
            self.rect.y -= self.speed_y

        if keys[pygame.K_s]:
            self.rect.y += self.speed_x
