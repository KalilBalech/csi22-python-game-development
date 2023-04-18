import pygame
import prop
import soldier
import coin
import obstacle

# init
pygame.init()

# game general properties
basics = prop.Prop()
basics.initialConfig()

#player
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

capitaoJoao = soldier.Soldier(player_dimensions)

# coins
jetpackCoins = coin.Coin()

# obstacle
jetpackRockets = obstacle.Obstacle()
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

    # see if any coins have been collected or obstacles have been hitted
    playerRect = pygame.Rect(player_position[0], player_position[1], player_width, player_height)
    jetpackCoins.verifyCollection(playerRect)
    jetpackRockets.verifyCollision(playerRect)

    # update

    # draw

    #background
    basics.fillBackground()

    # platform display
    basics.platformsDisplay()
    
    # coins
    # make coin chains appear AND UPDATE STEP WALKED
    jetpackCoins.createCoinChain() 
    # make coin images update after 8 times this function run
    jetpackCoins.update()
    # make the coins move and make the coins appear in the screen
    jetpackCoins.draw() 

    # obstacles  
    jetpackRockets.createRocket()
    jetpackRockets.draw()

    basics.soldierDisplay(capitaoJoao.image, (player_position[0], player_position[1]))
    # screen.blit(capitaoJoao.image, (player_position[0], player_position[1]))

    # Player information display

    # user interface
    basics.userInterfaceDisplay(jetpackCoins.singleImage, jetpackCoins.coinsCollected[0])
    
    # final config
    basics.finalCongig()

# quit
pygame.quit()