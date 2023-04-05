import pygame
# constant variables

SCREEN_SIZE = (800,700)
DARK_GREY = (50,50,50)

# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('De volta para o lar')

running = True
while running:
# game loop

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(DARK_GREY)
    pygame.display.flip()

# quit
pygame.quit()