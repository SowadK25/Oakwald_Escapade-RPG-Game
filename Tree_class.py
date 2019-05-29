import pygame

Trees = []

class Tree(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()

        Trees.append(self)
        self.rect = pygame.Rect(position[0], position[1], 50, 50)
