import pygame

Floors = []


class Floor(pygame.sprite.Sprite):
    """Class for loading floor image"""

    def __init__(self, position):
        super().__init__()

        Floors.append(self)
        self.image = pygame.image.load(self.name)
        self.rect = pygame.Rect(position[0], position[1], 50, 50)
        self.rect = self.image.get_rect()
        self.size = 45
        self.name = "floor.png"
        pass
