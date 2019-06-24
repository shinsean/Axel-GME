from import_libraries import *

pygame.init()

#TODO: Make the user be able to change the display width and height. 
# Possibly use a .txt file or JSON.
FPS = 30
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
DISPLAY = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

clock = pygame.time.Clock()