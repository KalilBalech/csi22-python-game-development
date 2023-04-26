import pygame
import random
import obstacle

class DynamicObstacle(obstacle.Obstacle):

    def __init__(self, game, soldier):
        super().__init__(game, soldier)
        # default
        self.angleSpeed = 4
        self.angle = [0]
        self.obstacleSpeed = 5

        # particular
        #self.singleImage = pygame.image.load('images/spike-ball.png')
        #self.obstacleDimensions = (32, 32)

    def draw(self):
        super().draw()

    def verifyCollision(self):
        return super().verifyCollision()
    
    def createObstacle(self, securityMargin):
        super().createObstacle(securityMargin)
