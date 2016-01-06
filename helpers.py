# -*- coding: utf-8 -*-
import config
from config import *

def displayer():
    # White syntactic sugar (sniff, sniff, snort) // added alpha value
    WHITE = (255, 255, 255, 1)
    # initiates a Surface display object with a resolution defined in config as res_x, res_y
    DISPLAY = pygame.display.set_mode((config.res_x, config.res_y))
    pygame.display.set_caption("Testy medyczne na Twojej Starej")
    return DISPLAY

def blitter(display_name, image, position):
    # takes object's image parameter and blits it to the display
    # note: the pix variable depreciated in favor of image loading in the Sprite class definitions
    display_name.blit(image, position)
    pygame.display.update()

def quitter():
    # handy way to execute a quit sequence without rewriting shit
    pygame.quit()
    sys.exit()

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
