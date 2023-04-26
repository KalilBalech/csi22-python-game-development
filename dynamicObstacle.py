import pygame
import random
import obstacle
from abc import ABC

# CLASSE GERAL DE OBSTACULOS DINÂMICO COM METODOS E ATRIBUTOS ADICIONAIS PARA QUE O OBJETO, ALEM DE ROTACIONAR, SE MOVA NA MESMA VELOCIDADE
# DAS MOEDASS
class DynamicObstacle(obstacle.Obstacle, ABC):

    def __init__(self, game, soldier):
        super().__init__(game, soldier)
        # default
        self.angleSpeed = 4
        self.angle = [0]
        self.obstacleSpeed = 5
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationSpeed = 8

    def update(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0
            self.imageIndex += 1
            if self.imageIndex > len(self.imageList) - 1:
                self.imageIndex = 0

    def draw(self):
        image = self.imageList[self.imageIndex]
        for r in self.obstacles:
            if(r[0] < -50):
                self.obstacles.remove(r)
            else:
                r[0] -= self.obstacleSpeed
                self.angle[0] += self.angleSpeed
                rotated_image = pygame.transform.rotate(image, self.angle[0])
                self.game.screen().blit(rotated_image, (r[0], r[1]))

    def verifyCollision(self):
        return super().verifyCollision()
    
    def createObstacle(self, securityMargin):
        super().createObstacle(securityMargin)
