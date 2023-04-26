import pygame
import prop
import soldier
import coin
import rocket
import spike
import barSpinning
import spikeBarVertical
import spikeBarHorizontal

# init
pygame.init()

# game general properties 
basics = prop.Prop() 
basics.initialConfig()

capitaoJoao = soldier.Soldier()

# coins
jetpackCoins = coin.Coin(basics, capitaoJoao)

# obstacle 
rockets = rocket.Rocket(basics, capitaoJoao)
spikeObstacles = spike.Spike(basics, capitaoJoao)
barSpinnigObstacles = barSpinning.BarSpinning(basics, capitaoJoao)
spikeBarVertical = spikeBarVertical.SpikeBarVertical(basics, capitaoJoao)
spikeBarHorizontal = spikeBarHorizontal.SpikeBarHorizontal(basics, capitaoJoao)

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
        rockets.verifyCollision()
        spikeObstacles.verifyCollision()
        barSpinnigObstacles.verifyCollision()
        spikeBarVertical.verifyCollision()
        spikeBarHorizontal.verifyCollision()

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
        rockets.createObstacle()
        rockets.draw()
        
        spikeObstacles.createObstacle() 
        spikeObstacles.draw()
        
        barSpinnigObstacles.createObstacle()
        barSpinnigObstacles.draw()
        
        spikeBarVertical.createObstacle()
        spikeBarVertical.draw()
        
        spikeBarHorizontal.createObstacle()
        spikeBarHorizontal.draw()

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