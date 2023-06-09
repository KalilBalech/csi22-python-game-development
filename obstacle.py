import pygame
import random
from abc import ABC


# CLASSE GERAL DE OBSTACULOS COM OS METODOS E ATRIBUTOS PADRÃO PARA QUE O OBSTÁCULO PRECISE
class Obstacle(ABC):
    def __init__(self, game, soldier):
        self.obstacleSpeed = 15
        self.obstacles = []
        self.obstacleSteps = [0]
        self.game = game
        self.soundHitted = pygame.mixer.Sound('songs/endGame.ogg') # alterar som enquanto o foguete tá na tela
        self.soldier = soldier
        self.soundComing = None

    # DESENHA OS OBSTACULOS NA TELA COM A POSIÇÃO ATUALIZADA
    def draw(self):
        for r in self.obstacles:
            if(r[0] < -50):
                self.obstacles.remove(r)
            else:
                r[0] -= self.obstacleSpeed
                self.game.screen().blit(self.singleImage, (r[0], r[1]))

    # VERIFICA SE ALGUM OBSTÁCULO FOI COLIDIDO COM O CAPITÃO JOÃO
    def verifyCollision(self):
        playerRect = pygame.Rect(self.soldier.xPosition(), self.soldier.yPosition(), self.soldier.xDimensions(), self.soldier.yDimensions())
        for r in self.obstacles: 
            if r.colliderect(playerRect):
                self.game.state = 'lose'
                pygame.mixer.stop()
                self.soundHitted.play()

    # CRIA OBSTÁCULOS ALEATORIAMENTE NA TELA
    def createObstacle(self, securityMarginInput):
        securityMargin = securityMarginInput
        self.obstacleSteps[0] += self.obstacleSpeed
        randomObstacleGeneration = random.randint(1, 400)
        if(self.obstacleSteps[0] > self.game.screen_width * randomObstacleGeneration):
            self.obstacleSteps[0] = 0
            obstacle_height = random.randint(10, self.game.screen_height - self.game.platformHeight() - securityMargin)
            self.obstacles.append(pygame.Rect(self.game.screen_width + securityMargin, obstacle_height, self.obstacleDimensions[0], self.obstacleDimensions[1]))
            if(self.soundComing != None):
                self.soundComing.play()