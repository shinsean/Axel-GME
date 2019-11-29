import pygame
import json

import map_editor as mp_edit
import colors as clr

pygame.init()

#TODO: Make the user be able to change the display width and height. 
# Possibly use a .txt file or JSON.
with open('settings.json') as settings_json:
    settings = json.load(settings_json)

for setting in settings["main"]:
    FPS = setting["FPS"]
    DISPLAY_WIDTH = setting["DISPLAY_WIDTH"]
    DISPLAY_HEIGHT = setting["DISPLAY_HEIGHT"]

# FPS = 30
# DISPLAY_WIDTH = 600
# DISPLAY_HEIGHT = 600
DISPLAY = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

clock = pygame.time.Clock()

def main_loop():
    program_state = mp_edit.Editing_State(DISPLAY_WIDTH, DISPLAY_HEIGHT, 30)
    
    while True:
        pressed_buttons = pygame.key.get_pressed()
        program_state.handle_events(pressed_buttons, 30)

        program_state.update()
        DISPLAY.fill(clr.BLACK)

        program_state.render(DISPLAY)

        pygame.display.update()
        clock.tick(FPS)

main_loop()