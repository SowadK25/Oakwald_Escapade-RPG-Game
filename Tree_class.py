import pygame

Trees = []

class Tree(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()

        Trees.append(self)
        self.rect = pygame.Rect(position[0], position[1], 50, 50)
        

'''import pygame



pygame.init()

height = 750
width = 750

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Oakwald Escapade")



screen.fill(WHITE)
pygame.display.flip()





sentence(big, "Hello", RED, 500, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False'''
