import pygame
import random
import math
import obstacle
from abc import ABC

# CLASSE GERAL DE OBSTACULOS ESTÁTICO COM OS METODOS E ATRIBUTOS PADRÕES IDENTICOS AO DA CLASSE OBSTACULO
class StaticObstacle(obstacle.Obstacle, ABC):
    def __init__(self, game, soldier):
        super().__init__(game, soldier)
    
    def draw(self):
        super().draw()

    def verifyCollision(self):
        return super().verifyCollision()
    
    def createObstacle(self, securityMargin):
        super().createObstacle(securityMargin)
