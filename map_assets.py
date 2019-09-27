import pygame

import colors as clr

class Block(pygame.sprite.Sprite):
    def __init__(self, raw_x, raw_y):
        super().__init__()

        self.side_length = 30

        self.raw_x = raw_x
        self.raw_y = raw_y

        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(clr.GREEN)
        self.rect = self.image.get_rect()
        self.set_grid_positions()

    def set_grid_positions(self):
        self.rect.x = (int(self.raw_x/self.side_length)
            * self.side_length)
        
        self.rect.y = (int(self.raw_y/self.side_length)
<<<<<<< HEAD
            * self.side_length)
        
class Button(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, width, length, color):
        super().__init__()
        
        self.width = width
        self.length = length
        
        self.image = pygame.Surface([self.width, self.side_length])
        self.image.fill(color)
        self.rect = self.image.get_rect
        
        self.rect.x = x_position
        self.rect.y = y_position

    def update(self, click_position):
        self.mouse_x, self.mouse_y = click_position
        self.detect_cursor(self)
=======
            * self.side_length)
>>>>>>> parent of b2e00f6... Add Button class and init method
