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


player = Player()
