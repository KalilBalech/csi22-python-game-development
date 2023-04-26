import pygame
import dynamicObstacle

class Spike(dynamicObstacle.DynamicObstacle):

    def __init__(self, game, soldier):
        super().__init__(game, soldier)
        self.singleImage = pygame.image.load('images/spikes.png')
        self.obstacleDimensions = (60, 60)
    
    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def verifyCollision(self):
        return super().verifyCollision()
    
    def createObstacle(self):
        super().createObstacle(self.obstacleDimensions[0]*2)
