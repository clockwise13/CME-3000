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

    #spawner = classes.Spawn("Peon", (config.res_x/1.5, config.res_y/3), 50, 50)
    #spawner.activate()

    # create a Clock instance for updates and FPS management
    fpsClock = pygame.time.Clock()
    FPS = 60

    # create I/O handler

    EventHandler = config.classes.Event()

    # main loop
    while quit_flag == False:

        # reset the Surface for clean redrawing
        EKRAN.fill(config.WHITE)

        # retrieve events - IMPORTANT: main I/O output, don't add other handlers
        EventHandler.get_events()

        """This is the 'main menu' part of the main module code. It can be
        pickled once as a special level instance and loaded on boot to slim down
        the code of main."""

        # draw menu buttons for "New Game" and "Quit"

        NewGameButton = config.classes.GUI_BUTTON("new_game.png", \
        (config.res_x/2-200, config.res_y/2-100), config.helpers.new_game, EventHandler, 185, 150)

        QuitButton = config.classes.GUI_BUTTON("happy_baton.png", \
        (config.res_x/2+150, config.res_y/2+75), config.helpers.quitter, EventHandler, 279, 274)

        # finalise the loop
        GUI_list.update()
        GUI_list.draw(EKRAN)
        fpsClock.tick(FPS)
        pygame.display.flip()

if __name__ == '__main__':
    main()
