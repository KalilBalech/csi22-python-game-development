import pygame
import math

class Prop:
    def __init__(self):
        self.__screenDimensions = (900, 600)
        self.screen_width = self.__screenDimensions[0]
        self.screen_height = self.__screenDimensions[1]
        self.__screen = pygame.display.set_mode(self.__screenDimensions)
        self.__font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.__clock = pygame.time.Clock()
        self.__platformHeight = 50
        self.__platforms = [pygame.Rect(0, self.screen_height-self.__platformHeight, self.screen_width, self.__platformHeight),
             pygame.Rect(0, 0, self.screen_width, 1)]
        self.state = 'playing'
        self.__runDistance = [0]
        self.__endSound = pygame.mixer.Sound('songs/endGame.ogg')
        self.__background = pygame.image.load('images/background.jpg')
        self.__tiles = math.ceil(self.screen_width/self.__background.get_width()) + 1
        self.__scroll = [0]
        self.__backgroundSpeed = 5
    
    def initialConfig(self):
        music = pygame.mixer.music.load('songs/galinha.ogg')
        pygame.mixer.music.play(-1)
        pygame.display.set_caption('De volta para o lar')
    
    def platformsDisplay(self):
        pass
        # BLACK = (0, 0, 0)
        # for p in self.__platforms:
        #     pygame.draw.rect(self.__screen, BLACK, p)
    
    def soldierDisplay(self, soldierImage, soldierPosition):
        self.__screen.blit(soldierImage, soldierPosition)
    
    def updateDistance(self):
        self.__runDistance[0] += 0.2
    
    def changeState(self, newState):
        self.state = newState

    def fillBackground(self):
        for i in range (0, self.__tiles):
            self.__screen.blit(self.__background, (i*self.__background.get_width() + self.__scroll[0], 0))
        
        self.__scroll[0] -= 5

        if abs(self.__scroll[0]) > self.__background.get_width():
            self.__scroll[0] = 0
        # LIGHT_BLUE = (15, 235, 255)
        # self.__screen.fill(LIGHT_BLUE)
    
    def userInterfaceDisplay(self, coinsCollected):
        LIGHT_BLUE = (15, 235, 255)
        BLACK = (0, 0, 0)

        coinImage = pygame.image.load('images/coin_0.png')
        pegadaImage = pygame.image.load('images/pegada.png')
        

        self.__screen.blit(coinImage, (20, 20))
        coin_text = self.__font.render(str(coinsCollected), True, BLACK, LIGHT_BLUE)
        coin_text_rectangle = coin_text.get_rect()
        coin_text_rectangle.topleft = (55, 25)
        self.__screen.blit(coin_text, coin_text_rectangle)

        self.__screen.blit(pegadaImage, (20, 70))
        run_text = self.__font.render(str(int(self.__runDistance[0])) + ' metros', True, BLACK, LIGHT_BLUE)
        run_text_rectangle = run_text.get_rect()
        run_text_rectangle.topleft = (60, 75)
        self.__screen.blit(run_text, run_text_rectangle)
    
    def loseInterface(self, coinAmout, distance):
        BLACK = (0, 0, 0)
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
        self.__screen.blit(surface, (0, 0))

        self.__screen.blit(coinImage, (300, 250))
        coin_text = self.__font.render(str(coinAmout), True, BLACK, WHITE)
        coin_text_rectangle = coin_text.get_rect()
        coin_text_rectangle.topleft = (350, 250)
        self.__screen.blit(coin_text, coin_text_rectangle)
        
        self.__screen.blit(pegadaImage, (300, 300))
        distance_text = self.__font.render(str(int(distance)), True, BLACK, WHITE)
        distance_text_rectangle = distance_text.get_rect()
        distance_text_rectangle.topleft = (350, 300)
        self.__screen.blit(distance_text, distance_text_rectangle)

        end_text = self.__font.render('A derrota é temporária, mas a humilhação é eterna', True, BLACK, WHITE)
        end_text_rectangle = end_text.get_rect()
        end_text_rectangle.topleft = (200, 200)
        self.__screen.blit(end_text, end_text_rectangle)

        # Atualize a tela
        pygame.display.update()
    
    def finalConfig(self):
        self.__clock.tick(60)
        pygame.display.flip()
    
    def state(self):
        return self.state

    def platforms(self):
        return self.__platforms

    def platformHeight(self):
        return self.__platformHeight

    def screen(self):
        return self.__screen
    
    def runDistance(self):
        return self.__runDistance[0]