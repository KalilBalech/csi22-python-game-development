import pygame
import staticObstacle

class Rocket(staticObstacle.StaticObstacle):
    def __init__(self, game, soldier):
        super().__init__(game, soldier)

        self.singleImage = pygame.image.load('images/rocket.png')
        self.obstacleDimensions = (58, 36)
        self.soundComing = pygame.mixer.Sound('songs/piupiu.ogg')
    
    def draw(self):
        super().draw()

    def verifyCollision(self):
        return super().verifyCollision()
    
    def createObstacle(self):
        super().createObstacle(self.obstacleDimensions[0])
            # another diference is the absence of sound