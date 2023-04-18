import pygame
import prop

class Soldier(prop.Prop):
    def __init__(self):
        self.image = pygame.image.load('images/soldier.png')
        self.gravity = 0.4
        self.impulse = -0.5
        self.dimensions = (58, 72)
        self.position = [200, 10]
        self.speed = [0, 0]
        self.acceleration = [0, 0.4]
        super().__init__()
    
    def movement(self):
        # player input
        current_player_rect = pygame.Rect(self.position[0], self.position[1], self.dimensions[0], self.dimensions[1])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.acceleration[1] = self.impulse
            if self.platforms[0].colliderect(current_player_rect):
                self.speed[1] = -5
        else:
            self.acceleration[1] = self.gravity

        # vertical movement
        # the new position has changed
        self.speed[1] += self.acceleration[1]
        player_new_y_position = self.position[1] + self.speed[1]
        # the future position prevision
        new_player_rect = pygame.Rect(self.position[0], player_new_y_position, self.dimensions[0], self.dimensions[1])
        y_collision = False
        for p in self.platforms:
            if p.colliderect(new_player_rect):
                y_collision = True
                self.speed[1] = 0

        # if doesnt collide, so turns to the current position
        if y_collision == False:
            self.position[1] = player_new_y_position
        
        # self.screen.blit(self.image, (position[0], position[1]))

        