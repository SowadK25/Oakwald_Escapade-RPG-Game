# Enemy character link: https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjstpKw2cviAhUBm1kKHaD2BWkQjRx6BAgB
# EAU&url=http%3A%2F%2Fpixelartmaker.com%2Fart%2F18aa1ab89b62bed&psig=AOvVaw3qtbOL5CJfSSaert4wUren&ust=1559595494982380

import pygame

height = 675
width = 675

RED = (255, 0, 0)


class Enemy(pygame.sprite.Sprite):
    """Enemy class to spawn enemies"""

    # Initializing the class
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([30, 20])
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0

        self.speed_y = 0
        self.speed_x = 0

    def update(self):
        """Enemies will move and bounce off walls"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right >= self.right or self.rect.left <= self.left:
            self.speed_x *= -1

        if self.rect.top <= self.top or self.rect.bottom >= self.bottom:
            self.speed_y *= -1
