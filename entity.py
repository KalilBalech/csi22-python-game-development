class Entity:
    def __init__(self, screenDimensions, platforms, screen):
        self.screen_width = screenDimensions[0]
        self.screen_height = screenDimensions[1]
        self.platforms = platforms
        self.platformHeight = platforms[0][3]
        self.screen = screen