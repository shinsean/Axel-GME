from map_assets import *

# TODO: Have a way to save whiel creating a new file.
def save_current_map(map_list_rep):
    open_save_file = open('test_save.txt', 'w+')
    for rows in map_list_rep:
        for letter in rows:
            open_save_file.write(letter)
    open_save_file.close()