import pygame

class Player(pygame.sprite.Sprite):
  
   # Initializing the class
    def __init__(self):
        super().__init__()
        
        # self.image = pygame.Surface(screen size cords go here)
        # self.image = pygame.image.load(player image goes here)
        self.rect = self.image.get_rect()
