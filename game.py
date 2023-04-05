import pygame
# constant variables

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

CHARACTER_HEIGHT = 72
CHARACTER_WIDTH = 58

PLATFORM_HEIGHT = 50

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
DARK_GREY = (50,50,50)
MUSTARD = (209,206,25)

# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('De volta para o lar')
clock = pygame.time.Clock()


#player
player_image = pygame.image.load('images/soldier.png')
player_x_position = 40
player_y_position = 10

player_y_speed = 0
player_y_acelleration = 0.4

#platforms
#ground
platforms = [pygame.Rect(0, SCREEN_HEIGHT-PLATFORM_HEIGHT, SCREEN_WIDTH, PLATFORM_HEIGHT),
             pygame.Rect(0, 0, SCREEN_WIDTH, 1)
            ]
running = True
while running:
# game loop

    # input

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        space_pressed = True
        player_y_speed = -5
        player_y_acelleration = -2
    else:
        space_pressed = False
        player_y_acelleration = 0.4

    # vertical movement
    # the new position has changed
    player_y_speed += player_y_acelleration
    player_new_y_position = player_y_position + player_y_speed
    # the future position prevision
    new_player_rect = pygame.Rect(player_x_position, player_new_y_position, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    y_collision = False
    for p in platforms:
        if p.colliderect(new_player_rect):
            y_collision = True
            player_y_speed = 0

    # if doesnt collide, so turns to the current position
    if y_collision == False:
        player_y_position = player_new_y_position



    # update

    # draw

    #background
    screen.fill(DARK_GREY)
    #platform
    for p in platforms:
        pygame.draw.rect(screen, MUSTARD, p)
    screen.blit(player_image, (player_x_position, player_y_position))
    pygame.display.flip()

    clock.tick(60)

# quit
pygame.quit()