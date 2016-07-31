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

    """with open(cur_dir + "/" + 'Levels' + '/' + "level1ogur.txt", 'rb') as input_file:
        new_level = cPickle.load(input_file)
        #level_one = classes.Level_creator(input_file)
        print "New game initiated!"""
    with open(input_dir + 'level1ogur.txt', 'rb') as input_file:
        new_level = classes.Level_creator(input_file)

    #load_level_one = config.classes.Level_creator(input_file)
    #load_level_one.play_it_again_sam()

def spawner(class_type, init_values):
    obj = class_type(init_values)
    config.Head_list.append(obj)
    for lst in config.Object_list:
            for obj_name in lst:
                print "Pizda nad głową!"
            #   print len(config.Object_list)
            #   print
            #   print len(lst)
    else:
        print "Nic"


def collider(test_subject):
    # uses the default pygame Sprite collision method
    collisions_list = pygame.sprite.spritecollide(test_subject, config.Peon_list, True)

def mover(pos, vector):
    pass
    # return new_item_pos

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
