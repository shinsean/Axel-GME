import pygame

import colors as clr

class Block(pygame.sprite.Sprite):
    def __init__(self, raw_x, raw_y):
        super().__init__()

        self.side_length = 30

        self.raw_x = raw_x
        self.raw_y = raw_y

        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.set_grid_positions()

    def set_grid_positions(self):
        self.rect.x = (int(self.raw_x/self.side_length)
            * self.side_length)
        
        self.rect.y = (int(self.raw_y/self.side_length)
            * self.side_length)