from import_libraries import *

class Block(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super().__init__()

        self.side_length = 10

        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        self.rect.x = x_position
        self.rect.y = y_position