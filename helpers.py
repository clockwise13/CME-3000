# -*- coding: utf-8 -*-
import config
from config import *

def displayer():
    # initiates a Surface display object with a resolution defined in config as res_x, res_y
    DISPLAY = pygame.display.set_mode((config.res_x, config.res_y))
    pygame.display.set_caption("CME DREITAUESEND")
    return DISPLAY

def quitter():
    # handy way to execute a quit sequence without rewriting shit
    pygame.quit()
    sys.exit()

def new_game():
    # open first level from a pickled file

    cur_dir = os.getcwd()
    input_dir = cur_dir + "/" + 'Levels' + '/'

    # initialize level elements
    with open(input_dir + 'level1ogur.txt', 'rb') as input_file:
        New_level = classes.Level_creator(input_file)
        # purge the GUI_list to remove the clickable rects from the menu's buttons
        config.GUI_list.empty()
        New_level.set_background()
        New_level.play_it_again_Sam()
        New_level.activate_spawners()
    return New_level

def collider(test_subject):
    # uses the default pygame Sprite collision method
    collisions_list = pygame.sprite.spritecollide(test_subject, config.Peon_list, True)

def get_peons():
    # get's the list of Peons and prints it out to the interpreter
    for p in config.Peon_list:
        print dir(p) + "\n"
    return config.Peon_list

def saver():
    pass
    # return save

def loader():
    pass
    # return load
