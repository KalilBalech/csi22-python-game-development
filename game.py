import pygame
# constant variables

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

CHARACTER_HEIGHT = 72
CHARACTER_WIDTH = 58

PLATFORM_HEIGHT = 50

WHITE = (255, 255, 255)
DARK_GREY = (50,50,50)
MUSTARD = (209,206,25)
LIGHT_BLUE = (15, 235, 255)
BLACK = (0, 0, 0)

# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('De volta para o lar')
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)


#player
player_image = pygame.image.load('images/soldier.png')
player_x_position = 40
player_y_position = 10

player_y_speed = 0
player_y_acelleration = 0.4

#platforms
#ground
platforms = [pygame.Rect(0, SCREEN_HEIGHT-PLATFORM_HEIGHT, SCREEN_WIDTH, PLATFORM_HEIGHT),
             pygame.Rect(0, 0, SCREEN_WIDTH, 1)]

# background song
music = pygame.mixer.music.load('songs/galinha.ogg')
pygame.mixer.music.play(-1)

# coin sound
coin_sound = pygame.mixer.Sound('songs/coin.ogg')

# coins
coin_image = pygame.image.load('images/coin_0.png')
coins = [
            pygame.Rect(1300, 450, 32, 32),
            pygame.Rect(1200, 400, 32, 32),
            pygame.Rect(1100, 350, 32, 32),
            pygame.Rect(1000, 300, 32, 32),
            pygame.Rect(900, 250, 32, 32),

            pygame.Rect(2000, 250, 32, 32),
            pygame.Rect(2200, 250, 32, 32),
            pygame.Rect(2400, 250, 32, 32),
            pygame.Rect(2600, 250, 32, 32),
            pygame.Rect(2800, 250, 32, 32),

            pygame.Rect(4000, 200, 32, 32),
            pygame.Rect(4200, 250, 32, 32),
            pygame.Rect(3800, 250, 32, 32),
            pygame.Rect(4200, 350, 32, 32),
            pygame.Rect(3800, 350, 32, 32),
            pygame.Rect(4300, 300, 32, 32),
            pygame.Rect(3700, 300, 32, 32),
            pygame.Rect(4000, 400, 32, 32),

            pygame.Rect(5000, 450, 32, 32),
            pygame.Rect(5200, 400, 32, 32),
            pygame.Rect(5400, 350, 32, 32),
            pygame.Rect(5600, 300, 32, 32),
            pygame.Rect(5800, 250, 32, 32),

            pygame.Rect(7000, 450, 32, 32),
            pygame.Rect(5200, 400, 32, 32),
            pygame.Rect(5400, 350, 32, 32),
            pygame.Rect(5600, 300, 32, 32),
            pygame.Rect(5800, 250, 32, 32),
            
            pygame.Rect(8000, 200, 32, 32),
            pygame.Rect(8050, 200, 32, 32),
            pygame.Rect(8100, 200, 32, 32),
            pygame.Rect(8150, 200, 32, 32),
            pygame.Rect(8200, 200, 32, 32),
            pygame.Rect(8250, 200, 32, 32),
            pygame.Rect(8300, 200, 32, 32),
            pygame.Rect(8350, 200, 32, 32),
            pygame.Rect(8400, 200, 32, 32),
            pygame.Rect(8450, 200, 32, 32)
        ]

coin_speed = 5
coins_collected = 0

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
        if player_y_speed > 0:
            player_y_acelleration = -0.3
        else:
            player_y_acelleration = -0.2
        if platforms[0].colliderect(new_player_rect):
            player_y_speed = -5
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

    # see if any coins have been collected
    player_rect = pygame.Rect(player_x_position, player_y_position, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    for c in coins: 
        if c.colliderect(player_rect):
            coins.remove(c)
            coins_collected += 1
            coin_sound.play()

    # update

    # draw

    #background
    screen.fill(LIGHT_BLUE)

    #platforms
    for p in platforms:
        pygame.draw.rect(screen, BLACK, p)

    # coins
    for c in coins:
        c[0] -= coin_speed
        # screen.blit(coin_image, (c[0], c[1]))
        screen.blit(coin_image, (c[0], c[1]))

    screen.blit(player_image, (player_x_position, player_y_position))

    # Player information display

    #coins
    screen.blit(coin_image, (20, 20))
    coin_text = font.render(str(coins_collected), True, BLACK, LIGHT_BLUE)
    coin_text_rectangle = coin_text.get_rect()
    coin_text_rectangle.topleft = (55, 25)
    screen.blit(coin_text, coin_text_rectangle)
    
    pygame.display.flip()
    clock.tick(60)

# quit
pygame.quit()