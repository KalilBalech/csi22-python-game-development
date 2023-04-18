import pygame
import prop

class Soldier(prop.Prop):
    def __init__(self, dimensions, screenDimensions, screen):
        self.image = pygame.image.load('images/soldier.png')
        self.gravity = 0.4
        self.impulse = -0.5
        self.dimensions = dimensions
        super().__init__(screenDimensions, screen)
    
    def movement(self, position, speed, acelleration):
        # player input
        current_player_rect = pygame.Rect(position[0], position[1], self.dimensions[0], self.dimensions[1])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            acelleration[1] = self.impulse
            if self.platforms[0].colliderect(current_player_rect):
                speed[1] = -5
        else:
            acelleration[1] = self.gravity

        # vertical movement
        # the new position has changed
        speed[1] += acelleration[1]
        player_new_y_position = position[1] + speed[1]
        # the future position prevision
        new_player_rect = pygame.Rect(position[0], player_new_y_position, self.dimensions[0], self.dimensions[1])
        y_collision = False
        for p in self.platforms:
            if p.colliderect(new_player_rect):
                y_collision = True
                speed[1] = 0

        # if doesnt collide, so turns to the current position
        if y_collision == False:
            position[1] = player_new_y_position
        
        # self.screen.blit(self.image, (position[0], position[1]))

        