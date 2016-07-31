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

        def get_spawner_attr(self):
            # a get func for easy lookup of each spawner instance's attributes
            return (self.type, self.pos, self.interval, self.limiter, self.active)

class Level_creator():
    def __init__(self, ogur):
        """"Change of plans: create pickled instances of levels in the levelPickler module. Use this class to unpickle those
        instances and create a level out of them."""
        #print "This is the ogur variable: " + str(ogur) # debug print
        new_ogur = cPickle.load(open(os.getcwd() + "/" + 'Levels' + '/' + "level1ogur.txt", "rb"))
        print new_ogur
        #print "This is the new_ogur variable: " + str(new_ogur) # debug print

        self.music = new_ogur.music # pygame.mixer.Sound(new_ogur.music) # create a Sound object
        self.bg = new_ogur.background #load background image
        self.spawners = new_ogur.spawners # load spawners
        self.misc = new_ogur.misc


    def play_it_again_sam(self):
        print self.music
        #self.music.play(-1) # start playing the Sound object; mixer picks the channel; -1 for infinite looping

    def music_volume(self, volume):
        self.music.set_volume(volume) # set's music volume; use float values from 0.0 to 1.0

    def stop_the_music(self):
        self.music.stop() # stops the music playback

    def set_background(self):
        # this sets the level background to be filled with every frame (?)
        currentDisplay = pygame.display.get_surface() # retreive the currently used display surface
        bg = pygame.image.load(self.bg) # create a Surface object from the BG image
        currentDisplay.blit(bg) # blit the GB Surface onto the display Surface

    def spawn_spawners(self):
        # this turns on the random spawn mechanic of the Spawn class; will not yield any result if the spawners are not active!
        for spawner in self.spawners:
            spawner.spawning()

    def activate_spawners(self):
        for spawner in self.spawners:
            spawner.activate()

    def deactivate_spawners(self):
        for spawner in self.spawners:
            spawner.deactivate()

    def get_spawners(self):
        temp_spawner_table = []
        for spawner in self.spawners:
            spawner_lookup = spawner.get_spawner_attr()
            temp_spawner_table.append(spawner_lookup)
        return temp_spawner_table

    def set_misc_elements(self):
        # this will need to be filled out if we have any misc items that need special treatment
        pass

class Event():
    "A class meant to handle I/O events in the game, possibly other ones as well"
    def __init__(self):
        mousex = 0 # x coordinate of the mouse event
        mousey = 0 # y coordinate of the mouse event
        self.event = []

    def get_events(self):
        event_list = config.pygame.event.get()
        for event in event_list:
            """If the event getter will be invoked every frame, won't it lag down the input? TEST THIS"""
            self.event = event
            if event.type == config.pygame.QUIT or \
            (event.type == config.pygame.KEYUP and \
            event.key == config.pygame.K_ESCAPE):
                config.quitter()

                # mouse movement and clicking handler

            elif event.type == config.pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                return event
            elif event.type == config.pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                return event
            else:
                return None

class GUI_BUTTON(pygame.sprite.Sprite):
    """Might be a good idea to use class inheritance for this - make a GUI class as template for interactive
    graphic objects for the interface and then specify the details for every group (buttons, sliders, meters etc.)
    IMPORTANT: pass the variable used for creating the event handler to the function, don't create a new one!"""
    def __init__(self, image, pos, func, event_handler_instance, width, height):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet(image)
        self.pos = pos
        self.function = func
        self.event_handler = event_handler_instance
        self.dimension = (width, height)
        self.image = sprite_sheet.get_image(0, 0, self.dimension[0], self.dimension[1])
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.add(config.GUI_list)

    def update(self):
        self.event_handler.get_events()

        # check for mouse-click collsions with the button rect, then do stuff
        if self.event_handler.event.type == config.pygame.MOUSEBUTTONDOWN and \
        self.rect.collidepoint(self.event_handler.event.pos) == True:
            self.function()
        else:
            pass
