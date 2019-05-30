import pygame
from Player_class import Player

pygame.init()

height = 750
width = 750
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Oakwald Escapade')

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

image = pygame.image.load("board.png")
screen.blit(image, (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()

player = Player()
all_sprites_list.add(player)



running = True  # While the game is running, the following actions will be done
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Stops running if the program quits
            running = False

        if event.type == pygame.KEYDOWN:
            pygame.display.update()
            player.update()
            if event.key == pygame.K_d:
                player.move_right()

            if event.key == pygame.K_a:
                player.move_left()

            if event.key == pygame.K_w:
                player.move_up()

            if event.key == pygame.K_s:
                player.move_down()

    pygame.display.flip()
    all_sprites_list.clear(screen, image)  # Clearing all sprites from the screen

    all_sprites_list.update()  # Updating the all sprites list
    all_sprites_list.draw(screen)  # Drawing all sprites created on the screen

    clock.tick(60)

pygame.quit()
