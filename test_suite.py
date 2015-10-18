# test module for game

# place to import game files


import config
from config import *

# Removed additional imports to streamline importing queue



# GLOBALS

image = "Peon"

# blitter and displayer import replaced by * import from helpers in config
# pygame.locals reference moved to config file

#pygame.init() --> to be removed, init moved to config

FPS = 60 # I was fucking around with different FPS to get different animation speeds
fpsClock = pygame.time.Clock()

DISPLAY = config.displayer(config.res_x, config.res_y)

'''
I am experimenting below primarily with the horizontal movement and blitting.

I added imports from pygame and sys above that I have seen in "Making Games with
Python & Pygame". I don't want to mess up your class/OOP structure,
so I'm changing as little as possible.

I'm guessing you will probably want - and know how to - move some of the stuff
I added to separate files (e.g. "helpers").

I changed the background to WHITE in the "helpers" file.

Please feel free to delete comments as they become obsolete or irrelevant. 
'''

headx = config.res_x / 2 # That's how I refer to the position of the head.
heady = config.res_y / 2
head_direction = 'right' # The default head_direction of the movement.

peonx = config.res_x / 2
peony = config.res_y / 2
peon_direction = 'left'

'''
From what I remember you have to do something special
to blit more than one image at a time properly...?
Need to look that up.
'''

while True: # Main Game Loop.

# Another question to self: How do I refer to "position" in the class / object?

    Chuj = config.classes.Head((None, None))
    Chuj.Head_blit((headx, heady), DISPLAY)

    spawner(config.classes.Head, ((headx, heady), (None, None)))

    Pizda = config.classes.Peon((None, None))
    Pizda.Peon_blit((peonx, peony), DISPLAY)
    
    if head_direction == 'right':
        headx += 10
        if headx == config.res_x:
            head_direction = 'left'
    elif head_direction == 'left':
        headx -= 10
        if headx == 0:
            head_direction = 'right'

    if peon_direction == 'left':
        peonx -= 10
        if peonx == 0:
            peon_direction = 'right'
    elif peon_direction == 'right':
        peonx += 10
        if peonx == config.res_x:
            peon_direction = 'left'
    
    for event in pygame.event.get():
        if event.type == QUIT:
            config.quitter()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                config.quitter()
            else:
                None
    pygame.display.update()
    fpsClock.tick(FPS)


