import pygame

import colors as clr

class Block(pygame.sprite.Sprite):
    def __init__(self, raw_x, raw_y):
        super().__init__()

        self.width = 30
        self.length = 30

        self.raw_x = raw_x
        self.raw_y = raw_y

        self.image = pygame.Surface([self.width, self.length])
        self.image.fill(clr.GREEN)
        self.rect = self.image.get_rect()
        self.set_grid_positions()

    def set_grid_positions(self):
        self.rect.x = (int(self.raw_x/self.width)
            * self.width)
        
        self.rect.y = (int(self.raw_y/self.length)
            * self.length)
        
class Button(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, width, length, color, alt_color):
        super().__init__()
        
        self.width = width
        self.length = length
        
        self.reg_color = color
        self.alt_color = alt_color
        self.color = self.reg_color
        
        self.image = pygame.Surface([self.width, self.side_length])
        self.image.fill(self.color)
        self.rect = self.image.get_rect
        
        self.rect.x = x_position
        self.rect.y = y_position

    def update(self, cursor_position):
        self.cursor_x, self.cursor_y = cursor_position
        self.detect_mouse()

    def detect_mouse(self):
        if self.cursor_x >= self.rect.x and self.click_x <= (self.rect.x + self.length):
            if self.cursor_y >= self.rect.y and self.click_y <= (self.rect.y + self.width):
                self.hover = True
        else:
            self.hover = False

        if self.hover == True:
            self.color = self.alt_color
        else:
            self.color == self.reg_color
