# Player image link: https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwivr7r5ssviAhXOuFkKHagXBc0QjRx6BAgBEAU&url=https%3A%2F%2Fopengameart.org%2Fcontent%2Fanimated-top-down-survivor-player&psig=AOvVaw2UUZGjH8im__BITi9uZFX_&ust=1559585520031182

import pygame
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):
    """Class that contains player movement and spawning"""
  
# Initializing the class
    def __init__(self):
        super().__init__()
        
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
        """Angle, position, direction of player updated for smoothness"""
        self.image = pygame.transform.rotate(self.org_image, -self.angle)
        self.rect = self.image.get_rect()
        self.direction.rotate_ip(self.angle_speed)  # Rotating vector direction and image
        self.angle += self.angle_speed  # Angle of player moved at a fixed speed

        # Updating player's position vector and rectangle surface
        self.position += self.direction * self.speed
        self.rect.center = self.position

