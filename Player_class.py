import pygame


class Player(pygame.sprite.Sprite):
    """Class that contains player movement and spawning"""
  
   # Initializing the class
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([750, 750])
        self.image = pygame.image.load("pawn.png")
        self.rect = self.image.get_rect()

    def move_right(self):
        self.rect.x += 5

        if self.rect.x >= 650:
            self.rect.x = 650

    def move_left(self):
        self.rect.x -= 5

        if self.rect.x <= -50:
            self.rect.x = -50

    def move_up(self):
        self.rect.y -= 5

        if self.rect.y >= -30:
            self.rect.y = -30

    def move_down(self):
        self.rect.y += 5

        if self.rect.y <= 630:
            self.rect.y = 630

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player.move_right()

        if keys[pygame.K_a]:
            player.move_left()

        if keys[pygame.K_w]:
            player.move_up()

        if keys[pygame.K_s]:
            player.move_down()


player = Player()

