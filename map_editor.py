from map_assets import *

def end_program():
    pygame.quit()
    quit()

class State():
    def __init__(self):
        pass

    def render(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self):
        raise NotImplementedError

class Game_State(State):
    def __init__(self):
        # Will add more here as I make the program.
        super().__init__()

        self.all_sprites_list = pygame.sprite.Group()
        # Not exactly sure yet what I need this for.
        self.wall_list = pygame.sprite.Group()