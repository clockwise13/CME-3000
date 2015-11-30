# classes for Corpo Master 3000
import config
from config import *

class Peon():
    # single Peon init at pos; try with a random pos tuple
    def __init__(self):
        self.status = True
        self.pos = ((config.random.randrange(10, config.res_y),
                     config.random.randrange(10, config.res_y /2)))
        self.image = "Peon.png"
        self.vec = random.choice((1,-1))
        config.Peon_list.append(self)
        self.update()
        
    def Peon_blit(self, position, display_name):
        # change to make it blit on to a already initiated display
        config.helpers.displayer(config.res_x, config.res_y)
        config.helpers.blitter(display_name, "Peon", self.pos)
        
    def mover(self):
        print self.pos
        print
        random_offset = config.random.randrange(1, config.res_x/40) 
        self.pos = self.pos[0] + random_offset * self.vec, self.pos[1]
        print self.pos
        print
        return self.pos
        
    def update(self):
        if self.status == True:
            self.mover()
            #self.Peon_blit(self.pos, DISPLAY)


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

