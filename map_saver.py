from map_assets import *

# TODO: Have a way to save whiel creating a new file.
def save_current_map(map_list_rep):
    map_list_rep_edit = insert_newlines(map_list_rep)
    open_save_file = open('current_save.txt', 'w+')
    for rows in map_list_rep_edit:
        for letter in rows:
            open_save_file.write(letter)
    open_save_file.close()