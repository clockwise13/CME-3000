import config
from config import pygame as pygame

pygame.init()



def displayer(res_x, res_y):
    # initiates a Surface display object with a given resolution
    DISPLAY = pygame.display.set_mode((res_x, res_y))
    pygame.display.set_caption("Testy medyczne na Twojej Starej")
    return DISPLAY

def blitter(display_name, object_name, position):
    # takes object's name and uses it to build a filename, then blit's at pos
    pix = pygame.image.load(object_name + ".png")
    display_name.blit(pix, position)
    pygame.display.update()
    print 'displaying'

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

