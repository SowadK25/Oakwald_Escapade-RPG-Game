import pygame
from Player_class import Player

player = Player()
Trees = []


class Tree(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()

        Trees.append(self)
        self.rect = pygame.Rect(position[0], position[1], 50, 50)
        self.image = pygame.transform.scale(pygame.image.load("tree.png"), [45, 45])
        self.rect = self.image.get_rect()

    def collision(self):
        if self.rect.colliderect(player.rect):
            self.rect.clamp_ip(player.rect)
