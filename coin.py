import pygame
import random
import math
import prop

class Coin(prop.Prop):
    def __init__(self):
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
        super().__init__()
    
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
                self.screen.blit(image, (c[0], c[1]))

    def verifyCollection(self, playerRect):
        for c in self.coins: 
            if c.colliderect(playerRect):
                self.coins.remove(c)
                self.coinsCollected[0] += 1
                self.sound.play()
    
    def createCoinChain(self):
        minCoinAmount = 20
        maxCoinAmount = 40
        horizontalCoinDistance = 20
        securityMargin = 40
        self.coinSteps[0] += self.coinSpeed
        if(self.coinSteps[0] > self.screen_width):
            self.coinSteps[0] = 0
            coin_structure_type = random.randint(1, 6)
            # row
            if(coin_structure_type == 1):
                coin_height = random.randint(10, self.screen_height - self.platformHeight - securityMargin)
                coin_amount = random.randint(minCoinAmount, maxCoinAmount)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.screen_width + horizontalCoinDistance*i, coin_height, 32, 32))
            # rampa subindo
            elif(coin_structure_type == 2):
                coin_amount = random.randint(minCoinAmount/2, 3*maxCoinAmount/8)
                coin_height = random.randint(10 + coin_amount*20, self.screen_height - self.platformHeight - securityMargin)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.screen_width + horizontalCoinDistance*i, coin_height - 20*i, 32, 32))
            # rampa caindo
            elif(coin_structure_type == 3):
                coin_amount = random.randint(minCoinAmount/2, 3*maxCoinAmount/8)
                coin_height = random.randint(10, self.screen_height - self.platformHeight - coin_amount*20)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.screen_width + horizontalCoinDistance*i, coin_height + 20*i, 32, 32))
            # circle
            elif(coin_structure_type == 4):
                radius = 100
                coin_height = random.randint(100, self.screen_height - self.platformHeight - radius - securityMargin)
                for i in range (0, 30):
                    self.coins.append(pygame.Rect(self.screen_width + securityMargin + round(radius*math.cos(i*12*math.pi/180)), coin_height + round(radius*math.sin(i*12*math.pi/180)), 32, 32))
            # zig zag
            elif(coin_structure_type == 5):
                coin_height = random.randint(100, self.screen_height - self.platformHeight - securityMargin)
                coin_amount = random.randint(minCoinAmount, maxCoinAmount)
                rowDistance = 40
                for i in range (1, coin_amount):
                    if(i % 2 == 1):
                        delta_height = rowDistance
                    else:
                        delta_height = -rowDistance
                    self.coins.append(pygame.Rect(self.screen_width + horizontalCoinDistance*i, coin_height + delta_height, 32, 32))
            # rectangle
            elif(coin_structure_type == 6):
                coin_height = random.randint(10, self.screen_height - self.platformHeight - 2*securityMargin)
                coin_amount = random.randint(minCoinAmount, maxCoinAmount)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.screen_width + horizontalCoinDistance*i, coin_height, 32, 32))
                    self.coins.append(pygame.Rect(self.screen_width + horizontalCoinDistance*i, coin_height + 20, 32, 32))
                    self.coins.append(pygame.Rect(self.screen_width + horizontalCoinDistance*i, coin_height + 40, 32, 32))
                    self.coins.append(pygame.Rect(self.screen_width + horizontalCoinDistance*i, coin_height + 60, 32, 32))
                    self.coins.append(pygame.Rect(self.screen_width + horizontalCoinDistance*i, coin_height + 80, 32, 32))
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