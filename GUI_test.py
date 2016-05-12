"""For testing GUI elements"""

from config import *


def dummy_func():
    # dummy function for testing
    counter = 1
    print "I have executed the dummy function" +  str(counter)
    print
    counter += 1

# create a surface for display

EKRAN = helpers.displayer()
EKRAN.fill(config.WHITE)

# create an instance of the GUI elements

button = config.classes.GUI_BUTTON("happy_baton.png", (config.res_x/3, config.res_y/2), dummy_func)

GUI_list.draw(EKRAN)
