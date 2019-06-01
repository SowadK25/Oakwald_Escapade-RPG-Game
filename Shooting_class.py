import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Shoot(pygame.sprite.Sprite):
    """Contains how the player will shoot"""

    def __init__(self, pos, direction):
        super().__init__()
        # Class is being initialized

        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
