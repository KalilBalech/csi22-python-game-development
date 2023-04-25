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

capitaoJoao = soldier.Soldier()

# coins
jetpackCoins = coin.Coin(basics, capitaoJoao)

# obstacle 
jetpackRockets = obstacle.Obstacle(basics, capitaoJoao)
running = True
while running:
# game loop

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # player position based on input
    if basics.state == 'playing':
        capitaoJoao.movement()

        # see if any coins have been collected or obstacles have been hitted
        jetpackCoins.verifyCollection()
        jetpackRockets.verifyCollision()

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

        basics.updateDistance()

        basics.soldierDisplay(capitaoJoao.image, (capitaoJoao.position[0], capitaoJoao.position[1]))

        # Player information display

        # user interface
        basics.userInterfaceDisplay(jetpackCoins.coinsCollected[0])
    
    else:
        basics.loseInterface(jetpackCoins.coinsCollected[0], basics.runDistance[0])

    # final config
    basics.finalConfig()

# quit
pygame.quit()