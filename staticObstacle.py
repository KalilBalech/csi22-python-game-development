import pygame
import random
import math
import obstacle

class StaticObstacle(obstacle.Obstacle):
    def __init__(self, game, soldier):
        super().__init__(game, soldier)
    
    def draw(self):
        super().draw()

    def verifyCollision(self):
        return super().verifyCollision()
    
    def createObstacle(self, securityMargin):
        super().createObstacle(securityMargin)
            # another diference is the absence of sound