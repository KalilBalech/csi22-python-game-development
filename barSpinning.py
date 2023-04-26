import pygame
import dynamicObstacle

class BarSpinning(dynamicObstacle.DynamicObstacle):

    def __init__(self, game, soldier):
        super().__init__(game, soldier)
        self.singleImage = pygame.image.load('images/bar-dynamic/bar_0.png')
        self.obstacleDimensions = (200, 40)
    
    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def verifyCollision(self):
        return super().verifyCollision()
    
    def createObstacle(self):
        super().createObstacle(self.obstacleDimensions[0]*2)
