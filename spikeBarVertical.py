import pygame
import random
import staticObstacle

class SpikeBarVertical(staticObstacle.StaticObstacle):
    def __init__(self, game, soldier):
        super().__init__(game, soldier)
        self.obstacleSpeed = 8

        self.singleImage = pygame.image.load('images/staticBar.png')
        self.singleImageSecundary = pygame.image.load('images/staticBar-90.png')
        self.obstacleDimensions = (72, 139)
        self.obstacleDimensionsSecundary = (139, 72)
        self.soundComing = None
    
    def draw(self):
        super().draw()

    def verifyCollision(self):
        return super().verifyCollision()
    
    def createObstacle(self):
        super().createObstacle(self.obstacleDimensions[0])
            # another diference is the absence of sound