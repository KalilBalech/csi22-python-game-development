import pygame
import dynamicObstacle

class BarSpinning(dynamicObstacle.DynamicObstacle):

    def __init__(self, game, soldier):
        super().__init__(game, soldier)
        self.imageList = [
            pygame.image.load('images/bar-dynamic/bar_0.png'),
            pygame.image.load('images/bar-dynamic/bar_1.png'),
            pygame.image.load('images/bar-dynamic/bar_2.png'),
            pygame.image.load('images/bar-dynamic/bar_3.png'),
        ]
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
