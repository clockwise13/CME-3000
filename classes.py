# classes for Corpo Master 3000
import config
from config import *

class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        #convert alpha command
        image.set_colorkey(config.BLACK) # (0, 0, 0, XXX)
        return image

class Peon(pygame.sprite.Sprite):
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

        #Speed vectors
        self.change_x = 0
        self.change_y = 0

        #Right and left facing walking frames
        self.walking_frames_l = []
        self.walking_frames_r = []

        #Player direction
        self.direction = "R"

        #Loading the sprite sheet
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
        self.add(config.Object_list)


    def update(self):
        #Move left and right
        self.rect.x += self.change_x
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        #Moving controlled by player
    def go_left(self):
            self.change_x = -6
            self.direction = "L"

    def go_right(self):
            self.change_x = 6
            self.direction = "R"

    def stop(self):
            self.change_x = 0

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

class Spawn():
    """ a general spawner class: the idea is to place this in a level and make it spawn X by using X's internal methods; requires method consistency across classes obviously duh!"""
    def __init__(self, object_to_spawn, position_to_spawn, spawn_interval, limiter):
        self.type = object_to_spawn
        self.pos = position_to_spawn

        # this is the end of the range for the random generator, tweak to make spawning less/more frequent
        self.interval = spawn_interval

        #the limiter deactivates the spawner after n critters are spawned in; usefull for un-clusterfucking the spawn procedure
        self.limiter = limiter

        # flag for turning a spawner on and off
        self.active = False

    def activate(self):
        # turn spawner on
        self.active = True
        print "Spawner active"

    def deactivate(self):
        #turn spawner off
        self.active = False
        print "Spawner deactivated"

    def spawning(self):
        if self.active == True:
            if random.randrange(0, self.interval) <= 1 and len(config.Peon_list) < self.limiter or self.limiter == -1:
                """ Random number generation based spawning: with every program loop, if the spawning method is called it will have a spawn_interval/100 chance of creating an object. Use -1 value for unlimited spawning and resulting clusterfuck."""

                if self.type == "Peon":
                    # spawn the critter
                    obj = Peon()
                    obj.rect.x = self.pos[0]
                    obj.rect.y = self.pos[1]
                    # randomly assign an initial vector of movement - move this to a more sensible place
                    movin = random.choice(("left", "right"))
                    if movin == "left":
                        obj.go_left()
                    else:
                        obj.go_right()
                    return
                else:
                    pass
            elif len(config.Peon_list) >= self.limiter:
                self.deactivate()
                return

class Level_creator():
    def __init__(self, background, object_dict, music):
        """" all of the components of a level are to be placed below; this class is only for the purposes of level creation in the levelPickler module; any name assignment and name persistency issues should be handled by a separate class and the use of unpickling thr pre-prepared levels"""
        # set the background of the level to an image
        self.background = pygame.image.load(background).convert()

        # use an object dictionary to organize the objects
        self.object_dict = object_dict

        # list of spawners represented by tuples of arguments to be passed into the Spawn class
        self.spawners = []

        # music loader
        self.music = pygame.mixer.Sound(music)

        # unpack the dictionary with the object lists and place them in the level
        """ This is the tricky part: I need to find a way to make a series of assignments that will place everything where it needs to be (using tuples to indicate pos); this will most likely demand some disciplined formatting of the inputs for the level construction"""
        for key in self.object_dict:
            if key == Peon:
                pass
            elif key == Head:
                pass
            elif key == Projectile:
                pass
            elif key == Spawn:
                self.spawners = self.object_dict[Spawn]
            else:
                pass
