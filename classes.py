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
    """single Peon init at pos; try with a random pos tuple
    class rewritten to be a derivate of the pygame.sprite class template"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Speed vectors
        self.vector = [0,0] # 2-D vector for movement and collision calcs

        #Right and left facing walking frames
        self.walking_frames_l = []
        self.walking_frames_r = []

        #Peon direction
        self.direction = config.random.choice(("R","L"))

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

        # get timestamp of the initialization of a given Peon instance

        self.time = config.time.time()


        # add instance of Peon object to Peon_list Sprite group
        self.add(config.Peon_list)
        self.add(config.Object_list)


    def update(self):
        #Move left and right
        self.rect.center = (self.rect.center[0] + self.vector[0], \
        self.rect.center[1] + self.vector[1])

        self.random_silly_walk()

        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]


    def random_silly_walk(self):
        # randomized stop-and-walk behavior
        update_time = config.time.time()
        delta_time_floor = int(update_time - self.time)

        if delta_time_floor > 0 and delta_time_floor % 9 == 0:
            walk_or_go = config.random.randrange(1,5)
            #print "Timestamp: " + str(delta_time_floor)
            #print "Decision: " + str(walk_or_go)
            #print

            if walk_or_go == 1:
                self.direction = "L"
                self.go_left()
            elif walk_or_go == 2:
                self.direction = "R"
                self.go_right()
            elif walk_or_go == 3:
                self.stop()
            else:
                pass
        else:
            pass


        #Moving controlled by player
    def go_left(self):
            self.vector[0] = -2
            self.direction = "L"

    def go_right(self):
            self.vector[0] = 2
            self.direction = "R"

    def stop(self):
            self.vector = [0,0]

class Head(pygame.sprite.Sprite):
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

class Spawn(pygame.sprite.Sprite):
    """A general spawner class: the idea is to place this in a level and make
    it spawn X by using X's internal methods; requires method consistency across
    classes obviously duh!
    Update: the class is now a child of the pygame.sprite.Sprite class, to
    enable the use of the update() method on every frame.
    """
    def __init__(self, object_to_spawn, position_to_spawn, spawn_interval, limiter):
        super(Spawn, self).__init__()
        self.type = object_to_spawn
        self.pos = position_to_spawn

        # this is the end of the range for the random generator, tweak to make spawning less/more frequent
        self.interval = spawn_interval

        #the limiter deactivates the spawner after n critters are spawned in; usefull for un-clusterfucking the spawn procedure
        self.limiter = limiter

        # flag for turning a spawner on and off
        self.active = False

        # make the spawner a member of the sprite group in config
        self.add(config.Spawner_list)

    def activate(self):
        # turn spawner on
        self.active = True

    def deactivate(self):
        #turn spawner off
        self.active = False

    def update(self):
        if self.active == True:
            if random.randrange(0, self.interval) <= 1 and len(config.Peon_list) < self.limiter or self.limiter == -1:
                """ Random number generation based spawning: with every program
                loop, if the spawning method is called it will have a
                spawn_interval/100 chance of creating an object.
                Use -1 value for unlimited spawning and resulting clusterfuck."""

                if self.type == "Peon":
                    # spawn the critter
                    obj = Peon()
                    obj.rect.x = self.pos[0]
                    obj.rect.y = self.pos[1]

                    if obj.direction == "L":
                        obj.go_left()
                    else:
                        obj.go_right()
                else:
                    pass
            elif len(config.Peon_list) >= self.limiter:
                print "Len too long, deactivating"
                self.deactivate()
        else:
            pass

    def get_spawner_attr(self):
        # a get func for easy lookup of each spawner instance's attributes
        attr_list = [self.type, self.pos, self.interval, self.limiter, self.active]
        for attr in attr_list:
            print str(attr) + "\n"

class Level_creator():
    def __init__(self, ogur):
        """"Change of plans: create pickled instances of levels in the
        levelPickler module. Use this class to unpickle those instances and
        create a level out of them."""

        new_ogur = cPickle.load(ogur)

        self.music = new_ogur.music # assign the ambient music object here
        self.bg = new_ogur.background #load background image
        self.spawners = new_ogur.spawners # load spawners
        self.misc = new_ogur.misc

    def play_it_again_Sam(self):
        music_object = pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1) # plays music; mixer picks the channel; -1 for infinite looping

    def music_volume(self, volume):
        pygame.mixer.music.set_volume(volume) # set's music volume; use float values from 0.0 to 1.0

    def stop_the_music(self):
        pygame.mixer.music.stop() # stops the music playback

    def set_background(self):
        # this sets the level background to be filled with every frame (?)
        current_Display = pygame.display.get_surface() # retreive the currently used display surface
        if self.bg == None:
            current_Display.fill(config.WHITE)
            print "YoMamaError nr. 3423425678: No display Surface to use."
        else:
            # make it blit with the ever useful GUI_OBJECT class
            bg  = GUI_OBJECT(self.bg, (config.res_x/2,config.res_y/2), None, None, 960, 665)

    def activate_spawners(self):
        """Activates spawners in the Object_list Sprite group. This has to be
        made via loop, since the spwaners-as-members-of-a-group live in the
        config module's namespace."""

        for obj in config.Spawner_list:
            obj.activate()
            #obj.active = True

    def deactivate_spawners(self):
        """Deactivates spawners, mimicking the activate_spawners behavior"""

        for obj in config.Spawner_list:
            obj.deactivate()

    def get_spawners(self):
        """custom debug function for getting the spawner attributes, links with
        the get_spawner_attr() function in the Spawn class"""

        for obj in config.Object_list:
            if obj.__class__.__name__ == "Spawn":
                obj.get_spawner_attr()

    def set_misc_elements(self):
        """this will need to be filled out if we have any misc
        items that need special treatment"""
        pass

class Event():
    "A class meant to handle I/O events in the game, possibly other ones as well"
    def __init__(self):
        mousex = 0 # x coordinate of the mouse event
        mousey = 0 # y coordinate of the mouse event
        self.event = []
        self.time = config.time.time() # init timestamp
        self.peon_enviro_collisions = [] # empty list for collider
        self.peon_head_collisions = [] # empty list for collider


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

    def get_delta(self):
        delta = config.helpers.delta_timer(self)
        self.check_time_cycles(delta)

    def check_time_cycles(self, delta):
        if delta > 0 and delta % 9 == 0:
            print "ping! " + str(delta % 9)
        else:
            print delta % 9


    def get_collisions(self):
        """Checks for collisions between objects' lists pairwise, returns a dict
        of colliding objects"""

        # Peon_list x Enviro_list --> returns dict

        self.peon_enviro_collisions = pygame.sprite.groupcollide(config.Peon_list,\
        config.Enviro_list, False, False)

        # Peon_list x Head_list --> returns dict

        self.peon_head_collisions = pygame.sprite.groupcollide(config.Peon_list,\
        config.Head_list, False, False)


    def process_collisions(self):
        try:
            for p in self.peon_enviro_collisions:
                p.vector[0] = p.vector[0] * -1
        except:
            print "The process_collisions method in Event failed"




class GUI_OBJECT(pygame.sprite.Sprite):
    """GUI class template for graphic objects for the interface and then
    specify the details for every group (buttons, sliders, meters etc.)
    IMPORTANT: pass the variable used for creating the event handler to the
    function, don't create a new one!"""

    def __init__(self, image, pos, func, event_handler_instance, width, height):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet(image)
        self.pos = pos
        self.function = func # pass None to make a non-interactive object
        self.event_handler = event_handler_instance
        self.dimension = (width, height)
        self.image = sprite_sheet.get_image(0, 0, self.dimension[0], self.dimension[1])
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.add(config.GUI_list)

    def update(self):
        if self.function != None:
            self.event_handler.get_events()
            # check for mouse-click collsions with the button rect, then do stuff
            if self.event_handler.event.type == config.pygame.MOUSEBUTTONDOWN and \
            self.rect.collidepoint(self.event_handler.event.pos) == True:
                self.function()
            else:
                pass
        else:
            pass

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

class Environment_Wall(pygame.sprite.Sprite):
    def __init__(self):
        super(Environment_Wall, self).__init__()
        self.pos = (None, None) # pos to be updated through class methods
        self.image = config.pygame.image.load(config.os.path.join(os.getcwd() +\
        "/Resources/Walls/" + "metal.png"))
        self.rect = self.image.get_rect()
        self.mass = 101 # this makes the object to massive to be moved
        self.add(config.Enviro_list)
        self.add(config.Object_list)

    def set_pos(self, pos_tuple):
        # use this method to set the pos for the object
        self.pos = pos_tuple
        self.rect.center = self.pos
        print self.pos

    def update(self):
        pass
