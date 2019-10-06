import pygame

import map_assets as mp_ast

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
        super().__init__()

        self.all_sprites_list = pygame.sprite.Group()
        # Not exactly sure yet what I need this for.
        self.wall_list = pygame.sprite.Group()
        # Buttons will go into this list instead of the all_sprites_list.
        self.buttons_list = pygame.sprite.Group()

        self.temp_map_list = []
        self.map_list = []

        # TODO: Change this so that the desired_save is changeable.
        self.load_save("save_file.txt", display_width, display_height, block_side_length)

    def load_save(self, desired_save, display_width, display_height, block_side_length):
        try:
            with open(desired_save, "r") as opened_file:
                self.opened_save_file = opened_file.read()

            self.convert_save_to_list(self.opened_save_file)
            self.create_loaded_blocks(block_side_length)
        # TODO: Change this so that the user can choose whether to reset save file.
        # In fact, just allow them to create a new file as an option
        # instead of resetting the map and having to save again.
        except:
            self.reset_map(display_width, display_height, block_side_length)

    def convert_save_to_list(self, opened_save_file):
        self.opened_save_file = self.opened_save_file.split()
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

        self.save_current_map(self.map_list)

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
    def update(self):
        self.all_sprites_list.update()
    #

    # Core function.
    def handle_events(self, pressed_button, block_side_length):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save_current_map(self.map_list)
                end_program()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.left_click, self.scroll_button, self.right_click = pygame.mouse.get_pressed()
                if self.left_click == 1:
                    self.create_block(event.pos, block_side_length)
                elif self.right_click == 1:
                    self.delete_block(event.pos, block_side_length)
    #

    # TODO: Have a way to save whiel creating a new file.
    def save_current_map(self, map_list_rep):
        self.open_save_file = open('save_file.txt', 'w')
        for rows in map_list_rep:
            for letter in rows:
                self.open_save_file.write(letter)
        self.open_save_file.close()

    def update_map_list(self, mouse_click_x_location, mouse_click_y_location,
        block_side_length, action_type):
        self.list_index_x = int(mouse_click_x_location/block_side_length)
        self.list_index_y = int(mouse_click_y_location/block_side_length)
        
        if action_type == "Create":
            self.map_list[self.list_index_y][self.list_index_x] = "X"
        elif action_type == "Delete":
            self.map_list[self.list_index_y][self.list_index_x] = "0"

    def create_block(self, click_position, block_side_length):
        self.raw_x, self.raw_y = click_position
        self.block = mp_ast.Block(self.raw_x, self.raw_y)
        self.update_map_list(self.raw_x, self.raw_y, block_side_length, "Create")
        self.wall_list.add(self.block)
        self.all_sprites_list.add(self.block)

    def delete_block(self, click_position, block_side_length):
        self.raw_click_x, self.raw_click_y = click_position
        self.grid_set_x = (int(self.raw_click_x/block_side_length) * block_side_length)
        self.grid_set_y = (int(self.raw_click_y/block_side_length) * block_side_length)
        for block in (list(self.wall_list)):
            if (block.rect.x, block.rect.y) == (self.grid_set_x, self.grid_set_y):
                block.kill()
        
        self.update_map_list(self.grid_set_x, self.grid_set_y, block_side_length, "Delete")
