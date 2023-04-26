import pygame
import random
import math

class Coin():
    def __init__(self, game, soldier):
        self.__imageList =   [pygame.image.load('images/coin_0.png'),
                            pygame.image.load('images/coin_1.png'),
                            pygame.image.load('images/coin_2.png'),
                            pygame.image.load('images/coin_3.png'),
                            pygame.image.load('images/coin_4.png'),
                            pygame.image.load('images/coin_5.png'),
                            pygame.image.load('images/coin_6.png')]
        self.__singleImage = pygame.image.load('images/coin_0.png')
        self.__imageIndex = 0
        self.__animationTimer = 0
        self.__animationSpeed = 8
        self.__coinsCollected = [0]
        self.__coinSpeed = 5
        self.__coins = []
        self.__sound = pygame.mixer.Sound('songs/coin.ogg')
        self.__coinSteps = [0]
        self.__game = game
        self.__soldier = soldier
    
    def update(self):
        self.__animationTimer += 1
        if self.__animationTimer >= self.__animationSpeed:
            self.__animationTimer = 0
            self.__imageIndex += 1
            if self.__imageIndex > len(self.__imageList) - 1:
                self.__imageIndex = 0
    def draw(self):
        image = self.__imageList[self.__imageIndex]
        for c in self.__coins:
            if(c[0] < 0):
                self.__coins.remove(c)
            else:
                c[0] -= self.__coinSpeed
                self.__game.screen().blit(image, (c[0], c[1]))

    def verifyCollection(self):
        playerRect = pygame.Rect(self.__soldier.xPosition(), self.__soldier.yPosition(), self.__soldier.xDimensions(), self.__soldier.yDimensions())
        for c in self.__coins: 
            if c.colliderect(playerRect):
                self.__coins.remove(c)
                self.__coinsCollected[0] += 1
                self.__sound.play()
    
    def coinsCollected(self):
        return self.__coinsCollected[0]

    def createCoinChain(self):
        minCoinAmount = 20
        maxCoinAmount = 40
        horizontalCoinDistance = 20
        verticalCoinDistance = horizontalCoinDistance
        securityMargin = 40
        self.__coinSteps[0] += self.__coinSpeed
        if(self.__coinSteps[0] > self.__game.screen_width):
            self.__coinSteps[0] = 0
            coin_structure_type = random.randint(6, 9)
            # row
            if(coin_structure_type == 1):
                coin_height = random.randint(10, self.__game.screen_height - self.__game.platformHeight() - securityMargin)
                coin_amount = random.randint(minCoinAmount, maxCoinAmount)
                for i in range (1, coin_amount):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height, 32, 32))
            # rampa subindo
            elif(coin_structure_type == 2):
                coin_amount = random.randint(minCoinAmount/2, 3*maxCoinAmount/8)
                coin_height = random.randint(10 + coin_amount*20, self.__game.screen_height - self.__game.platformHeight() - securityMargin)
                for i in range (1, coin_amount):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height - 20*i, 32, 32))
            # rampa caindo
            elif(coin_structure_type == 3):
                coin_amount = random.randint(minCoinAmount/2, 3*maxCoinAmount/8)
                coin_height = random.randint(10, self.__game.screen_height - self.__game.platformHeight() - coin_amount*20)
                for i in range (1, coin_amount):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + 20*i, 32, 32))
            # rectangle
            elif(coin_structure_type == 4):
                coin_height = random.randint(10, self.__game.screen_height - self.__game.platformHeight() - 4*securityMargin)
                coin_amount = random.randint(minCoinAmount, maxCoinAmount)
                for i in range (1, coin_amount):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height, 32, 32))
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + 20, 32, 32))
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + 40, 32, 32))
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + 60, 32, 32))
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + 80, 32, 32))
            # circle
            elif(coin_structure_type == 5):
                radius = 100
                coin_height = random.randint(100, self.__game.screen_height - self.__game.platformHeight() - radius - securityMargin)
                for i in range (0, 30):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + securityMargin + round(radius*math.cos(i*12*math.pi/180)), coin_height + round(radius*math.sin(i*12*math.pi/180)), 32, 32))
            # zig zag
            elif(coin_structure_type == 6):
                coin_height = random.randint(100, self.__game.screen_height - self.__game.platformHeight() - securityMargin)
                coin_amount = random.randint(minCoinAmount, maxCoinAmount)
                rowDistance = 40
                for i in range (1, coin_amount):
                    if(i % 2 == 1):
                        delta_height = rowDistance
                    else:
                        delta_height = 0
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + delta_height, 32, 32))
            # arrow
            elif(coin_structure_type == 7):
                coin_height = random.randint(10, self.__game.screen_height - self.__game.platformHeight() - 5*securityMargin)
                coin_amount = 8
                for i in range (1, coin_amount):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height, 32, 32))
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + verticalCoinDistance, 32, 32))
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + 2*verticalCoinDistance, 32, 32))
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + 3*verticalCoinDistance, 32, 32))
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + 4*verticalCoinDistance, 32, 32))
                for i in range(1,7):
                    for j in range(0, 7-i):
                        self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(coin_amount+i-1), coin_height + (j+i-4)*verticalCoinDistance, 32, 32))
                for i in range(1,7):
                    for j in range(0, 7-i):
                        self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(coin_amount+i-1), coin_height + (8-i-j)*verticalCoinDistance, 32, 32))
            # YANO EU TE AMO
            elif(coin_structure_type == 8):
                self.__coinSteps[0] = -2*self.__game.screen_width
                coin_height = random.randint(10, self.__game.screen_height - self.__game.platformHeight() - 5*securityMargin)
                # write Y
                    # descida
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*i, coin_height + verticalCoinDistance*i, 32, 32))
                    # pauzinho vertical
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*5, coin_height + verticalCoinDistance*(5+i), 32, 32))
                    # subida
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(5+i), coin_height + verticalCoinDistance*(5-i), 32, 32))

                # write A
                # subida
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(6 +i/2), coin_height + verticalCoinDistance*(10-i), 32, 32))
                # descida
                for i in range (1, 9):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(10 +(i+1)/2), coin_height + verticalCoinDistance*(i+1), 32, 32))
                # pauzinho horizontal
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(7 +1/2 + i), coin_height + verticalCoinDistance*(6), 32, 32))

                # write N
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(15+1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # descida
                for i in range (1, 9):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(15 + 3*i/4), coin_height + verticalCoinDistance*(i+1), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(21), coin_height + verticalCoinDistance*(i), 32, 32))
                
                #write O
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(22), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(22 + i), coin_height + verticalCoinDistance*(1), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(22 + i), coin_height + verticalCoinDistance*(9), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(26+1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                
                # distance between words = 4*horizontalCoinsDistance
                # for each letter -> horizontal = 4 ; vertical = 9;
                #write E
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(33), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(32 + i + 1/2), coin_height + verticalCoinDistance*(1), 32, 32))
                # middle horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(32 + i + 1/2), coin_height + verticalCoinDistance*(5), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(32 + i + 1/2), coin_height + verticalCoinDistance*(9), 32, 32))
                
                #write U
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(38), coin_height + verticalCoinDistance*(i), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(38 -1/2 + i), coin_height + verticalCoinDistance*(9), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(42), coin_height + verticalCoinDistance*(10-i), 32, 32))
                
                #write T
                # top horizontal rod
                for i in range (1,7):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(45 + i), coin_height + verticalCoinDistance*(1), 32, 32))
                # middle vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(48 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                
                #write E
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(52), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(51 + i + 1/2), coin_height + verticalCoinDistance*(1), 32, 32))
                # middle horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(51 + i + 1/2), coin_height + verticalCoinDistance*(5), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(51 + i + 1/2), coin_height + verticalCoinDistance*(9), 32, 32))

                # write A
                # subida
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(59 +i/2), coin_height + verticalCoinDistance*(10-i), 32, 32))
                # descida
                for i in range (1, 9):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(63 +(i+1)/2), coin_height + verticalCoinDistance*(i+1), 32, 32))
                # pauzinho horizontal
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(59 +3/2 + i), coin_height + verticalCoinDistance*(6), 32, 32))

                #write M
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(68), coin_height + verticalCoinDistance*(i), 32, 32))
                # descida
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(67+1/2+i/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # subida
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(73+1/2-i/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(73), coin_height + verticalCoinDistance*(i), 32, 32))

                #write O
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(74), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(74 + i), coin_height + verticalCoinDistance*(1), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(74 + i), coin_height + verticalCoinDistance*(9), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(79), coin_height + verticalCoinDistance*(i), 32, 32))
            # KARLA MEU AMOR
            elif(coin_structure_type == 9):
                self.__coinSteps[0] = -2*self.__game.screen_width
                coin_height = random.randint(10, self.__game.screen_height - self.__game.platformHeight() - 5*securityMargin)

                #write K
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(1), coin_height + verticalCoinDistance*(i), 32, 32))
                # cima
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(5 - 3*i/4), coin_height + verticalCoinDistance*(i), 32, 32))
                # baixo
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(5 - 3*i/4), coin_height + verticalCoinDistance*(10-i), 32, 32))
                
                # write A
                # subida
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(4 + 1/4 +i/2), coin_height + verticalCoinDistance*(10-i), 32, 32))
                # descida
                for i in range (1, 9):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(8 + 1/4 +(i+1)/2), coin_height + verticalCoinDistance*(i+1), 32, 32))
                # pauzinho horizontal
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(6 + 1/4 + i), coin_height + verticalCoinDistance*(6), 32, 32))

                #write R
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(13), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(12 + i), coin_height + verticalCoinDistance*(1), 32, 32))
                # middle horizontal rod
                for i in range (1,4):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(13 + i), coin_height + verticalCoinDistance*(5), 32, 32))
                # second vertical rod
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(17), coin_height + verticalCoinDistance*(i), 32, 32))
                # baixo descida
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(17 + 3/4 - 3*i/4), coin_height + verticalCoinDistance*(10-i), 32, 32))
                
                #write L
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(18 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(18 + 1/2 + i), coin_height + verticalCoinDistance*(9), 32, 32))
                
                # write A
                # subida
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(23 +i/2), coin_height + verticalCoinDistance*(10-i), 32, 32))
                # descida
                for i in range (1, 9):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(27 +(i+1)/2), coin_height + verticalCoinDistance*(i+1), 32, 32))
                # pauzinho horizontal
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(25 + i), coin_height + verticalCoinDistance*(6), 32, 32))
                
                #write M
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(36 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # descida
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(36+i/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # subida
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(42-i/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(41+1/2), coin_height + verticalCoinDistance*(i), 32, 32))

                #write E
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(42 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(42 + i), coin_height + verticalCoinDistance*(1), 32, 32))
                # middle horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(42 + i), coin_height + verticalCoinDistance*(5), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(42 + i), coin_height + verticalCoinDistance*(9), 32, 32))
                
                #write U
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(47 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(47  + 1/2+ i), coin_height + verticalCoinDistance*(9), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(52 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                
                # write A
                # subida
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(57 +i/2), coin_height + verticalCoinDistance*(10-i), 32, 32))
                # descida
                for i in range (1, 9):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(61 +(i+1)/2), coin_height + verticalCoinDistance*(i+1), 32, 32))
                # pauzinho horizontal
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(59 + i), coin_height + verticalCoinDistance*(6), 32, 32))
                
                #write M
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(66 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # descida
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(66+i/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # subida
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(72-i/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(71+1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                
                #write O
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(72 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(72 + 1/2 + i), coin_height + verticalCoinDistance*(1), 32, 32))
                # bottom horizontal rod
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(72 + 1/2 + i), coin_height + verticalCoinDistance*(9), 32, 32))
                # second vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(77 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                
                #write R
                # first vertical rod
                for i in range (1, 10):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(78 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # top horizontal rod
                for i in range (1,5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(77 + 1/2 + i), coin_height + verticalCoinDistance*(1), 32, 32))
                # middle horizontal rod
                for i in range (1,4):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(78 + 1/2 + i), coin_height + verticalCoinDistance*(5), 32, 32))
                # second vertical rod
                for i in range (1, 6):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(82 + 1/2), coin_height + verticalCoinDistance*(i), 32, 32))
                # baixo descida
                for i in range (1, 5):
                    self.__coins.append(pygame.Rect(self.__game.screen_width + horizontalCoinDistance*(83 + 1/4 - 3*i/4), coin_height + verticalCoinDistance*(10-i), 32, 32))

# coin_structure = {1: 'Row', 
#                   2:'Ascending ramp', 
#                   3:'Descending ramp', 
#                   4:'Circle Sequence', 
#                   5:'Heart', 
#                   6:'Rectangle', 
#                   7:'LittleSquare Sequence', 
#                   8:'Yano Eu Te Amo', 
#                   9:'karla Meu Amor',
#                   10:'Arrow',
#                   11:'Double Row',
#                   12:'Triple Row',
#                   13: 'X'
# }