import pygame
import random

class Obstacle():
    def __init__(self, game, soldier):
        self.singleImage = pygame.image.load('images/rocket.png') # alterar imagem
        self.rocketSpeed = 15
        self.rockets = []
        self.rocketDimensions = (58, 36)
        self.soundComing = pygame.mixer.Sound('songs/quack.ogg') # alterar som enquanto o foguete tá na tela
        self.soundHitted = pygame.mixer.Sound('songs/ketchup.ogg') # alterar som enquanto o foguete tá na tela
        self.rocketSteps = [0]
        self.game = game
        self.soldier = soldier
    
    # def update(self):
    #     self.animationTimer += 1
    #     if self.animationTimer >= self.animationSpeed:
    #         self.animationTimer = 0
    #         self.imageIndex += 1
    #         if self.imageIndex > len(self.imageList) - 1:
    #             self.imageIndex = 0

    def draw(self):
        for r in self.rockets:
            if(r[0] < 0):
                self.rockets.remove(r)
            else:
                r[0] -= self.rocketSpeed
                self.game.screen.blit(self.singleImage, (r[0], r[1]))

    def verifyCollision(self):
        playerRect = pygame.Rect(self.soldier.position[0], self.soldier.position[1], self.soldier.dimensions[0], self.soldier.dimensions[1])
        for r in self.rockets: 
            if r.colliderect(playerRect):
                self.game.state = 'lose'
                pygame.mixer.stop()
                music = self.soundHitted
                pygame.mixer.music.play(-1)
    
    def createRocket(self):
        securityMargin = 50
        self.rocketSteps[0] += self.rocketSpeed
        randomRocketGeneration = random.randint(1, 50)
        if(self.rocketSteps[0] > self.game.screen_width * randomRocketGeneration):
            self.rocketSteps[0] = 0
            rocket_height = random.randint(10, self.game.screen_height - self.game.platformHeight - securityMargin)
            self.rockets.append(pygame.Rect(self.game.screen_width + securityMargin, rocket_height, self.rocketDimensions[0], self.rocketDimensions[1]))
            self.soundComing.play()