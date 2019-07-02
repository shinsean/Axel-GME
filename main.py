from map_editor import *

pygame.init()

#TODO: Make the user be able to change the display width and height. 
# Possibly use a .txt file or JSON.
FPS = 30
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
DISPLAY = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

clock = pygame.time.Clock()

def main_loop():
    program_state = Editing_State()
    
    while True:
        pressed_buttons = pygame.key.get_pressed()
        program_state.handle_events(pressed_buttons)

        # Placeholder in case of the future.
        program_state.update()

        program_state.render(DISPLAY)

        pygame.display.update()
        clock.tick(FPS)

main_loop()