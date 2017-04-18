"""This is to be the main module, consolidating and managing all other modules.
This module needs to be opened first as __main__. It's designed to launch the
main menu screen and then handle all input/output, loading levles etc. It's
supposed to be as lean as possible, but will have to contain at least these
elements:
- config imort and all other imports if necessary
- track record keeping via save/load
- new game/load game logic
- main game logic
- mechanics for object interactions? (might be better to move to a separate
module and import at boot)

//based on the simplePythonTest.py template"""

import config
from config import *

def main():
    quit_flag = False
    # create the main Surface
    EKRAN = helpers.displayer()
    wall_array_x = config.res_x/config.wall_size[0]
    wall_array_y = config.res_y/config.wall_size[1]
    wall_array_list = []

    for n in range(1, wall_array_y):
        """This for loop creates n-number of wall objects to cover the sides of
        the screen. With a bit of work this could provie a basic and rather
        unsexy wall array generator. Good for testing tho."""

        wall = classes.Environment_Wall()
        posx = 0
        posy = config.res_y - config.wall_size[1] * n
        wall.set_pos((posx, posy))
        wall_array_list.append(wall)

    spawner = classes.Spawn("Peon", (config.res_x/1.5, config.res_y/3), 50, 50)
    spawner.activate()

    # create a Clock instance for updates and FPS management
    fpsClock = pygame.time.Clock()
    FPS = 60

    # create I/O handler

    EventHandler = config.classes.Event()
    pygame.mixer.init() # initialize the mixer

    # main loop
    while quit_flag == False:

        # reset the Surface for clean redrawing
        EKRAN.fill(config.WHITE)

        # retrieve events - IMPORTANT: main I/O output, don't add other handlers
        EventHandler.get_events()
        EventHandler.get_collisions()
        EventHandler.get_time_delta()
        
        """This is the 'main menu' part of the main module code. It can be
        pickled once as a special level instance and loaded on boot to slim down
        the code of main."""

        """for obj in Enviro_list:
            #this loop is waaaaaaaaaaaaay inefficient; collider should work
            #on the Object_list or smth simillar check between the collisions_list
            #there
            config.helpers.collider(obj)"""

        # finalise the loop
        Enviro_list.draw(EKRAN)
        Peon_list.update()
        Peon_list.draw(EKRAN)
        Object_list.update()
        Spawner_list.update()
        GUI_list.update()
        GUI_list.draw(EKRAN)
        fpsClock.tick(FPS)
        pygame.display.flip()

if __name__ == '__main__':
    main()
