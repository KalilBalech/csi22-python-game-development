class Entity:
    def __init__(self, screenDimensions, platformHeight):
        self.screen_width = screenDimensions[0]
        self.screen_height = screenDimensions[1]
        self.platform_height = platformHeight