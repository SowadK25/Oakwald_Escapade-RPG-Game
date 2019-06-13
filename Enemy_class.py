# Enemy character link: https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjstpKw2cviAhUBm1kKHaD2BWkQjRx6BAgB
# EAU&url=http%3A%2F%2Fpixelartmaker.com%2Fart%2F18aa1ab89b62bed&psig=AOvVaw3qtbOL5CJfSSaert4wUren&ust=1559595494982380

import pygame
import random
# Screen dimensions
height = 675
width = 675
sizes = [10,100,200,300,400,500]

class Enemy(pygame.sprite.Sprite):
    """Enemy class to spawn enemies"""

    # Initializing the class
    def __init__(self):
        super().__init__()

        # Creating surface and loading image into rect for enemy
        self.image = pygame.Surface([30, 20])
        self.image = pygame.transform.scale(pygame.image.load("Images/ghost 1.png"), [30, 30])
        self.rect = self.image.get_rect()
        # Screen dimension variables to be used later
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
        # Speed of enemy
        self.speed_y = 0
        self.speed_x = 0

    def update(self):
        """Enemies will move and bounce off walls"""

        # Enemies will move by its speed specified
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # If the enemy reaches end of the screen, it switches its direction
        if self.rect.right >= self.right or self.rect.left <= self.left:
            self.speed_x *= -1

        if self.rect.top <= self.top or self.rect.bottom >= self.bottom:
            self.speed_y *= -1
