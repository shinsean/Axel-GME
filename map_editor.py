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

class Editing_State(State):
    def __init__(self):
        # Will add more here as I make the program.
        super().__init__()

        self.all_sprites_list = pygame.sprite.Group()
        # Not exactly sure yet what I need this for.
        self.wall_list = pygame.sprite.Group()

    # Core function.
    def render(self, display):
        self.all_sprites_list.draw(display)
    #

    # Core function.
    # I don't think I need this method which is why I am leaving it blank.
    def update(self):
        pass
    #

    # Core function.
    # MAJOR TODO: Add a way (most likely right click) for the user to delete
    # placed blocks. If it is right click, make the program differentiate
    # between left click and right click.
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_program()

            if event.type == MOUSEBUTTONDOWN:
                self.raw_x, self.raw_y = event.pos
                self.block = Block(raw_x, raw_y)
                self.wall_list.add(block)
                self.all_sprites_list.add(block)
    #