import pygame

Floors = []


class Floor(pygame.sprite.Sprite):
    """Class for loading floor image"""

    def __init__(self, position):
        super().__init__()

        Floors.append(self)
        self.rect = pygame.Rect(position[0], position[1], 50, 50)
        self.size = 45
        pass
