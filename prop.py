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
        self.state = 'playing'
        self.runDistance = [0]
        self.endSound = pygame.mixer.Sound('songs/ketchup.ogg')
    
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
    
    def updateDistance(self):
        self.runDistance[0] += 0.2
    
    def changeState(self, newState):
        self.state = newState

    def fillBackground(self):
        LIGHT_BLUE = (15, 235, 255)
        self.screen.fill(LIGHT_BLUE)
    
    def userInterfaceDisplay(self, coinsCollected):
        LIGHT_BLUE = (15, 235, 255)
        BLACK = (0, 0, 0)

        coinImage = pygame.image.load('images/coin_0.png')
        pegadaImage = pygame.image.load('images/pegada.png')
        

        self.screen.blit(coinImage, (20, 20))
        coin_text = self.font.render(str(coinsCollected), True, BLACK, LIGHT_BLUE)
        coin_text_rectangle = coin_text.get_rect()
        coin_text_rectangle.topleft = (55, 25)
        self.screen.blit(coin_text, coin_text_rectangle)

        self.screen.blit(pegadaImage, (20, 70))
        run_text = self.font.render(str(int(self.runDistance[0])) + ' metros', True, BLACK, LIGHT_BLUE)
        run_text_rectangle = run_text.get_rect()
        run_text_rectangle.topleft = (60, 75)
        self.screen.blit(run_text, run_text_rectangle)
    
    def loseInterface(self, coinAmout, distance):
        BLACK = (0, 0, 0)
        LIGHT_BLUE = (15, 235, 255)
        WHITE = (255, 255, 255)
        # Carregue a imagem
        image = pygame.image.load('images/time.jpg')
        coinImage = pygame.image.load('images/coin_0.png')
        pegadaImage = pygame.image.load('images/pegada.png')

        # Redimensione a imagem para as dimensões da tela
        image = pygame.transform.scale(image, (self.screen_width, self.screen_height))

        # Crie uma superfície vazia com as dimensões da tela
        surface = pygame.Surface((self.screen_width, self.screen_height))

        # Cole a imagem na superfície vazia
        surface.blit(image, (0, 0))

        # Desenhe a superfície vazia na tela
        self.screen.blit(surface, (0, 0))

        self.screen.blit(coinImage, (300, 250))
        coin_text = self.font.render(str(coinAmout), True, BLACK, WHITE)
        coin_text_rectangle = coin_text.get_rect()
        coin_text_rectangle.topleft = (350, 250)
        self.screen.blit(coin_text, coin_text_rectangle)
        
        self.screen.blit(pegadaImage, (300, 300))
        distance_text = self.font.render(str(int(distance)), True, BLACK, WHITE)
        distance_text_rectangle = distance_text.get_rect()
        distance_text_rectangle.topleft = (350, 300)
        self.screen.blit(distance_text, distance_text_rectangle)

        end_text = self.font.render('A derrota é temporária, mas a humilhação é eterna', True, BLACK, WHITE)
        end_text_rectangle = end_text.get_rect()
        end_text_rectangle.topleft = (200, 200)
        self.screen.blit(end_text, end_text_rectangle)

        pygame.mixer.stop()

        music = self.endSound
        pygame.mixer.music.play(-1)
        # Atualize a tela
        pygame.display.update()
    
    def finalConfig(self):
        self.clock.tick(60)
        pygame.display.flip()
