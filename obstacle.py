import pygame
import random
import math
import entity

class Obstacle(entity.Entity):
    def __init__(self, screenDimensions, platforms, screen):
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
        self.coinsCollected = 0
        self.coinSpeed = 5
        self.coins = []
        self.sound = pygame.mixer.Sound('songs/coin.ogg')
        super().__init__(screenDimensions, platforms, screen)
    
    def update(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0
            self.imageIndex += 1
            if self.imageIndex > len(self.imageList) - 1:
                self.imageIndex = 0
    def draw(self, screen):
        image = self.imageList[self.imageIndex]
        for c in self.coins:
            c[0] -= self.coinSpeed
            screen.blit(image, (c[0], c[1]))

    def verifyCollection(self, playerRect):
        for c in self.coins: 
            if c.colliderect(playerRect):
                self.coins.remove(c)
                self.coinsCollected += 1
                self.sound.play()
    
    def createCoinChain(self, steps_walked):
        steps_walked[0] += self.coinSpeed
        if(steps_walked[0] > self.screen_width):
            steps_walked[0] = 0
            coin_structure_type = random.randint(1, 5)
            if(coin_structure_type == 1):
                coin_height = random.randint(10, self.screen_height - self.platformHeight - 80)
                coin_amount = random.randint(5, 12)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.screen_width + 50*i, coin_height, 32, 32))
            elif(coin_structure_type == 2):
                coin_height = random.randint(10 + 12*20, self.screen_height - self.platformHeight -80)
                coin_amount = random.randint(5, 12)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.screen_width + 50*i, coin_height - 20*i, 32, 32))
            elif(coin_structure_type == 3):
                coin_height = random.randint(10, self.screen_height - self.platformHeight - 12*20 - 50)
                coin_amount = random.randint(5, 12)
                for i in range (1, coin_amount):
                    self.coins.append(pygame.Rect(self.screen_width + 50*i, coin_height + 20*i, 32, 32))
            elif(coin_structure_type == 4):
                coin_height = random.randint(100, self.screen_height - self.platformHeight - 100 - 50)
                for i in range (1, 12):
                    self.coins.append(pygame.Rect(self.screen_width + 200 + round(100*math.cos(i*45*math.pi/180)), coin_height + round(100*math.sin(i*45*math.pi/180)), 32, 32))
            elif(coin_structure_type == 5):
                coin_height = random.randint(100, self.screen_height - self.platformHeight - 50)
                coin_amount = random.randint(5, 12)
                for i in range (1, coin_amount):
                    if(i % 2 == 1):
                        delta_height = 100
                    else:
                        delta_height = -100
                    self.coins.append(pygame.Rect(self.screen_width + 50*i, coin_height + delta_height, 32, 32))