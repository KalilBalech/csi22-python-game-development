import pygame
import coin
import random
import math
# constant variables

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


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

gravity = 0.4
impulse = -0.5

#player
player_image = pygame.image.load('images/soldier.png')

player_height = 72
player_width = 58

player_x_position = 40
player_y_position = 10

player_x_speed = 0
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
coin_image_list = [
    pygame.image.load('images/coin_0.png'),
    pygame.image.load('images/coin_1.png'),
    pygame.image.load('images/coin_2.png'),
    pygame.image.load('images/coin_3.png'),
    pygame.image.load('images/coin_4.png'),
    pygame.image.load('images/coin_5.png'),
    pygame.image.load('images/coin_6.png')]

coin_image = pygame.image.load('images/coin_0.png')

coins = []
coin_speed = 5
coins_collected = 0
steps_walked = [0]
jetpackCoins = coin.Coin(coin_image_list, coin_speed, coins, SCREEN_SIZE, PLATFORM_HEIGHT)
coin_structure = {1: 'Row', 
                  2:'Ascending ramp', 
                  3:'Descending ramp', 
                  4:'Circle Sequence', 
                  5:'Heart', 
                  6:'Rectangle', 
                  7:'LittleSquare Sequence', 
                  8:'Yano Eu Te Amo', 
                  9:'Carla Meu Amor',
                  10:'Arrow',
                  11:'Double Row',
                  12:'Triple Row',
                  13: 'X'
}

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
        player_y_acelleration = impulse
        if platforms[0].colliderect(new_player_rect):
            player_y_speed = -5
    else:
        space_pressed = False
        player_y_acelleration = gravity

    # vertical movement
    # the new position has changed
    player_y_speed += player_y_acelleration
    player_new_y_position = player_y_position + player_y_speed
    # the future position prevision
    new_player_rect = pygame.Rect(player_x_position, player_new_y_position, player_width, player_height)
    y_collision = False
    for p in platforms:
        if p.colliderect(new_player_rect):
            y_collision = True
            player_y_speed = 0

    # if doesnt collide, so turns to the current position
    if y_collision == False:
        player_y_position = player_new_y_position

    # see if any coins have been collected
    player_rect = pygame.Rect(player_x_position, player_y_position, player_width, player_height)
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
    
    jetpackCoins.createCoinChain(steps_walked)
    # steps_walked += coin_speed
    # if(steps_walked > SCREEN_WIDTH):
    #     steps_walked = 0
    #     coin_structure_type = random.randint(1, 5)
    #     if(coin_structure_type == 1):
    #         coin_height = random.randint(10, SCREEN_HEIGHT - PLATFORM_HEIGHT - 80)
    #         coin_amount = random.randint(5, 12)
    #         for i in range (1, coin_amount):
    #             coins.append(pygame.Rect(SCREEN_WIDTH + 50*i, coin_height, 32, 32))
    #     elif(coin_structure_type == 2):
    #         coin_height = random.randint(10 + 12*20, SCREEN_HEIGHT - PLATFORM_HEIGHT -80)
    #         coin_amount = random.randint(5, 12)
    #         for i in range (1, coin_amount):
    #             coins.append(pygame.Rect(SCREEN_WIDTH + 50*i, coin_height - 20*i, 32, 32))
    #     elif(coin_structure_type == 3):
    #         coin_height = random.randint(10, SCREEN_HEIGHT - PLATFORM_HEIGHT - 12*20 - 50)
    #         coin_amount = random.randint(5, 12)
    #         for i in range (1, coin_amount):
    #             coins.append(pygame.Rect(SCREEN_WIDTH + 50*i, coin_height + 20*i, 32, 32))
    #     elif(coin_structure_type == 4):
    #         coin_height = random.randint(100, SCREEN_HEIGHT - PLATFORM_HEIGHT - 100 - 50)
    #         for i in range (1, 12):
    #             coins.append(pygame.Rect(SCREEN_WIDTH + 200 + round(100*math.cos(i*45*math.pi/180)), coin_height + round(100*math.sin(i*45*math.pi/180)), 32, 32))
    #     elif(coin_structure_type == 5):
    #         coin_height = random.randint(100, SCREEN_HEIGHT - PLATFORM_HEIGHT - 50)
    #         coin_amount = random.randint(5, 12)
    #         for i in range (1, coin_amount):
    #             if(i % 2 == 1):
    #                 delta_height = 100
    #             else:
    #                 delta_height = -100
    #             coins.append(pygame.Rect(SCREEN_WIDTH + 50*i, coin_height + delta_height, 32, 32))

    # coins
    jetpackCoins.update()
    for c in coins:
        c[0] -= coin_speed
        jetpackCoins.draw(screen, c[0], c[1])

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