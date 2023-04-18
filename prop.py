import pygame

class Prop:
    def __init__(self):
        self.screenDimensions = (900, 600)
        self.screen_width = self.screenDimensions[0]
        self.screen_height = self.screenDimensions[1]
        self.screen = pygame.display.set_mode(self.screenDimensions)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.clock = pygame.time.Clock()
        self.platformHeight = 50
        self.platforms = [pygame.Rect(0, self.screen_height-self.platformHeight, self.screen_width, self.platformHeight),
             pygame.Rect(0, 0, self.screen_width, 1)]
    
    def initialConfig(self):
        music = pygame.mixer.music.load('songs/galinha.ogg')
        pygame.mixer.music.play(-1)
        pygame.display.set_caption('De volta para o lar')
    
    def platformsDisplay(self):
        BLACK = (0, 0, 0)
        for p in self.platforms:
            pygame.draw.rect(self.screen, BLACK, p)
    
    def soldierDisplay(self, soldierImage, soldierPosition):
        self.screen.blit(soldierImage, soldierPosition)
    
    def fillBackground(self):
        LIGHT_BLUE = (15, 235, 255)
        self.screen.fill(LIGHT_BLUE)
    
    def userInterfaceDisplay(self, coinImage, coinsCollected):
        LIGHT_BLUE = (15, 235, 255)
        BLACK = (0, 0, 0)
        self.screen.blit(coinImage, (20, 20))
        coin_text = self.font.render(str(coinsCollected), True, BLACK, LIGHT_BLUE)
        coin_text_rectangle = coin_text.get_rect()
        coin_text_rectangle.topleft = (55, 25)
        self.screen.blit(coin_text, coin_text_rectangle)
    
    def finalCongig(self):
        self.clock.tick(60)
        pygame.display.flip()
