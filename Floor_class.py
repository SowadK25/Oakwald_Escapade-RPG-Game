import pygame

Floors = []

class Floor(pygame.sprite.Sprite):


    def __init__(self, position):
        super().__init__()

        Floors.append(self)
        self.rect = pygame.Rect(position [0], position [1], 50, 50)


class bestClassInTheGame:
    def __init__(self):
        pass

variable = bestClassInTheGame()