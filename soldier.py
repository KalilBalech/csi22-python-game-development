import pygame
import prop

class Soldier():
    def __init__(self, game):
        self.image = pygame.image.load('images/soldier.png')
        self.__gravity = 0.4
        self.__impulse = -0.5
        self.__dimensions = (58, 72)
        self.__position = [200, 10]
        self.__speed = [0, 0]
        self.__acceleration = [0, 0.4]
        self.__game = game
        super().__init__()
    
    # realiza a dinâmica de movimento do soldado
    def movement(self):
        # player input
        current_player_rect = pygame.Rect(self.__position[0], self.__position[1], self.__dimensions[0], self.__dimensions[1])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.__acceleration[1] = self.__impulse
            if self.__game.platforms()[0].colliderect(current_player_rect):
                self.__speed[1] = -5
        else:
            self.__acceleration[1] = self.__gravity

        # vertical movement
        # the new position has changed
        self.__speed[1] += self.__acceleration[1]
        player_new_y_position = self.__position[1] + self.__speed[1]
        # the future position prevision
        new_player_rect = pygame.Rect(self.__position[0], player_new_y_position, self.__dimensions[0], self.__dimensions[1])
        y_collision = False
        for p in self.__game.platforms():
            if p.colliderect(new_player_rect):
                y_collision = True
                self.__speed[1] = 0

        # if doesnt collide, so turns to the current position
        if y_collision == False:
            self.__position[1] = player_new_y_position
        
        # self.__screen.blit(self.__image, (position[0], position[1]))

    # métodos que garantem a privacidade de alguns atributos
    def xPosition(self):
        return self.__position[0]
    
    def yPosition(self):
        return self.__position[1]
    
    def xDimensions(self):
        return self.__dimensions[0]
    
    def yDimensions(self):
        return self.__dimensions[1]
    