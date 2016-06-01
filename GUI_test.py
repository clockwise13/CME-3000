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



def main():
    #fps Clock
    Clock = pygame.time.Clock()
    fps = 60

    # event handler for I/O

    Event = config.classes.Event()
    # create an instance of the GUI elements
    button = config.classes.GUI_BUTTON("happy_baton.png", (config.res_x/2, config.res_y/2), dummy_func, Event)

    while True:
        #Event.get_events() # at the moment the get_events function is called in the update function of objects waiting for input
        EKRAN.fill(config.WHITE)
        GUI_list.update()
        GUI_list.draw(EKRAN)
        Clock.tick(fps)
        pygame.display.flip()

if __name__ == '__main__':
    main()
