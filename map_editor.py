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

        self.temp_map_list = []
        self.map_list = []

        # TODO: Change this so that the desired_save is changeable.
        self.load_save("test_save.txt", display_width, display_height, block_side_length)

    def load_save(self, desired_save, display_width, display_height, block_side_length):
        try:
            self.opened_save_file = open(desired_save, "r")
            self.convert_save_to_list(self.opened_save_file)
            self.create_loaded_blocks(block_side_length)
        # TODO: Change this so that the user can choose whether to reset save file.
        # In fact, just allow them to create a new file as an option
        # instead of resetting the map and having to save again.
        except:
            self.reset_map(display_width, display_height, block_side_length)

    def convert_save_to_list(self, opened_save_file):
        for rows in opened_save_file:
            for letters in rows:
                self.temp_map_list.append(letters)

            self.map_list.append(self.temp_map_list)
            self.temp_map_list = []

    # TODO: This will be used when the user wants to create a new save file. 
    def reset_map(self, display_width, display_height, block_side_length):
        for j in range(int(display_width/block_side_length)):
            self.temp_map_list.append("0")
        self.temp_map_list.append("\n")

        for i in range(int(display_height/block_side_length)):
            self.map_list.append(list(self.temp_map_list))

        save_current_map(self.map_list)

    def create_loaded_blocks(self, block_side_length):
        for y_index in range(len(self.map_list)):
            for x_index in range(len(self.map_list[y_index])):
                if self.map_list[y_index][x_index] == 'X':
                    self.create_block(((x_index * block_side_length),
                        (y_index * block_side_length)), block_side_length)

    # Core function.
    def render(self, display):
        self.all_sprites_list.draw(display)
    #

    # Core function.
    # I don't think I need this method which is why I am leaving it blank.
    def update(self):
        pass
    #

    # Clean this up.
    def update_map_list(self, mouse_click_x_location, mouse_click_y_location, block_side_length):
        self.list_index_x = int(mouse_click_x_location/block_side_length)
        self.list_index_y = int(mouse_click_y_location/block_side_length)

        self.map_list[self.list_index_y][self.list_index_x] = "X"

    # Core function.
    # MAJOR TODO: Add a way (most likely right click) for the user to delete
    # placed blocks. If it is right click, make the program differentiate
    # between left click and right click.
    def handle_events(self, pressed_button, block_side_length):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_current_map(self.map_list)
                end_program()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.left_click, self.scroll_button, self.right_click = pygame.mouse.get_pressed()
                self.create_block(event.pos, block_side_length)
    #

    def create_block(self, click_position, block_side_length):
        self.raw_x, self.raw_y = click_position
        self.block = Block(self.raw_x, self.raw_y)
        self.update_map_list(self.raw_x, self.raw_y, block_side_length)
        self.wall_list.add(self.block)
        self.all_sprites_list.add(self.block)
