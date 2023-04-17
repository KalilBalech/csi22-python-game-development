import pygame
import coin
import soldier
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

#platforms
#ground
platforms = [pygame.Rect(0, SCREEN_HEIGHT-PLATFORM_HEIGHT, SCREEN_WIDTH, PLATFORM_HEIGHT),
             pygame.Rect(0, 0, SCREEN_WIDTH, 1)]

#player
player_image = pygame.image.load('images/soldier.png')

player_dimensions = (58, 72)
player_width = player_dimensions[0]
player_height = player_dimensions[1]

player_position = [100, 10]
player_x_position = player_position[0]
player_y_position = player_position[1]

player_speed = [0, 0]
player_x_speed = player_speed[0]
player_y_speed = player_speed[1]

player_acelleration = [0, 0.4]
player_x_acelleration = player_acelleration[0]
player_y_acelleration = player_acelleration[1]

capitaoJoao = soldier.Soldier(player_image, gravity, impulse, player_dimensions, platforms, SCREEN_SIZE, screen)


# background song
music = pygame.mixer.music.load('songs/galinha.ogg')
pygame.mixer.music.play(-1)

# coins
steps_walked = [0]
jetpackCoins = coin.Coin(SCREEN_SIZE, platforms, screen)
# coin_structure = {1: 'Row', 
#                   2:'Ascending ramp', 
#                   3:'Descending ramp', 
#                   4:'Circle Sequence', 
#                   5:'Heart', 
#                   6:'Rectangle', 
#                   7:'LittleSquare Sequence', 
#                   8:'Yano Eu Te Amo', 
#                   9:'Carla Meu Amor',
#                   10:'Arrow',
#                   11:'Double Row',
#                   12:'Triple Row',
#                   13: 'X'
# }

running = True
while running:
# game loop

    # input

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # player position based on input
    capitaoJoao.movement(player_position, player_speed, player_acelleration)

    # see if any coins have been collected
    playerRect = pygame.Rect(player_position[0], player_position[1], player_width, player_height)
    jetpackCoins.verifyCollection(playerRect)

    # update

    # draw

    #background
    screen.fill(LIGHT_BLUE)

    #platforms
    for p in platforms:
        pygame.draw.rect(screen, BLACK, p)
    
    # coins
    # make coin chains appear
    jetpackCoins.createCoinChain(steps_walked) 
    # make coin images update after 8 times this function run
    jetpackCoins.update()
    # make the coins move and make the coins appear in the screen
    jetpackCoins.draw(screen)

    screen.blit(player_image, (player_position[0], player_position[1]))

    # Player information display

    # user interface
    screen.blit(jetpackCoins.singleImage, (20, 20))
    coin_text = font.render(str(jetpackCoins.coinsCollected), True, BLACK, LIGHT_BLUE)
    coin_text_rectangle = coin_text.get_rect()
    coin_text_rectangle.topleft = (55, 25)
    screen.blit(coin_text, coin_text_rectangle)
    
    pygame.display.flip()
    clock.tick(60)

# quit
pygame.quit()