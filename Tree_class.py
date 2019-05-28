import pygame

class Tree(object):

    def __init__(self, position):
        Trees.append(self)
        self.rect = pygame.Rect(position[0],position[1],50,50)