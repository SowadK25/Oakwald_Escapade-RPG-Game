import pygame
from pygame.math import Vector2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Shoot(pygame.sprite.Sprite):
    """Contains how the player will shoot"""

    def __init__(self, pos, direction):
        super().__init__()
        # Class is being initialized

        # Creating 10 by 10 square for bullet
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        # Bullets position and speed is being set as a vector quantity
        self.position = Vector2(pos)
        self.vel = direction * 10

    def update(self):
        """Allow bullets to be moved"""
        self.position += self.vel  # Bullet will move based on its velocity
        self.rect.center = self.position  # Bullet rectangle is updated
