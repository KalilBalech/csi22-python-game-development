import pygame
import random
import prop

class Obstacle(prop.Prop):
    def __init__(self, screenDimensions, screen):
        self.singleImage = pygame.image.load('images/coin_0.png') # alterar imagem
        self.rocketSpeed = 15
        self.rockets = []
        self.soundComing = pygame.mixer.Sound('songs/coin.ogg') # alterar som enquanto o foguete tá na tela
        self.soundHitted = pygame.mixer.Sound('songs/coin.ogg') # alterar som enquanto o foguete tá na tela
        self.rocketSteps = [0]
        super().__init__(screenDimensions, screen)
    
    # def update(self):
    #     self.animationTimer += 1
    #     if self.animationTimer >= self.animationSpeed:
    #         self.animationTimer = 0
    #         self.imageIndex += 1
    #         if self.imageIndex > len(self.imageList) - 1:
    #             self.imageIndex = 0
    def draw(self, screen):
        for r in self.rockets:
            r[0] -= self.rocketSpeed
            screen.blit(self.singleImage, (r[0], r[1]))

    def verifyCollision(self, playerRect):
        for r in self.rockets: 
            if r.colliderect(playerRect):
                print('Game over') # implementar fim do jogo
                self.soundHitted.play()
    
    def createRocket(self):
        securityMargin = 50
        self.rocketSteps[0] += self.rocketSpeed
        randomRocketGeneration = random.randint(1, 50)
        if(self.rocketSteps[0] > self.screen_width * randomRocketGeneration):
            self.rocketSteps[0] = 0
            rocket_height = random.randint(10, self.screen_height - self.platformHeight - securityMargin)
            self.rockets.append(pygame.Rect(self.screen_width + securityMargin, rocket_height, 32, 32))