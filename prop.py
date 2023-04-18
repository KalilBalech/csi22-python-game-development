import pygame

class Prop:
    def __init__(self, screenDimensions, screen):
        self.screen_width = screenDimensions[0]
        self.screen_height = screenDimensions[1]
        self.platformHeight = 50
        self.platforms = [pygame.Rect(0, self.screen_height-self.platformHeight, self.screen_width, self.platformHeight),
             pygame.Rect(0, 0, self.screen_width, 1)]
        self.screen = screen
    
    def platformsInit(self):
        BLACK = (0, 0, 0)
        for p in self.platforms:
            pygame.draw.rect(self.screen, BLACK, p)