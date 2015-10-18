# -*- coding: utf-8 -*-
import config
from config import *

# I don't like these imports here

print __name__

def displayer(res_x, res_y):
    # White syntactic sugar (sniff, sniff, snort) // added alpha value
    WHITE = (255, 255, 255, 1)
    # initiates a Surface display object with a given resolution
    DISPLAY = pygame.display.set_mode((res_x, res_y))
    pygame.display.set_caption("Testy medyczne na Twojej Starej")

    DISPLAY.fill(WHITE)
    return DISPLAY

def blitter(display_name, object_name, position):
    # takes object's name and uses it to build a filename, then blit's at pos
    pix = pygame.image.load(object_name + ".png")
    display_name.blit(pix, position)
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


def collider():
    pass

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

