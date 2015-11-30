# classes for Corpo Master 3000
import config
from config import *

class Peon():
    # single Peon init at pos; try with a random pos tuple
    def __init__(self, position):
        self.status = True
        self.pos = position
        self.vec = random.choice((1,-1))
        config.Peon_list.append(self)
    def Peon_blit(self, position, display_name):
        config.helpers.displayer(config.res_x, config.res_y)
        config.helpers.blitter(display_name, "Peon", position)

class Head():
    def __init__(self, position):
        self.status = True
        self.pos = position
    def Head_blit(self, position, display_name):
        config.helpers.displayer(config.res_x, config.res_y)
        config.helpers.blitter(display_name, "TheBigHead", position)
 
class Projectile():
    # here does the code lie
    pass

