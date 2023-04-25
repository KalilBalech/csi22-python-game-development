import pygame
import random
import math

class Coin():
    def __init__(self, game, soldier):
        self.imageList =   [pygame.image.load('images/coin_0.png'),
                            pygame.image.load('images/coin_1.png'),
                            pygame.image.load('images/coin_2.png'),
                            pygame.image.load('images/coin_3.png'),
                            pygame.image.load('images/coin_4.png'),
                            pygame.image.load('images/coin_5.png'),
                            pygame.image.load('images/coin_6.png')]
        self.singleImage = pygame.image.load('images/coin_0.png')
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationSpeed = 8
        self.coinsCollected = [0]
        self.coinSpeed = 5
        self.coins = []
        self.sound = pygame.mixer.Sound('songs/coin.ogg')
        self.coinSteps = [0]
        self.game = game
        self.soldier = soldier
    
    def update(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0
            self.imageIndex += 1
            if self.imageIndex > len(self.imageList) - 1:
                self.imageIndex = 0
    def draw(self):
        image = self.imageList[self.imageIndex]
        for c in self.coins:
            if(c[0] < 0):
                self.coins.remove(c)
            else:
                c[0] -= self.coinSpeed
                self.game.screen.blit(image, (c[0], c[1]))

    def verifyCollection(self):
        playerRect = pygame.Rect(self.soldier.position[0], self.soldier.position[1], self.soldier.dimensions[0], self.soldier.dimensions[1])
        for c in self.coins: 
            if c.colliderect(playerRect):
                self.coins.remove(c)
                self.coinsCollected[0] += 1
                self.sound.play()
    
    def createCoinChain(self):
        minCoinAmount = 20
        maxCoinAmount = 40
        horizontalCoinDistance = 20
        verticalCoinDistance = horizontalCoinDistance
        securityMargin = 40
        self.coinSteps[0] += self.coinSpeed
        if(self.coinSteps[0] > self.game.screen_width):
            self.coinSteps[0] = 0
            coin_structure_type = random.randint(8, 8)
            # row
            if(coin_structure_type == 1):
                coin_height = random.randint(10, self.game.screen_height - self.game.platformHeight - securityMargin)
                coin_amount = random.randint(minCoinAmount, maxCoinAmount)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height, 32, 32))
            # rampa subindo
            elif(coin_structure_type == 2):
                coin_amount = random.randint(minCoinAmount/2, 3*maxCoinAmount/8)
                coin_height = random.randint(10 + coin_amount*20, self.game.screen_height - self.game.platformHeight - securityMargin)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height - 20*i, 32, 32))
            # rampa caindo
            elif(coin_structure_type == 3):
                coin_amount = random.randint(minCoinAmount/2, 3*maxCoinAmount/8)
                coin_height = random.randint(10, self.game.screen_height - self.game.platformHeight - coin_amount*20)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + 20*i, 32, 32))
            # circle
            elif(coin_structure_type == 4):
                radius = 100
                coin_height = random.randint(100, self.game.screen_height - self.game.platformHeight - radius - securityMargin)
                for i in range (0, 30):
                    self.coins.append(pygame.Rect(self.game.screen_width + securityMargin + round(radius*math.cos(i*12*math.pi/180)), coin_height + round(radius*math.sin(i*12*math.pi/180)), 32, 32))
            # zig zag
            elif(coin_structure_type == 5):
                coin_height = random.randint(100, self.game.screen_height - self.game.platformHeight - securityMargin)
                coin_amount = random.randint(minCoinAmount, maxCoinAmount)
                rowDistance = 40
                for i in range (1, coin_amount):
                    if(i % 2 == 1):
                        delta_height = rowDistance
                    else:
                        delta_height = 0
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + delta_height, 32, 32))
            # rectangle
            elif(coin_structure_type == 6):
                coin_height = random.randint(10, self.game.screen_height - self.game.platformHeight - 4*securityMargin)
                coin_amount = random.randint(minCoinAmount, maxCoinAmount)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height, 32, 32))
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + 20, 32, 32))
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + 40, 32, 32))
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + 60, 32, 32))
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + 80, 32, 32))
            # arrow
            elif(coin_structure_type == 7):
                coin_height = random.randint(10, self.game.screen_height - self.game.platformHeight - 5*securityMargin)
                coin_amount = 8
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height, 32, 32))
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + verticalCoinDistance, 32, 32))
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + 2*verticalCoinDistance, 32, 32))
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + 3*verticalCoinDistance, 32, 32))
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + 4*verticalCoinDistance, 32, 32))
                for i in range(1,7):
                    for j in range(0, 7-i):
                        self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(coin_amount+i-1), coin_height + (j+i-4)*verticalCoinDistance, 32, 32))
                for i in range(1,7):
                    for j in range(0, 7-i):
                        self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(coin_amount+i-1), coin_height + (8-i-j)*verticalCoinDistance, 32, 32))
            # YANO EU TE AMO
            elif(coin_structure_type == 8):
                self.coinSteps[0] = -self.game.screen_width
                coin_height = random.randint(10, self.game.screen_height - self.game.platformHeight - 5*securityMargin)
                # write Y
                    # descida
                for i in range (1, 6):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*i, coin_height + verticalCoinDistance*i, 32, 32))
                    # pauzinho vertical
                for i in range (1, 5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*5, coin_height + verticalCoinDistance*(5+i), 32, 32))
                    # subida
                for i in range (1, 5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(5+i), coin_height + verticalCoinDistance*(5-i), 32, 32))

                # write A
                # subida
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(7 +i/2), coin_height + verticalCoinDistance*(10-i), 32, 32))
                # descida
                for i in range (1, 9):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(11 +(i+1)/2), coin_height + verticalCoinDistance*(i+1), 32, 32))
                # pauzinho horizontal
                for i in range (1, 6):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(7 +3/2 + i), coin_height + verticalCoinDistance*(6), 32, 32))

                # write N
                # first vertical rod
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(17), coin_height + verticalCoinDistance*(i), 32, 32))
                # descida
                for i in range (1, 9):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(16 + 1/2 + 3*i/4), coin_height + verticalCoinDistance*(i+1), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(22 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                
                #write O
                # first vertical rod
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(24 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(24 + i + 1/2), coin_height + verticalCoinDistance*(1), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(24 + i + 1/2), coin_height + verticalCoinDistance*(9), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(29), coin_height + verticalCoinDistance*(i), 32, 32))
                # distance between words = 4*horizontalCoinsDistance
                # for each letter -> horizontal = 4 ; vertical = 9;
                #write E
                # first vertical rod
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(33), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(32 + i + 1/2), coin_height + verticalCoinDistance*(1), 32, 32))
                # middle horizontal rod
                for i in range (1,5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(32 + i + 1/2), coin_height + verticalCoinDistance*(5), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(32 + i + 1/2), coin_height + verticalCoinDistance*(9), 32, 32))
                
                #write U
                # first vertical rod
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(38), coin_height + verticalCoinDistance*(i), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(38 -1/2 + i), coin_height + verticalCoinDistance*(9), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(42), coin_height + verticalCoinDistance*(10-i), 32, 32))
                
                #write T
                # top horizontal rod
                for i in range (1,7):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(45 + i), coin_height + verticalCoinDistance*(1), 32, 32))
                # middle vertical rod
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(48 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                
                #write E
                # first vertical rod
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(52), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(51 + i + 1/2), coin_height + verticalCoinDistance*(1), 32, 32))
                # middle horizontal rod
                for i in range (1,5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(51 + i + 1/2), coin_height + verticalCoinDistance*(5), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(51 + i + 1/2), coin_height + verticalCoinDistance*(9), 32, 32))

                # write A
                # subida
                for i in range (1, 10):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(59 +i/2), coin_height + verticalCoinDistance*(10-i), 32, 32))
                # descida
                for i in range (1, 9):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(63 +(i+1)/2), coin_height + verticalCoinDistance*(i+1), 32, 32))
                # pauzinho horizontal
                for i in range (1, 6):
                    self.coins.append(pygame.Rect(self.game.screen_width + horizontalCoinDistance*(59 +3/2 + i), coin_height + verticalCoinDistance*(6), 32, 32))


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