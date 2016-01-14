# classes for Corpo Master 3000
import config
from config import *

class Peon(config.pygame.sprite.Sprite):
    # single Peon init at pos; try with a random pos tuple
    # class rewritten to be a derivate of the pygame.sprite class template
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        '''Old code for movement here:
        # randomly assign a position to the Peon instance;
        #might be replaced by a later spawner on a group level        
        self.pos = ((config.random.randrange(10, config.res_x),
                     config.random.randrange(10, config.res_y /2)))
        self.direction = "R"'''
        
        #right and left facing walking frames
        self.walking_frames_l = []
        self.walking_frames_r = []

        #loading the sprite sheet
        sprite_sheet = SpriteSheet("Peon_Animated.png")

        #Appending to the right-facing walking frames
        #Parameters for .get_image: (X, Y, WIDTH, HEIGHT)
        image = sprite_sheet.get_image(0, 0, 25, 72)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(25, 0, 25, 72)
        self.walking_frames_r.append(image)
        
        #Flipping right-facing walking frames
        #And appending them to left-facing walking frames
        image = sprite_sheet.get_image(0, 0, 25, 72)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(25, 0, 25, 72)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        

        # add instance of Peon object to Peon_list Sprite group
        self.add(config.Peon_list)

    def update(self):

        '''Old code here:        
        random_offset = config.random.randrange(1, config.res_x/50)
        self.vec = random.choice((1,-1))
        self.rect.move_ip(random_offset * self.vec, 0)'''
        
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift #This needs to change!
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
            
    def direction(self):
        if self.rect.x = res_x:
            self.direction = "R"
            self.change_x = 6
        elif self.rect.x = 0:
            self.direction = "L"
            self.change_X = -6
        
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

class SpriteSheet(object):
    def __init__(selfself, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.BLACK)
        return image

class Projectile():
    # here does the code lie
    pass
