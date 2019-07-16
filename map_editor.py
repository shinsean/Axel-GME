from map_saver import *

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
    def __init__(self, display_width, display_height, block_side_length):
        # Will add more here as I make the program.
        super().__init__()

        self.all_sprites_list = pygame.sprite.Group()
        # Not exactly sure yet what I need this for.
        self.wall_list = pygame.sprite.Group()

        self.reset_list(display_width, display_height, block_side_length)

    # TODO: Change this so that it factors in the screen size in the future. 
    def reset_list(self, display_width, display_height, block_side_length):
        self.temp_map_list = []
        self.map_list = []

        for j in range(int(display_width/block_side_length)):
            print(j)
            print((int(display_width/block_side_length)))
            if j == (int(display_width/block_side_length)) - 1:
                self.temp_map_list.append("0\n")
            else:
                self.temp_map_list.append("0")

        for i in range(int(display_height/block_side_length)):
            self.map_list.append(self.temp_map_list)

        print(self.map_list)
        save_current_map(self.map_list)

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
    def handle_events(self, pressed_button):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_program()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.raw_x, self.raw_y = event.pos
                self.block = Block(self.raw_x, self.raw_y)
                self.wall_list.add(self.block)
                self.all_sprites_list.add(self.block)
    #