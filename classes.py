# classes for Corpo Master 3000
import config
from config import *

class Peon(config.pygame.sprite.Sprite):
    # single Peon init at pos; try with a random pos tuple
    # class rewritten to be a derivate of the pygame.sprite class template
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # randomly assign a position to the Peon instance; might be replaced by a later spawner on a group level
        self.pos = ((config.random.randrange(10, config.res_x),
                     config.random.randrange(10, config.res_y /2)))
        self.image = config.pygame.image.load("Peon_Animated.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        # add instance of Peon object to Peon_list Sprite group
        self.add(config.Peon_list)

    def update(self):
        random_offset = config.random.randrange(1, config.res_x/50)
        #self.rect.x = self.pos[0] + random_offset * self.vec
        self.vec = random.choice((1,-1))
        self.rect.move_ip(random_offset * self.vec, 0)

class Head(config.pygame.sprite.Sprite):
    def __init__(self):
        super(Head, self).__init__()
        self.pos = (config.res_x - 200, config.res_y - 300)
        self.image = config.pygame.image.load("TheBigHead.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.vec = -1 # initial 1-D movement vector to start movement up
        # add instance of Head to Object_list and Head_list
        self.add(config.Head_list)
        self.add(config.Object_list)

    def update(self):
        random_offset = config.random.randrange(1, config.res_x/40) # offset for prototype purposes only
        # a simple sample of a collison mechanic; the goal is to bounce the fucket of the edges of the window
        if self.rect.top <= 3 or self.rect.bottom >= config.res_y - 3:
            self.vec = -self.vec
        else:
            pass
        self.rect.move_ip(0, random_offset * self.vec)

class Projectile():
    # here does the code lie
    pass
