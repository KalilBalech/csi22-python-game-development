import pygame
import random
import staticObstacle

class SpikeBarVertical(staticObstacle.StaticObstacle):
    def __init__(self, game, soldier):
        super().__init__(game, soldier)
        self.obstacleSpeed = 8
        self.imageList = [pygame.image.load('images/staticBar.png')]
        self.singleImage = pygame.image.load('images/staticBar.png')
        self.obstacleDimensions = (72, 139)
        self.soundComing = None
    
    def draw(self):
        super().draw()

    def verifyCollision(self):
        return super().verifyCollision()
    
    def createObstacle(self):
        super().createObstacle(self.obstacleDimensions[0])
            # another diference is the absence of sound