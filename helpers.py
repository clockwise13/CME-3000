# -*- coding: utf-8 -*-
import config
from config import *

def displayer():
    # initiates a Surface display object with a resolution defined in config as res_x, res_y
    DISPLAY = pygame.display.set_mode((config.res_x, config.res_y))
    pygame.display.set_caption("Testy medyczne na Twojej Starej")
    return DISPLAY

def quitter():
    # handy way to execute a quit sequence without rewriting shit
    pygame.quit()
    sys.exit()

def new_game():
    # open first level from a pickled file

    cur_dir = os.getcwd()
    input_dir = cur_dir + "/" + 'Levels' + '/'

    with open(input_dir + 'level1ogur.txt', 'rb') as input_file:
        New_level = classes.Level_creator(input_file)

    New_level.play_it_again_Sam()
    GUI_list = [] # to avoid redrawing the GUI elements
    New_level.set_background()
    New_level.get_spawners()
    New_level.activate_spawners()
    return New_level


def collider(test_subject):
    # uses the default pygame Sprite collision method
    collisions_list = pygame.sprite.spritecollide(test_subject, config.Peon_list, True)

def get_pos():
    pass
    # return item_pos

def get_peons():
    pass
    # return peon_list

def get_head():
    pass
    # return head_status

def saver():
    pass
    # return save

def loader():
    pass
    # return load
